# Push Verification Rules

## Never Push Poor-Fit JDs
If a JD was pre-filtered out (Phase 1 disqualification or Phase 2 failure), DO NOT push a resume for it. The pre-filter exists for a reason. Forcing a resume through for a poor-fit JD wastes the pipeline and clutters the dashboard.

Exception: if you're explicitly testing the pipeline end-to-end, push locally but verify output before marking JD as processed.

## Always Verify Before Pushing
After assembling the .tex file, verify locally before pushing:
1. Read the .tex file back from disk
2. Check `Functional Programming` or other unprovable claims are NOT in Concepts
3. Check no commented-out project blocks exist (unnecessary)
4. Check all bullets have 2-4 bolded keywords
5. Check no em dashes anywhere

## Push via Python, Never via curl-d
**CRITICAL:** Large .tex files (6000-8000 chars) break when embedded inline in a JSON curl-d string. Backslashes get double-escaped and the payload gets truncated. Always use Python urllib/requests reading from the local file:

```python
import json, urllib.request
with open("/opt/data/profiles/<PROFILE_SLUG>/home/<RESUMES_DIR>/<slug>.tex") as f:
    latex = f.read()
payload = {"company_name": "...", "latex_content": latex, ...}
data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request("<DASHBOARD_BASE_URL>/api/generated-resumes",
    data=data, headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}, method="POST")
```

## After Pushing
Verify the pushed content size matches the local file size. If sizes differ by more than 5 chars, the content was corrupted/truncated. Re-push immediately.

