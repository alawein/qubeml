"""Edge-case and additional coverage tests for src/materials_utils.py.

The main happy-path tests live in test_materials_utils.py.  This file adds:
  - Error/validation paths
  - estimate_bulk_modulus (untested in the original suite)
  - generate_2d_material_params warning for unknown material
  - Boundary conditions for Coulomb matrix, graph representation, etc.
"""

import numpy as np
import pytest
import warnings

from src.materials_utils import (
    create_crystal_descriptors,
    calculate_composition_entropy,
    generate_coulomb_matrix,
    calculate_band_gap_features,
    create_graph_representation,
    calculate_formation_energy_features,
    generate_2d_material_params,
    estimate_bulk_modulus,
)


# ---------------------------------------------------------------------------
# create_crystal_descriptors — validation
# ---------------------------------------------------------------------------

class TestCrystalDescriptorsValidation:

    def test_wrong_lattice_param_count(self):
        with pytest.raises(ValueError, match="exactly 6 values"):
            create_crystal_descriptors(
                [5.0, 5.0, 5.0],  # only 3
                [14],
                np.array([[0, 0, 0]]),
            )

    def test_empty_atomic_numbers(self):
        with pytest.raises(ValueError, match="cannot be empty"):
            create_crystal_descriptors(
                [5.0, 5.0, 5.0, 90, 90, 90],
                [],
                np.array([]).reshape(0, 3),
            )

    def test_non_cubic_volume(self):
        """Triclinic cell: volume should differ from a*b*c."""
        params = [5.0, 6.0, 7.0, 80.0, 85.0, 75.0]
        desc = create_crystal_descriptors(params, [14], np.array([[0, 0, 0]]))
        # For a non-orthogonal cell the volume is strictly less than a*b*c
        assert desc["volume"] < 5.0 * 6.0 * 7.0


# ---------------------------------------------------------------------------
# calculate_composition_entropy — edge cases
# ---------------------------------------------------------------------------

class TestCompositionEntropyEdge:

    def test_single_atom(self):
        """Single-atom list should return 0 entropy."""
        assert np.isclose(calculate_composition_entropy([26]), 0.0)

    def test_large_system_symmetry(self):
        """Equal counts should give the same entropy regardless of Z values."""
        e1 = calculate_composition_entropy([1, 2, 3, 4])
        e2 = calculate_composition_entropy([10, 20, 30, 40])
        assert np.isclose(e1, e2)


# ---------------------------------------------------------------------------
# generate_coulomb_matrix — edge / boundary
# ---------------------------------------------------------------------------

class TestCoulombMatrixEdge:

    def test_single_atom(self):
        cm = generate_coulomb_matrix([6], np.array([[0.0, 0.0, 0.0]]))
        assert cm.shape == (1, 1)
        assert np.isclose(cm[0, 0], 0.5 * 6**2.4)

    def test_padding_smaller_than_n_atoms(self):
        """When size < n_atoms, padding should be skipped."""
        cm = generate_coulomb_matrix(
            [1, 1], np.array([[0, 0, 0], [1, 0, 0]]), size=1
        )
        # size=1 < n_atoms=2 => no padding, original shape kept
        assert cm.shape == (2, 2)

    def test_symmetry(self):
        """Coulomb matrix must be symmetric."""
        cm = generate_coulomb_matrix(
            [6, 8, 1],
            np.array([[0, 0, 0], [1.5, 0, 0], [0, 1.2, 0]]),
        )
        np.testing.assert_array_almost_equal(cm, cm.T)


# ---------------------------------------------------------------------------
# calculate_band_gap_features — boundary
# ---------------------------------------------------------------------------

