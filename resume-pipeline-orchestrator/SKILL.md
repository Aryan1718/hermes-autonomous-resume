---
name: resume-pipeline-orchestrator
description: Master orchestrator for the resume pipeline. Run this to process unprocessed job descriptions (capped at 10 per run). Fetches JDs from the dashboard API, runs pre-filter on each, then the full pipeline (extraction, project selection, point re-pointing, LaTeX assembly) on passing JDs one at a time. Pushes completed resumes to the dashboard, marks successful JDs as processed, and posts one summary log at the end of the run.
version: 1.5.0
metadata:
  conventions:
    profile: <PROFILE_SLUG>
    storage: all files stored under /opt/data/profiles/<PROFILE_SLUG>/ only
    resumes_dir: /opt/data/profiles/<PROFILE_SLUG>/home/<RESUMES_DIR>/
    pool_dir: /opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/
    skills_dir: /opt/data/profiles/<PROFILE_SLUG>/skills/
    env_file: /opt/data/profiles/<PROFILE_SLUG>/.env
required_environment_variables:
  - name: <DASHBOARD_API_KEY_ENV>
    prompt: "Enter your dashboard API key"
    help: "Found in your dashboard settings. Format: <DASHBOARD_API_KEY>"
    required_for: "All API calls to the dashboard"
metadata:
  hermes:
    tags:
      - resume
      - orchestrator
      - pipeline
      - job-search
    category: resume-pipeline
    related_skills:
      - jd-prefilter
      - jd-extraction
      - project-selection
      - point-repointing
      - latex-assembly
      - candidate-profile
      - pool-versioning
      - pool-intake
      - feedback-processor
---

# Resume Pipeline Orchestrator

This skill runs the complete resume pipeline from start to finish. It fetches all unprocessed job descriptions from the dashboard, processes each one sequentially, and posts a single summary log when the batch is done. Run this once — it stops when the batch is complete.

**All file paths are under the `<PROFILE_SLUG>` profile:**
- Resumes saved to: `/opt/data/profiles/<PROFILE_SLUG>/home/<RESUMES_DIR>/`
- Pool (projects, OSS, work-experience) stored under: `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/`
- API key loaded from: `/opt/data/profiles/<PROFILE_SLUG>/.env`

---

## When to Use

Run this skill when you want to process all pending job descriptions from your dashboard. It handles everything in one uninterrupted run:

- Fetching unprocessed JDs (cap at 10 per run)
- Pre-filtering each JD
- Running the full pipeline on passing JDs
- Pushing completed resumes to the dashboard
- Marking processed JDs as used
- Posting a final summary log

Do not run this skill to process a single specific JD manually. For manual runs, invoke the individual skills directly in sequence.

---

## Dashboard API

**Base URL:** `<DASHBOARD_BASE_URL>`
**Auth:** `Authorization: Bearer <DASHBOARD_API_KEY_ENV>` (from `/opt/data/profiles/<PROFILE_SLUG>/.env`)

| Step | Method | Endpoint | When called |
|---|---|---|---|
| Fetch batch | GET | `/api/job-descriptions/next` | Once at start |
| Push resume | POST | `/api/generated-resumes` | Per JD — on full pipeline success |
| Mark processed | PATCH | `/api/job-descriptions/{id}/use` | Per JD — after successful resume push |
| Event log | POST | `/api/workflow-logs` | Per JD + batch summary |

**Push resume:** Always send BOTH `job_description` (full text string) AND `job_description_id` (UUID). Use Python `urllib.request` — never embed .tex in curl -d. See `references/api-reference.md` for the push script and all endpoint details.

**Workflow log status values:** `success`, `failed`, `skipped`. Always include `job_description_id` for per-JD logs. Omit for orchestrator errors and batch summary. See `references/api-reference.md` for status logic and message templates.

**Python API helper:** All API calls use `urllib.request` (NOT `requests`). See `references/api-reference.md` for reusable Python scripts (generic caller, push resume, workflow log, mark processed).

See `references/api-reference.md` for complete endpoint documentation, response shapes, curl examples, and Python helper scripts.

---

## Quality vs. Speed Priority Principle

**Quality is paramount.** JD extraction, project selection, and point-repointing are the core value steps — they should be as thorough as needed. Never rush or cut corners on:
- Scoring projects against JD requirements
- Picking the right verb (honest calibration to seniority)
- Checking if a bullet is truthful and supported by raw.md evidence
- Reading raw files for full context before re-pointing
- Building bullets with problem→action→outcome

**Speed is for mechanical steps only.** Optimize the "plug and play" parts:
- LaTeX assembly (fixed template, just slot in content)
- Version file writes (batch into minimal write calls)
- Dashboard API pushes (straightforward urllib POST)
- idx.md updates (simple append, no analysis needed)

