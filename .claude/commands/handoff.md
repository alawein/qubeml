---
description: "Save session state to HANDOFF.md before ending work"
allowed-tools:
  - Bash(pwd)
  - Bash(git:*)
  - Bash(ls:*)
  - Bash(date:*)
  - Read
  - Write
  - Edit
  - Grep
---

# Handoff

Save current session state before ending work or switching projects.

## Steps

1. **Gather state:**
   - `git status --short` — uncommitted changes
   - `git log --oneline -5` — recent commits
   - `git diff --stat` — changed files
   - Current date

2. **Read existing HANDOFF.md** if present (preserve structure and frozen sections).

3. **Write/update HANDOFF.md:**
   ```markdown
   # {Project} -- Handoff ({date})

   ## Status: {one-line summary}

   ## What was done this session
   - {completed work, bullet list}

   ## Uncommitted changes
   - {from git status, or "None"}

   ## Next tasks
   - {priority-ordered next steps}

   ## Gotchas discovered
   - {anything surprising the next session needs}
   ```

4. **Suggest commit** if uncommitted changes exist.

5. **Confirm:** "Handoff saved. Safe to end session."

## Rules

- Only record actual completed work — do not fabricate.
- Preserve existing frozen/done sections in HANDOFF.md.
- Keep it compact — the next agent reads this at bootstrap.
- Record gotchas — these are the highest-value handoff content.
