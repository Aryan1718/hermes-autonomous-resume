#!/usr/bin/env python3
"""Push a resume PDF or LaTeX to the dashboard.
Usage: python3 push_resume.py <file_path> <company_name> <job_description_json> [source]

Reads the file from disk and POSTs it to /api/generated-resumes.
Uses urllib (built-in) instead of requests to avoid LaTeX backslash 
serialization issues that corrupt JSON in curl -d commands.
"""
import os, sys, json, urllib.request, urllib.error

def load_api_key():
    env_file = "/opt/data/profiles/<PROFILE_SLUG>/.env"
    if not os.path.exists(env_file):
        print("ERROR: .env file not found at", env_file)
        return None
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line.startswith("<DASHBOARD_API_KEY_ENV>="):
                return line.split("=", 1)[1]
    return None

def api_request(method, endpoint, payload=None, api_key=None):
    url = f"<DASHBOARD_BASE_URL>{endpoint}"
    data = json.dumps(payload).encode("utf-8") if payload else None
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"FAILED: HTTP {e.code} — {e.read().decode()}")
        return None

def push_resume(file_path, company_name, job_description_text, jd_id=None, source="<SOURCE_NAME>"):
    api_key = load_api_key()
    if not api_key:
        print("ERROR: <DASHBOARD_API_KEY_ENV> not set in /opt/data/profiles/<PROFILE_SLUG>/.env")
        return None

    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        return None

    with open(file_path, "r") as f:
        content = f.read()

    print(f"Read {len(content)} chars from {file_path}")

    payload = {
        "company_name": company_name,
        "job_description": job_description_text,  # required by backend validation
        "latex_content": content,
        "source": source
    }
    if jd_id:
        payload["job_description_id"] = jd_id

    result = api_request("POST", "/api/generated-resumes", payload, api_key)
    if result and "generated_resume" in result:
        resume_id = result["generated_resume"].get("id", "unknown")
        pushed_len = len(result["generated_resume"].get("latex_content", ""))
        print(f"PUSH_SUCCESS: id={resume_id}, pushed={pushed_len} chars")
        return resume_id
    return None

def post_workflow_log(jd_id, status, message):
    api_key = load_api_key()
    if not api_key:
        return False
    payload = {"status": status, "message": message}
    if jd_id:
        payload["job_description_id"] = jd_id
    result = api_request("POST", "/api/workflow-logs", payload, api_key)
    return result is not None

def mark_jd_processed(jd_id):
    api_key = load_api_key()
    if not api_key:
        return False
    result = api_request("PATCH", f"/api/job-descriptions/{jd_id}/use", None, api_key)
    return result is not None

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: push_resume.py <file_path> <company_name> <job_description_text> [jd_id]")
        sys.exit(1)
    jd_id = sys.argv[4] if len(sys.argv) > 4 else None
    resume_id = push_resume(sys.argv[1], sys.argv[2], sys.argv[3], jd_id=jd_id)
    sys.exit(0 if resume_id else 1)


