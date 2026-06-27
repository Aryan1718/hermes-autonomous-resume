---
id: pool-intake
title: Pool Intake
sidebar_position: 2
slug: /setup/pool-intake
---

import SourceRepoNote from '@site/src/components/SourceRepoNote';

# Pool intake

The pool is the evidence base Hermes uses to tailor resumes honestly.

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

Run this after `profile-bootstrap` has already been used to replace candidate placeholders locally. At that point, `pool-intake` becomes the normal way to take the user's experience, project, or OSS markdown files and place them into the right location and format on the VPS or wherever Hermes is running.

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

<SourceRepoNote>
  If you want the actual pool-related skill files and file contracts referenced on this page, use the public source repository.
</SourceRepoNote>
