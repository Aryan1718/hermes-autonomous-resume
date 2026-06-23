---
id: first-run
title: First Run
sidebar_position: 3
slug: /getting-started/first-run
---

# First-run checklist

Before running the orchestrator for the first time, make sure the repository is configured for a real candidate rather than left in template mode.

If you want to inspect the actual skill files named on this page, use the public source repository:

- [hermes-autonomous-resume on GitHub](https://github.com/Aryan1718/hermes-autonomous-resume)

## Required steps

1. Run `profile-bootstrap`.
2. Confirm `candidate-profile/SKILL.md` contains real candidate data.
3. Load the pool with real work experience, projects, and OSS material using `pool-intake`.
4. Fill any runtime placeholders the orchestrator depends on if you plan to use dashboard/API integration.
5. Verify that `jd-prefilter` and `resume-pipeline-orchestrator` are reading the current candidate profile, not stale template content.

## Readiness criteria

The system is minimally ready when:

- `candidate-profile` no longer contains unresolved required placeholders
- the pool contains enough evidence to support resume tailoring
- the orchestrator's runtime values are known
- the dashboard has job descriptions available for processing

## First live sequence

```text
profile-bootstrap
-> pool-intake
-> candidate-profile review
-> resume-pipeline-orchestrator
```

## Common failure mode

The most common bad setup is trying to run `resume-pipeline-orchestrator` while `candidate-profile` is still a template. That pushes the whole system into fake assumptions early and weakens every downstream step.
