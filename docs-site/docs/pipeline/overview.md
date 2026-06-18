---
id: overview
title: Pipeline Overview
sidebar_position: 1
slug: /pipeline/overview
---

# Pipeline overview

The Hermes resume pipeline is a staged process that narrows, enriches, and tailors information rather than trying to produce a final resume in one jump.

For the operator-facing walkthrough, use [Resume Agent](/docs/resume-agent/overview). This page is the compact internal pipeline reference.

```mermaid
flowchart TD
  O[resume-pipeline-orchestrator] --> A[Fetch unprocessed JDs]
  P[candidate-profile] --> B[jd-prefilter]
  A --> B
  B -->|Disqualified / failed binary / score < 40| C[Skip and log]
  B -->|Score >= 40| D[jd-extraction]
  P --> D
  E[Pool projects + OSS evidence] --> F[project-selection]
  D --> F
  P --> F
  P --> G[point-repointing]
  D --> G
  F --> G
  H[All work experience] --> G
  G --> I[latex-assembly]
  I --> J[Self-review gate]
  J --> K[Push to dashboard]
```

## Stage purposes

- `resume-pipeline-orchestrator`: fetch JDs, call downstream stages, and handle push and logging
- `jd-prefilter`: reject obvious bad fits quickly
- `jd-extraction`: turn raw JD text into structured downstream signals
- `project-selection`: choose supporting projects and OSS evidence only
- `point-repointing`: tailor selected projects plus all work experience without inventing facts
- `latex-assembly`: build the final resume artifact

## Why this split works

Each stage reduces one failure mode:

- prefilter reduces wasted compute on bad roles
- extraction reduces vague JD interpretation
- selection reduces irrelevant project evidence
- repointing reduces generic resumes
- assembly reduces format drift

See also:

- [Resume Agent > Skill Workflow](/docs/resume-agent/skill-workflow)
- [Resume Agent > Run and Verify](/docs/resume-agent/run-and-verify)
