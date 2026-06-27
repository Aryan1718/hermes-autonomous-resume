---
id: candidate-setup
title: Candidate Setup
sidebar_position: 1
slug: /setup/candidate-setup
---

import SourceRepoNote from '@site/src/components/SourceRepoNote';

# Candidate setup

Candidate setup starts with `profile-bootstrap`.

If you are following the main resume workflow, treat [Resume Agent > Setup Guide](/docs/resume-agent/setup-guide) as the primary onboarding path and use this page as supporting detail for the candidate-specific portion.

This skill exists to prevent users from hand-editing scattered placeholders across the repository. It asks for the minimum inputs the pipeline needs, then writes the candidate-dependent source of truth in one pass.

In practice, this is the first step you run locally before adding the rest of the resume skills to Hermes. Most of the other skills are still reusable templates until this personalization step is complete.

## What profile-bootstrap should collect

- candidate identity and current search scope
- target roles and seniority
- work authorization constraints
- hard disqualifiers
- always-provable skills
- provable-with-framing skills
- strongest signals
- ranked career direction fits
- preferred signals

It can also optionally collect runtime placeholders such as:

- `<PROFILE_SLUG>`
- `<POOL_DIR>`
- `<RESUMES_DIR>`
- `<DASHBOARD_BASE_URL>`
- `<DASHBOARD_API_KEY_ENV>`

## Why candidate-profile matters

`candidate-profile` is the only place candidate-specific filtering and scoring assumptions should live.

That means:

- `jd-prefilter` reads it instead of hard-coding geography or seniority assumptions
- `jd-extraction` uses it for calibration
- `point-repointing` uses it to constrain allowed skills and claims

## Setup rule

Do not let multiple skills invent candidate facts independently. Candidate facts should be entered once and then consumed by the rest of the system.

Continue in the main flow:

- [Resume Agent > Setup Guide](/docs/resume-agent/setup-guide)
- [Resume Agent > Run and Verify](/docs/resume-agent/run-and-verify)

<SourceRepoNote>
  If you want the actual setup skill files referenced on this page, use the public source repository.
</SourceRepoNote>
