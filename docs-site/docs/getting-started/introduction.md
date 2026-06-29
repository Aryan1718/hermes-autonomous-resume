---
id: introduction
title: Introduction
sidebar_position: 1
slug: /getting-started/introduction
---

import SourceRepoNote from '@site/src/components/SourceRepoNote';

# Hermes Resume Agent

<div className="docBadge">Getting Started</div>

<div className="docIntro">
  <p>
    This documentation explains how to use the Hermes agentic framework to build a resume agent that generates tailored resumes from personal knowledge, including work experience, projects, and open-source contributions.
  </p>

  <p>
    The system follows a straightforward workflow. A scraper agent collects new jobs on a schedule, typically in the morning. After that, the resume agent runs the full pipeline for each scraped job description, generates a tailored resume, and pushes the result to the dashboard.
  </p>

  <p>
    The dashboard used in this setup is a custom implementation, but it can be replaced with any equivalent interface. What matters is that the required backend API contracts are available and integrated correctly. This documentation will include a dedicated section for each API so those integration points can be referenced clearly during implementation.
  </p>

  <p>
    If your dashboard or workflow needs a separate LaTeX-to-PDF conversion step, use the external LaTeX Resume Engine docs at <a href="https://latex-resume-engine.onrender.com/docs" target="_blank" rel="noreferrer">latex-resume-engine.onrender.com/docs</a>. That service takes generated LaTeX resume content and returns a PDF.
  </p>

  <p>
    This resume system uses multiple Hermes skills internally, but the operator workflow is simpler than that. Users first run <code>profile-bootstrap</code> locally to replace placeholders with their actual candidate and runtime values, then use <code>pool-intake</code> to place experience, project, and OSS markdown files into the right runtime location and format, and then run <code>resume-pipeline-orchestrator</code> manually or on a cron schedule.
  </p>

  <p>
    The goal of these docs is to show how a Hermes-based resume system can be built, deployed on private infrastructure, and adapted to different workflows.
  </p>
</div>

## Why Hermes

The main reason for using Hermes here is its self-learning loop. Over time, the resume agent can use feedback from generated resumes to improve how it writes, what it emphasizes, and how well it aligns with stronger ATS outcomes. That makes Hermes a good fit for a system that is meant to improve over the long run rather than produce one-off outputs.

Hermes is also useful because it follows instructions well. In this resume workflow, that matters because the agent should stay grounded in real candidate information and avoid fabricating experience, achievements, or skills that are not actually supported by the source material.

## How it works

You can run this resume system in two ways, depending on how automated you want the workflow to be.

- Set up a cron job to run the pipeline on a schedule, such as every morning after new job descriptions have been collected.
- Run the pipeline manually whenever you want to process a job description batch on demand.

In both cases, the flow stays the same: the system reads candidate knowledge, takes scraped or provided job descriptions, runs the resume pipeline through the orchestrator, generates tailored resumes, and pushes the results to the dashboard.

The important usability rule is: users do not normally invoke every downstream resume skill one by one. First personalize the repo with `profile-bootstrap`, then let the orchestrator handle the internal sequence.

<div className="flowBlock">

This is the normal operator flow for the resume system.

```mermaid
flowchart LR
  classDef setup fill:#ecfeff,stroke:#0891b2,color:#164e63,stroke-width:1px;
  classDef runtime fill:#ccfbf1,stroke:#0f766e,color:#134e4a,stroke-width:1px;
  classDef output fill:#fff7ed,stroke:#ea580c,color:#9a3412,stroke-width:1px;

  A[profile-bootstrap<br/>set up candidate]:::setup
  B[pool-intake<br/>add evidence]:::setup
  C[resume-pipeline-orchestrator<br/>run pipeline]:::runtime
  D[Tailored resume]:::output
  E[Dashboard]:::output

  A --> B --> C --> D --> E
```

</div>

- Start with `profile-bootstrap` locally so the placeholders are replaced before the other skills are added to Hermes.
- Add candidate evidence through `pool-intake`, which places the user's markdown files into the right runtime location and format.
- Use `resume-pipeline-orchestrator` as the normal runtime entry point.

## Skills

This resume system uses a small set of focused skills to move a job description through the pipeline. Each skill handles one part of the flow, and the orchestrator ties them together so the run can happen consistently whether it is scheduled or manual.

Core skills in this setup include:

- a scraper-profile skill that can invoke `scraper/jobright.py` for prompts like `scrape 20 jobs`
- scraper utilities such as `scraper/jobright.py` and `scraper/tiny_fish_job_description.py`
- API-related skills for dashboard and backend integration
- candidate and evidence skills for storing personal knowledge
- resume-generation skills for processing job descriptions and creating tailored resumes
- `resume-pipeline-orchestrator` for running the whole pipeline

## Deployment

In the reference setup documented here, the system runs on a Hostinger VPS, the agents are deployed there, and OpenRouter is used for model access.

The scraper, resume pipeline, and API integrations are documented here so the same approach can be reused in other environments.

## What you can build

- Building your own Hermes-style resume bot
- Running automated resume generation from scraped jobs
- Managing the workflow through reusable skills
- Deploying the agents on your own VPS
- Connecting the system to your own dashboard or backend

## Start here

Choose the route that matches what you want to do next.

<div className="docGrid">
  <a className="docCardLink" href="/docs/getting-started/installation">
    <h3>Installation</h3>
    <p>Install the docs site locally and understand the runtime prerequisites for the pipeline.</p>
  </a>
  <a className="docCardLink" href="/docs/resume-agent/setup-guide">
    <h3>Resume Agent Setup</h3>
    <p>Follow the main onboarding path for profile setup, pool prep, and run readiness.</p>
  </a>
  <a className="docCardLink" href="/docs/resume-agent/pool-content-guide">
    <h3>Pool Content Guide</h3>
    <p>Load work history, projects, and OSS evidence in the structure the pipeline expects.</p>
  </a>
  <a className="docCardLink" href="/docs/resume-agent/how-it-works">
    <h3>How It Works</h3>
    <p>See the end-to-end flow from candidate profile and pool content to dashboard push.</p>
  </a>
  <a className="docCardLink" href="/docs/pipeline/orchestrator">
    <h3>Orchestrator</h3>
    <p>Understand how the end-to-end batch runner coordinates the skills and dashboard calls.</p>
  </a>
  <a className="docCardLink" href="/docs/architecture/system-design">
    <h3>System Design</h3>
    <p>View the bigger Hermes loop: scraper, dashboard, pipeline, and feedback.</p>
  </a>
</div>

<SourceRepoNote>
  If you want the actual repository files and skill contracts referenced throughout these docs, use the public source repository.
</SourceRepoNote>
