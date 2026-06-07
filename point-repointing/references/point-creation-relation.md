# Relationship to Point-Creation Skill

## Division of Labor

| | **`point-creation` skill** | **This guide (point-repointing)** |
|---|---|---|
| **Question it answers** | "What makes a good point?" | "How do I aim a point at *this* JD?" |
| **Scope** | Constant — true for every resume, every JD | Per-run — changes with every JD |
| **JD-aware?** | No. No concept of a job description. | Yes. The JD drives every decision. |

**This guide is the driver. The `point-creation` skill is the library it calls into.**

When this guide needs to construct or compress a bullet — apply the quality bar, choose STAR vs XYZ vs CAR, surface numbers — it defers to the `point-creation` skill. What this guide adds *on top* is the JD-awareness layer: the aim list, verb mirroring, coverage-driven emphasis, seniority calibration, and the honesty gate.

**Rule of delegation:** whenever a decision is about *bullet craft*, follow `point-creation`. Whenever a decision is about *what to aim at*, follow this guide.

## Lazy-Loading Strategy

The full `point-creation` skill is ~550 lines. Loading it all upfront when only the formatting rules are routinely needed wastes context budget.

**Always have in context:** the formatting rules (no em dashes, bold numbers/keywords, 230-320 chars, story flow) — these are applied to every bullet.

**Load STAR/XYZ/CAR deep-dive files only when needed:** if a bullet's structure is unclear, if the agent can't decide between two methods, or if a bullet draft feels weak after the first pass. Load via: `skill_view(name='point-creation', file_path='references/STAR.md')` etc.

**Full skill load:** only if there's a quality issue the formatting rules alone can't resolve.

This keeps ~400 lines of craft reference files out of context during routine re-pointing.

## Reference Convention

Always use skill-name-only references, never hardcoded file paths:
- ✅ `` `point-creation` `` — agent resolves via `skill_view(name='point-creation')`
- ✅ `` `candidate-profile` `` — agent resolves via `skill_view(name='candidate-profile')`
- ✅ `` `pool-versioning` `` — agent resolves via `skill_view(name='pool-versioning')`
- ✗ `` `skills/point-creation/SKILL.md` `` — never use hardcoded paths

Use absolute paths only for system-level things: `/opt/data/profiles/<PROFILE_SLUG>/.env`, `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/`, `/opt/data/profiles/<PROFILE_SLUG>/home/<RESUMES_DIR>/`.

