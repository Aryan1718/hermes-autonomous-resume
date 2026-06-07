---
id: system-design
title: System Design
sidebar_position: 1
slug: /architecture/system-design
---

# System design

Hermes is easiest to understand as a loop of four systems:

1. job intake
2. candidate-aware filtering and tailoring
3. dashboard delivery
4. feedback-driven improvement

```mermaid
flowchart LR
  A[Job Scraper] --> B[Dashboard]
  B --> C[resume-pipeline-orchestrator]
  C --> D[Skill pipeline]
  D --> E[Generated resume]
  E --> B
  B --> F[Feedback and review]
  F --> C
```

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
