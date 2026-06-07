# API Reference — Dashboard Endpoints

> **For the resume-pipeline-orchestrator skill.** All dashboard API calls use `urllib.request` (NOT `requests`, NOT inline `curl -d` with JSON strings).

**Base URL:** `<DASHBOARD_BASE_URL>`
**Auth header (all calls):** `Authorization: Bearer <DASHBOARD_API_KEY_ENV>`
**API key location:** `/opt/data/profiles/<PROFILE_SLUG>/.env` (`<DASHBOARD_API_KEY_ENV>=...`)

## Endpoints Overview

| Step | Method | Endpoint | When called |
|---|---|---|---|
| Fetch batch | GET | `/api/job-descriptions/next` | Once at start |
| Push resume | POST | `/api/generated-resumes` | Per JD — on full pipeline success |
| Mark processed | PATCH | `/api/job-descriptions/{id}/use` | Per JD — after successful resume push |
| Event log | POST | `/api/workflow-logs` | Per JD (success/fail/skip) + once at end of batch + on orchestrator error |

---

## GET /api/job-descriptions/next

Returns all unprocessed JDs (`is_used = false`) as an array ordered by `created_at ASC`.

**Success response shape:**
```json
{
  "success": true,
  "job_descriptions": [
    {
      "id": "6f4d1d60-3d13-4f8f-9f53-47c64266d633",
      "company_name": "<TARGET_COMPANY>",
      "job_description": "Senior backend engineer role...",
      "is_used": false,
      "created_at": "2026-05-25T18:00:00.000Z"
    }
  ]
}
```

**No data response:**
```json
{ "success": false, "message": "No unused job descriptions available" }
```

---

## POST /api/generated-resumes

**CRITICAL:** The backend requires `job_description` as a string for validation, even when `job_description_id` is also sent. Omitting `job_description` causes a 400 error. **Always send both fields.**

**Also use `write_file` + Python script for this call — never embed .tex content in a curl -d JSON string.** See `references/api-helper-scripts.md` for the push script pattern.

```json
{
  "company_name": "<TARGET_COMPANY>",
  "job_description": "<full JD text from the fetched JD> — required string field",
  "job_description_id": "<jd_id from the fetch response> — optional UUID for linking",
  "latex_content": "<full assembled .tex content>",
  "source": "<SOURCE_NAME>"
}
```

---

## PATCH /api/job-descriptions/{id}/use

Marks the JD as used (`is_used = true`). No request body needed.

---

## POST /api/workflow-logs

Called after every notable event: each JD outcome (success, failed, skipped), any orchestrator-level error, and once more at the very end as a batch summary.

**Required fields:** `status` — must be one of `success`, `failed`, or `skipped`.
**Optional fields:** `job_description_id`, `request_id`, `message`.

### Status Logic

- **Per-JD:** `success` (resume pushed), `failed` (pipeline broke), `skipped` (pre-filter rejected)
- **Batch summary:** `success` if ≥1 JD succeeded, `failed` if 0 succeeded and ≥1 failed, `skipped` only if ALL JDs were skipped

### `job_description_id` Rule

- **Always send** for per-JD logs (success, failed, skipped)
- **Omit** for orchestrator-level errors (no JD context) and batch summary

### Message Templates

**Per JD — success:**
`"<TARGET_COMPANY> (backend-engineer): resume assembled, pushed, and JD marked processed. Pre-filter score: 82. Projects: enterprise-rag, <work-company-slug>, discovermap."`

**Per JD — success with PATCH warning:**
`"<TARGET_COMPANY> (backend-engineer): resume built and pushed but PATCH /use failed. JD still shows unprocessed — review manually."`

**Per JD — pipeline failure:**
`"<TARGET_COMPANY> (backend-engineer): pipeline broke at point-repointing. Error: idx.md not found for enterprise-rag. JD left unprocessed."`

**Per JD — pre-filter skip:**
`"Globex (platform-engineer): pre-filter score 28. Reason: no A-priority provable must-haves matched."`

