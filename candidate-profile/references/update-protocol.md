# Candidate Profile — Update Protocol

## When to Update

When something changes — a new role, a new skill proven in production, a shift in career direction, a new hard constraint — update the relevant section and append a short note to the Change Log with the date and what changed.

## Update Protocol (Major Overhauls)

1. **Re-read ALL pool raw.md files** before editing. Never carry forward project names, company names, or role details from a previous profile version — the pool is the source of truth.
2. **Ask clarifying questions in a single batch** after reading. Don't write until the user confirms the plan.
3. **Cross-check all dates** (graduation, role start/end dates) against what the user actually told you — don't assume from the previous version.
4. **After writing the profile, scan `home/<RESUMES_DIR>/*.tex`** for any generated resume files that contain the old data (especially dates and role names) and update them too. The profile skill and the generated resumes must stay in sync.
5. **Update memory** if role dates or graduation date changed — memory entries are injected into every session and stale dates there will cause repeated errors.

## Bulk-Update Protocol

When the user asks to refresh or overhaul this profile (e.g. "update this skill with my current context"), follow this sequence — **do not skip steps**:

1. **Read all source data first.** Load every `raw.md` from `workspace/pool/` (work-experience, projects, oss) via `read_file`. Also load `memory` facts about the user. Do this before asking anything.
2. **Ask clarifying questions.** Identify gaps, stale entries, and ambiguities. Ask the user — do not guess. Present questions in a single focused batch.
3. **Confirm the plan.** Summarize what you understood and what you plan to change. Get user confirmation before writing.
4. **Execute all edits.** Use `patch` for targeted edits across sections. Group related changes. Verify the final file.
5. **Update the Change Log.** Append one entry per session covering what changed and why.

