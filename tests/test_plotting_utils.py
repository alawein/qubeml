"""Tests for QubeML plotting utility functions.

All plotting tests use the Agg backend (set in conftest.py) so no GUI
windows appear.  We verify that each function returns a matplotlib Figure
and that the figure contains the expected axes / annotations.
"""

import numpy as np
import pytest
import matplotlib
import matplotlib.pyplot as plt

from src.plotting_utils import (
    setup_plotting_style,
    plot_quantum_state,
    plot_measurement_results,
    plot_convergence,
    plot_band_structure,
    plot_crystal_structure,
)


class TestSetupPlottingStyle:
    """Tests for setup_plotting_style."""

    def test_sets_rcparams(self):
        """Calling setup_plotting_style should update figure.figsize."""
        setup_plotting_style()
        assert plt.rcParams["figure.figsize"] == [10, 6]
        assert plt.rcParams["font.size"] == 12
        assert plt.rcParams["axes.grid"] is True

    def test_idempotent(self):
        """Calling twice should not raise."""
        setup_plotting_style()
        setup_plotting_style()


class TestPlotQuantumState:
    """Tests for plot_quantum_state."""

    def test_returns_figure(self, bell_phi_plus):
        fig = plot_quantum_state(bell_phi_plus)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)

    def test_axes_count(self, bell_phi_plus):
        """Should produce two subplots (probability + phase)."""
        fig = plot_quantum_state(bell_phi_plus)
        assert len(fig.axes) >= 2
        plt.close(fig)

    def test_custom_title(self, zero_state_2q):
        fig = plot_quantum_state(zero_state_2q, title="Test Title")
        ax_titles = [ax.get_title() for ax in fig.axes]
        assert any("Test Title" in t for t in ax_titles)
        plt.close(fig)

    def test_custom_basis_labels(self):
        state = np.array([1, 0, 0, 0], dtype=complex)
        labels = ["a", "b", "c", "d"]
        fig = plot_quantum_state(state, basis_labels=labels)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)

    def test_larger_state(self):
        """3-qubit state (8 amplitudes)."""
        state = np.zeros(8, dtype=complex)
        state[0] = 1.0
        fig = plot_quantum_state(state, title="3-qubit")
        assert isinstance(fig, plt.Figure)
        plt.close(fig)


class TestPlotMeasurementResults:
    """Tests for plot_measurement_results."""

    def test_returns_figure(self):
        counts = {"00": 500, "11": 500}
        fig = plot_measurement_results(counts)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)

    def test_single_outcome(self):
        counts = {"000": 1000}
        fig = plot_measurement_results(counts, title="Single outcome")
        assert isinstance(fig, plt.Figure)
        plt.close(fig)

    def test_many_outcomes(self):
        counts = {format(i, "04b"): np.random.randint(1, 100) for i in range(16)}
        fig = plot_measurement_results(counts)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)


class TestPlotConvergence:
    """Tests for plot_convergence."""

    def test_returns_figure(self):
        iters = list(range(20))
        vals = [10 / (i + 1) for i in iters]
        fig = plot_convergence(iters, vals)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)

    def test_with_target_value(self):
        iters = list(range(10))
        vals = [5 - 0.5 * i for i in iters]
        fig = plot_convergence(iters, vals, target_value=0.5, ylabel="Energy")
        # Should have a legend when target_value is provided
        ax = fig.axes[0]
        assert ax.get_legend() is not None
        plt.close(fig)

    def test_without_target_value(self):
        iters = list(range(5))
        vals = [1.0] * 5
        fig = plot_convergence(iters, vals)
        ax = fig.axes[0]
        assert ax.get_legend() is None
        plt.close(fig)


class TestPlotBandStructure:
    """Tests for plot_band_structure."""

    def test_returns_figure(self):
        k = np.linspace(0, 1, 50)
        energies = np.column_stack([np.sin(k * np.pi), np.cos(k * np.pi)])
        fig = plot_band_structure(k, energies)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)

    def test_with_fermi_energy(self):
        k = np.linspace(0, 1, 30)
        energies = np.column_stack([k, k + 1])
        fig = plot_band_structure(k, energies, fermi_energy=0.5)
        ax = fig.axes[0]
        assert ax.get_legend() is not None
        plt.close(fig)

    def test_single_band(self):
        k = np.linspace(0, 1, 20)
        energies = k.reshape(-1, 1)
        fig = plot_band_structure(k, energies, title="Single band")
        assert isinstance(fig, plt.Figure)
        plt.close(fig)


class TestPlotCrystalStructure:
    """Tests for plot_crystal_structure."""

    def test_returns_figure(self, si2o2_structure):
        positions = si2o2_structure["positions"]
        atomic_numbers = si2o2_structure["atomic_numbers"]
        fig = plot_crystal_structure(positions, atomic_numbers)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)

    def test_with_lattice_vectors(self):
        positions = np.array([[0, 0, 0], [1, 1, 1.0]])
        atomic_numbers = [14, 8]
        lattice_vectors = np.eye(3) * 5.0
        fig = plot_crystal_structure(
            positions, atomic_numbers, lattice_vectors=lattice_vectors
        )
        assert isinstance(fig, plt.Figure)
        plt.close(fig)

    def test_known_element_symbols(self):
        """Atoms with Z in the element_symbols dict should not raise."""
        positions = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
        atomic_numbers = [1, 6, 8]  # H, C, O
        fig = plot_crystal_structure(positions, atomic_numbers)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)

    def test_unknown_element(self):
        """Atoms with Z not in the symbol dict should still render."""
        positions = np.array([[0, 0, 0]])
        atomic_numbers = [79]  # Au, not in the hard-coded dict
        fig = plot_crystal_structure(positions, atomic_numbers)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
