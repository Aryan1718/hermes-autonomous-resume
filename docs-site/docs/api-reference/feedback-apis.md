---
id: feedback-apis
title: Feedback APIs
sidebar_position: 5
slug: /api-reference/feedback-apis
---

# Feedback APIs

These endpoints support the loop where people review outputs and Hermes incorporates the results later.

## GET /api/feedback/pending

**Purpose:** Fetch feedback items that still need Hermes review.

**Used by:** Hermes agent.

**Used in skills:** `feedback-processor` related workflow, pending-item fetch step before analysis/review work begins.

**Authentication:** API key auth.

**Request format:** No body required.

**Behavior:** Returns feedback records that have been submitted by users but not yet reviewed by the automated feedback processor. Implementations often filter to the authenticated tenant or user scope automatically.

**Success response:**

```json
{
  "success": true,
  "feedback": [
    {
      "id": "<FEEDBACK_ID>",
      "generated_resume_id": "<GENERATED_RESUME_ID>",
      "status": "pending",
      "comment": "Bullets were accurate but too backend-heavy."
    }
  ]
}
```

**Failure/empty-state behavior:** Returns an empty array or equivalent empty-state payload when there is no pending feedback.

**Why it matters:** This is how Hermes discovers which human reviews still need processing.

**Example request:**

```bash
curl "<DASHBOARD_BASE_URL>/api/feedback/pending" \
  -H "Authorization: Bearer <API_KEY>"
```

## PATCH /api/feedback/:id/review

**Purpose:** Save Hermes's review result for an existing feedback item.

**Used by:** Hermes agent.

**Used in skills:** `feedback-processor` related workflow, writeback step after Hermes finishes reviewing the feedback item.

**Authentication:** API key auth.

**Request format:** JSON body with the review decision, structured notes, or both.

```json
{
  "status": "reviewed",
  "review_summary": "Feedback confirms the resume needs stronger data-platform emphasis.",
  "action_items": [
    "Prioritize distributed systems experience earlier.",
    "Reduce generic tooling bullets."
  ]
}
```

**Behavior:** Updates a pending feedback record with Hermes's review output and moves it out of the pending queue. The backend should validate that the target record exists and is reviewable.

**Success response:**

```json
{
  "success": true,
  "feedback": {
    "id": "<FEEDBACK_ID>",
    "status": "reviewed"
  }
}
```

**Failure/empty-state behavior:** Returns `404` if the feedback item does not exist and `409` or a similar validation response if it has already been reviewed.

**Why it matters:** This closes the automated side of the feedback loop and creates review output the team can act on later.

**Example request:**

```bash
curl -X PATCH "<DASHBOARD_BASE_URL>/api/feedback/<FEEDBACK_ID>/review" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "reviewed",
    "review_summary": "Feedback confirms the resume needs stronger data-platform emphasis.",
    "action_items": [
      "Prioritize distributed systems experience earlier.",
      "Reduce generic tooling bullets."
    ]
  }'
```

## POST /api/feedback

**Purpose:** Submit a new feedback item about a generated resume or run result.

**Used by:** Website user and dashboard frontend.

**Used in skills:** No repository skill calls this route directly today. It is the browser-side entry point that creates work for the later Hermes feedback-review flow.

**Authentication:** Website session auth.

**Request format:** JSON body with the target artifact and user feedback text.

```json
{
  "generated_resume_id": "<GENERATED_RESUME_ID>",
  "rating": 3,
  "comment": "The content was solid, but the role emphasis missed my infra background."
}
```

**Behavior:** Creates a feedback record owned by the authenticated user. The backend should derive ownership from the session rather than accepting an arbitrary `user_id` from the browser.

**Success response:**

```json
{
  "success": true,
  "feedback": {
    "id": "<FEEDBACK_ID>",
    "status": "pending"
  }
}
```

**Failure/empty-state behavior:** Returns `400` for missing comment or target identifiers and `404` if the referenced generated resume does not exist.

**Why it matters:** This is the human input that allows Hermes to improve over time instead of treating every run as disposable.

**Example request:**

```bash
curl -X POST "<DASHBOARD_BASE_URL>/api/feedback" \
  -H "Content-Type: application/json" \
  -b "<SESSION_COOKIE>" \
  -d '{
    "generated_resume_id": "<GENERATED_RESUME_ID>",
    "rating": 3,
    "comment": "The content was solid, but the role emphasis missed my infra background."
  }'
```
