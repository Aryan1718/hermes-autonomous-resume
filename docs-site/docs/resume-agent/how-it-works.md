---
id: how-it-works
title: How It Works
sidebar_position: 5
slug: /resume-agent/how-it-works
---

import SourceRepoNote from '@site/src/components/SourceRepoNote';

# How It Works

The resume agent is a staged workflow, not one long prompt. It reads candidate truth from `candidate-profile`, pulls evidence from the pool, processes one JD at a time, and writes only at the stages that are supposed to persist state.

For live runs, treat `resume-pipeline-orchestrator` as the operational source of truth for control flow. In the current repo contract, JDs are fetched in a batch, then processed sequentially; JDs that are disqualified, fail the binary gate, or score below `40` are skipped, and JDs at `40+` continue downstream one at a time.

## End-to-end flow

1. Run `profile-bootstrap` for a new candidate to establish the candidate profile and runtime placeholders.
2. Confirm `candidate-profile/SKILL.md` is filled with the current candidate's real facts.
3. Add evidence into the pool with `pool-intake`.
4. Fetch unprocessed JDs through `resume-pipeline-orchestrator`.
5. Run `jd-prefilter` to skip obvious non-fits quickly.
6. Run `jd-extraction` on passing JDs.
7. Run `project-selection` against `masters.md` to choose 3 supporting projects or OSS items.
8. Run `point-repointing` to tailor selected projects plus all work experience.
9. Run `latex-assembly` to produce the final `.tex`.
10. Run the orchestrator self-review gate.
11. Push the resume, mark the JD processed, and log the run.

## Write boundaries

- Read-only stages: `candidate-profile`, `jd-prefilter`, `jd-extraction`, `project-selection`
- Pool-writing stage: `point-repointing`
- Resume-writing stage: `latex-assembly` plus local `.tex` save
- Dashboard API stage: `resume-pipeline-orchestrator`

## Operator flow

For a new operator, the flow starts with candidate setup, then evidence intake, then orchestration.

```mermaid
flowchart LR
  classDef setup fill:#ecfeff,stroke:#0891b2,color:#164e63,stroke-width:1px;
  classDef runtime fill:#ccfbf1,stroke:#0f766e,color:#134e4a,stroke-width:1px;
  classDef output fill:#fff7ed,stroke:#ea580c,color:#9a3412,stroke-width:1px;

  A[profile-bootstrap]:::setup
  B[candidate-profile]:::setup
  C[pool-intake]:::setup
  D[resume-pipeline-orchestrator]:::runtime
  E[Generated resume]:::output
  F[Dashboard review]:::output

  A --> B --> C --> D --> E --> F
```

- `profile-bootstrap` is the first setup action.
- `candidate-profile` must be real before JD processing.
- `pool-intake` prepares evidence for downstream tailoring.

## Internal orchestration

Inside the orchestrator, the run becomes a stage-by-stage execution flow with API side effects and structured candidate inputs.

```mermaid
flowchart TD
  classDef input fill:#f8fafc,stroke:#94a3b8,color:#0f172a,stroke-width:1px;
  classDef stage fill:#ecfeff,stroke:#0891b2,color:#164e63,stroke-width:1px;
  classDef api fill:#fff7ed,stroke:#ea580c,color:#9a3412,stroke-width:1px;

  A[GET next JD]:::api --> B[jd-prefilter]:::stage
  B -->|skip| C[POST workflow log]:::api
  B -->|pass| D[jd-extraction]:::stage
  D --> E[project-selection]:::stage
  E --> F[point-repointing]:::stage
  F --> G[latex-assembly]:::stage
  G --> H[Save .tex]:::api
  H --> I[Self-review]:::stage
  I -->|pass| J[POST generated resume]:::api
  J --> K[PATCH JD use]:::api
  K --> L[POST workflow log]:::api

  M[candidate-profile]:::input --> B
  M --> D
  M --> F
  N[Pool evidence]:::input --> E
  N --> F
```

- `candidate-profile` provides candidate-specific truth.
- Pool evidence supports selection and tailoring.
- API calls happen at fetch, push, status update, and logging boundaries.

## What writes where

| Stage | Writes files? | Calls dashboard APIs? | Output |
|---|---|---|---|
| `candidate-profile` | No | No | Candidate truth |
| `pool-intake` | Yes | No | `raw.md`, `idx.md`, `versions/`, optionally `masters.md` |
| `jd-prefilter` | No | No | Pass/skip decision and score |
| `jd-extraction` | No | No | JD extraction artifact |
| `project-selection` | No | No | 3 selected projects/OSS items |
| `point-repointing` | Yes | No | New version files and updated `idx.md` |
| `latex-assembly` | No pool writes; produces `.tex` content for save | No | Resume LaTeX |
| `resume-pipeline-orchestrator` | Saves `.tex` locally | Yes | Resume push, PATCH `/use`, workflow logs |

Continue to [Setup Guide](/docs/resume-agent/setup-guide) for the first-time operator path. That setup page should be read before this one by a new operator.

<SourceRepoNote>
  If you want the actual skills and file contracts behind this flow, use the public source repository.
</SourceRepoNote>
