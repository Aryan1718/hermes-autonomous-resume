---
id: pool-content-guide
title: Pool Content Guide
sidebar_position: 3
slug: /resume-agent/pool-content-guide
---

# Pool Content Guide

The pool is the evidence base for the entire resume agent. If the pool is thin, stale, or loosely structured, `project-selection` and `point-repointing` have no reliable material to work from.

This is the page to read when you want to know how to add candidate files into the system.

## What the user actually does

For pool setup, the user workflow is simple:

1. Prepare or upload a file describing one project, one OSS contribution, or one work-experience entry.
2. Make sure the file has the correct `type:` and required metadata.
3. Run `pool-intake` so the file is placed into the right location and format on the VPS or wherever Hermes is running.
4. Repeat until the candidate's evidence pool is complete.

The user does not manually place files into `projects/`, `oss/`, or `work-experience/` by hand as part of the normal workflow. `pool-intake` is the skill that makes sure the file lands in the right place on the runtime machine and gets the right initialization files.

This page assumes `profile-bootstrap` has already been run locally and the candidate placeholders have already been replaced. `pool-intake` is the next setup step after that personalization pass.

## The three required content types

All pool content lives under `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/`.

| Content type | Stored under | Used for |
|---|---|---|
| `personal_project` | `projects/<slug>/` | Selectable supporting evidence |
| `oss_contribution` | `oss/<slug>/` | Selectable supporting evidence with third-party validation |
| `work_experience` | `work-experience/<slug>/` | Always included on the resume and tailored later |

## Onboarding sequence

Use this sequence every time you add evidence:

1. Prepare one raw source file.
2. Put `type:` in the header and fill the required metadata for that type.
3. Run `pool-intake`.
4. Let intake create the pool item structure:
   - `raw.md`
   - `idx.md`
   - `versions/`
5. For `personal_project` and `oss_contribution`, update `masters.md`.

After intake, the item is available to the downstream pipeline.

## What to add before running the orchestrator

Before you try `resume-pipeline-orchestrator`, the pool should usually contain:

- all major work experience entries
- the strongest personal projects
- the strongest merged OSS contributions

If the pool is incomplete, the orchestrator will still run, but selection and tailoring quality will be weaker.

## Generated structure

Each item should end up as:

```text
pool/<type-folder>/<slug>/
|- raw.md
|- idx.md
`- versions/
```

`idx.md` starts with `current_version: 0`. `versions/` starts empty. `point-repointing` writes the first version file later.

## Personal projects

### What the file must prove

The file should prove what problem was solved, what was actually built, what the candidate personally owned, and what outcomes are real.

### Mandatory fields

- `type`
- `name`
- `situation`
- `task`
- `action`
- `result`
- `skills`
- `domain`
- `role`
- `date_started`
- `date_ended`
- `metrics`

### What matters downstream

- concrete system details in `action`
- specific ownership in `role`
- measurable evidence in `metrics` or `result`
- enough technical detail for `masters.md` summaries and later bullet tailoring

### Common mistakes

- vague "built an app" language without architecture or decisions
- listing tools without saying how they were used
- omitting role ownership, which weakens seniority framing
- leaving metrics empty when any real numbers exist

## OSS contributions

### What the file must prove

The file should prove externally validated contribution to a real codebase, including what changed and why that contribution matters.

### Mandatory fields

- `type`
- `name`
- `repo`
- `pr_link`
- `merged`
- `merge_date`
- `contribution`
- `skills`
- `codebase_scale`
- `validated_outcome`
- `what_this_proves`

### What matters downstream

- merged state, because unmerged work is not intake-ready
- clear technical change description
- proof of the codebase scope or significance
- honest statement of what this contribution can and cannot prove

### Common mistakes

- trying to intake `merged: false`
- treating OSS as a keyword list instead of a concrete change
- weak outcome language that hides the validation signal
- splitting repeated contributions to the same repo when one combined entry would tell a stronger story

## Work experience

### What the file must prove

The file should prove the full factual reality of the role: scope, systems touched, ownership boundaries, metrics, and what the role can honestly support on a tailored resume.

### Mandatory fields

- `type`
- `name`
- `title`
- `company`
- `dates`
- `employment_type`
- `team_size`
- `reporting_to`
- `everything_done`
- `real_ownership`
- `metrics`
- `what_this_proves`

### What matters downstream

- `everything_done` needs enough detail to support multiple future JD angles
- `real_ownership` keeps the resume honest
- `what_this_proves` helps constrain over-claiming
- work experience is not optional in selection flow because it is always included and tailored later

### Common mistakes

- compressing the role too early instead of preserving full raw detail
- mixing observed team work with personal ownership
- dropping metrics that later could have supported impact-heavy JDs
- creating two entries for one company when the candidate had sequential roles there

## Multi-role companies

If the candidate held multiple sequential roles at the same company, keep them in one `work_experience` pool entry. Use one slug, one `raw.md`, one `idx.md`, and one `versions/` folder. The raw file should show the full date span plus sub-role date lines and separate sections for each phase of the role.

Do not create separate folders for `intern` and `full-time` at the same company when they represent one progression story.

## Keeping `masters.md` in sync

`masters.md` is the selection-facing summary index for `personal_project` and `oss_contribution`.

Rules:

- update it after every successful intake for those two content types
- update it again whenever `raw.md` changes
- keep the `path` field exact, because `point-repointing` later relies on it
- keep titles aligned with the `#` heading in `raw.md`

If `masters.md` goes stale, `project-selection` scores against outdated evidence.

Supporting reference: [Setup > Pool Intake](/docs/setup/pool-intake). Next: [Skill Workflow](/docs/resume-agent/skill-workflow).
