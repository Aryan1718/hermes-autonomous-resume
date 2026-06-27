---
id: overview
title: Overview
sidebar_position: 1
slug: /api-reference
---

import SourceRepoNote from '@site/src/components/SourceRepoNote';

# API Overview

The Hermes dashboard API is the handoff point between three different actors:

- browser clients used by the dashboard frontend
- Hermes agents that fetch work, save outputs, and review feedback
- scraper services that ingest new job descriptions

Use this reference to understand which endpoints belong to which part of the workflow and what each call is expected to do.

## Scope of this reference

These pages document the endpoints currently used by this repository and its documented Hermes workflows.

You are not required to copy this API surface exactly. If your setup needs additional routes, different route names, or extra workflow-specific endpoints, you can design them that way as long as the skills and frontend code that depend on them are updated accordingly.

Treat this section as the current working contract for this repo, not as a rule that your backend can never extend.

## Base URL

All examples in this section use:

```text
<DASHBOARD_BASE_URL>
```

Keep the real deployment URL out of shared docs, prompts, and examples.

## Authentication modes

- Website session auth: used by browser-based dashboard features such as login, logout, and current-user lookups.
- API key auth: used by Hermes agents and other trusted server-side clients with an `Authorization: Bearer <API_KEY>` header.
- Scraper ingest auth: used by scraper services that push job descriptions into the queue with a dedicated shared secret or ingest token.

## Security rules

- Do not send `user_id` from frontend clients unless an endpoint explicitly requires it.
- Ownership is resolved server-side from the authenticated user or API key.
- Hashes, internal secrets, and other credential material should never appear in responses.
- Use placeholders such as `<API_KEY>`, `<SCRAPER_INGEST_SECRET>`, and `<JOB_DESCRIPTION_ID>` in examples and setup docs.

## How to read this reference

- If you are building the dashboard UI, focus on Authentication APIs, Feedback APIs, and Hermes Integration APIs.
- If you are wiring the Hermes orchestrator, focus on Job Description APIs, Resume Output APIs, Workflow Logging APIs, and Feedback APIs.
- If you are building a scraper, focus on `POST /api/job-descriptions` plus the scraper-specific authentication notes.

## Current skill usage map

This map shows where the currently documented endpoints are used inside the Hermes workflow.

| Endpoint | Current skill usage | Workflow part |
|---|---|---|
| `GET /api/job-descriptions/next` | `resume-pipeline-orchestrator` | Batch intake at the start of the pipeline |
| `POST /api/generated-resumes` | `resume-pipeline-orchestrator` | Final artifact persistence after LaTeX assembly and self-review |
| `PATCH /api/job-descriptions/:id/use` | `resume-pipeline-orchestrator` | Queue state update after a successful resume push |
| `POST /api/workflow-logs` | `resume-pipeline-orchestrator` | Per-JD status logging, orchestrator error logging, and batch summary logging |
| `GET /api/feedback/pending` | `feedback-processor` related workflow | Fetch pending human feedback for review |
| `PATCH /api/feedback/:id/review` | `feedback-processor` related workflow | Write Hermes review output back to the dashboard |
| `POST /api/feedback` | Dashboard frontend | User submits feedback on generated output |
| `POST /api/integrations/hermes` | Dashboard frontend | Save Hermes connection/configuration |
| `POST /api/hermes/test` | Dashboard frontend | Verify the saved Hermes connection |
| `POST /api/hermes/dispatch` | Dashboard frontend | Trigger Hermes work from the dashboard |
| `POST /api/auth/login` | Dashboard frontend | Start session |
| `POST /api/auth/logout` | Dashboard frontend | End session |
| `GET /api/auth/me` | Dashboard frontend | Resolve current session user |
| `POST /api/auth/register` | Dashboard frontend | Account creation |
| `POST /api/auth/api-key` | Dashboard frontend and `resume-pipeline-orchestrator` setup | Issue the API key later used by Hermes |

## Reference sections

- [Job Description APIs](/docs/api-reference/job-description-apis)
- [Resume Output APIs](/docs/api-reference/resume-output-apis)
- [Workflow Logging APIs](/docs/api-reference/workflow-logging-apis)
- [Feedback APIs](/docs/api-reference/feedback-apis)
- [Hermes Integration APIs](/docs/api-reference/hermes-integration-apis)
- [Authentication APIs](/docs/api-reference/authentication-apis)

<SourceRepoNote>
  If you want the actual skills and repository workflows that consume these endpoints, use the public source repository.
</SourceRepoNote>
