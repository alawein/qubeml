# QubeML

Status:      frozen
Category:    lab
Owner:       alawein
Visibility:  public
Purpose:     Quantum machine learning experiments and research.

## Abstract

QubeML is a notebook-first teaching repo for quantum computing and materials
informatics, aimed at graduate students and researchers learning the tooling.
Six notebook modules cover Qiskit, Cirq, and PennyLane for quantum algorithms,
plus PyTorch, scikit-learn, and Kwant for crystal graphs, classical ML pipelines,
and 2D transport. The goal is reproducible graduate-level examples, not
production library APIs.

## Status

- Lifecycle: frozen
- Verification date: 2026-08-31
- Scope: educational notebooks and small utility modules; no active feature work

## Runtime requirements

- Python 3.9-3.12 (classifiers cap at 3.12); the `numpy<2.0` pin in
  `pyproject.toml` has no prebuilt wheel for 3.13+, and building it from
  source needs a C compiler this repo does not otherwise require
- Base install (`pip install -e ".[dev]"`) covers `src/` and the pytest suite
- Optional extras for notebooks: `quantum` (Qiskit, Cirq, PennyLane), `ml`
  (PyTorch, scikit-learn), `materials` (Kwant, pymatgen, ASE), `visualization`
- Optional: Google Colab for hosted notebook runs; notebooks needing Kwant or
  pymatgen need a local environment instead (see `docs/troubleshooting.md`)

## Reproducibility

```bash
git clone https://github.com/alawein/qubeml.git
cd qubeml
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -e ".[dev]"
python -m pytest tests/ -q
```

Verified 2026-08-31 on Python 3.12: 80 passed, 1 skipped. `test_materials_discovery.py`
(18 tests) needs the `ml` extra (`pip install -e ".[ml]"`) and is
not part of this run.

Run notebooks from `quantum_computing/` or `materials_informatics/` with the
matching extra installed.

## Datasets

- `data/sample_crystals.csv` and `data/bandgap_examples.json` ship with the repo;
  provenance in [data/README.md](data/README.md)
- Crystal structures were originally sourced from the Materials Project
  database; the repo has no live Materials Project API integration, only the
  bundled files

## Architecture

```text
qubeml/
├── src/                   # shared notebook utilities
├── quantum_computing/     # Qiskit, Cirq, PennyLane notebooks
├── materials_informatics/ # PyTorch, scikit-learn, Kwant notebooks
├── integrative_projects/  # cross-domain notebooks
├── data/                  # bundled fixtures
├── tests/                 # pytest for src/
└── docs/                  # architecture, theory, operations
```

Detail: [docs/architecture/topology.md](docs/architecture/topology.md) and [docs/architecture.md](docs/architecture.md).

## Docs map

- [docs/README.md](docs/README.md)
- [SSOT.md](SSOT.md)
- [LESSONS.md](LESSONS.md)
