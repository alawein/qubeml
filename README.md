# QubeML

QubeML is a notebook-first teaching repo for quantum computing and materials
informatics. The work is organized around concrete toolchains rather than one
abstract "quantum AI" layer: Qiskit, Cirq, and PennyLane on one side; PyTorch,
scikit-learn, and Kwant on the other.

The shared `src/` layer exists only to support those notebooks with utilities.
The notebooks remain the primary learning surface, and they should stay runnable
without assuming a local workstation more capable than Google Colab free tier.

## Core surfaces

- `quantum_computing/`: notebook families for Qiskit, Cirq, and PennyLane
- `materials_informatics/`: notebook families for PyTorch, scikit-learn, and
  Kwant
- `src/`: shared utility layer for plotting, materials helpers, and quantum
  helpers
- `tests/`: verification for the shared Python utilities
- `docs/`: architecture, theory, and notebook progression notes

## Quick start

```bash
git clone https://github.com/alawein/qubeml.git
cd qubeml
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

## Notebook families

| Surface | Role |
|---------|------|
| `quantum_computing/qiskit/` | VQE, ansatz comparison, chemistry examples |
| `quantum_computing/cirq/` | Gates, noise, and calibration workflows |
| `quantum_computing/pennylane/` | Quantum ML and kernel methods |
| `materials_informatics/pytorch/` | Graph and neural models for materials |
| `materials_informatics/scikit_learn/` | Classical materials ML workflows |
| `materials_informatics/kwant/` | Transport and device simulations |

## Development

```bash
pip install -e ".[dev]"
pytest
```

## Documentation

Start with [docs/README.md](docs/README.md) for architecture notes, theory, and
the notebook progression matrix.
