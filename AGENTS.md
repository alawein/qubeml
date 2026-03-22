---
type: normative
authority: canonical
audience: [agents, contributors, maintainers]
last-verified: 2026-03-09
<!-- CUSTOM OVERRIDE: Educational notebook governance with Colab free-tier constraints and quantum/materials domain rules [Task 1.4 audit Batch 2] -->
---

# AGENTS — qubeml

> Educational Jupyter notebooks for quantum computing and materials informatics.

## Repository Scope

Six tool modules covering Qiskit, Cirq, and PennyLane for quantum algorithms,
plus PyTorch, scikit-learn, and Kwant for materials modeling. Designed for
graduate students and researchers; all notebooks work in Google Colab free tier.

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `quantum_computing/qiskit/` | VQE tutorials, ansatz comparison, basis set studies |
| `quantum_computing/cirq/` | Gate decomposition, error models, qubit calibration |
| `quantum_computing/pennylane/` | Quantum embeddings, kernel methods |
| `materials_informatics/pytorch/` | CGCNN for band gaps, descriptor engineering |
| `materials_informatics/scikit_learn/` | Materials Project queries, feature importance |
| `materials_informatics/kwant/` | Graphene ribbons, MoS2 transistors, strain effects |

## Commands

- `pip install -r requirements.txt` -- install dependencies
- `jupyter notebook` -- launch notebook server
- `pytest` -- run tests

## Agent Rules

- Read this file before making changes
- All notebooks must work in Google Colab free tier
- Include `pip install` cells at the top of each notebook for Colab
- Include clear markdown explanations between code cells
- Add tests for utility functions (`pytest`)
- Do not add dependencies that exceed Colab's free tier resources
- Keep notebooks self-contained and runnable independently
- Use conventional commit messages: `feat(scope):`, `fix(scope):`, etc.

## Naming Conventions

- Notebooks: `snake_case.ipynb`
- Python modules: `snake_case.py`
- Classes: `PascalCase`
- Functions: `snake_case`

See [CLAUDE.md](CLAUDE.md) | [SSOT.md](SSOT.md)