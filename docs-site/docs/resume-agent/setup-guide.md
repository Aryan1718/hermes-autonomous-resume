---
id: setup-guide
title: Setup Guide
sidebar_position: 2
slug: /resume-agent/setup-guide
---

import SourceRepoNote from '@site/src/components/SourceRepoNote';

# Resume Agent Setup Guide

Use this page for first-time setup before any JD processing. The goal is to leave the repository in a state where `resume-pipeline-orchestrator` can run without inventing candidate facts or failing on missing runtime config.

## Quick start

If you only want the shortest correct path:

1. Run `profile-bootstrap` locally.
2. Make sure repository placeholders and `candidate-profile/SKILL.md` now contain your real candidate and runtime values.
3. Only then add the rest of the resume skills to Hermes.
4. Set up dashboard auth.
5. Start adding evidence files through `pool-intake`.

Do not start by running the downstream resume skills manually.

## Step 1: Prepare the resume profile and runtime placeholders

Set up the Hermes profile that will own resume generation. Keep the resume workflow isolated from scraping so the profile-specific prompts, pool files, and runtime values stay clean.

Required placeholders to understand before going further:

- `<PROFILE_SLUG>`
- `<POOL_DIR>`
- `<RESUMES_DIR>`
- `<DASHBOARD_BASE_URL>`
- `<DASHBOARD_API_KEY_ENV>`

These resolve to the documented runtime roots:

- Pool root: `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/`
- Resume output root: `/opt/data/profiles/<PROFILE_SLUG>/home/<RESUMES_DIR>/`

If you want the repo personalized in one pass, start with `profile-bootstrap`. This is the correct first action for a new candidate because the rest of the skills are still template-shaped until this step is done. Supporting detail: [Setup > Candidate Setup](/docs/setup/candidate-setup).

## Step 2: Fill `candidate-profile`

This must happen before JD processing.

`candidate-profile` is the only place candidate-specific filtering and scoring assumptions should live. `jd-prefilter`, `jd-extraction`, and `point-repointing` all depend on it. If it still contains placeholders or another person's facts, the rest of the pipeline becomes unreliable immediately.

Recommended path:

1. Run `profile-bootstrap`.
2. Let it replace the candidate and runtime placeholders across the setup files it owns.
3. Confirm `candidate-profile/SKILL.md` now reflects the current candidate's real facts.
4. Re-scan the file for unresolved placeholders and stale candidate content.

This is the main setup action the user performs directly. Until this is complete, the rest of the resume skills should be treated as placeholders or templates rather than ready-to-run candidate skills.

## Step 3: Connect dashboard auth and API requirements

Before the orchestrator can fetch JDs or push resumes, the dashboard side must be reachable and authenticated.

You need:

- a real `<DASHBOARD_BASE_URL>`
- an API key stored under the environment variable named by `<DASHBOARD_API_KEY_ENV>`
- the queue, resume output, and workflow logging endpoints described in [API Reference](/docs/api-reference)

Most important orchestrator-facing endpoints:

- `GET /api/job-descriptions/next`
- `POST /api/generated-resumes`
- `PATCH /api/job-descriptions/:id/use`
- `POST /api/workflow-logs`

Supporting detail: [Setup > Dashboard Integration](/docs/setup/dashboard-integration).

## Step 4: Confirm output and pool locations

Verify that the intended directories are the ones the docs and skills expect:

- pool content under `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/`
- final resumes under `/opt/data/profiles/<PROFILE_SLUG>/home/<RESUMES_DIR>/`
- dashboard API key in `/opt/data/profiles/<PROFILE_SLUG>/.env`

At this point, "ready to run" means:

- the profile is real
- the pool path exists
- the resumes output path is known
- dashboard auth is available
- the evidence pool contains real candidate content

Important: being "ready to run" does not mean "run individual resume skills by hand." It means the repository is ready for evidence intake and then for `resume-pipeline-orchestrator`.

## Step 5: Use `pool-intake` to place evidence where the pipeline expects it

After `profile-bootstrap` is complete and the candidate values are real, start onboarding evidence with `pool-intake`.

`pool-intake` is not just a generic upload step. Its job is to take each user-provided experience, project, or OSS markdown file and place it into the right location and format on the VPS or wherever Hermes is running so the pipeline can use it later.

That means the user should provide source files, then let `pool-intake` create or update the correct item folder instead of manually arranging files by hand.

## Readiness checklist

- `candidate-profile` contains real candidate facts and no required placeholders.
- The repository has been personalized by running `profile-bootstrap` locally before adding the rest of the skills to Hermes.
- Pool root and resume output root are defined using the documented placeholders.
- Dashboard API configuration is in place and matches the [API Reference](/docs/api-reference).
- At least one work-experience entry exists in the pool.
- Personal projects and/or OSS contributions have been onboarded where available.
- You understand that `resume-pipeline-orchestrator` is the normal execution path once setup is complete.
- You understand that `profile-bootstrap` and `pool-intake` are the main user-invoked setup skills before orchestration.

Next: [Pool Content Guide](/docs/resume-agent/pool-content-guide).

<SourceRepoNote>
  If you want the actual files behind names like `candidate-profile/SKILL.md` and the referenced skills, use the public source repository.
</SourceRepoNote>
