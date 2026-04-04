"""Edge-case and additional coverage tests for src/quantum_utils.py.

Supplements test_quantum_utils.py with:
  - Error paths (invalid Bell state type, GHZ < 2 qubits, unknown noise)
  - Entanglement entropy edge cases (full partition)
  - measure_state determinism check with seed
  - apply_noise property checks
"""

import numpy as np
import pytest
import warnings

from src.quantum_utils import (
    create_bell_state,
    create_ghz_state,
    state_fidelity,
    measure_state,
    calculate_entanglement_entropy,
    apply_noise,
)


# ---------------------------------------------------------------------------
# create_bell_state — error paths
# ---------------------------------------------------------------------------

class TestBellStateErrors:

    def test_invalid_type_raises(self):
        with pytest.raises(ValueError, match="Unknown Bell state"):
            create_bell_state("invalid_name")

    def test_phi_plus_specific_amplitudes(self):
        s = create_bell_state("phi_plus")
        assert np.isclose(s[0], 1 / np.sqrt(2))
        assert np.isclose(s[1], 0.0)
        assert np.isclose(s[2], 0.0)
        assert np.isclose(s[3], 1 / np.sqrt(2))

    def test_psi_minus_specific_amplitudes(self):
        s = create_bell_state("psi_minus")
        assert np.isclose(s[0], 0.0)
        assert np.isclose(s[1], 1 / np.sqrt(2))
        assert np.isclose(s[2], -1 / np.sqrt(2))
        assert np.isclose(s[3], 0.0)


# ---------------------------------------------------------------------------
# create_ghz_state — error paths
# ---------------------------------------------------------------------------

class TestGHZStateErrors:

    def test_single_qubit_raises(self):
        with pytest.raises(ValueError, match="at least 2 qubits"):
            create_ghz_state(1)

    def test_zero_qubits_raises(self):
        with pytest.raises(ValueError, match="at least 2 qubits"):
            create_ghz_state(0)

    def test_large_ghz(self):
        """5-qubit GHZ: 32 amplitudes, only first and last non-zero."""
        state = create_ghz_state(5)
        assert len(state) == 32
        assert np.isclose(np.linalg.norm(state), 1.0)
        assert np.isclose(np.abs(state[0]), 1 / np.sqrt(2))
        assert np.isclose(np.abs(state[-1]), 1 / np.sqrt(2))
        assert np.allclose(state[1:-1], 0)


# ---------------------------------------------------------------------------
# state_fidelity — additional cases
# ---------------------------------------------------------------------------

class TestStateFidelityExtra:

    def test_unnormalized_inputs(self):
        """Fidelity should internally normalize."""
        s1 = np.array([2, 0, 0, 0], dtype=complex)
        s2 = np.array([3, 0, 0, 0], dtype=complex)
        assert np.isclose(state_fidelity(s1, s2), 1.0)

    def test_2d_input_shape(self):
        """Column vector should work (flattened internally)."""
        s1 = np.array([[1], [0], [0], [0]], dtype=complex)
        s2 = np.array([[0], [1], [0], [0]], dtype=complex)
        assert np.isclose(state_fidelity(s1, s2), 0.0)

    def test_fidelity_range(self):
        """Fidelity of random states must be in [0, 1]."""
        for _ in range(10):
            s1 = np.random.randn(4) + 1j * np.random.randn(4)
            s2 = np.random.randn(4) + 1j * np.random.randn(4)
            f = state_fidelity(s1, s2)
            assert 0.0 <= f <= 1.0 + 1e-10


# ---------------------------------------------------------------------------
# measure_state — determinism and statistics
# ---------------------------------------------------------------------------

class TestMeasureStateExtra:

    def test_deterministic_with_seed(self, zero_state_2q):
        """With fixed seed (conftest), repeated calls should be identical."""
        np.random.seed(123)
        c1 = measure_state(zero_state_2q, n_shots=100)
        np.random.seed(123)
        c2 = measure_state(zero_state_2q, n_shots=100)
        assert c1 == c2

    def test_total_shots_match(self, bell_phi_plus):
        counts = measure_state(bell_phi_plus, n_shots=500)
        assert sum(counts.values()) == 500

    def test_ghz_measurement_outcomes(self, ghz_3q):
        """GHZ-3 should only produce '000' and '111'."""
        counts = measure_state(ghz_3q, n_shots=5000)
        assert set(counts.keys()).issubset({"000", "111"})


# ---------------------------------------------------------------------------
# calculate_entanglement_entropy — edge cases
# ---------------------------------------------------------------------------

class TestEntanglementEntropyExtra:

    def test_full_partition_warning(self):
        """Partitioning all qubits => nothing to trace => 0."""
        state = np.array([1, 0, 0, 0], dtype=complex)
        with pytest.warns(UserWarning, match="No qubits to trace out"):
            entropy = calculate_entanglement_entropy(state, partition=[0, 1])
        assert entropy == 0.0

    def test_ghz3_entropy(self, ghz_3q):
        """3-qubit GHZ: tracing out 2 qubits gives max 1-qubit entropy."""
        entropy = calculate_entanglement_entropy(ghz_3q, partition=[0])
        assert np.isclose(entropy, 1.0)

    def test_product_state_any_partition(self):
        """|00> is a product state; entropy should be 0 for either qubit."""
        state = np.array([1, 0, 0, 0], dtype=complex)
        assert np.isclose(calculate_entanglement_entropy(state, [0]), 0.0)
        assert np.isclose(calculate_entanglement_entropy(state, [1]), 0.0)


# ---------------------------------------------------------------------------
# apply_noise — error path and properties
# ---------------------------------------------------------------------------

class TestApplyNoiseExtra:

    def test_unknown_noise_type_raises(self):
        state = np.array([1, 0, 0, 0], dtype=complex)
        with pytest.raises(ValueError, match="Unknown noise type"):
            apply_noise(state, noise_prob=0.1, noise_type="unknown")

    def test_depolarizing_full_mix(self):
        """With p=1 the state should be close to maximally mixed."""
        state = np.array([1, 0, 0, 0], dtype=complex)
        noisy = apply_noise(state, noise_prob=1.0, noise_type="depolarizing")
        # After normalization, all amplitudes should be roughly equal
        assert np.allclose(np.abs(noisy), np.abs(noisy)[0], atol=0.05)

    def test_original_state_unchanged(self):
        """apply_noise should not mutate the input array."""
        state = np.array([1, 0, 0, 0], dtype=complex)
        original = state.copy()
        apply_noise(state, noise_prob=0.5, noise_type="depolarizing")
        np.testing.assert_array_equal(state, original)

    def test_normalization_after_noise(self):
        """Every noise type should return a normalized state."""
        state = np.array([1, 0, 0, 0], dtype=complex)
        for ntype in ["depolarizing", "phase_flip", "bit_flip"]:
            noisy = apply_noise(state, noise_prob=0.3, noise_type=ntype)
            assert np.isclose(np.linalg.norm(noisy), 1.0)
