---
id: installation
title: Installation
sidebar_position: 2
slug: /getting-started/installation
---

# Installation

The docs site and the pipeline are separate concerns.

## Docs site prerequisites

To run this Docusaurus site locally, install:

- Node.js 18+
- npm, pnpm, or yarn

From the repository root:

```bash
cd docs-site
npm install
npm run start
```

That will start the docs site locally and serve the pages under the Docusaurus dev server.

## Pipeline prerequisites

The resume pipeline itself depends on your broader Hermes environment. At minimum you should expect to configure:

- a candidate profile
- a populated evidence pool
- dashboard/API runtime values
- whatever execution environment your agent uses to call the skills

## Recommended repo workflow

Use this order:

```text
1. docs-site/ for project docs
2. profile-bootstrap for candidate-specific setup
3. pool-intake for evidence onboarding
4. resume-pipeline-orchestrator for live JD processing
```

## Notes

- The docs site does not need to be deployed before the pipeline can run.
- The pipeline should not be considered ready until `candidate-profile` is filled with real candidate facts.
