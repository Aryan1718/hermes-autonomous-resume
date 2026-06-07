---
id: candidate-setup
title: Candidate Setup
sidebar_position: 1
slug: /setup/candidate-setup
---

# Candidate setup

Candidate setup starts with `profile-bootstrap`.

This skill exists to prevent users from hand-editing scattered placeholders across the repository. It asks for the minimum inputs the pipeline needs, then writes the candidate-dependent source of truth in one pass.

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
