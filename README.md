<h1 align="center">Hermes Autonomous Resume</h1>

<p align="center">
  A Hermes-based job application system with a scraper agent and a resume agent that generates resumes customized to each job description.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/framework-Hermes-0f766e?style=for-the-badge" alt="Hermes">
  <img src="https://img.shields.io/badge/models-OpenRouter-e11d48?style=for-the-badge" alt="OpenRouter">
  <img src="https://img.shields.io/badge/deploy-Hostinger%20VPS-2563eb?style=for-the-badge" alt="Hostinger VPS">
  <img src="https://img.shields.io/badge/interface-Custom%20Dashboard-475569?style=for-the-badge" alt="Custom Dashboard">
  <img src="https://img.shields.io/badge/output-LaTeX%20%26%20PDF-7c3aed?style=for-the-badge" alt="LaTeX and PDF">
  <img src="https://img.shields.io/badge/docs-Docusaurus-16a34a?style=for-the-badge" alt="Docusaurus">
  <img src="https://img.shields.io/badge/docs%20hosted-Vercel-111827?style=for-the-badge" alt="Vercel">
</p>

<p align="center">
  <a href="https://hermes-autonomous-resume.vercel.app/docs/getting-started/introduction">Docs</a> &bull;
  <a href="https://hermes-autonomous-resume.vercel.app/docs/resume-agent/overview">Resume Agent</a> &bull;
  <a href="https://hermes-autonomous-resume.vercel.app/docs/scraper-agent/overview">Scraper Agent</a> &bull;
  <a href="https://hermes-autonomous-resume.vercel.app/docs/architecture/system-design">Architecture</a>
</p>

The system is designed to run continuously. The scraper agent can run on a schedule to collect jobs and store them in the database, where they appear in the dashboard. The resume agent can run on its own schedule to process all scraped job descriptions through the full resume pipeline, then store the generated LaTeX and PDF outputs in the database so they can also be reviewed in the dashboard.

At a high level, the product combines:

- a scraper agent that acquires job descriptions and stores them for review
- a resume agent that reads candidate truth and evidence, runs the full pipeline, and stores generated resumes

## Read The Docs

If you want to run this system yourself or build your own version, start here:

- Docs: https://hermes-autonomous-resume.vercel.app/docs/getting-started/introduction
- Docs source: [docs-site/docs/getting-started/introduction.md](docs-site/docs/getting-started/introduction.md)

Recommended doc entry points:

- `Getting Started` for installation and first-run context
- `Resume Agent` for the operator workflow
- `Scraper Agent` for the job collection workflow
- `Architecture` for system boundaries and lifecycle
- `API Reference` if you are building your own dashboard/backend

## System View

```mermaid
flowchart LR
  A[Scraper agent<br/>scheduled or manual] --> B[Scrape job descriptions]
  B --> C[Store JDs in database]
  C --> D[Dashboard shows scraped jobs]

  C --> E[Resume agent<br/>scheduled or manual]
  F[Candidate profile] --> E
  G[Evidence pool] --> E
  E --> H[Run full resume pipeline]
  H --> I[Generate LaTeX and PDF resumes]
  I --> J[Store resumes in database]
  J --> K[Dashboard shows resume outputs]
```

## Screenshots

### Scraper Agent Run

![Scraper agent scheduled run](assets/readme/scraper-agent-run.png)

### Resume Agent Run

![Resume agent scheduled run](assets/readme/resume-agent-run.png)

### Dashboard Jobs Queue

![Dashboard jobs queue](assets/readme/dashboard-jobs-queue.png)

### Job Detail And Generated Resume Output

![Dashboard job detail with generated resume state](assets/readme/dashboard-job-detail.png)

### Resume PDF Preview

![Generated resume PDF preview](assets/readme/resume-pdf-preview.png)

## What This Repo Contains

- the Hermes skills that power candidate setup, evidence intake, JD processing, resume generation, and orchestration
- scraper utilities for collecting jobs
- the docs site for running the system or building your own version

## Core Skills

| Skill | Description |
|---|---|
| `profile-bootstrap` | Personalizes the repo for a real candidate and fills runtime placeholders. |
| `candidate-profile` | Stores the candidate truth the rest of the resume system reads from. |
| `pool-intake` | Adds work, project, and OSS evidence into the expected pool structure. |
| `jd-prefilter` | Quickly rejects weak-fit job descriptions before deeper processing. |
| `jd-extraction` | Turns a job description into structured signals for downstream resume work. |
| `project-selection` | Chooses the strongest supporting project and OSS evidence for a JD. |
| `point-repointing` | Tailors experience and project bullets to the target job description. |
| `latex-assembly` | Assembles the final resume output in LaTeX form. |
| `resume-pipeline-orchestrator` | Runs the end-to-end resume flow and pushes results to the dashboard. |
