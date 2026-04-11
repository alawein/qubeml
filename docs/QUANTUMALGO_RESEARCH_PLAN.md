---
type: canonical
authority: canonical
last-verified: 2026-04-08
---

# Implementation & Research Plan — QuantumAlgo

**Scope:** Quantum algorithms as a primary research direction — distinct from OptiQAP's classical/hybrid approach.
**Current base:** QubeML educational notebooks (`~/Desktop/Dropbox/GitHub/alawein/qubeml/`)
**Status:** 💡 Planned — not yet started as a research project.

---

## What Exists (QubeML)

QubeML is an educational repo, not a research project. It provides the foundation:

| Module | Content | Status |
|---|---|---|
| `quantum_computing/qiskit/` | VQE, ansatz comparison, basis set effects | ✅ Educational notebooks |
| `quantum_computing/cirq/` | Error mitigation, qubit calibration | ✅ Educational notebooks |
| `quantum_computing/pennylane/` | Quantum embeddings, kernel methods | ✅ Educational notebooks |
| `materials_informatics/` | Crystal GNNs, 2D material transport | ✅ Educational notebooks |
| `src/quantum_utils.py` | Utility functions for quantum circuits | ✅ |
| `src/materials_utils.py` | Materials informatics utilities | ✅ |

---

## Research Directions

### Direction 1: QAOA for QAP (bridge to OptiQAP)

Apply QAOA to small QAP instances and compare against OptiQAP's classical methods.

**Why:** Establishes whether quantum advantage exists for QAP at any scale. Even negative results (QAOA worse than classical) are publishable and scientifically valuable.

**Approach:**
1. Map QAP to QUBO (already done in `optiqap/src/qaplibria/methods/qap_to_qubo.py`)
2. Apply QAOA to the QUBO formulation using PennyLane or Qiskit
3. Benchmark on small instances (n ≤ 15) where exact solutions are known
4. Compare: QAOA vs OptiQAP classical methods vs exact solver

**Target instances:** had12, nug12, chr12a (n=12, exact solutions known)

### Direction 2: Bell Inequality Paper (in progress)

**Current state:** v1.2 written, two peer reviews received. See `BELL_PAPER.md` on Desktop.

**Revision needed (both reviews agree):**
1. Engage more specifically with Wang et al.'s multiphoton interference architecture
2. Clarify 4/η − 2 benchmark scope in main text (not just Appendix A)
3. Check whether Wang et al. already report any Table 4 diagnostics — quote absences specifically
4. Reframe Monte Carlo as verification check, not primary result
5. Acknowledge toy filter is adversarially constructed, not physically motivated

**Target venue:** Physical Review Letters or Quantum (after revision)

### Direction 3: Quantum Walks for Graph Problems

Quantum walks as a search primitive for combinatorial optimization. More speculative — depends on Direction 1 results.

### Direction 4: Formal Verification of Quantum Algorithms

Connect to Morphism's governance work — formal proofs of quantum algorithm correctness using Lean 4 or similar. Long-horizon, low priority until Morphism is further along.

---

## Phase 1: Bell Paper Revision (immediate, spare cycles)

This is the only active quantum research item. Everything else is planned.

**Estimated effort:** 1–2 focused days.

**Steps:**
1. Read Wang et al. (2025) methods section carefully — identify what physical mechanism plays the role of the acceptance filter
2. Check whether they report: setting-pair-resolved acceptance rates, raw pre-selection correlations, no-signaling checks
3. Revise paper to engage with their specific experimental architecture
4. Reframe Monte Carlo section as "numerical verification of analytic result" not "primary evidence"
5. Add explicit statement that toy filter is adversarially constructed
6. Resubmit

---

## Phase 2: QAOA-QAP Experiment (first research sprint)

**Prerequisites:** OptiQAP Phase 1 (data quality) complete, spare sprint available.

**Setup:**
```bash
# New repo or branch in qubeml
cd ~/Desktop/Dropbox/GitHub/alawein/qubeml
git checkout -b qaoa-qap-experiment

# Dependencies
pip install pennylane qiskit-optimization
```

**Experiment design:**
```python
# notebooks/qaoa_qap_comparison.ipynb

# 1. Load small QAP instance
from qaplibria import load_qaplib
instance = load_qaplib('had12.dat')  # n=12, BKS=1652

# 2. Convert to QUBO (reuse OptiQAP's converter)
from qaplibria.methods.qap_to_qubo import qap_to_qubo
Q = qap_to_qubo(instance.F, instance.D)

# 3. Run QAOA
import pennylane as qml
# ... QAOA circuit definition ...

# 4. Compare against OptiQAP
from qaplibria import QAPSolver
classical = QAPSolver(method='nesterov').solve(instance)
```

**Output:** Notebook + results table comparing QAOA vs classical on had12, nug12, chr12a.

---

## Phase 3: Decide Research Direction

After Phase 2, decide based on results:

- If QAOA shows promise on small instances → pursue quantum-classical hybrid for QAP
- If QAOA underperforms → document and publish as negative result, pivot to quantum walks
- Either way → Bell paper revision is independent and should proceed regardless

---

## Documentation Plan

**QubeML docs to add:**
- `docs/research-directions.md` — this file's content, condensed
- `docs/qaoa-qap-notes.md` — running notes from QAOA experiment

**New repo (when ready):** `quantumalgo/` — separate from QubeML once research direction is clear. QubeML stays as educational content.

---

## Connection to Other Projects

| Project | Connection |
|---|---|
| OptiQAP | QAOA-QAP experiment uses OptiQAP's QUBO converter and benchmark instances |
| Morphism | Formal verification of quantum algorithms (long-horizon) |
| Bell paper | Independent physics/foundations work, publishable standalone |
