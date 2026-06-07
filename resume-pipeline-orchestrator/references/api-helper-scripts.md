# API Helper Scripts for Cron Mode

When running as a cron job, `execute_code` is blocked. Use these patterns instead:
write Python scripts to disk via `write_file`, then run via `terminal`.

## Pattern: Read API key from .env (shell-safe)

```python
# Always parse .env programmatically — never use $<DASHBOARD_API_KEY_ENV> in shell
api_key = None
with open("/opt/data/profiles/<PROFILE_SLUG>/.env") as f:
    for line in f:
        line = line.strip()
        idx = line.index("=")  # find first '=' — handles values containing '='
        key = line[:idx]
        val = line[idx+1:]
        if key == "<DASHBOARD_API_KEY_ENV>":
            api_key = val
            break
```

## Pattern: Push Resume + Mark Processed + Log (all-in-one)

Write to `/opt/data/profiles/<PROFILE_SLUG>/home/push_and_mark.py`:

```python
import json, urllib.request, urllib.error, sys

def load_api_key():
    with open("/opt/data/profiles/<PROFILE_SLUG>/.env") as f:
        for line in f:
            line = line.strip()
            idx = line.index("=")
            if line[:idx] == "<DASHBOARD_API_KEY_ENV>":
                return line[idx+1:]
    return None

def push_and_mark(company, jd_text, jd_id, tex_file):
    api_key = load_api_key()
    with open(tex_file, "r") as f:
        latex_content = f.read()
    
    # Push resume
    payload = {"company_name": company, "job_description": jd_text,
               "job_description_id": jd_id, "latex_content": latex_content, "source": "<SOURCE_NAME>"}
    url = "<DASHBOARD_BASE_URL>/api/generated-resumes"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data,
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + api_key},
        method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8")
        print("PUSH_SUCCESS: " + str(json.loads(body).get("generated_resume", {}).get("id", "unknown")))
    
    # Mark processed
    url2 = "<DASHBOARD_BASE_URL>/api/job-descriptions/" + jd_id + "/use"
    req2 = urllib.request.Request(url2, data=None,
        headers={"Authorization": "Bearer " + api_key}, method="PATCH")
    with urllib.request.urlopen(req2, timeout=15) as resp:
        print("PATCH_SUCCESS: " + str(resp.status))
    
    # Log
    payload3 = {"job_description_id": jd_id, "status": "success",
                "message": company + ": resume assembled, pushed, and JD marked processed."}
    url3 = "<DASHBOARD_BASE_URL>/api/workflow-logs"
    data3 = json.dumps(payload3).encode("utf-8")
    req3 = urllib.request.Request(url3, data=data3,
        headers={"Authorization": "Bearer " + api_key, "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(req3, timeout=15) as resp:
        print("LOG_SUCCESS: " + str(resp.status))

if __name__ == "__main__":
    push_and_mark(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
```

Run with:
```bash
python3 /opt/data/profiles/<PROFILE_SLUG>/home/push_and_mark.py "<TARGET_COMPANY>" "<JD_TEXT>" "<JD_UUID>" "/path/to/resume.tex"
```

## Pattern: Workflow Log Only

```python
import json, urllib.request, urllib.error

api_key = None
with open("/opt/data/profiles/<PROFILE_SLUG>/.env") as f:
    for line in f:
        line = line.strip()
        idx = line.index("=")
        if line[:idx] == "<DASHBOARD_API_KEY_ENV>":
            api_key = line[idx+1:]
            break

payload = {
    "job_description_id": "jd-uuid",  # omit for batch summary
    "status": "success",              # "success", "failed", or "skipped"
    "message": "Message here"
}
url = "<DASHBOARD_BASE_URL>/api/workflow-logs"
data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=data,
    headers={"Authorization": "Bearer " + api_key, "Content-Type": "application/json"},
    method="POST")
with urllib.request.urlopen(req, timeout=15) as resp:
    print("LOG_SUCCESS: " + str(resp.status))
```

## Pattern: Skip Log

```python
# Same as above but with status="skipped" and a reason message
payload = {
    "job_description_id": "jd-uuid",
    "status": "skipped",
    "message": "Company (title): pre-filter score N. Reason: ..."
}
```

## Batch Summary Log

```python
# Omit job_description_id for batch summary
payload = {
    "status": "success",
    "message": "Batch complete. Fetched: N. Succeeded: N. Failed: N. Skipped: N."
}
```