**Speed is learned.** Each run should make the mechanical steps faster through better patterns, fewer read_file calls, and batched writes. The thinking steps should stay thorough. The target of <20 min is for the MECHANICAL overhead — the thinking time for extraction/selection/repointing is sacred.

**When in doubt about a decision (project pick, verb choice, bullet content) — make the best call and proceed. Never block on ambiguity. Never ask the user for permission during an automated run.**

---

## Efficiency Rules (every run)

- **Read only what you need:** 3 selected project raw.md + 3 work-exp raw.md = 6 files max. Score from masters.md. Never read all 7+ project files.
- **Batch ALL writes:** Version files + idx.md updates in ONE execute_code call (interactive mode) or in sequential write_file calls (cron mode — execute_code is blocked). Never write one file at a time when avoidable.
- **Never use delegate_task for the full pipeline.** The pipeline is sequential — run it directly in the parent agent. Subagents do NOT inherit memory or session context. All rules must be in the skill files.
- **Target: <20 minutes** for automated cron runs. If a step takes >5 min, something is wrong — usually too many read_file calls.
- **Write .tex files via Python raw string script** — write a .py file with r\"\"\"...\"\"\" content, then run via terminal. Never construct .tex content inline in write_file arguments (causes double backslash escaping).
- **In cron mode:** Write Python helper scripts to disk via `write_file`, then execute via `terminal`. See `references/api-helper-scripts.md` for reusable patterns.
- **No user interaction during automated runs.** Do NOT use clarify, do NOT ask for permission. Make decisions and proceed.
- **Bullet length consistency:** ALL bullets must be 230-320 chars (target 250-300). After writing every bullet, measure length. Bullets outside this range MUST be adjusted before pushing. All sections (work experience + projects) must have consistent bullet lengths — no section should be noticeably longer or shorter than another.
- **Point budget enforcement:** Use the section budgets derived by `point-repointing` from the current candidate's resume shape. Most sections should have 2 bullets. Use 3 only for unusually strong anchor roles or projects with distinct coverage. Count bullets per section and verify none exceeds its justified limit. If over budget, compress or merge — never exceed what the one-page layout can support.
- **Mid-run quality gate (after every 3rd JD in a batch):** Before continuing, review the last resume's bullets. Check length, specificity, no `--`, bold terms, and bullet count per section. If quality is degrading, re-read raw.md for the next JD before proceeding. Better to produce 7 excellent resumes than 10 mediocre ones.

**References:**
- `references/pipeline-checklist.md` — full timing + quality + efficiency checklist.
- `references/cron-quality-gates.md` — context management for sequential cron runs, quality architecture (defense in depth), reference bullet, and bullet standards.
- `references/jd-batch-context-management.md` — write JD batch to temp file to avoid holding all JD texts in conversation history.

---

## Post-Run Self-Review — HARD GATE (Blocking)

> **This is a BLOCKING GATE. Do NOT push any resume to the dashboard until it passes this review. No exceptions. Not even for cron runs under time pressure. A resume that fails this review is NOT pushed.**

After every pipeline execution (including single JD test runs), BEFORE pushing to the dashboard, do a self-review:

1. **Timing:** How long did each step take? Target <20 min total for automated cron runs. Identify what slowed the run down.

2. **Quality check — EVERY bullet (not just a sample):**
   - No em dashes (`--` or `—`) anywhere? **Search every bullet. If any `--` found, fix BEFORE pushing.**
   - Every bullet has problem→action→outcome?
   - Numbers and keywords bolded? Every bullet must have **at least 2 bold terms** (technologies, tools, metrics, or key concepts).
   - **Bullet length — ALL bullets must be 230-320 chars (target 250-300).** Measure every bullet. Any bullet under 230 chars MUST be expanded. Any bullet over 320 chars MUST be compressed. Use the Redis caching bullet as the reference example (~285 chars): "Deployed a Redis caching layer on AWS with cache refresh controls for a production SaaS platform serving thousands of users, reducing database load by 75% on time-sensitive operational workflows and improving response consistency during traffic spikes." After normalizing, verify that work-experience bullets and project bullets are in the same range — no section should be noticeably longer or shorter than another.
   - No invented skills or metrics?
   - **Bullet budget per section — respected?** Verify each section stays within the dynamic budget chosen by `point-repointing`, and verify the overall resume still fits cleanly on one page. Prefer fewer stronger bullets over padded sections.
   - **Specificity check:** Every bullet must name specific technologies, system names, or exact metrics. Bullets like "Built scalable backend services" are too generic and MUST be rewritten with named technologies and numbers.

3. **File format check:**
   - .tex file starts with `\documentclass{article}` on line 1? If line 1 starts with `%`, fix immediately.
   - No metadata comment headers before `\documentclass`?
   - Version files have ONLY header + bullets (no `---` separators, no LaTeX commands)?
   - idx.md preserved existing structure?

4. **Efficiency check:**
   - How many read_file calls? (Target: 6 — 3 selected projects + 3 work-exp)
   - Were writes batched in single execute_code calls?

