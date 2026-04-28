---
type: canonical
source: none
sync: none
sla: none
authority: canonical
audience: [ai-agents, contributors]
last_updated: 2026-04-15
last-verified: 2026-04-15
---

# CLAUDE.md — QubeML

## Workspace identity

QubeML is an educational-notebooks repo for quantum computing and materials
informatics. The notebooks are the primary teaching surface. The small `src/`
package exists to support those notebooks, not to replace them with a generic
library story.

Shared voice and research-writing contract:

- <https://github.com/alawein/alawein/blob/main/docs/style/VOICE.md>
- <https://github.com/alawein/alawein/blob/main/prompt-kits/AGENT.md>

## Directory structure

- `quantum_computing/qiskit/`: VQE, chemistry, and ansatz notebooks
- `quantum_computing/cirq/`: circuit, noise, and calibration notebooks
- `quantum_computing/pennylane/`: quantum ML notebooks
- `materials_informatics/pytorch/`: graph and neural materials notebooks
- `materials_informatics/scikit_learn/`: classical materials ML notebooks
- `materials_informatics/kwant/`: transport notebooks
- `src/`: shared utilities for notebooks
- `tests/`: utility verification

## Governance rules

1. Keep the notebooks as the primary learning surface.
2. The shared `src/` utilities support notebook clarity; they should not absorb
   notebook-specific teaching context unless reuse is real.
3. Notebooks should stay runnable in Google Colab free tier unless a notebook
   explicitly declares a heavier requirement.
4. Keep install cells and explanatory markdown in notebooks aligned with the
   actual environment assumptions.
5. Avoid dependency creep that makes teaching notebooks fragile.
6. Keep quantum and materials terminology precise rather than collapsing both
   sides into vague "AI" language.

## Code conventions

- Shared Python helpers live under `src/`.
- Comments and markdown should teach the idea, not narrate the obvious code.
- Keep mathematical notation clean and consistent with the notebook exposition.
- Tests belong on the shared utility layer when behavior moves out of notebooks.

## Build and test commands

```bash
pip install -r requirements.txt
pip install -e ".[dev]"
pytest
jupyter notebook
```
