---
id: hermes-integration-apis
title: Hermes Integration APIs
sidebar_position: 6
slug: /api-reference/hermes-integration-apis
---

# Hermes Integration APIs

These endpoints connect the dashboard to Hermes-specific configuration and dispatch flows.

## POST /api/integrations/hermes

**Purpose:** Save or update the dashboard's Hermes integration configuration.

**Used by:** Dashboard frontend.

**Used in skills:** No current repository skill calls this route directly. It belongs to the dashboard-side setup flow that prepares later Hermes interactions.

**Authentication:** Website session auth.

**Request format:** JSON body with the integration settings the dashboard needs to remember.

```json
{
  "profile_slug": "resume",
  "base_url": "http://localhost:3000",
  "api_key_label": "local-resume-agent"
}
```

**Behavior:** Persists the user's Hermes connection details and related settings. Sensitive values should be stored securely server-side and never echoed back in full.

**Success response:**

```json
{
  "success": true,
  "integration": {
    "provider": "hermes",
    "profile_slug": "resume",
    "configured": true
  }
}
```

**Failure/empty-state behavior:** Returns `400` for incomplete configuration and `403` if the current user is not allowed to manage integrations.

**Why it matters:** This is the saved bridge between the dashboard UI and a specific Hermes profile.

**Example request:**

```bash
curl -X POST "<DASHBOARD_BASE_URL>/api/integrations/hermes" \
  -H "Content-Type: application/json" \
  -b "<SESSION_COOKIE>" \
  -d '{
    "profile_slug": "resume",
    "base_url": "http://localhost:3000",
    "api_key_label": "local-resume-agent"
  }'
```

## POST /api/hermes/test

**Purpose:** Verify that the saved Hermes connection details are valid before dispatching real work.

**Used by:** Dashboard frontend.

**Used in skills:** No current repository skill calls this route directly. It is part of the dashboard-side connection test flow.

**Authentication:** Website session auth.

**Request format:** JSON body with either a saved integration reference or a temporary test configuration.

```json
{
  "profile_slug": "resume"
}
```

**Behavior:** Performs a lightweight connectivity or credential check and returns whether the dashboard can reach the target Hermes integration successfully.

**Success response:**

```json
{
  "success": true,
  "connected": true,
  "message": "Hermes integration test succeeded."
}
```

**Failure/empty-state behavior:** Returns `400` for incomplete input and a non-success response when Hermes is unreachable or credentials fail validation.

**Why it matters:** It prevents users from saving or using broken dashboard-to-Hermes wiring.

**Example request:**

```bash
curl -X POST "<DASHBOARD_BASE_URL>/api/hermes/test" \
  -H "Content-Type: application/json" \
  -b "<SESSION_COOKIE>" \
  -d '{
    "profile_slug": "resume"
  }'
```

## POST /api/hermes/dispatch

**Purpose:** Send a command from the dashboard to Hermes.

**Used by:** Dashboard frontend.

**Used in skills:** No current repository skill calls this route directly. It is part of the dashboard-to-Hermes dispatch bridge.

**Authentication:** Website session auth.

**Request format:** JSON body describing the target profile and requested action.

```json
{
  "profile_slug": "resume",
  "command": "run_pipeline",
  "payload": {
    "job_description_id": "<JOB_DESCRIPTION_ID>"
  }
}
```

**Behavior:** Queues or forwards a dashboard-originated Hermes action. The backend should validate that the caller owns the target integration and that the command is part of the allowed dispatch surface.

**Success response:**

```json
{
  "success": true,
  "dispatch": {
    "id": "<DISPATCH_ID>",
    "status": "queued"
  }
}
```

**Failure/empty-state behavior:** Returns `400` for unsupported commands, `403` for ownership violations, and an integration error if Hermes is offline.

**Why it matters:** This is the operational handoff that lets the dashboard trigger Hermes work on demand.

**Example request:**

```bash
curl -X POST "<DASHBOARD_BASE_URL>/api/hermes/dispatch" \
  -H "Content-Type: application/json" \
  -b "<SESSION_COOKIE>" \
  -d '{
    "profile_slug": "resume",
    "command": "run_pipeline",
    "payload": {
      "job_description_id": "<JOB_DESCRIPTION_ID>"
    }
  }'
```
