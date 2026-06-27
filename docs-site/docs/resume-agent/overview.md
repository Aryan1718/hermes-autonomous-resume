---
id: overview
title: Overview
sidebar_position: 1
slug: /resume-agent/overview
---

import SourceRepoNote from '@site/src/components/SourceRepoNote';

# Resume Agent Overview

The Resume Agent section is the main operator handbook for this repository. Read it top to bottom if you want to configure a candidate, build the evidence pool, run the orchestrator, and verify the output without stitching the workflow together from scattered reference pages.

## The actual user flow

Most users only need to understand three actions:

1. Run `profile-bootstrap` once to set up the candidate and runtime placeholders.
2. Add or upload candidate evidence files and let `pool-intake` place them into the pool correctly.
3. Run `resume-pipeline-orchestrator` to process JDs.

After setup, users should not need to invoke `jd-prefilter`, `jd-extraction`, `project-selection`, `point-repointing`, or `latex-assembly` manually during normal operation. Those are orchestrator-managed stages.

## What the resume agent owns

- Candidate truth in `candidate-profile`
- Pool onboarding and structure for personal projects, OSS contributions, and work experience
- JD processing through `jd-prefilter` and `jd-extraction`
- Evidence selection and tailoring through `project-selection` and `point-repointing`
- Final resume generation through `latex-assembly`
- Dashboard push, workflow logging, and JD queue state through `resume-pipeline-orchestrator`

## Before you start

Confirm all of these before trying to process job descriptions:

- A dedicated Hermes resume profile exists for this workflow.
- Runtime placeholders are resolved where needed: `<PROFILE_SLUG>`, `<POOL_DIR>`, `<RESUMES_DIR>`, `<DASHBOARD_BASE_URL>`, `<DASHBOARD_API_KEY_ENV>`.
- `candidate-profile/SKILL.md` has real candidate facts, not template placeholders.
- Dashboard API auth is configured and the endpoint contracts in [API Reference](/docs/api-reference) are available.
- Evidence files exist for the candidate's work experience, personal projects, and OSS contributions.

## Core operating model

This system is not a monolithic prompt. It is a sequence of skills plus one orchestrator:

1. `profile-bootstrap` helps fill candidate and runtime setup.
2. `candidate-profile` becomes the candidate-specific source of truth.
3. `pool-intake` and `pool-versioning` establish the evidence pool.
4. JD-facing skills process, select, and tailor content.
5. `resume-pipeline-orchestrator` coordinates the run and handles dashboard side effects.

## Read this section in order

If you are trying to understand how to use the system as an operator, follow this order:

1. [Setup Guide](/docs/resume-agent/setup-guide)
2. [Pool Content Guide](/docs/resume-agent/pool-content-guide)
3. [Run and Verify](/docs/resume-agent/run-and-verify)
4. [How It Works](/docs/resume-agent/how-it-works)
5. [Skill Workflow](/docs/resume-agent/skill-workflow)

## Canonical flow

Use this section as the complete Resume Agent handbook:

- [Setup Guide](/docs/resume-agent/setup-guide) for first-time setup
- [Pool Content Guide](/docs/resume-agent/pool-content-guide) for adding evidence
- [Run and Verify](/docs/resume-agent/run-and-verify) for daily usage
- [How It Works](/docs/resume-agent/how-it-works) for the internal pipeline flow
- [Skill Workflow](/docs/resume-agent/skill-workflow) for per-skill contracts

Reference pages under `Setup`, `Pipeline`, and `API Reference` still matter, but they are supporting material after this flow is in place.

<SourceRepoNote>
  If you want the actual skills and repository files referenced in this section, use the public source repository.
</SourceRepoNote>
