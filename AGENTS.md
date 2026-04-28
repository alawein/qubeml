---
type: canonical
source: none
sync: none
sla: none
authority: canonical
audience: [agents, contributors, maintainers]
last_updated: 2026-04-15
last-verified: 2026-04-15
---

# AGENTS — QubeML

## Workspace identity

QubeML is an educational-notebooks repo for quantum computing and materials
informatics.

## Directory structure

- `quantum_computing/`: quantum notebook families
- `materials_informatics/`: materials notebook families
- `src/`: shared utility layer
- `tests/`: required verification for utilities

## Governance rules

1. Notebooks are the primary learning surface.
2. Keep notebooks runnable in Colab-friendly environments where practical.
3. Add or update tests when shared utility behavior changes.
4. Do not bury teaching context in opaque helper code.
5. Comments and markdown should explain the scientific idea first.

## Code conventions

- `src/` utilities stay small and reusable
- Notebook names remain descriptive and stable
- Conventional commits only

## Build and test commands

```bash
pip install -r requirements.txt
pip install -e ".[dev]"
pytest
jupyter notebook
```
