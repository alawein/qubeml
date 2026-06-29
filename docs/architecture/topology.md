---
type: canonical
last_updated: 2026-06-29
---

# Repository topology

Archetype: `python-research-package` (fleet topology canon).

On-disk layout as of 2026-06-29. Notebook-first teaching repo; roles, not aspirational renames.

## Tree

```text
qubeml/
├── src/                         # shared utilities installed via pip install -e .
│   ├── quantum_utils.py         # Qiskit, Cirq, PennyLane helpers
│   ├── materials_utils.py       # crystal graphs, Materials Project loaders
│   └── plotting_utils.py        # figure helpers for notebooks
├── quantum_computing/           # notebook families by toolchain
│   ├── qiskit/
│   ├── cirq/
│   └── pennylane/
├── materials_informatics/       # classical ML and transport notebooks
│   ├── pytorch/
│   ├── scikit_learn/
│   └── kwant/
├── integrative_projects/        # cross-domain notebooks
│   ├── quantum_ml_hybrid/
│   └── materials_qsim/
├── data/                        # bundled fixtures (sample_crystals.csv, bandgap_examples.json)
├── tests/                       # pytest for src/ utilities
├── scripts/                     # repo maintenance helpers
├── reports/                     # generated or exported report artifacts
└── docs/                        # architecture, theory, operations
```

## Surfaces

| Path | Role |
|------|------|
| `quantum_computing/`, `materials_informatics/` | Primary compute units: Jupyter notebooks |
| `src/` | Small shared package imported by notebooks |
| `integrative_projects/` | Notebooks that combine quantum and materials lanes |
| `data/` | Small fixtures only; live API keys stay out of committed notebooks |
| `tests/` | Regression checks on `src/` helpers, not notebook execution |

## Related docs

- [architecture.md](../architecture.md) for data flow and dependency groups
- [api.md](../api.md) for the `src/` helper surface
