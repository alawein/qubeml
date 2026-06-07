---
type: canonical
owner: platform-engineering
last-reviewed: 2026-03-31
---

# Architecture Overview - qubeml

QubeML is an educational notebooks repository. There is no server or application runtime; the architecture is the directory layout and the shared utility package.

## Components

- `quantum_computing/`: Qiskit, Cirq, and PennyLane notebook families covering VQE, ansatz design, noise modeling, and quantum ML.
- `materials_informatics/`: PyTorch graph networks, scikit-learn classical ML, and Kwant transport notebooks.
- `integrative_projects/`: cross-domain notebooks combining quantum simulation with materials modeling.
- `src/`: small shared utility package (data loaders, evaluation helpers) installed via `pip install -e ".[dev]"`.
- `tests/`: pytest suite covering `src/` utilities.

## Data Flow

Notebooks are the primary compute unit. Each notebook runs end-to-end in a Jupyter kernel. The `src/` package provides helpers imported by notebooks; no data flows between notebooks automatically. Input datasets live under `data/` or are fetched inline from public sources.

## Dependencies

Runtime dependencies are declared in `pyproject.toml`. Optional groups:
- `[quantum]`: Qiskit, Cirq, PennyLane
- `[ml]`: PyTorch, torch-geometric, scikit-learn
- `[materials]`: kwant, pymatgen, ASE
- `[visualization]`: seaborn, plotly, networkx

Install with `pip install -e ".[dev]"` for development; use `".[all]"` for all optional extras.

## Constraints

- Python >= 3.9 required; notebooks target Colab-compatible environments where practical.
- No server process, database, or persistent state outside local files.
- Heavy extras (kwant, pymatgen) may not install on Colab free tier; affected notebooks document this.

