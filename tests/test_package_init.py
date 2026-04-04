"""Tests for the src package-level __init__.py exports."""

import pytest


class TestPackageInit:
    """Verify that the top-level package exposes the expected modules."""

    def test_import_src(self):
        import src
        assert hasattr(src, "__version__")
        assert hasattr(src, "__author__")

    def test_version_string(self):
        from src import __version__
        # Semantic version pattern: digits.digits.digits
        parts = __version__.split(".")
        assert len(parts) == 3
        assert all(p.isdigit() for p in parts)

    def test_exports_quantum_utils(self):
        from src import quantum_utils
        assert hasattr(quantum_utils, "create_bell_state")
        assert hasattr(quantum_utils, "pauli_matrices")

    def test_exports_materials_utils(self):
        from src import materials_utils
        assert hasattr(materials_utils, "create_crystal_descriptors")
        assert hasattr(materials_utils, "generate_coulomb_matrix")

    def test_exports_plotting_utils(self):
        from src import plotting_utils
        assert hasattr(plotting_utils, "plot_quantum_state")

    def test_all_list(self):
        import src
        assert set(src.__all__) == {"quantum_utils", "materials_utils", "plotting_utils"}