class TestBandGapFeaturesEdge:

    def test_heterogeneous_compound(self):
        """Binary compound should have nonzero differences."""
        features = calculate_band_gap_features(
            valence_electrons=[4, 6],
            atomic_radii=[1.1, 0.6],
            electronegativities=[1.9, 3.4],
        )
        assert features["valence_range"] == 2
        assert features["electronegativity_diff"] == pytest.approx(1.5)
        assert 0 < features["ionic_character"] < 1
        assert features["size_mismatch"] > 0

    def test_zero_radius_guard(self):
        """If max radius is 0, radius_ratio should be 1.0."""
        features = calculate_band_gap_features(
            valence_electrons=[1],
            atomic_radii=[0.0],
            electronegativities=[2.2],
        )
        assert features["radius_ratio"] == 1.0


# ---------------------------------------------------------------------------
# create_graph_representation — edge cases
# ---------------------------------------------------------------------------

class TestGraphRepresentationEdge:

    def test_no_edges_within_cutoff(self):
        """All atoms far apart => no edges."""
        positions = np.array([[0, 0, 0], [100, 100, 100.0]])
        node_features, edge_index, edge_features = create_graph_representation(
            positions, [6, 6], cutoff_radius=1.0
        )
        assert edge_index.shape == (2, 0)

    def test_single_atom_graph(self):
        """Single atom: no edges possible."""
        nf, ei, ef = create_graph_representation(
            np.array([[0, 0, 0.0]]), [14], cutoff_radius=5.0
        )
        assert nf.shape == (1, 1)
        assert ei.shape == (2, 0)


# ---------------------------------------------------------------------------
# calculate_formation_energy_features
# ---------------------------------------------------------------------------

class TestFormationEnergyEdge:

    def test_missing_reference_falls_back_to_zero(self):
        """Element not in reference_energies should contribute 0."""
        fe = calculate_formation_energy_features(
            atomic_numbers=[99],  # not in dict
            reference_energies={},
            total_energy=-5.0,
        )
        # (-5 - 0) / 1 = -5
        assert np.isclose(fe, -5.0)


# ---------------------------------------------------------------------------
# generate_2d_material_params — unknown material warning
# ---------------------------------------------------------------------------

class TestGenerate2dMaterialParamsEdge:

    def test_unknown_material_warns(self):
        with pytest.warns(UserWarning, match="Unknown material"):
            params = generate_2d_material_params("UnknownMat")
        # Should fall back to MoS2 defaults
        assert np.isclose(params["bandgap"], 1.8)

    def test_negative_strain(self):
        """Compressive strain should also reduce bandgap."""
        params_0 = generate_2d_material_params("MoS2", strain=0.0)
        params_neg = generate_2d_material_params("MoS2", strain=-3.0)
        assert params_neg["bandgap"] < params_0["bandgap"]
        # Lattice constant should shrink
        assert params_neg["lattice_constant"] < params_0["lattice_constant"]


# ---------------------------------------------------------------------------
# estimate_bulk_modulus
# ---------------------------------------------------------------------------

class TestEstimateBulkModulus:

    def test_returns_float(self):
        result = estimate_bulk_modulus(
            volume=125.0,
            formation_energy=-3.0,
            atomic_numbers=[14, 14, 8, 8],
        )
        assert isinstance(result, float)

    def test_within_bounds(self):
        """Bulk modulus should be clipped to [10, 400] GPa."""
        result = estimate_bulk_modulus(
            volume=125.0,
            formation_energy=-3.0,
            atomic_numbers=[14, 14, 8, 8],
        )
        assert 10 <= result <= 400

    def test_extreme_values_clipped(self):
        """Very small volume / large energy should still be <= 400."""
        result = estimate_bulk_modulus(
            volume=0.1,
            formation_energy=-100.0,
            atomic_numbers=[92, 92, 92, 92],
        )
        assert result == 400.0

    def test_weak_material(self):
        """Near-zero formation energy and large volume => lower bound."""
        result = estimate_bulk_modulus(
            volume=10000.0,
            formation_energy=-0.001,
            atomic_numbers=[1],
        )
        assert result == 10.0

    def test_positive_formation_energy(self):
        """Positive formation energy should still yield a positive result."""
        result = estimate_bulk_modulus(
            volume=50.0,
            formation_energy=2.0,
            atomic_numbers=[6, 6],
        )
        assert result > 0
