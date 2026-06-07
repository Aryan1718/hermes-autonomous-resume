---
name: profile-bootstrap
description: Use when a user wants to initialize or refresh this resume pipeline for a specific person. Ask for the minimum required candidate and optional environment inputs, fill candidate-profile with real data, and replace any requested runtime placeholders needed by downstream skills.
---

# Profile Bootstrap

Use this skill when the user wants to set up the repository for a real candidate instead of leaving it as a reusable template.

This skill owns the initial interview and the writeback step for candidate-dependent configuration.

## What This Skill Fills

Required:
- `candidate-profile/SKILL.md`

Optional, only if the user wants environment-specific setup:
- orchestrator-facing placeholders such as `<PROFILE_SLUG>`, `<POOL_DIR>`, `<RESUMES_DIR>`, `<DASHBOARD_BASE_URL>`, and `<DASHBOARD_API_KEY_ENV>` in runtime/docs files that are meant to be personalized

## Read Order

1. Read `candidate-profile/SKILL.md`.
2. Read `candidate-profile/references/update-protocol.md`.
3. If the user also wants environment/runtime setup, read `resume-pipeline-orchestrator/SKILL.md` and `references/write-targets.md`.
4. Read `references/question-groups.md` before asking questions.

Do not bulk-read unrelated skill folders.

## Operating Rules

- Treat `candidate-profile` as the source of truth for all candidate-specific filtering and ranking logic.
- Do not invent facts, infer identity details from old content, or carry forward another candidate's assumptions.
- Ask only for fields that are required to make the current pipeline usable.
- Batch related questions together to reduce back-and-forth.
- If an answer is missing, keep a clearly marked placeholder only where the user explicitly declined to answer or truly does not know yet.
- When rewriting the profile, replace old candidate content in one pass. Do not mix two candidates in the same file.

## Interview Flow

Run the interview in this order:

1. Core identity and search scope
2. Role fit and seniority
3. Work authorization and hard disqualifiers
4. Provable skills and strongest signals
5. Career direction and preferred signals
6. Optional environment/runtime settings

Use the exact field list and batching guidance in `references/question-groups.md`.

## Writeback Tasks

### A. Candidate Profile

After collecting answers:

1. Rewrite `candidate-profile/SKILL.md` so it describes the current candidate with real facts.
2. Fill these sections completely:
   - Identity Snapshot
   - Target Roles
   - Seniority
   - Location
   - Work Authorization
   - Hard Disqualifiers
   - Always Provable
   - Provable with Framing
   - Strongest Signals
   - Career Direction
   - Preferred Signals
   - Industry Restrictions
   - Compensation
3. Keep evaluator-facing language. Do not write in first person.
4. Use concise evidence-backed content rather than generic self-description.

### B. Environment and Runtime Placeholders

Only do this when the user explicitly wants the repository personalized beyond `candidate-profile`.

If provided, apply the environment values to the files listed in `references/write-targets.md`:
- profile slug
- pool directory name
- resumes directory name
- dashboard base URL
- dashboard API key env var name

Do not touch unrelated placeholders.

## Validation

Before finishing:

1. Scan `candidate-profile/SKILL.md` for unresolved required placeholders.
2. Confirm no stale facts from a previous candidate remain in the rewritten profile.
3. If environment setup was requested, scan the touched files for unresolved copies of the specific runtime placeholders the user asked to fill.
4. Summarize what was written and what remains intentionally unset.

## When To Stop And Ask

Stop and ask the user only if:
- the current candidate's facts are too incomplete to write a minimally usable profile
- two answers conflict materially
- the user wants environment-specific setup but does not know which runtime values should be written

Otherwise, proceed with reasonable structure and write the files.

## References

- `references/question-groups.md` - question batches and minimum field list
- `references/write-targets.md` - optional runtime placeholders and where they live
