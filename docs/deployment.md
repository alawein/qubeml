---
type: canonical
owner: platform-engineering
last-reviewed: 2026-03-31
---

# Deployment and Release - qubeml

QubeML has no server deployment. The deliverable is the notebook and source package. Release means tagging a version and optionally publishing the `qubeml` package to PyPI.

## Deployment Process

There is no running service. "Deployment" means making notebooks available to learners:

1. Merge to `main` after CI passes (`pytest`, lint).
2. Notebooks on `main` are usable directly via GitHub or by cloning the repo.
3. Google Colab links in notebooks point to the `main` branch; no additional publishing step is required.

## Release Strategy

Versions follow semantic versioning declared in `pyproject.toml`. A release tag (`vX.Y.Z`) triggers the publish workflow if configured. Increment patch for notebook corrections, minor for new notebook families, major for breaking changes to the `src/` API.

## Rollback Procedures

Rollback is a `git revert` of the offending commit on `main`. Because there is no running infrastructure, reverting the source is sufficient. No database migration or cache flush is needed.

## Environment Configuration

No environment variables are required for normal notebook use. Individual notebooks that call external APIs document their own credentials in their setup cells.