5. **Log findings** in `/opt/data/profiles/<PROFILE_SLUG>/pipeline-review-log.md` — one entry per run with:
   - JD name, date, result
   - Timing breakdown
   - Mistakes found
   - Fixes applied to which guide files

6. **Apply fixes** to the relevant guide files via skill_manage patch. Every mistake becomes a new trap or rule — never leave a known issue unpatched.

**If a resume fails ANY quality check, DO NOT PUSH IT. Fix the issues first, then push. A bad resume on the dashboard is worse than no resume at all.**

**CRITICAL: NOTING quality issues is NOT sufficient.** If you find a bullet under 230 chars, a missing bold term, or any `--` — you MUST fix it before pushing. A quality note in the summary that says \"slightly short but pushed\" is a violation of this gate. Fix every issue. If you cannot fix it (e.g., the role has no more content to expand), skip the JD entirely — do NOT push a resume with known defects. Pushing resumes with known quality failures degrades the user's dashboard reputation.

**This step is mandatory. A run without a review is incomplete. A push without a review is a failure.**

---

## Pipeline Flow

```
START
  │
  ▼
[1] Pre-flight check
    → <DASHBOARD_API_KEY_ENV> set? If not → HALT
  │
  ▼
[2] Fetch unprocessed JDs (cap at 10)
    GET /api/job-descriptions/next
    → parse job_descriptions array
    → take first 10 entries max (ordered by created_at ASC)
  │
  ├── success: false or empty array
  │     → POST log (no data) → STOP
  │
  ├── HTTP error
  │     → POST log (orchestrator error) → STOP
  │
  └── array has items → record count (max 10), proceed
  │
  ▼
[3] For each JD in job_descriptions (sequential — one at a time):
  │
  ├── [3a] Run jd-prefilter skill
  │         │
  │         ├── DISQUALIFIED / FAILED_BINARY / score < 40
  │         │     → increment skipped_count
  │         │     → do NOT call PATCH /use
  │         │     → POST /api/workflow-logs (skipped + reason)
  │         │     → continue to next JD
  │         │
  │         └── score ≥ 40 → continue
  │               │
  │               ▼
  │         [3b] jd-extraction skill
  │               │
  │               ├── FAIL → POST log (failed)
  │               │           increment failed_count
  │               │           do NOT call PATCH /use
  │               │           POST /api/workflow-logs (failed + step + error)
  │               │           continue to next JD
  │               │
  │               └── OK → extraction artifact
  │               │
  │               ▼
  │         [3c] project-selection skill
  │               │
  │               ├── FAIL → same as above
  │               └── OK → selection artifact (3 picks + covers lists + project_type)
  │               │
  │               ▼
  │         [3d] point-repointing skill
  │               Inputs: extraction artifact (3b)
  │                     + selection artifact — 3 projects (3c)
  │                     + ALL work-experience role folders from pool
  │               │
  │               ├── FAIL → same as above
  │               └── OK → re-pointed points for projects + work experience
  │                         (writes version files to pool for both)
  │               │
  │               ▼
  │         [3e] latex-assembly skill
  │               │
  │               ├── FAIL → same as above
  │               └── OK → latex_content (.tex string)
  │               │
  │               ▼
  │         [3f] Save .tex file locally
  │               → $HOME/<RESUMES_DIR>/{company-slug}-{YYYY-MM-DD}.tex
  │
  │               │
  │               ▼
  │         [3f.5] SELF-REVIEW (mandatory blocking gate — see full details above)
  │                → Check EVERY bullet: 230-320 chars, ≥2 bold terms, no `--`,
  │                  problem→action→outcome, POINT BUDGET not exceeded
  │                → If ANY bullet fails ANY check: fix NOW, then re-check.
  │                  Do NOT proceed to push with quality failures.
  │                → Fix or skip the JD. Do not push broken resumes.
  │               │
  │               ▼
  │         [3g] POST /api/generated-resumes
  │               │
  │               ├── FAIL → POST log (failed)
  │               │           do NOT call PATCH /use
  │               │           increment failed_count
  │               │           continue to next JD
  │               │
  │               └── OK → resume pushed
  │               │
  │               ▼
  │         [3h] PATCH /api/job-descriptions/{id}/use
  │               │
  │               ├── FAIL → POST log (success with warning)
  │               │           increment succeeded_count (resume was built)
  │               │           note the JD id for manual review
  │               │
  │               └── OK → JD marked processed
  │                         increment succeeded_count
  │                         continue to next JD
  │
  ▼
[4] All JDs done
    → POST /api/workflow-logs (batch summary)
    → STOP
```

---

## Directory Structure

All paths resolve under the `<PROFILE_SLUG>` profile. Set these variables at the start of every run:

