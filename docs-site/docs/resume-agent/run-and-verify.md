---
id: run-and-verify
title: Run and Verify
sidebar_position: 6
slug: /resume-agent/run-and-verify
---

# Run and Verify

Once setup is complete, the normal path is to run `resume-pipeline-orchestrator`. This page explains both the manual mental model and the outputs you should verify after a run.

## The normal user path

After setup, this is the intended operating flow:

1. Run `profile-bootstrap` once for the candidate.
2. Add all candidate evidence through `pool-intake`.
3. Run `resume-pipeline-orchestrator`.

That orchestrator run can happen in two ways:

- manual run, when you want to process JDs on demand
- cron job, when you want the system to process JDs automatically on a schedule

In normal usage, the orchestrator is the only runtime skill the user needs to invoke for JD processing.

## What you should not do in normal usage

Do not manually chain:

- `jd-prefilter`
- `jd-extraction`
- `project-selection`
- `point-repointing`
- `latex-assembly`

Those are internal pipeline stages. They are useful for debugging or development, but not for the normal operator workflow.

## Manual understanding of the run

The stepwise path is:

1. confirm `candidate-profile`
2. confirm the pool is ready
3. fetch unprocessed JDs
4. prefilter
5. skip JDs that are disqualified, fail the binary gate, or score below `40`
6. extract
7. select 3 projects or OSS items
8. repoint those items plus all work experience
9. assemble LaTeX
10. run self-review
11. push, PATCH, and log

This is useful when you are debugging one stage or validating the workflow contract.

## Recommended normal path

For day-to-day operation, use `resume-pipeline-orchestrator`. It is the canonical entry point for live JD processing because it:

- fetches the batch
- coordinates the downstream skills in order
- saves the `.tex`
- pushes to the dashboard
- handles PATCH `/use`
- logs skipped, failed, and successful outcomes

## Recommended operator instructions

### Manual mode

Use this when you want to run the resume pipeline yourself:

1. Confirm setup is complete.
2. Confirm the evidence pool is populated.
3. Run `resume-pipeline-orchestrator`.
4. Check the outputs listed below.

### Cron mode

Use this when you want the system to run on a schedule:

1. Confirm setup is complete.
2. Confirm the evidence pool is populated.
3. Schedule `resume-pipeline-orchestrator` with your cron job or equivalent scheduler.
4. Check workflow logs and generated resume outputs after runs.

## Expected outputs

After a successful run, expect to see:

- updated version files under the selected project, OSS, and work-experience `versions/` folders
- updated `idx.md` files for the touched pool items
- a saved `.tex` file under `/opt/data/profiles/<PROFILE_SLUG>/home/<RESUMES_DIR>/`
- a successful dashboard resume push via [Resume Output APIs](/docs/api-reference/resume-output-apis)
- the JD marked processed via [Job Description APIs](/docs/api-reference/job-description-apis)
- workflow logs recorded via [Workflow Logging APIs](/docs/api-reference/workflow-logging-apis)

## Verification checklist

- The saved `.tex` starts with `\documentclass{article}` on line 1.
- The `.tex` does not contain broken double backslashes where single LaTeX commands were expected.
- The self-review gate passed the bullet quality checks, including length and specificity.
- The dashboard push succeeded.
- PATCH `/api/job-descriptions/:id/use` succeeded, or if it failed, the run was logged as a success-with-warning state and the JD was left for manual review.
- The workflow log reflects whether the JD was skipped, failed, or completed.

## Failure modes to expect

### Missing candidate profile

`jd-prefilter` should stop rather than infer candidate facts from the JD.

### Weak or incomplete pool evidence

`project-selection` and `point-repointing` can only be as strong as the source material. Thin raw files produce thin tailored bullets.

### Skipped JDs from prefilter

This is expected behavior for out-of-scope roles, failed binary gates, or low-scoring matches under the orchestrator threshold. Skipped JDs should be logged, not forced through the full pipeline.

### Push succeeds but PATCH fails

This is an administrative follow-up issue, not a content-generation failure. The resume exists on the dashboard, but the JD may still appear unprocessed until the PATCH issue is resolved.

### Stale `masters.md`

If `masters.md` no longer matches the current `raw.md` files, `project-selection` may pick the wrong evidence set.

## Final operator check

If the Resume Agent section has been followed in order, you should be able to understand and run the system without depending on the `Setup` or `Pipeline` sections for missing core steps. Use those sections as reference depth, not as the primary onboarding path.
