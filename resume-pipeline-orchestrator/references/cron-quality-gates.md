# Cron Quality Gates — June 2026

## Context Management for Sequential Cron Runs

When running 10 JDs sequentially in a single cron session (no subagents), context grows as:

| Component | Size |
|-----------|------|
| Memory injection (fixed) | ~2,000 chars |
| Skills loaded (4-5 skills) | ~30,000-50,000 chars |
| Per JD (raw.md + JD text) | ~10,000-20,000 chars x 10 |
| Turn history | grows with each JD + quality checks |

Mitigation: The 10 JD cap (down from 20) is the primary context control. Quality gates add turns but reduce total context vs. rework.

## Quality Architecture (Defense in Depth)

Three layers prevent quality degradation:

1. Per-bullet checklist (point-repointing 2f) - 6-point check after EACH bullet. Catch errors immediately, not at the end.
2. Per-resume self-review (orchestrator) - Full review before each push. Blocking gate.
3. Mid-run quality gate (after every 3rd JD) - Detects drift early. If bullets getting shorter/generic, re-read raw.md for next JD before proceeding.

## Reference Bullet (Quality Target)

"Deployed a Redis caching layer on AWS with cache refresh controls for a production SaaS platform serving thousands of users, reducing database load by 75% on time-sensitive operational workflows and improving response consistency during traffic spikes."

~285 chars. Named tech (Redis, AWS), specific action, scale (thousands of users), measurable outcome (75% reduction).

## Bullet Standard

- Length: 230-320 chars (target 250-300)
- Bold terms: At least 2 per bullet (technologies, tools, metrics, key concepts)
- No em dashes: Zero -- or (em dash) anywhere
- Structure: Problem -> Action -> Outcome
- Specificity: Must name specific technologies, system names, or exact metrics
