"""Shared pytest fixtures for QubeML test suite."""

import numpy as np
import pytest


# ---------------------------------------------------------------------------
# Reproducibility
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def seed_rng():
    """Fix numpy random seed for deterministic tests."""
    np.random.seed(42)
    yield


# ---------------------------------------------------------------------------
# Crystal / materials fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def cubic_lattice_params():
    """Simple cubic lattice parameters (a=b=c=5 A, all angles 90 deg)."""
    return [5.0, 5.0, 5.0, 90.0, 90.0, 90.0]


@pytest.fixture
def si2o2_structure(cubic_lattice_params):
    """Si2O2 crystal structure in a cubic cell."""
    return {
        "lattice_params": cubic_lattice_params,
        "atomic_numbers": [14, 14, 8, 8],
        "positions": np.array([
            [0.0, 0.0, 0.0],
            [0.5, 0.5, 0.5],
            [0.25, 0.25, 0.25],
            [0.75, 0.75, 0.75],
        ]),
    }


@pytest.fixture
def h2_molecule():
    """H2 molecule: two hydrogen atoms separated by 0.74 A."""
    return {
        "atomic_numbers": [1, 1],
        "positions": np.array([[0.0, 0.0, 0.0], [0.74, 0.0, 0.0]]),
    }


@pytest.fixture
def ch3_molecule():
    """Simplified CH3 fragment for graph tests."""
    return {
        "atomic_numbers": [6, 1, 1, 1],
        "positions": np.array([
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]),
    }


@pytest.fixture
def lattice_vectors_10A():
    """10 Angstrom cubic lattice vectors."""
    return np.eye(3) * 10.0


# ---------------------------------------------------------------------------
# Quantum state fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def zero_state_2q():
    """|00> state for 2-qubit system."""
    return np.array([1, 0, 0, 0], dtype=complex)


@pytest.fixture
def bell_phi_plus():
    """Bell |Phi+> = (|00> + |11>) / sqrt(2)."""
    return np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)


@pytest.fixture
def ghz_3q():
    """3-qubit GHZ state."""
    state = np.zeros(8, dtype=complex)
    state[0] = 1.0 / np.sqrt(2)
    state[-1] = 1.0 / np.sqrt(2)
    return state


# ---------------------------------------------------------------------------
# Matplotlib backend (non-interactive for CI)
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def _mpl_agg_backend():
    """Force Agg backend so no GUI windows open during tests."""
    import matplotlib
    matplotlib.use("Agg")
    yield