**Orchestrator error (no JD id):**
`"Orchestrator halted unexpectedly. Stage: fetching JDs. Error: HTTP 401 Unauthorized. Processed 0 JDs before halt."`

**End of batch summary:**
`"Batch complete. Fetched: 5. Succeeded: 3. Failed: 1. Skipped: 1."`

---

## Python API Helper

All dashboard API calls should use this Python helper instead of inline `curl -d` JSON commands. This prevents JSON serialization errors with LaTeX content and handles special characters properly.

**IMPORTANT: Use `urllib.request` — the `requests` module is NOT installed on this machine.**

### Generic API call script

Replace `<METHOD>`, `<ENDPOINT>`, `<PAYLOAD_JSON>` as needed:

```bash
source /opt/data/profiles/<PROFILE_SLUG>/.env
python3 - <<'PYEOF'
import os, json, urllib.request, urllib.error

# Load API key from .env
api_key = None
with open("/opt/data/profiles/<PROFILE_SLUG>/.env") as f:
    for line in f:
        line = line.strip()
        if line.startswith("<DASHBOARD_API_KEY_ENV>="):
            api_key = line.split("=", 1)[1]
            break

if not api_key:
    print("ERROR: <DASHBOARD_API_KEY_ENV> not set")
    exit(1)

# ---- CONFIGURE THIS PER CALL ----
method = "<METHOD>"          # "POST" or "PATCH"
endpoint = "<ENDPOINT>"      # e.g. "/api/generated-resumes"
payload = <PAYLOAD_JSON>     # Python dict or None for PATCH-with-no-body
# ---------------------------------

url = f"<DASHBOARD_BASE_URL>{endpoint}"
data = json.dumps(payload).encode("utf-8") if payload else None
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

req = urllib.request.Request(url, data=data, headers=headers, method=method)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8")
        print(f"SUCCESS: {resp.status}")
        try:
            print(json.dumps(json.loads(body), indent=2))
        except:
            pass
except urllib.error.HTTPError as e:
    print(f"FAILED: HTTP {e.code} — {e.read().decode('utf-8')}")
    exit(1)
PYEOF
```

### Push resume

Use the dedicated Python script shown in `references/api-helper-scripts.md`. **Never embed .tex content in a curl -d JSON string.**

### Workflow log

Replace inline `curl -d` with:

```bash
python3 - <<'PYEOF'
import json, urllib.request, urllib.error

api_key = None
with open("/opt/data/profiles/<PROFILE_SLUG>/.env") as f:
    for line in f:
        line = line.strip()
        if line.startswith("<DASHBOARD_API_KEY_ENV>="):
            api_key = line.split("=", 1)[1]
            break

payload = {
    "job_description_id": "<jd_id>",    # omit for batch summary
    "status": "<status>",               # "success", "failed", or "skipped"
    "message": "<message>"
}

url = "<DASHBOARD_BASE_URL>/api/workflow-logs"
data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}, method="POST")

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        print(f"SUCCESS: {resp.status}")
except urllib.error.HTTPError as e:
    print(f"FAILED: HTTP {e.code} — {e.read().decode('utf-8')}")
PYEOF
```

### Mark JD as processed

```bash
python3 - <<'PYEOF'
import urllib.request, urllib.error

api_key = None
with open("/opt/data/profiles/<PROFILE_SLUG>/.env") as f:
    for line in f:
        line = line.strip()
        if line.startswith("<DASHBOARD_API_KEY_ENV>="):
            api_key = line.split("=", 1)[1]
            break

jd_id = "<jd_id>"
url = f"<DASHBOARD_BASE_URL>/api/job-descriptions/{jd_id}/use"
req = urllib.request.Request(url, data=None, headers={
    "Authorization": f"Bearer {api_key}"
}, method="PATCH")

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        print(f"SUCCESS: {resp.status}")
except urllib.error.HTTPError as e:
    print(f"FAILED: HTTP {e.code} — {e.read().decode('utf-8')}")
PYEOF
```



