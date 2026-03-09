---
type: lessons
authority: observed
audience: [ai-agents, contributors, future-self]
last-verified: 2026-03-09
last-updated: 2026-03-04
---

# LESSONS — QubeML

> Observed patterns only. Minimal initial entry — update as lessons accumulate.

## Patterns That Work

- **Module-per-topic notebook organization**: Structuring six distinct modules (VQE, quantum kernels, crystal GNNs, 2D material transport, etc.) as independent notebooks lets graduate students use them selectively without running the full suite.
- **Dual-framework examples (Qiskit + PennyLane)**: Showing equivalent implementations in multiple quantum frameworks helps learners understand that concepts are framework-agnostic, which is pedagogically valuable.

## Anti-Patterns

- **Assuming all notebooks can run on a single machine**: Some modules require Kwant (for transport calculations) or PyTorch with GPU; document minimum environment requirements per module rather than assuming a uniform setup.
- **Using unstable experimental APIs in educational notebooks**: Notebooks are reference material; using pre-release or deprecated APIs causes learner frustration when code breaks after install.

## Pitfalls

- **Qiskit 1.x breaking changes**: The Qiskit 0.x → 1.x migration changed many core APIs; notebooks written for 0.x will silently produce wrong results or errors on 1.x without explicit version pinning.
- **Long notebook runtimes blocking learners**: VQE and quantum kernel training notebooks can take minutes to hours without a simulator; include a pre-computed results cell so learners can inspect outputs without running full training.
