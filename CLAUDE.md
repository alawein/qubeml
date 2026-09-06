---
type: canonical
source: none
sync: none
sla: none
authority: canonical
audience: [ai-agents, contributors]
last_updated: 2026-09-06
last-verified: 2026-09-06
---

# CLAUDE.md: QubeML

Universal agent rules and simplicity defaults live in [AGENTS.md](AGENTS.md). Read that first.

## Claude-specific deltas

Shared voice and research-writing contract:

- <https://github.com/alawein/alawein/blob/main/docs/style/VOICE.md>
- <https://github.com/alawein/alawein/blob/main/prompt-kits/AGENT.md>

Lint, format, and type-check (config in `pyproject.toml`):

```bash
black .          # format (line-length 88)
black --check .  # verify formatting without writing
flake8           # lint
mypy src         # type-check (python 3.9)
```

Keep quantum and materials terminology precise rather than collapsing both sides into vague "AI" language.
