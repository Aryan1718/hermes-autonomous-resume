---
id: overview
title: Pipeline Overview
sidebar_position: 1
slug: /pipeline/overview
---

# Pipeline overview

The Hermes resume pipeline is a staged process that narrows, enriches, and tailors information rather than trying to produce a final resume in one jump.

```mermaid
flowchart TD
  A[candidate-profile] --> B[jd-prefilter]
  C[Pool] --> D[project-selection]
  B -->|Pass| E[jd-extraction]
  E --> D
  D --> F[point-repointing]
  A --> F
  C --> F
  F --> G[latex-assembly]
  G --> H[Self-review gate]
  H --> I[Push to dashboard]
```

## Stage purposes

- `jd-prefilter`: reject obvious bad fits quickly
- `jd-extraction`: turn raw JD text into structured downstream signals
- `project-selection`: pick the best supporting evidence
- `point-repointing`: reshape bullets toward the JD without inventing facts
- `latex-assembly`: build the final resume artifact

## Why this split works

Each stage reduces one failure mode:

- prefilter reduces wasted compute on bad roles
- extraction reduces vague JD interpretation
- selection reduces irrelevant proof points
- repointing reduces generic resumes
- assembly reduces format drift
