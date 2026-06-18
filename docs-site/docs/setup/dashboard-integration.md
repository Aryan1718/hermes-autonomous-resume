---
id: dashboard-integration
title: Dashboard Integration
sidebar_position: 3
slug: /setup/dashboard-integration
---

# Dashboard integration

In the full Hermes loop, the dashboard is the coordination layer between job ingestion, resume generation, status tracking, and feedback.

This page is supporting reference material. For the end-to-end operator flow, start with [Resume Agent > Setup Guide](/docs/resume-agent/setup-guide) and come here when you need the dashboard-specific setup details.

## What the orchestrator expects

The orchestrator-side instructions reference runtime placeholders such as:

- `<DASHBOARD_BASE_URL>`
- `<DASHBOARD_API_KEY_ENV>`
- `<PROFILE_SLUG>`
- `<RESUMES_DIR>`
- `<POOL_DIR>`

Those values should be filled only when the user wants this repository personalized for a real deployment environment.

## Expected flow

1. The job scraper or upstream system sends job descriptions to the dashboard.
2. `resume-pipeline-orchestrator` fetches unprocessed JDs.
3. Passing JDs move through the pipeline.
4. Generated resumes are pushed back to the dashboard.
5. Successful JDs are marked as processed.
6. Feedback on outputs informs future refinement work.

## Separation of concerns

This repository documents how the pipeline interacts with the dashboard, but the scraper and dashboard application are separate systems. Keep that boundary clear in your docs and setup instructions.

For endpoint details, use [API Reference](/docs/api-reference).
