# Cron Failure Patterns — June 2026

## Root Cause: Subagent Memory Isolation

The #1 root cause of quality loss: cron subagents do NOT inherit memory or session context. They only have the skill files and the explicit prompt text. All critical rules MUST be encoded in skill files.

## Failure Pattern 1: Short, Generic Bullets

Cron: "Built 4 production AI blueprints with distributed architecture" (generic)
Should be: "Independently built 4 of 15 production AI blueprints from scratch including AccessIQ (MCP-based RBAC/ABAC authorization) and OmniRoute (multi-agent planner with intent classification)"

**Cause:** cron agent didn't read raw.md. Generated from JD text alone.

## Failure Pattern 2: -- Em Dashes Everywhere

Cron: "Orchestrating multi-agent workflow with RBAC/ABAC -- distributed system enforcing data boundaries"
Should be: "Orchestrating the multi-agent workflow layer that enforces RBAC/ABAC access control around protected health information, ensuring each agent only accesses authorized data"

## Failure Pattern 3: Inconsistent Bullet Lengths

Some bullets 120 chars, others 400+. Breaks resume layout.

**Rule:** ALL bullets 230-320 chars (target 250-300). All sections must be consistent.

## Failure Pattern 4: Metadata Headers in .tex

Cron adds "% Company -- Job Title" before \documentclass.
**Rule:** .tex must start with \documentclass{article} on line 1.

## Failure Pattern 5: Double Backslashes in .tex

Writing .tex inline in write_file doubles backslashes.
**Fix:** Use Python raw string script saved to disk, run via terminal.

## Failure Pattern 7: Quality Degradation Over Long Batches

**Discovered:** June 4, 2026. Cron batch cap was 20 JDs. Agent quality degrades significantly after JD #5-7 — bullets get shorter, more generic, and the agent skips re-reading raw.md.

**Fix:** Batch cap reduced from 20 to 10. Added mid-run quality gate: after every 3rd JD, review last resume before continuing. If quality degrading, re-read raw.md for next JD.

**Rule:** Better to produce 10 excellent resumes than 20 mediocre ones. Remaining JDs picked up next day.

## Failure Pattern 8: No Per-Bullet Quality Check

**Discovered:** June 4, 2026. Agent writes all 15 bullets first, then checks quality. By then it's in "assembly mode" and doesn't want to go back and fix.

**Fix:** Per-bullet checklist (6 points) run AFTER EACH bullet. If any check fails, rewrite BEFORE moving to next bullet. Do NOT batch-write first and check later.

Six checks: (1) 230-320 chars, (2) >=2 bold terms, (3) no --, (4) problem->action->outcome, (5) specific not generic, (6) targets JD requirement.

## Failure Pattern 9: Truncated-from-Tailoring Bullets

**Discovered:** June 5, 2026. When rewriting the same bullet for different JDs, the agent drops qualifier words ("production", "large-scale", "across platforms") to shorten it, accidentally undershooting 230 chars.

**Example of the failure:**
- Alps backend: "Developed FastAPI endpoints and Python backend services for order-processing workflows handling large data volumes" (OK, 194 chars without metrics)
- Tailored shorter: "Developed FastAPI endpoints and Python services for order-processing workflows" (FAIL, 120 chars)

**Fix:** After writing every bullet, strip formatting and count raw chars immediately. If under 230, the FIRST fix is to add back dropped specifics (scale, technologies, domain context) — NOT to pad with filler.

**Rule:** Tailoring changes the LEAD and METRIC, not the core. Every bullet's spine (tech + action + outcome) should be the same length across JDs. Only the contextual framing around that spine changes.

## Failure Pattern 10: Python Variable Ordering in Batch Scripts

**Discovered:** June 5, 2026. In multi-section batch scripts, variables used by list literals must be defined BEFORE the list. Python evaluates f-strings at list-definition time, not at use time.

```python
# WRONG — NameError: name 'DATE' is not defined
idx_entries = [
    (folder, f"### v{ver} --- {slug}\n{DATE} | {COMPANY}\n")
]
COMPANY = "Acme"
DATE = "2026-06-05"

# RIGHT — define constants before any list that uses them
COMPANY = "Acme"
DATE = "2026-06-05"
idx_entries = [
    (folder, f"### v{ver} --- {slug}\n{DATE} | {COMPANY}\n")
]
```

## Reference Bullet (Quality Target)

Use this ~285-char bullet as the quality reference for every bullet you write:

"Deployed a Redis caching layer on AWS with cache refresh controls for a production SaaS platform serving thousands of users, reducing database load by 75% on time-sensitive operational workflows and improving response consistency during traffic spikes."

Every bullet should have: named technologies, specific action, scale, and measurable outcome.
