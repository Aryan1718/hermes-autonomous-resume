---
id: system-design
title: System Design
sidebar_position: 1
slug: /architecture/system-design
---

import SourceRepoNote from '@site/src/components/SourceRepoNote';

# System design

Hermes is easiest to understand as a loop of four systems:

1. job intake
2. candidate-aware filtering and tailoring
3. dashboard delivery
4. feedback-driven improvement

This diagram shows the system boundaries and the main handoffs between profiles, backend services, and persistent candidate data.

```mermaid
flowchart LR
  classDef actor fill:#ecfeff,stroke:#0891b2,color:#164e63,stroke-width:1px;
  classDef system fill:#f8fafc,stroke:#94a3b8,color:#0f172a,stroke-width:1px;
  classDef data fill:#fff7ed,stroke:#ea580c,color:#9a3412,stroke-width:1px;

  A[Scraper profile]:::actor
  B[Dashboard / backend]:::system
  C[Resume profile]:::actor
  D[candidate-profile]:::data
  E[Evidence pool]:::data
  F[Feedback review]:::system

  A -->|ingest jobs| B
  D -->|candidate truth| C
  E -->|work, projects, OSS| C
  C -->|fetch JDs / push resumes / log runs| B
  B -->|generated resumes and queue state| F
  F -->|improve candidate facts| D
  F -->|improve evidence quality| E
```

- The scraper and resume agent should stay in separate Hermes profiles.
- `candidate-profile` and the evidence pool feed the resume profile.
- Feedback should improve future inputs, not silently mutate a live run.

## Components

### Job scraper

Finds or receives new job descriptions and sends them into the dashboard.

### Dashboard

Acts as the operational queue and output surface:

- stores incoming JDs
- stores generated resumes
- tracks processed state
- captures human feedback

### Pipeline repository

This repository owns the candidate-aware tailoring logic and output construction.

### Feedback loop

Human review should influence future profile updates, pool improvements, ranking logic, and quality checks.

<SourceRepoNote>
  If you want the actual skills, scraper files, and repository pieces behind this diagram, use the public source repository.
</SourceRepoNote>
