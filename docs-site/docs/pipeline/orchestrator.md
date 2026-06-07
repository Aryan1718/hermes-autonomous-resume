---
id: orchestrator
title: Orchestrator
sidebar_position: 3
slug: /pipeline/orchestrator
---

# Orchestrator

`resume-pipeline-orchestrator` is the execution layer that ties the skills together for live JD processing.

## Responsibilities

- fetch unprocessed job descriptions from the dashboard
- load `candidate-profile`
- run `jd-prefilter`
- run the deeper pipeline for passing JDs
- save and push final resumes
- mark successful JDs as processed
- log failures and skipped items

## Control flow

```mermaid
flowchart TD
  A[Fetch JD batch] --> B[jd-prefilter]
  B -->|Skip| C[Log skipped JD]
  B -->|Pass| D[jd-extraction]
  D --> E[project-selection]
  E --> F[point-repointing]
  F --> G[latex-assembly]
  G --> H[Save .tex]
  H --> I[Self-review]
  I -->|Pass| J[Push resume]
  J --> K[Mark JD processed]
  I -->|Fail| L[Fix or skip]
```

## Important rule

The orchestrator should consume candidate-specific truth from `candidate-profile`. It should not introduce its own hidden assumptions about location, sponsorship, seniority, or role fit.
