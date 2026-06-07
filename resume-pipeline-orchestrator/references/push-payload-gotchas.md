# Push Payload Requirements

## Critical: Send BOTH job_description AND job_description_id

The `/api/generated-resumes` endpoint requires **both** fields:

```python
payload = {
    "company_name": "<company_name>",
    "job_description": "<full JD text>",
    "job_description_id": "<jd_id>",
    "latex_content": latex_content,
    "source": "<SOURCE_NAME>"
}
```

**Gotcha:** Omitting `job_description` causes HTTP 400.

## Tool Reminders

- Use `urllib.request` — `requests` NOT installed
- Use `write_file` for .tex — `patch` DOUBLES backslashes
- Verify .tex files by reading back after writing

