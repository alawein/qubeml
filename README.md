# QubeML

Status:      frozen
Category:    research
Owner:       alawein
Visibility:  public
Purpose:     Quantum machine learning experiments and research.
Next action: continue

## Abstract

QubeML is a notebook-first teaching repo for quantum computing and materials
informatics. Six tool modules cover Qiskit, Cirq, and PennyLane for quantum
algorithms, plus PyTorch, scikit-learn, and Kwant for crystal graphs, classical
ML pipelines, and 2D transport. The goal is reproducible graduate-level examples,
not production library APIs.

## Status

- Lifecycle: frozen
- Verification date: 2026-06-29
- Scope: educational notebooks and small utility modules; no active feature work

## Runtime requirements

- Python 3.9+
- Dependencies in `requirements.txt` (Qiskit, PennyLane, PyTorch, scikit-learn, Kwant, Jupyter)
- Optional: Google Colab for hosted notebook runs
- Materials Project API key for live database queries (not required for bundled sample data)

## Reproducibility

```bash
git clone https://github.com/alawein/qubeml.git
cd qubeml
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m pytest tests/ -v
```

Run notebooks from `quantum_computing/` or `materials_informatics/` after install.
Document dependency versions and seeds when adapting examples for publication.

## Datasets

- `data/sample_crystals.csv` and `data/bandgap_examples.json` ship with the repo
- See [data/README.md](data/README.md) for provenance and usage notes
- Live Materials Project queries require an API key; keep keys out of committed notebooks

## Docs map

- [docs/README.md](docs/README.md)
- [SSOT.md](SSOT.md)
- [LESSONS.md](LESSONS.md)
