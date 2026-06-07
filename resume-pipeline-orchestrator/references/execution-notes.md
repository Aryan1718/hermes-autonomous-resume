# Resume Pipeline — Execution Notes

> **Placement:** This file is referenced from the resume-pipeline-orchestrator SKILL.md agent workflow section. Load it when the orchestrator skill is loaded.

## Do NOT use delegate_task for the pipeline

**Problem:** `delegate_task` for the full resume pipeline times out after 600s. The subagent gets stuck on slow API calls or context-heavy skill loading (the pipeline loads 6+ skills and reads 10+ files).

**Solution:** Run pipeline steps directly in the main agent. The pipeline is 5 sequential steps that work well as direct tool calls:

1. **jd-prefilter** — score JD, check hard disqualifiers
2. **jd-extraction** — extract must-haves, behavioral signals, scope signals, cultural intent
3. **project-selection** — read `masters.md`, score projects, pick top 3, then open only those 3 raw.md files
4. **point-repointing** — re-aim bullets for selected projects + all work-experience roles; write version files in batch via `execute_code`
5. **latex-assembly** — assemble .tex file; use `write_file` (never terminal heredoc with LaTeX backslashes)

Push/mark/log via Python `urllib.request` script (not curl, not requests module).

## Batch write pattern for version files

Use a SINGLE `execute_code` call to write ALL version files + update ALL idx.md files at once. Do NOT write one at a time — each `write_file` call adds tool output to context and slows the run.

## Patch tool path requirement

`patch()` requires **absolute paths** from profile root: `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/...`. Relative paths silently fail with "File not found" — no error, no edit.

## LaTeX file writing

Use `write_file` for .tex files. NEVER use terminal heredoc or echo with LaTeX content — backslashes get mangled.

## Push payload requirements

When pushing to `/api/generated-resumes`:
- `job_description`: full JD text string (required, causes 400 if omitted)
- `job_description_id`: JD UUID string
- `latex_content`: read from local .tex file
- `source`: "hermes"

## Cron job setup

User preference: 9AM PDT daily = `0 16 * * *` UTC. Results delivered back to originating Telegram chat.

