---
description: "Load project context at session start — read HANDOFF, CLAUDE, AGENTS, git state"
allowed-tools:
  - Bash(pwd)
  - Bash(git:*)
  - Bash(ls:*)
  - Bash(basename:*)
  - Read
  - Grep
---

# Bootstrap

Load project context before doing any work. Run at the start of every session.

## Steps

1. **Identify project.** Run `pwd`, read the nearest `CLAUDE.md` to get the project name and purpose.

2. **Read anchors** (in order, skip if missing):
   - `CLAUDE.md` — project rules, build commands, conventions
   - `HANDOFF.md` — current state, last session's work, next tasks
   - `AGENTS.md` — invariants (what must never break)

3. **If no HANDOFF.md exists**, state: "No HANDOFF.md found. This is either a first session or a dormant project. I'll create one when work begins."

4. **Check git state:**
   ```
   git log --oneline -5
   git status --short
   git branch --show-current
   ```

5. **Print context card:**
   ```
   === BOOTSTRAP: {project-name} ===
   Branch: {branch} ({clean | N dirty files})
   Last commit: {hash} {message}
   State: {HANDOFF status line, or "No HANDOFF.md"}
   Next: {first 3 next-tasks from HANDOFF, or "Read CLAUDE.md for project scope"}
   Build: {build command from CLAUDE.md, or "See CLAUDE.md"}
   ===
   ```

6. **Declare context:** "I am now working in {project-name}. Following conventions in CLAUDE.md, respecting invariants in AGENTS.md."

## Rules

- Do NOT start working before reading HANDOFF.md (if it exists).
- Do NOT assume anything from a previous session — verify git state.
- If HANDOFF.md says something is DONE or FROZEN, do not redo it.
