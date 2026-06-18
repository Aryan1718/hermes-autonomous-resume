---
id: workflow-logging-apis
title: Workflow Logging APIs
sidebar_position: 4
slug: /api-reference/workflow-logging-apis
---

# Workflow Logging APIs

These endpoints record what happened during scraper runs, Hermes runs, and related system activity.

## POST /api/workflow-logs

**Purpose:** Store a workflow status record tied to a user-facing Hermes run or JD outcome.

**Used by:** Hermes agent and dashboard backend services.

**Used in skills:** `resume-pipeline-orchestrator`, used for skipped JDs after `jd-prefilter`, failed JDs after downstream skill errors, successful completions, orchestrator-level errors, and the final batch summary.

**Authentication:** API key auth.

**Request format:** JSON body with a status plus optional identifiers and human-readable context.

```json
{
  "job_description_id": "<JOB_DESCRIPTION_ID>",
  "status": "success",
  "message": "Acme: resume assembled, pushed, and JD marked processed.",
  "request_id": "<REQUEST_ID>"
}
```

**Behavior:** Used for per-JD success, failed, and skipped outcomes, plus batch summaries and orchestrator-level errors. For per-JD logs, include `job_description_id`. For batch summaries and top-level failures, omit it when there is no JD context.

**Success response:**

```json
{
  "success": true,
  "workflow_log": {
    "id": "<WORKFLOW_LOG_ID>",
    "status": "success",
    "job_description_id": "<JOB_DESCRIPTION_ID>"
  }
}
```

**Failure/empty-state behavior:** Returns `400` when `status` is missing or outside the allowed set such as `success`, `failed`, or `skipped`.

**Why it matters:** This is the audit trail that explains what Hermes did and where a run stopped when something breaks.

**Example request:**

```bash
curl -X POST "<DASHBOARD_BASE_URL>/api/workflow-logs" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "job_description_id": "<JOB_DESCRIPTION_ID>",
    "status": "success",
    "message": "Acme: resume assembled, pushed, and JD marked processed.",
    "request_id": "<REQUEST_ID>"
  }'
```

## POST /api/workflow-logs/event

**Purpose:** Record lower-level shared events that are useful outside a single user-owned Hermes run.

**Used by:** Scraper services, integration workers, and system-level automation.

**Used in skills:** No current repository skill is documented as calling this route directly. It is meant for shared operational event reporting around scraper and integration activity.

**Authentication:** API key auth or scraper ingest auth, depending on which service is sending the event.

**Request format:** JSON body describing the event type, source, and message.

```json
{
  "event_type": "scraper_run_completed",
  "source": "jobright",
  "status": "success",
  "message": "Fetched 20 jobs and ingested 18 new records."
}
```

**Behavior:** Use this endpoint for shared operational events that are not best modeled as a user-specific workflow result. Typical examples are scraper health, ingestion summaries, and integration heartbeats.

**Success response:**

```json
{
  "success": true,
  "event": {
    "id": "<WORKFLOW_EVENT_ID>",
    "event_type": "scraper_run_completed",
    "status": "success"
  }
}
```

**Failure/empty-state behavior:** Returns `400` for malformed event payloads and `401` or `403` when the sender is not allowed to publish shared events.

**Why it matters:** It separates system telemetry from per-user Hermes output logs so operators can monitor the platform cleanly.

**Example request:**

```bash
curl -X POST "<DASHBOARD_BASE_URL>/api/workflow-logs/event" \
  -H "Authorization: Bearer <SCRAPER_INGEST_SECRET>" \
  -H "Content-Type: application/json" \
  -d '{
    "event_type": "scraper_run_completed",
    "source": "jobright",
    "status": "success",
    "message": "Fetched 20 jobs and ingested 18 new records."
  }'
```