```bash
# Profile root
PROFILE_DIR="/opt/data/profiles/<PROFILE_SLUG>"

# Resumes output directory
RESUME_DIR="$PROFILE_DIR/home/<RESUMES_DIR>"
mkdir -p "$RESUME_DIR"

# Pool root (projects, OSS, work-experience)
POOL_DIR="$PROFILE_DIR/workspace/pool"

# .env file location
ENV_FILE="$PROFILE_DIR/.env"

# Load API key
source "$ENV_FILE"
```

The expected pool structure under `$POOL_DIR/`:
```
pool/
  projects/
    <project-id>/
      idx.md
      versions/
        v1.md
        v2.md
        ...
  oss/
    <project-id>/
      idx.md
      versions/
        ...
  work-experience/
    <role-id>/
      idx.md
      versions/
        ...
```

---

## Python API Helper

See `references/api-reference.md` for all Python helper scripts:
- Generic API call script (works for all 4 endpoints)
- Push resume script (handles LaTeX content safely)
- Workflow log script
- Mark JD as processed script

**Key rule:** Use `urllib.request` — `requests` module is NOT installed. Never embed .tex content in curl -d JSON strings.

### Step 1 — Pre-flight check

Before any API call, verify `<DASHBOARD_API_KEY_ENV>` is set:

```bash
source /opt/data/profiles/<PROFILE_SLUG>/.env
if [ -z "$<DASHBOARD_API_KEY_ENV>" ]; then
  echo "HALT: <DASHBOARD_API_KEY_ENV> not set in /opt/data/profiles/<PROFILE_SLUG>/.env"
  exit 1
fi
```

Also load the `candidate-profile` skill into context — it is required by both `jd-prefilter` and `jd-extraction`.

