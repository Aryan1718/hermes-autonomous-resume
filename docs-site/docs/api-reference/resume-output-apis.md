---
id: resume-output-apis
title: Resume Output APIs
sidebar_position: 3
slug: /api-reference/resume-output-apis
---

# Resume Output APIs

These endpoints persist the artifacts produced by the Hermes resume agent.

## POST /api/generated-resumes

**Purpose:** Save a finished generated resume and link it back to the source job description.

**Used by:** Hermes agent.

**Used in skills:** `resume-pipeline-orchestrator`, final persistence step after `latex-assembly` and the mandatory self-review gate.

**Authentication:** API key auth.

**Request format:** JSON body containing the rendered output plus the source JD context.

```json
{
  "company_name": "Acme",
  "job_description": "We are hiring a senior platform engineer...",
  "job_description_id": "<JOB_DESCRIPTION_ID>",
  "latex_content": "\\documentclass{article} ...",
  "source": "jobright"
}
```

**Behavior:** The backend stores the generated artifact and associates it with the source JD. The orchestrator contract requires both `job_description` and `job_description_id`; the raw JD string is still validated even when the ID is present.

**Success response:**

```json
{
  "success": true,
  "generated_resume": {
    "id": "<GENERATED_RESUME_ID>",
    "job_description_id": "<JOB_DESCRIPTION_ID>",
    "company_name": "Acme",
    "created_at": "2026-06-16T15:23:44.000Z"
  }
}
```

**Failure/empty-state behavior:** Returns `400` if required fields are missing, including the raw `job_description` string. Returns `404` or validation errors if the JD reference is invalid.

**Why it matters:** This is the persistence step that turns a successful Hermes run into a dashboard-visible artifact.

**Example request:**

```bash
curl -X POST "<DASHBOARD_BASE_URL>/api/generated-resumes" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "company_name": "Acme",
    "job_description": "We are hiring a senior platform engineer...",
    "job_description_id": "<JOB_DESCRIPTION_ID>",
    "latex_content": "\\documentclass{article} ...",
    "source": "jobright"
  }'
```
