---
id: pool-intake
title: Pool Intake
sidebar_position: 2
slug: /setup/pool-intake
---

# Pool intake

The pool is the evidence base Hermes uses to tailor resumes honestly.

If you want the actual pool-related skill files and file contracts referenced on this page, use the public source repository:

- [hermes-autonomous-resume on GitHub](https://github.com/Aryan1718/hermes-autonomous-resume)

For the full operator walkthrough, use [Resume Agent > Pool Content Guide](/docs/resume-agent/pool-content-guide). This page stays brief on purpose and acts as the shared reference entry point.

## What goes into the pool

- work experience
- personal projects
- OSS contributions

## Why it matters

The pipeline cannot produce strong resumes from weak source material. `project-selection` and `point-repointing` both depend on the pool being structured, complete, and credible.

## How to onboard material

Use:

- `pool-intake` to add new items
- `pool-versioning` to understand the structure and write boundaries

The standard intake result is:

- `raw.md` copied or transformed into the pool item folder
- `idx.md` initialized with `current_version: 0`
- empty `versions/`
- `masters.md` updated for `personal_project` and `oss_contribution`

## Quality bar

The pool should contain enough detail that the system can answer:

- what was built
- why it mattered
- what technologies were actually used
- what results or outputs are provable

If that evidence is absent, the pipeline should stay conservative rather than inventing claims.

Next reading:

- [Resume Agent > Pool Content Guide](/docs/resume-agent/pool-content-guide)
- [Resume Agent > Skill Workflow](/docs/resume-agent/skill-workflow)
