---
id: authentication-apis
title: Authentication APIs
sidebar_position: 7
slug: /api-reference/authentication-apis
---

# Authentication APIs

These endpoints cover the browser-facing auth flows that frontend builders usually need.

## POST /api/auth/login

**Purpose:** Start an authenticated website session for an existing user.

**Used by:** Dashboard frontend.

**Used in skills:** No repository skill calls this route directly. It is part of the browser login flow.

**Authentication:** No existing session required.

**Request format:** JSON body with user credentials.

```json
{
  "email": "candidate@example.com",
  "password": "<PASSWORD>"
}
```

**Behavior:** Validates the credentials and establishes a session cookie or equivalent browser session token.

**Success response:**

```json
{
  "success": true,
  "user": {
    "email": "candidate@example.com"
  }
}
```

**Failure/empty-state behavior:** Returns `401` for invalid credentials.

**Why it matters:** This is the entry point for the dashboard UI.

**Example request:**

```bash
curl -X POST "<DASHBOARD_BASE_URL>/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "candidate@example.com",
    "password": "<PASSWORD>"
  }'
```

## POST /api/auth/logout

**Purpose:** End the current website session.

**Used by:** Dashboard frontend.

**Used in skills:** No repository skill calls this route directly. It is part of the browser logout flow.

**Authentication:** Website session auth.

**Request format:** No body required.

**Behavior:** Invalidates the current session and clears any server-side session state associated with the browser.

**Success response:**

```json
{
  "success": true
}
```

**Failure/empty-state behavior:** Usually returns a success response even if the session has already expired, so logout remains idempotent from the UI perspective.

**Why it matters:** It cleanly closes browser access to dashboard features.

**Example request:**

```bash
curl -X POST "<DASHBOARD_BASE_URL>/api/auth/logout" \
  -b "<SESSION_COOKIE>"
```

## GET /api/auth/me

**Purpose:** Return the currently authenticated user.

**Used by:** Dashboard frontend.

**Used in skills:** No repository skill calls this route directly. It is part of session bootstrap and session validation in the dashboard.

**Authentication:** Website session auth.

**Request format:** No body required.

**Behavior:** Resolves the active user from the session and returns the profile data the frontend needs to bootstrap authenticated screens.

**Success response:**

```json
{
  "success": true,
  "user": {
    "id": "<USER_ID>",
    "email": "candidate@example.com",
    "name": "Candidate Name"
  }
}
```

**Failure/empty-state behavior:** Returns `401` when the caller is not logged in.

**Why it matters:** Frontends use this to detect whether a session is still valid and which user owns the current workspace.

**Example request:**

```bash
curl "<DASHBOARD_BASE_URL>/api/auth/me" \
  -b "<SESSION_COOKIE>"
```

## POST /api/auth/register

**Purpose:** Create a new dashboard user account.

**Used by:** Dashboard frontend.

**Used in skills:** No repository skill calls this route directly. It is part of the dashboard signup flow.

**Authentication:** No existing session required.

**Request format:** JSON body with the registration fields required by the application.

```json
{
  "name": "Candidate Name",
  "email": "candidate@example.com",
  "password": "<PASSWORD>"
}
```

**Behavior:** Creates the user account, applies validation rules such as unique email checks, and may establish a session immediately after registration.

**Success response:**

```json
{
  "success": true,
  "user": {
    "id": "<USER_ID>",
    "email": "candidate@example.com"
  }
}
```

**Failure/empty-state behavior:** Returns `400` for invalid payloads and `409` when the email is already in use.

**Why it matters:** This is the onboarding path for new dashboard users.

**Example request:**

```bash
curl -X POST "<DASHBOARD_BASE_URL>/api/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Candidate Name",
    "email": "candidate@example.com",
    "password": "<PASSWORD>"
  }'
```

## POST /api/auth/api-key

**Purpose:** Create or rotate an API key for Hermes and other trusted server-side integrations.

**Used by:** Dashboard frontend.

**Used in skills:** Used indirectly by `resume-pipeline-orchestrator` setup, because the key issued here becomes the credential Hermes later uses for protected dashboard API calls.

**Authentication:** Website session auth.

**Request format:** JSON body with an optional label or scope description.

```json
{
  "label": "resume-agent"
}
```

**Behavior:** Generates a new API key for the authenticated user or workspace. The full secret should be shown only at creation time and never returned later in read APIs.

**Success response:**

```json
{
  "success": true,
  "api_key": {
    "label": "resume-agent",
    "token": "<API_KEY>"
  }
}
```

**Failure/empty-state behavior:** Returns `403` if the caller is not allowed to manage API credentials.

**Why it matters:** This is how the dashboard issues the credentials that Hermes uses for protected backend calls.

**Example request:**

```bash
curl -X POST "<DASHBOARD_BASE_URL>/api/auth/api-key" \
  -H "Content-Type: application/json" \
  -b "<SESSION_COOKIE>" \
  -d '{
    "label": "resume-agent"
  }'
```
