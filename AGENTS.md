---
type: canonical
source: none
sync: none
sla: none
authority: canonical
audience: [agents, contributors, maintainers]
last_updated: 2026-09-06
last-verified: 2026-09-06
---

# AGENTS - QubeML

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

6. Notebooks should stay runnable in Google Colab free tier unless a notebook explicitly declares a heavier requirement.

7. Keep install cells and explanatory markdown aligned with actual environment assumptions.

8. Avoid dependency creep that makes teaching notebooks fragile.

## Simplicity defaults

- Make the smallest change that satisfies the acceptance criteria.
- Prefer direct functions and plain data structures.
- No class when a function suffices. No framework for one implementation.
- No shared abstraction before real duplication exists.
- Prefer the standard library or an existing dependency.
- Avoid factories, registries, adapters, plugins, and config layers without multiple real consumers.
- Keep control flow direct. Use early returns when clearer. Keep errors explicit.
- Comments explain invariants, assumptions, and failure modes. Delete dead code instead of commenting it out.
- Keep pull requests single-purpose. Stop when tests and acceptance criteria pass. Do not rewrite adjacent working code without a stated need.

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
