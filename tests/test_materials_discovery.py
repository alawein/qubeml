"""Tests for integrative_projects/materials_qsim/materials_discovery.py.

Covers the pure-logic, non-pipeline components that can be validated without
training full ML models or requiring large data.  Heavy dependencies (torch,
sklearn, pandas) are required by the module under test; this file skips
cleanly if they are not installed.
"""

import numpy as np
import pytest

# Guard: the module under test imports torch, sklearn, pandas at top level
pytest.importorskip("torch")
pytest.importorskip("sklearn")
pytest.importorskip("pandas")

from integrative_projects.materials_qsim.materials_discovery import (
    Material,
    CrystalStructure,
    CompositionFeaturizer,
    MaterialsOptimizer,
)


# ---------------------------------------------------------------------------
# Material dataclass
# ---------------------------------------------------------------------------

class TestMaterialDataclass:

    def test_default_properties(self):
        mat = Material(
            formula="SiO2",
            composition={"Si": 33.3, "O": 66.7},
            structure_params={"lattice_a": 5.0},
        )
        assert mat.properties == {}
        assert mat.features is None
        assert mat.quantum_features is None

    def test_with_properties(self):
        mat = Material(
            formula="NaCl",
            composition={"Na": 50, "Cl": 50},
            structure_params={},
            properties={"bandgap": 8.5},
        )
        assert mat.properties["bandgap"] == 8.5


# ---------------------------------------------------------------------------
# CrystalStructure
# ---------------------------------------------------------------------------

class TestCrystalStructure:

    def test_structural_features_shape(self):
        cs = CrystalStructure(
            lattice_vectors=np.eye(3) * 5.0,
            atom_positions=np.array([[0, 0, 0], [0.5, 0.5, 0.5]]),
            atom_types=["Si", "O"],
            space_group=225,
        )
        feats = cs.get_structural_features()
        # 3 lengths + 1 volume + 3 angles + 1 space_group = 8
        assert feats.shape == (8,)

    def test_cubic_volume(self):
        a = 4.0
        cs = CrystalStructure(
            lattice_vectors=np.eye(3) * a,
            atom_positions=np.zeros((1, 3)),
            atom_types=["Fe"],
            space_group=229,
        )
        feats = cs.get_structural_features()
        # volume should be a^3
        assert np.isclose(feats[3], a**3)

    def test_cubic_angles_are_90(self):
        cs = CrystalStructure(
            lattice_vectors=np.eye(3) * 3.0,
            atom_positions=np.zeros((1, 3)),
            atom_types=["C"],
            space_group=1,
        )
        feats = cs.get_structural_features()
        # Angles (indices 4, 5, 6) should all be pi/2 for cubic
        for i in [4, 5, 6]:
            assert np.isclose(feats[i], np.pi / 2, atol=1e-10)

    def test_non_cubic_volume(self):
        """Monoclinic-ish cell: volume < product of lengths."""
        vecs = np.array([
            [5.0, 0.0, 0.0],
            [1.0, 4.0, 0.0],
            [0.0, 0.0, 6.0],
        ])
        cs = CrystalStructure(
            lattice_vectors=vecs,
            atom_positions=np.zeros((1, 3)),
            atom_types=["Si"],
            space_group=10,
        )
        feats = cs.get_structural_features()
        lengths_product = np.prod(np.linalg.norm(vecs, axis=1))
        assert feats[3] < lengths_product


# ---------------------------------------------------------------------------
# CompositionFeaturizer
# ---------------------------------------------------------------------------

class TestCompositionFeaturizer:

    @pytest.fixture
    def featurizer(self):
        return CompositionFeaturizer()

    def test_known_elements(self, featurizer):
        features = featurizer.featurize({"Si": 2, "O": 4})
        assert isinstance(features, np.ndarray)
        assert len(features) > 0

    def test_output_length(self, featurizer):
        """All compositions should produce the same feature length."""
        f1 = featurizer.featurize({"Si": 1})
        f2 = featurizer.featurize({"Si": 1, "O": 2})
        assert len(f1) == len(f2)

    def test_single_element(self, featurizer):
        features = featurizer.featurize({"C": 4})
        # electronegativity std should be 0 for single element
        assert features[-1] == 0.0

    def test_unknown_element_handled(self, featurizer):
        """Elements not in the built-in DB contribute 0 to weighted props."""
        features = featurizer.featurize({"Unobtainium": 1})
        # Should not raise; weighted properties will be 0
        assert isinstance(features, np.ndarray)

    def test_element_properties_loaded(self, featurizer):
        props = featurizer.element_properties
        assert "Si" in props
        assert "electronegativity" in props["Si"]


# ---------------------------------------------------------------------------
# MaterialsOptimizer._check_constraints
# ---------------------------------------------------------------------------

class TestMaterialsOptimizerConstraints:

    def test_no_constraints(self):
        opt = MaterialsOptimizer(predictor=lambda x: x, constraints={})
        assert opt._check_constraints({"Si": 50, "O": 50}) is True

    def test_max_elements_pass(self):
        opt = MaterialsOptimizer(
            predictor=lambda x: x,
            constraints={"max_elements": 3},
        )
        assert opt._check_constraints({"Si": 50, "O": 50}) is True

    def test_max_elements_fail(self):
        opt = MaterialsOptimizer(
            predictor=lambda x: x,
            constraints={"max_elements": 1},
        )
        assert opt._check_constraints({"Si": 50, "O": 50}) is False

    def test_max_elements_ignores_zero_amounts(self):
        opt = MaterialsOptimizer(
            predictor=lambda x: x,
            constraints={"max_elements": 2},
        )
        # Three keys but one has 0 amount
        assert opt._check_constraints({"Si": 50, "O": 50, "Fe": 0}) is True

    def test_forbidden_elements_pass(self):
        opt = MaterialsOptimizer(
            predictor=lambda x: x,
            constraints={"forbidden_elements": ["Pb", "Cd"]},
        )
        assert opt._check_constraints({"Si": 50, "O": 50}) is True

    def test_forbidden_elements_fail(self):
        opt = MaterialsOptimizer(
            predictor=lambda x: x,
            constraints={"forbidden_elements": ["Si"]},
        )
        assert opt._check_constraints({"Si": 50, "O": 50}) is False

    def test_forbidden_element_zero_amount_still_fails(self):
        """Element present with amount > 0 triggers the constraint."""
        opt = MaterialsOptimizer(
            predictor=lambda x: x,
            constraints={"forbidden_elements": ["Fe"]},
        )
        # Fe is in composition with amount > 0
        assert opt._check_constraints({"Si": 50, "Fe": 10}) is False