**If `<DASHBOARD_API_KEY_ENV>` is missing — do not POST a log** (can't auth without the key). Halt immediately.

**If the orchestrator crashes or halts unexpectedly at any point after the key is confirmed present**, POST a log before stopping:
```json
{ "status": "failed", "message": "Orchestrator halted unexpectedly. Stage: {current_stage}. Error: {error}. Processed {N} JDs before halt (Succeeded: {s}, Failed: {f}, Skipped: {sk})." }
```

Initialise run counters:
```
fetched_count = 0
succeeded_count = 0
failed_count = 0
skipped_count = 0
failed_patch_ids = []   # JDs where resume pushed but PATCH /use failed
```

---

### Step 2 — Fetch the batch

```bash
RESPONSE=$(curl -s \
  -H "Authorization: Bearer $<DASHBOARD_API_KEY_ENV>" \
  <DASHBOARD_BASE_URL>/api/job-descriptions/next)
```

Parse the response:

- If `success: false` or `job_descriptions` is empty or null → stop cleanly. No log POST needed — there is nothing to report.
- If HTTP error or malformed JSON → POST orchestrator error log → stop.
- If `job_descriptions` is a non-empty array → **cap at 10 JDs maximum**. Take only the first 10 entries from the array (they are already ordered by `created_at ASC`). Set `fetched_count = min(array length, 10)`.
- **Capture the `id` field from each JD object** — this is the `job_description_id` that must be passed to `/api/generated-resumes` when pushing the resume. The same `id` is used for workflow logs and PATCH `/use`.
- **Do NOT re-fetch mid-run.** Process only the JDs from the first fetch. Unprocessed JDs will be picked up in the next scheduled run.

> **JD response format note:** The API returns each JD with a nested `job_description` JSON string containing the full job data. For pipeline processing, only these fields are needed from each JD object:
> - `id` — job_description_id for push, logs, PATCH
> - `company_name` — push payload
> - `job_description` — push payload (required string). Extract from it: `job.title`, `job.summary`, `job.core_skills`, `job.responsibilities`, `job.qualifications[0].mustHave`, `job.detail_qualifications[0].mustHave.hardSkill/softSkill`, `job.location`, `job.seniority`, `job.employment_type`, `job.work_model`
> - Outer fields: `is_h1b_sponsor`, `is_remote`, `is_citizen_only`, `is_clearance_required` — used by pre-filter
>
> Everything else (company metadata, funding, glassdoor, salary, h1b annual counts, etc.) is not used by the pipeline. If storing JDs in the database, a simplified format with only the above fields reduces token usage by ~60-70%.



---

### Step 3 — Process each JD

For each item in `job_descriptions`, track:

```yaml
id: {from response}
company_name: {from response — use directly, do not derive}
job_description: {full text from response}
prefilter_score: null
failed_step: null
error_message: null
resume_filename: null
```



#### 3a — Pre-filter

Load the `jd-prefilter` skill. Pass `job_description` text and the loaded `candidate-profile`.

The pre-filter returns a verdict and score. Decision:

| Result | Action |
|---|---|
| `DISQUALIFIED` | `skipped_count++` → POST log (`status: skipped`, `job_description_id: {jd_id}`) → next JD |
| `FAILED_BINARY` | `skipped_count++` → POST log (`status: skipped`, `job_description_id: {jd_id}`) → next JD |
| Score `< 40` | `skipped_count++` → POST log (`status: skipped`, `job_description_id: {jd_id}`) → next JD |
| Score `≥ 40` | Continue to 3b |

**Never call PATCH `/use` for a skipped JD.** It stays unprocessed so it can be re-evaluated after a candidate profile update.

**Log call for skipped JDs:**
```json
{ "job_description_id": "{jd_id}", "status": "skipped", "message": "{company_name}: pre-filter {result}. Reason: {reason}. Score: {score}." }
```

#### 3b — JD Extraction

Load the `jd-extraction` skill. Pass `job_description` text.

Capture the full extraction artifact: `must_haves`, `behavioral_signals`, `scope_signals`, `cultural_intent_signals`, `hard_screens`, `preferred`.

→ `failed_count++` → do NOT call PATCH `/use` → POST workflow log → next JD.

**Log call for pipeline failures** (same format for all steps — always name the step):
```json
{ "job_description_id": "{jd_id}", "status": "failed", "message": "{company_name}: pipeline broke at {step_name}. Error: {error_message}. JD left unprocessed." }
```

#### 3c — Project Selection

Load the `project-selection` skill. Pass the extraction artifact from 3b and the pool (structured per `pool-versioning` skill). Pool is at `$POOL_DIR`.

Capture: 3 selected projects with `id`, `title`, `project_type` (`personal` or `open_source`), `covers` lists, selection reasoning.

> **Note:** Project selection only selects from the projects and OSS pool — not work experience. Work experience roles are always included in the resume and are passed directly to 3d independently of what 3c selects.

On failure: same pattern — `failed_count++`, no PATCH, POST workflow log, next JD.

#### 3d — Point Re-Pointing

Load the `point-repointing` skill. Pass three inputs:

1. **Extraction artifact** from 3b — the full JD extraction (`must_haves`, `behavioral_signals`, `scope_signals`, etc.)
2. **Selection artifact** from 3c — the 3 selected projects with their `covers` lists and `project_type`
3. **All work-experience role folders** from `$POOL_DIR/work-experience/` — every role, not just selected ones. Work experience is always on the resume regardless of what 3c selected.

**Why work experience must be passed explicitly:** project selection (3c) only selects from the projects and OSS pool. It has no visibility into work experience. If 3d only receives 3c's output, work experience bullets never get re-pointed for the JD — they go into the resume in their generic canonical form, untuned to the role. The orchestrator is responsible for sourcing work experience folder paths from the pool and passing them alongside the selection output.

**How to get all work experience folder paths:**
```bash
# Pool base directory
POOL_DIR="/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>"

# List all work experience items in the pool
ls "$POOL_DIR/work-experience/"

# Pass each folder path to the point-repointing skill
# e.g. "$POOL_DIR/work-experience/<work-company-slug>/"
#      "$POOL_DIR/work-experience/alps-web-solutions/"
#      "$POOL_DIR/work-experience/bisag-n/"
```

The skill reads `idx.md` (for version tracking only), then **always reads `raw.md`** for actual content — raw is the source of truth. Prior version files are used for style/formatting reference only, never as content source. The skill re-points bullets for each, and writes new version files to the pool for both. This is a write operation — version files written before a failure **stay permanently**. Do not attempt to roll them back.

Capture: re-pointed LaTeX-ready points for:
- All 3 selected projects (Track A — from 3c selection output)
- All work-experience roles (Track B — from `$POOL_DIR/work-experience/`)
- Any `honesty_flags` for requirements the sources cannot honestly support

On failure: `failed_count++`, no PATCH, POST workflow log (include which item or sub-step failed in the message), next JD.

#### 3e — LaTeX Assembly

Load the `latex-assembly` skill. Pass the re-pointed points from 3d — this includes both the 3 selected projects (with their `project_type` for title line formatting) and all work-experience roles. Both are required for a complete resume.

Capture: the complete `.tex` string (`latex_content`).

On failure: same pattern — `failed_count++`, no PATCH, POST workflow log, next JD.

#### 3f — Save .tex file locally

```bash
RESUME_DIR="/opt/data/profiles/<PROFILE_SLUG>/home/<RESUMES_DIR>"
mkdir -p "$RESUME_DIR"

COMPANY_SLUG=$(echo "$COMPANY_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
FILENAME="${COMPANY_SLUG}-$(date +%Y-%m-%d).tex"

echo "$LATEX_CONTENT" > "$RESUME_DIR/$FILENAME"
```

**After saving, verify the file:**
```bash
# Read it back and check key things
grep -c "Functional Programming" "$RESUME_DIR/$FILENAME"  # Should be 0
grep -c "^% \\\\vspace" "$RESUME_DIR/$FILENAME"            # Should be 0 (no commented-out projects)
echo "$LATEX_CONTENT" > "$RESUME_DIR/$FILENAME"
```

Where `company_slug` is `company_name` lowercased with spaces replaced by hyphens (e.g., `<TARGET_COMPANY> Corp` → `acme-corp`).

#### 3g — Push resume to dashboard

**IMPORTANT: Only push resumes for JDs that passed pre-filter.** If a JD was disqualified in Phase 1 or failed Phase 2, do NOT push a resume. The pre-filter exists for a reason.

**IMPORTANT: Do NOT push resume content as inline JSON in a curl command.** LaTeX content contains backslashes (`\textbf`, `\%`, etc.) that break JSON serialization in shell commands, and large .tex files exceed curl's command-line limits. This causes silent truncation and corruption (bullets get cut, concepts get replaced).

**Use the Python helper script below to push. It reads the .tex file from disk and sends it properly via `urllib.request`:**

```bash
# Step 1: Save the .tex file (already done in 3f)
# File is at: $RESUME_DIR/<company-slug>-<YYYY-MM-DD>.tex

# Step 2: Push to dashboard using python3
source $ENV_FILE
python3 - <<'PYEOF'
import os, json, urllib.request, urllib.error

env_file = "/opt/data/profiles/<PROFILE_SLUG>/.env"
api_key = None
with open(env_file) as f:
    for line in f:
        line = line.strip()
        if line.startswith("<DASHBOARD_API_KEY_ENV>="):
            api_key = line.split("=", 1)[1]
            break

if not api_key:
    print("ERROR: <DASHBOARD_API_KEY_ENV> not set")
    exit(1)

company_slug = "<company-slug>"  # from Step 3f
resume_dir = "/opt/data/profiles/<PROFILE_SLUG>/home/<RESUMES_DIR>"
tex_file = os.path.join(resume_dir, f"{company_slug}-<YYYY-MM-DD>.tex")

with open(tex_file, "r") as f:
    latex_content = f.read()

payload = {
    "company_name": "<company_name>",
    "job_description": "<job_description>",  # full JD text from the fetch response — required by backend validation
    "job_description_id": "<jd_id>",  # from the JD fetch in Step 2 — the "id" field; links resume to JD
    "latex_content": latex_content,
    "source": "<SOURCE_NAME>"
}

url = "<DASHBOARD_BASE_URL>/api/generated-resumes"
data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, headers={
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}, method="POST")

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8")
        print(f"PUSH_SUCCESS: {json.loads(body).get('generated_resume', {}).get('id', 'unknown')}")
except urllib.error.HTTPError as e:
    print(f"PUSH_FAILED: HTTP {e.code} — {e.read().decode('utf-8')}")
    exit(1)
PYEOF
```

Replace `<company-slug>`, `<YYYY-MM-DD>`, `<company_name>`, and `<jd_id>` with actual values from the current JD run. The `jd_id` is the `id` field from the JD object returned by `/api/job-descriptions/next` (the same `id` used for workflow logs and PATCH `/use`). **Send BOTH `job_description` (the full JD text from the fetch response) AND `job_description_id`** — the backend requires `job_description` as a string field for validation, even though it also accepts `job_description_id` for linking. Omitting `job_description` causes a 400 error: `"Invalid input: expected string, received undefined"`.

**On push failure (`PUSH_FAILED` or non-zero exit):**
- Do NOT call PATCH `/use` — the dashboard has no record of this resume, so marking the JD as used would orphan it.
- POST workflow log (use the Python helper below for workflow logs too): `{ "job_description_id": "{jd_id}", "status": "failed", "message": "{company_name}: resume push failed. Error: {error}. File saved locally at {filename}. JD left unprocessed." }`
- `failed_count++` → next JD.

**On push success (`PUSH_SUCCESS`):**
- Continue to 3h.

#### 3h — Mark JD as processed

```bash
curl -s -X PATCH \
  -H "Authorization: Bearer $<DASHBOARD_API_KEY_ENV>" \
  <DASHBOARD_BASE_URL>/api/job-descriptions/{id}/use
```

**On PATCH failure:**
- Add `id` to `failed_patch_ids` list.
- POST workflow log: `{ "job_description_id": "{jd_id}", "status": "success", "message": "{company_name}: resume built and pushed but PATCH /use failed. Resume is on dashboard but JD still shows unprocessed — review manually." }`
- `succeeded_count++` — the resume was built and pushed successfully. The PATCH failure is an administrative issue, not a pipeline failure.
- Continue to next JD.

**On PATCH success:**
- POST workflow log: `{ "job_description_id": "{jd_id}", "status": "success", "message": "{company_name}: resume assembled, pushed, and JD marked processed. Pre-filter score: {score}. Projects: {p1}, {p2}, {p3}." }`
- `succeeded_count++` → next JD.

---

### Step 4 — End of batch

#### 4a — POST workflow log (batch summary)

Call this at the very end regardless of outcomes. This is the final log call of the run — individual JD outcomes were already logged as they happened throughout the run.

```bash
curl -s -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $<DASHBOARD_API_KEY_ENV>" \
  <DASHBOARD_BASE_URL>/api/workflow-logs \
  -d "{
    \"request_id\": null,
    \"status\": \"{batch_status}\",
    \"message\": \"Batch complete. Fetched: {fetched_count}. Succeeded: {succeeded_count}. Failed: {failed_count}. Skipped: {skipped_count}.\"
  }"
```

Where {batch_status} is:
- `success` — if succeeded_count > 0
- `failed` — if succeeded_count = 0 and failed_count > 0
- `skipped` — if succeeded_count = 0 and failed_count = 0 (all skipped by pre-filter)

If this call itself fails — silently continue. Do not retry. The run is complete regardless.

---

## State Tracking

Track this in memory per JD during the run:

```yaml
id: string                    # from API response
company_name: string          # from API response — use directly
job_description: string       # from API response — full text
prefilter_score: number|null  # set after 3a
failed_step: string|null      # set on any step failure
error_message: string|null    # set on any step failure
resume_filename: string|null  # set after 3f
resume_pushed: boolean        # set after 3g
marked_processed: boolean     # set after 3h
```

---

## Error Handling Reference

| Situation | PATCH /use? | POST log? | `job_description_id` in log? | Increment |
|---|---|---|---|---|
| `<DASHBOARD_API_KEY_ENV>` missing | No — HALT | No (can't auth) | — | — |
| Fetch returns empty/no data | No — STOP | No | — | — |
| Fetch HTTP error | No — STOP | Yes — orchestrator error | No | — |
| Pre-filter: disqualified | No | Yes — skipped | Yes | `skipped_count++` |
| Pre-filter: score < 40 | No | Yes — skipped | Yes | `skipped_count++` |
| jd-extraction fails | No | Yes — failed | Yes | `failed_count++` |
| project-selection fails | No | Yes — failed | Yes | `failed_count++` |
| point-repointing fails | No | Yes — failed | Yes | `failed_count++` |
| latex-assembly fails | No | Yes — failed | Yes | `failed_count++` |
| Resume push fails (3g) | No | Yes — failed | Yes | `failed_count++` |
| PATCH /use fails (3h) | Already tried | Yes — success with warning | Yes | `succeeded_count++` |
| Workflow log POST fails | Already done | N/A | N/A | — | Silently continue — do not retry |

---

## Pitfalls

1. **`<DASHBOARD_API_KEY_ENV>` not set.** The orchestrator halts at pre-flight before any API call is made. Add it to `/opt/data/profiles/<PROFILE_SLUG>/.env`.

2. **Calling PATCH `/use` on a failed JD.** Never. A failed JD must stay `is_used: false` so it can be manually reviewed and reprocessed.

3. **Calling PATCH `/use` on a skipped JD.** Never. A skipped JD may pass pre-filter after a candidate profile update. Marking it used would lose it permanently.

4. **Calling PATCH `/use` when the resume push failed.** Never. If the dashboard has no resume record, marking the JD as used creates a broken state — used but no resume attached.

5. **Running JDs in parallel.** Do not. The `point-repointing` skill writes version files to the pool sequentially by design. Parallel runs risk version number collisions in `idx.md`.

6. **Forgetting to POST a log when the orchestrator crashes mid-run.** If the pipeline breaks unexpectedly (not a per-JD failure but an orchestrator-level error), always POST a log describing what stage it broke at and how many JDs were processed before the halt.

7. **Deriving `company_name` from the JD text.** The `company_name` field comes directly from the API response. Use it as-is for both the resume push body and local filename generation.

8. **Stopping the batch on one JD failure.** One failure does not stop the run. Log it, skip it, continue. Only two situations stop the entire batch: missing API key and a failed fetch call.

9. **Not handling a failed PATCH `/use` as a warning.** If the resume was pushed successfully but PATCH failed, the pipeline succeeded — the resume exists on the dashboard. Counting this as a failure would misrepresent the run. Increment `succeeded_count`, note the ID for manual review.

10. **`patch` tool doubles backslashes in LaTeX code blocks inside markdown.** When editing `.md` files that contain LaTeX commands (e.g., `\\textbf`, `\\%`, `\\vspace`) inside code blocks or tables, the `patch` tool may double the backslashes (e.g., `\\vspace` → `\\\\vspace`). This corrupts the rendered LaTeX. **Always verify by reading the file after patching.** Use `write_file` or `sed` via `terminal` for files containing LaTeX backslashes. This is especially critical for `latex-assembly/SKILL.md` and any file with inline LaTeX examples.

11. **`requests` module not installed.** The `requests` Python package is NOT available on this machine. All Python API helper code in this skill uses `urllib.request` instead. If you see `import requests` in any code snippet, replace it with `import urllib.request, urllib.error` and rewrite the HTTP calls accordingly. Do NOT attempt to `pip install requests` — `pip3` is not available either.

12. **`API_SERVER_HOST` env var does not exist.** The hermes gateway reads the API server host from `config.yaml` (`api_server.host`), NOT from any environment variable. Adding `API_SERVER_HOST=0.0.0.0` to `.env` is silently ignored. The only env var that matters for the API server is `API_SERVER_ENABLED=true` (which activates the platform). Keep the host bind address in `config.yaml` only.

13. **`execute_code` is blocked in cron mode.** When running as a scheduled cron job, the `execute_code` tool is denied. Use `write_file` to write Python scripts to disk, then run them via `terminal` with `python3 <script_path>`. This affects the Efficiency Rules: "Batch ALL writes in ONE execute_code call" — in cron mode, batch writes using `write_file` calls instead (one per file, or use a Python script that writes multiple files).

14. **API key value breaks shell globbing and Python string matching.** The `<DASHBOARD_API_KEY_ENV>` value in `.env` may contain characters (e.g., `*`, `?`, `[`) that bash interprets as glob patterns when the variable is referenced in terminal commands. Never use `$<DASHBOARD_API_KEY_ENV>` directly in shell strings. In Python scripts that read `.env`, use `"<DASHBOARD_API_KEY_ENV>" in line and "=" in line` rather than `line.startswith("<DASHBOARD_API_KEY_ENV>=***` when the value might contain glob characters — the `startswith` approach works for the literal prefix but breaks if the full key=value is embedded in a string that gets glob-expanded. See `references/api-helper-scripts.md` for reusable patterns.

15. **idx.md corruption from naive string replace.** When batch-updating idx.md files, NEVER use `content.replace("\n## ", entry + "\n## ")` — this inserts the entry before ALL `##` section headers, corrupting the file structure. Instead, parse the file line-by-line, find the correct insertion point within the `## Version History` section, and insert there. Better yet, for batch runs, rewrite idx.md from scratch with all version entries in order, or use a dedicated Python script that properly parses the file structure.

16. **Version number tracking in batch runs.** When processing multiple JDs in one batch, version numbers for each pool item must be determined by counting existing version files (`ls <folder>/versions/ | wc -l`, then next = count + 1), NOT by reading idx.md — which may be stale mid-batch. Track version numbers in a Python dict that increments per JD processed, rather than re-reading idx.md each time.

17. **Re-fetch returns ALL unprocessed JDs, not just new ones.** The `GET /api/job-descriptions/next` endpoint returns every JD where `is_used = false`. If you re-fetch mid-run (e.g., after processing some JDs), already-processed JDs from the same batch will appear again. Track processed IDs in memory and skip duplicates. New JDs added since the first fetch will also appear — process them in the same run if time permits.

18. **Processing too many JDs in one run.** The pipeline is capped at 10 JDs per run. If more than 10 unprocessed JDs exist, only the 10 oldest (by created_at) are processed. The rest remain unprocessed and will be picked up in the next scheduled run. Never exceed 10 — quality degrades over long batches, and the agent should produce 10 excellent resumes rather than 20 mediocre ones.

19. **`HOME` directory not set in cron mode.** When running Python scripts via `terminal` in cron mode, the `HOME` environment variable may not be set, causing `Could not determine home directory` errors. Always run scripts with `HOME=/opt/data/profiles/<PROFILE_SLUG> python3 script.py` or `cd /opt/data/profiles/<PROFILE_SLUG> && python3 script.py`.

20. **f-strings break LaTeX in Python scripts.** LaTeX commands (`\textbf`, `\item`, etc.) contain backslashes that Python f-strings interpret as escape sequences, causing `SyntaxError`. Build LaTeX strings using list concatenation (`L.append()`, `"\n".join(L)`) or raw string concatenation — never use f-strings for LaTeX content. See `references/batch-script-template.md` for the working pattern.

---

## Verification

After a run completes, verify:

```bash
# Resumes saved locally
ls /opt/data/profiles/<PROFILE_SLUG>/home/<RESUMES_DIR>/

# New version files written by point-repointing
ls /opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/projects/*/versions/
ls /opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/oss/*/versions/
ls /opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/work-experience/*/versions/

# Updated idx.md files
grep current_version /opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/projects/*/idx.md
```

Check the dashboard for:
- Generated resumes in the resumes section
- The workflow log entry showing the batch summary
- Any JDs still showing `is_used: false` that should have been processed (indicates a PATCH failure)

---

*Calls: `jd-prefilter`, `jd-extraction`, `project-selection`, `point-repointing`, `latex-assembly`*
*Reads: `candidate-profile`, `pool-versioning`*
*Writes: pool version files, `idx.md` files, `/opt/data/profiles/<PROFILE_SLUG>/home/<RESUMES_DIR>/*.tex`*
*API: GET `/api/job-descriptions/next` · POST `/api/generated-resumes` · PATCH `/api/job-descriptions/{id}/use` · POST `/api/workflow-logs`*






