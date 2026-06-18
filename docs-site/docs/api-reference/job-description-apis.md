---
id: job-description-apis
title: Job Description APIs
sidebar_position: 2
slug: /api-reference/job-description-apis
---

# Job Description APIs

These endpoints manage the intake queue that feeds the resume pipeline.

## POST /api/job-descriptions

**Purpose:** Accept a newly scraped or manually submitted job description and store it in the queue.

**Used by:** Scraper services and trusted backend integrations.

**Used in skills:** No repository skill calls this endpoint directly today. It is the ingestion contract that scraper-side automation is expected to hit before `resume-pipeline-orchestrator` starts work.

**Authentication:** Scraper ingest auth, such as a shared ingest secret or server-side API credential.

**Request format:** JSON body with the job content plus enough metadata to identify the company and source.

```json
{
  "company_name": "Acme",
  "job_description": "We are hiring a senior platform engineer...",
  "source": "jobright",
  "source_url": "https://example.com/jobs/123",
  "external_job_id": "123"
}
```

**Behavior:** The backend stores the raw JD, attaches source metadata, and places it into the unprocessed queue. Implementations commonly dedupe on a source-specific identifier or repeated content so scrapers can retry safely.

**Success response:**

```json
{
  "success": true,
  "job_description": {
    "id": "<JOB_DESCRIPTION_ID>",
    "company_name": "Acme",
    "is_used": false,
    "created_at": "2026-06-16T15:04:12.000Z"
  }
}
```

**Failure/empty-state behavior:** Returns `400` for invalid payloads and `409` or an equivalent duplicate response when the same source job has already been ingested.

**Why it matters:** This is the queue entry point for the whole Hermes workflow.

**Example request:**

```bash
curl -X POST "<DASHBOARD_BASE_URL>/api/job-descriptions" \
  -H "Authorization: Bearer <SCRAPER_INGEST_SECRET>" \
  -H "Content-Type: application/json" \
  -d '{
    "company_name": "Acme",
    "job_description": "We are hiring a senior platform engineer...",
    "source": "jobright",
    "source_url": "https://example.com/jobs/123",
    "external_job_id": "123"
  }'
```

## GET /api/job-descriptions/next

**Purpose:** Fetch the current batch of unprocessed job descriptions.

**Used by:** Hermes agent.

**Used in skills:** `resume-pipeline-orchestrator`, batch intake step at the start of the run before `jd-prefilter`.

**Authentication:** API key auth.

**Request format:** No body required.

**Behavior:** Returns all unprocessed JDs with `is_used = false`, ordered oldest first. Because this is a queue snapshot, a re-fetch can include jobs already seen earlier in the run if they have not been marked used yet.

**Success response:**

```json
{
  "success": true,
  "job_descriptions": [
    {
      "id": "<JOB_DESCRIPTION_ID>",
      "company_name": "Acme",
      "job_description": "We are hiring a senior platform engineer...",
      "is_used": false,
      "created_at": "2026-06-16T15:04:12.000Z"
    }
  ]
}
```

**Failure/empty-state behavior:** If there are no available JDs, implementations typically return a non-success payload such as:

```json
{
  "success": false,
  "message": "No unused job descriptions available"
}
```

**Why it matters:** This is how Hermes discovers what work is waiting in the queue.

**Example request:**

```bash
curl "<DASHBOARD_BASE_URL>/api/job-descriptions/next" \
  -H "Authorization: Bearer <API_KEY>"
```

## GET /api/job-descriptions/latest

**Purpose:** Fetch the most recently ingested job description without draining the whole queue.

**Used by:** Dashboard frontend, manual QA flows, and lightweight integration checks.

**Used in skills:** No current repository skill depends on this route directly. It is primarily an operator/debugging endpoint.

**Authentication:** API key auth or an authenticated website session, depending on how your dashboard exposes read access.

**Request format:** No body required.

**Behavior:** Returns the newest JD record available to the caller. This is useful for sanity checks after scraper runs and for “show me the latest ingest” UI panels.

**Success response:**

```json
{
  "success": true,
  "job_description": {
    "id": "<JOB_DESCRIPTION_ID>",
    "company_name": "Acme",
    "job_description": "We are hiring a senior platform engineer...",
    "is_used": false,
    "created_at": "2026-06-16T15:04:12.000Z"
  }
}
```

**Failure/empty-state behavior:** Returns an empty-state response if no job descriptions have been ingested yet.

**Why it matters:** It gives operators a fast way to verify that scraper ingestion is actually landing in the dashboard.

**Example request:**

```bash
curl "<DASHBOARD_BASE_URL>/api/job-descriptions/latest" \
  -H "Authorization: Bearer <API_KEY>"
```

## GET /api/job-descriptions/:id

**Purpose:** Retrieve one stored job description by ID.

**Used by:** Dashboard frontend and Hermes debugging flows.

**Used in skills:** No current repository skill depends on this route directly. It is mainly for inspection, QA, and debugging.

**Authentication:** API key auth or an authenticated website session with ownership checks.

**Request format:** No body required. Pass the JD ID in the URL path.

**Behavior:** Returns the raw stored JD plus queue metadata. The backend should enforce ownership and visibility rules server-side rather than trusting client-supplied user identifiers.

**Success response:**

```json
{
  "success": true,
  "job_description": {
    "id": "<JOB_DESCRIPTION_ID>",
    "company_name": "Acme",
    "job_description": "We are hiring a senior platform engineer...",
    "source": "jobright",
    "is_used": false,
    "created_at": "2026-06-16T15:04:12.000Z"
  }
}
```

**Failure/empty-state behavior:** Returns `404` if the JD does not exist or is not visible to the caller.

**Why it matters:** It lets operators inspect the exact source text that produced a generated resume.

**Example request:**

```bash
curl "<DASHBOARD_BASE_URL>/api/job-descriptions/<JOB_DESCRIPTION_ID>" \
  -H "Authorization: Bearer <API_KEY>"
```

## PATCH /api/job-descriptions/:id/use

**Purpose:** Mark a job description as processed after a successful downstream run.

**Used by:** Hermes agent.

**Used in skills:** `resume-pipeline-orchestrator`, queue finalization step after `POST /api/generated-resumes` succeeds.

**Authentication:** API key auth.

**Request format:** No body required.

**Behavior:** Sets `is_used = true` for the matching JD. This call should happen only after the generated resume has been saved successfully, because it removes the JD from future `/next` batches.

**Success response:**

```json
{
  "success": true,
  "job_description": {
    "id": "<JOB_DESCRIPTION_ID>",
    "is_used": true
  }
}
```

**Failure/empty-state behavior:** Returns `404` when the JD does not exist and `409` or a similar guard response if the record has already been marked processed.

**Why it matters:** This is the queue state transition that prevents Hermes from reprocessing the same job.

**Example request:**

```bash
curl -X PATCH "<DASHBOARD_BASE_URL>/api/job-descriptions/<JOB_DESCRIPTION_ID>/use" \
  -H "Authorization: Bearer <API_KEY>"
```
