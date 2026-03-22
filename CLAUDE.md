---
type: guide
authority: canonical
audience: [ai-agents, contributors]
last-verified: 2026-03-03
---

# CLAUDE.md — qubeml
<!-- CUSTOM OVERRIDE: Educational notebooks with quantum computing and materials informatics specialization (Qiskit, Cirq, PennyLane, Colab compatibility) [Task 1.4 audit Batch 2] -->

## Repository Context

**Name:** QubeML  
**Type:** educational-notebooks  
**Purpose:** Educational Jupyter notebooks for quantum computing (Qiskit, Cirq, PennyLane) and materials informatics (PyTorch, scikit-learn, Kwant). Six modules covering VQE, quantum kernels, crystal graph neural networks, and 2D material transport — designed for graduate students and researchers.

## Tech Stack

- **Language:** Python 3.9+
- **Quantum:** Qiskit, Cirq, PennyLane
- **ML/Materials:** PyTorch, scikit-learn, Kwant
- **Environment:** `requirements.txt`, Google Colab compatible
- **Testing:** pytest

## Key Files

- `README.md` — Main documentation with module overview
- `requirements.txt` — Python dependencies
- `quantum_computing/qiskit/` — VQE tutorials, ansatz comparison, basis set studies
- `quantum_computing/cirq/` — Gate decomposition, error models, qubit calibration
- `quantum_computing/pennylane/` — Quantum embeddings, kernel methods
- `materials_informatics/pytorch/` — CGCNN for band gaps, descriptor engineering
- `materials_informatics/scikit_learn/` — Materials Project queries, feature importance
- `materials_informatics/kwant/` — Graphene ribbons, MoS2 transistors, strain effects

## Development Guidelines

1. All notebooks must work in Google Colab's free tier
2. Include clear markdown explanations between code cells
3. Add `pip install` cells at the top of each notebook for Colab
4. Add tests for utility functions (`pytest`)
5. Use conventional commits

## Common Tasks

### Running Tests
```bash
pytest
```

### Setting Up Locally
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

## Architecture

Notebook-first educational platform organized into six tool-based modules. Each module provides self-contained Jupyter notebooks with progressive tutorials — from basic quantum gates to VQE molecular simulations, and from crystal structure featurization to transport calculations in 2D materials.

## Governance
See [AGENTS.md](AGENTS.md) for rules. See [SSOT.md](SSOT.md) for current state.
