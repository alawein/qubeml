# QubeML

Status:      frozen
Category:    research
Owner:       alawein
Visibility:  public
Purpose:     Quantum machine learning experiments and research.
Next action: continue

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## About

Educational notebooks for quantum computing and materials informatics. Six tool modules covering Qiskit, Cirq, and PennyLane for quantum algorithms, plus PyTorch, scikit-learn, and Kwant for materials modeling.

## Public value

QubeML is a research-teaching portfolio candidate: it combines quantum
computing tutorials, materials informatics, and notebook-first explanation in a
way that is legible to graduate students and technical reviewers. Public polish
should focus on reproducible notebooks, dataset provenance, dependency
versions, and clear separation between educational examples and original
claims.

## Features

- **Quantum Computing** -- VQE for molecular ground states, custom gates, noise simulation, quantum kernels
- **Materials Informatics** -- Crystal graph neural networks, PCA on materials datasets, 2D material transport
- **Tutorial Notebooks** -- Jupyter notebooks designed for graduate students and researchers
- **Google Colab Support** -- All notebooks work in Colab's free tier

## Modules

| Module | Key Implementations |
|--------|-----------------------|
| Qiskit | VQE ground states, ansatz comparison, basis set effects |
| PyTorch | CGCNN for band gaps, descriptor engineering |
| Scikit-learn | Materials Project queries, feature importance |
| Kwant | Graphene ribbons, MoS2 transistors |
| Cirq | Error mitigation, qubit calibration |
| PennyLane | Quantum embeddings, kernel methods |

## Installation

```bash
git clone https://github.com/alawein/qubeml.git
cd qubeml
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

**Quantum Chemistry** (`quantum_computing/qiskit/`):
- Build H2 molecule, run VQE with UCCSD ansatz
- Compare to exact diagonalization
- Basis set convergence study

**Graph Neural Networks** (`materials_informatics/pytorch/`):
- Load crystal structures from CIF
- Build graph representation
- Train CGCNN on Materials Project data

**Transport** (`materials_informatics/kwant/`):
- Graphene nanoribbon conductance
- MoS2 field-effect transistor
- Strain effects on band structure

## Project Structure

```
qubeml/
├── quantum_computing/
│   ├── qiskit/        # VQE tutorials, molecule examples
│   ├── cirq/          # Gate decomposition, error models
│   └── pennylane/     # Quantum ML demos
├── materials_informatics/
│   ├── pytorch/       # GNN implementations
│   ├── scikit_learn/  # Classical ML pipelines
│   └── kwant/         # Transport simulations
├── src/               # Utilities (descriptors, plotting)
└── tests/             # Unit tests
```

## Testing

```bash
python -m pytest tests/ -v
```

## Data boundaries

Materials Project queries and generated notebook outputs should document their
source, access requirements, and regeneration path. Keep API keys, private
datasets, large generated artifacts, and machine-local notebook outputs out of
committed examples unless they are intentionally public and reproducible.

## References

- Qiskit Textbook: https://qiskit.org/textbook/
- Materials Project: https://materialsproject.org/
- CGCNN paper: Xie & Grossman, Phys. Rev. Lett. 120, 145301 (2018)

## License

MIT License -- see [LICENSE](LICENSE).

## Ownership

- **Maintainer:** @alawein
- **Support:** [GitHub Issues](https://github.com/alawein/qubeml/issues)
