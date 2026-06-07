---
type: canonical
owner: platform-engineering
last-reviewed: 2026-03-31
---

# Troubleshooting - qubeml

This page covers common failures when running QubeML notebooks and utilities.

## Common Issues

- **Import error for `qiskit`, `cirq`, or `pennylane`**: the quantum extras are not installed. Run `pip install -e ".[quantum]"` or install the specific package.
- **Import error for `torch` or `torch_geometric`**: run `pip install -e ".[ml]"`.
- **`kwant` or `pymatgen` fails to install on Colab free tier**: these packages require system libraries not available on Colab. Run affected notebooks locally.
- **`pytest` fails with `ModuleNotFoundError: qubeml`**: the package is not installed in development mode. Run `pip install -e ".[dev]"` from the repo root.
- **Notebook kernel dies mid-run**: most likely an out-of-memory condition from a large quantum simulation. Reduce the number of qubits or shots in the notebook's configuration cell.

## Diagnostic Steps

1. Confirm the virtual environment is active and `pip install -e ".[dev]"` has been run.
2. Run `pytest` to verify the utility layer is intact before debugging notebooks.
3. Check the notebook's first cell for explicit environment or version requirements.
4. Isolate the failing cell and run it alone after restarting the kernel.

## Known Failure Modes

- Qiskit API changes between minor releases sometimes break circuit construction syntax. Check the installed version against the notebook's documented requirement.
- `torch_geometric` wheel availability varies by Python and CUDA version. See the PyG installation guide for the correct index URL.

## FAQ

**Can I run these notebooks on Google Colab?** Most notebooks in `quantum_computing/` and `materials_informatics/scikit_learn/` work on Colab free tier. Notebooks that require `kwant`, `pymatgen`, or `torch_geometric` with CUDA typically need a local environment.

**Why does `pytest` show no tests?** Tests live under `tests/` and target `src/` utilities only. There are no notebook-level tests.

