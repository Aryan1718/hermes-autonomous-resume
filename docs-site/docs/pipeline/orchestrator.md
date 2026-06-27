---
id: orchestrator
title: Orchestrator
sidebar_position: 3
slug: /pipeline/orchestrator
---

import SourceRepoNote from '@site/src/components/SourceRepoNote';

# Orchestrator

`resume-pipeline-orchestrator` is the execution layer that ties the skills together for live JD processing.

For the full operator path, see [Resume Agent > Run and Verify](/docs/resume-agent/run-and-verify). This page stays focused on the orchestrator's role inside the broader pipeline.

## Responsibilities

- fetch unprocessed job descriptions from the dashboard
- load `candidate-profile`
- skip JDs that are disqualified, fail the binary gate, or score below `40`
- run `jd-extraction`, `project-selection`, `point-repointing`, and `latex-assembly` sequentially for JDs scoring `40+`
- save the generated `.tex` locally
- run the mandatory self-review gate before any push
- push successful resumes, PATCH `/use`, and log outcomes

## Control flow

This is the control flow the orchestrator owns during a live JD-processing run.

```mermaid
flowchart TD
  classDef fetch fill:#f8fafc,stroke:#94a3b8,color:#0f172a,stroke-width:1px;
  classDef process fill:#ecfeff,stroke:#0891b2,color:#164e63,stroke-width:1px;
  classDef output fill:#fff7ed,stroke:#ea580c,color:#9a3412,stroke-width:1px;

  A[Fetch JD batch]:::fetch --> B[Prefilter]:::process
  B -->|skip| C[Log skipped JD]:::output
  B -->|pass| D[Extract JD]:::process
  D --> E[Select supporting evidence]:::process
  E --> F[Tailor resume content]:::process
  F --> G[Assemble LaTeX]:::process
  G --> H[Save .tex]:::output
  H --> I[Self-review]:::process
  I -->|pass| J[Push resume]:::output
  J --> K[PATCH /use]:::output
  K --> L[Log success]:::output
  I -->|fail| M[Fix or skip]:::output
  M --> N[Log outcome]:::output
```

- The orchestrator is the runtime entry point.
- Users should not manually chain downstream stages in normal operation.
- Success and failure paths both end in logging.

## Important rule

The orchestrator should consume candidate-specific truth from `candidate-profile`. It should not introduce its own hidden assumptions about location, sponsorship, seniority, or role fit.

Manual one-off debugging can invoke individual skills directly, but normal JD processing should start with `resume-pipeline-orchestrator` only.

<SourceRepoNote>
  If you want the actual orchestrator and downstream skill files referenced here, use the public source repository.
</SourceRepoNote>
