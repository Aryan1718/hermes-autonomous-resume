---
name: pool-versioning
description: Reference skill defining how the candidate pool is organized on disk — folder structure, file schemas, naming conventions, and read/write boundaries. Read this when creating, reading, or writing any pool file.
version: 1.0.0
metadata:
  hermes:
    tags:
      - resume
      - pool
      - versioning
      - file-system
      - reference
    category: resume-pipeline
---

# File System and Versioning Guide

> **Purpose:** This is the canonical reference for how the pool is organized on disk. Every guide in the pipeline that reads from or writes to the pool follows the contracts defined here. When in doubt about file structure, naming, or what goes where — this file is the answer.
>
> **Pool base path:** `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/`
>
> **Used by:** The **Project Selection Guide** reads the pool during scoring. The **Point Re-Pointing Guide** reads and writes to the pool on every run. The **LaTeX Assembly Guide** uses the `project_type` field from pool metadata to format OSS contribution title lines correctly.

---

## Table of Contents

1. [Why This System Exists](#why-this-system-exists)
2. [Top-Level Pool Structure](#top-level-pool-structure)
3. [Folder Structure — All Content Types](#folder-structure--all-content-types)
4. [The Three File Contracts](#the-three-file-contracts)
5. [The Index File — Schema and Rules](#the-index-file--schema-and-rules)
6. [Version File — Schema and Rules](#version-file--schema-and-rules)
7. [Raw File — Schema by Content Type](#raw-file--schema-by-content-type)
8. [Version File Naming Convention](#version-file-naming-convention)
9. [How the Agent Reads the Pool](#how-the-agent-reads-the-pool)
10. [How the Agent Writes to the Pool](#how-the-agent-writes-to-the-pool)
11. [Adding a New Project, OSS Contribution, or Role](#adding-a-new-project-oss-contribution-or-role)
12. [Read and Write Boundaries](#read-and-write-boundaries)
13. [Traps to Avoid](#traps-to-avoid)

---

## Why This System Exists

The folder-based system exists so the agent always reads the **smallest file necessary** to make the next decision:

- The **index file** (`idx.md`) is always small — metadata only. Read first to find which version is relevant.
- A **version file** contains points for one JD only. The agent opens exactly one.
- The **raw file** is read only when no prior version is close enough to re-use.

Context stays clean regardless of how many JDs have been run.

---

## Top-Level Pool Structure

```
/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/
├── masters.md             ← unified condensed index: projects + OSS (read-only during selection)
├── projects/
│   └── <project-slug>/
│       ├── raw.md
│       ├── idx.md
│       └── versions/
│           ├── v1-<jd-slug>.md
│           ├── v2-<jd-slug>.md
│           └── v3-<jd-slug>.md
│
├── oss/
│   └── <contribution-slug>/
│       ├── raw.md
│       ├── idx.md
│       └── versions/
│           ├── v1-<jd-slug>.md
│           └── v2-<jd-slug>.md
│
└── work-experience/
    └── <company-slug>/
        ├── raw.md
        ├── idx.md
        └── versions/
            ├── v1-<jd-slug>.md
            └── v2-<jd-slug>.md
```

**Slugs are lowercase, hyphen-separated, no spaces.**

### The Masters Index (`masters.md`)

`masters.md` (at the pool root) is a **unified condensed index** of all personal projects AND OSS contributions. It is read by the **Project Selection Guide** during scoring — avoiding the need to open every `raw.md` during selection.

- **Format:** Per entry: slug, type (`personal_project` or `oss_contribution`), path (exact relative path to raw.md), title (exact `#` heading from raw.md), domain, tech stack, tagline, role, 2-3 condensed bullets. OSS entries also include `repo_url`.
- **Read during:** Project selection scoring (fast path)
- **Not read during:** Re-pointing (full `raw.md` is used for selected projects — resolved from the `path` field)
- **Updated by:** The **Pool Intake Guide** (Step 8) appends to masters.md on every new personal_project AND oss_contribution intake. Updated manually when any `raw.md` is edited.
- **Auto-sync rule:** When any project's or OSS contribution's `raw.md` is edited, the corresponding masters.md entry must be updated to match. Stale masters.md = wrong selection scores.

> **Replacement note:** The old `projects/master.md` (projects-only) has been merged into `masters.md`. If `projects/master.md` still exists, ignore it.

Examples:
- Project slugs: `enterprise-rag`, `ai-insights-workflow`, `discovermap`
- OSS slugs: `langchain-context-fix`, `fastapi-middleware-pr`
- Work experience slugs: `<work-company-slug>`, `alps-web-solutions`, `bisag-n`
- JD slugs: `synapse-ai-engineer`, `buildfast-backend`, `acme-senior-ai`

---

## Folder Structure — All Content Types

All three content types — personal projects, OSS contributions, and work experience — use **identical folder structure**. The agent uses the same read/write pattern everywhere.

The only difference is what goes inside `raw.md` — each type has a different raw schema (see below). Everything else — index format, version file format, naming convention, read/write boundaries — is identical.

---

## The Three File Contracts

| File | Who writes it | Who reads it | When it changes |
|---|---|---|---|
| `raw.md` | Human only | Agent (read-only) | Never — or only when correcting a factual error |
| `idx.md` | Point Re-Pointing Guide only | Project Selection + Point Re-Pointing | Every time a new version is written |
| `versions/vN-jd-slug.md` | Point Re-Pointing Guide only | Point Re-Pointing Guide only | Never after creation — permanent |

**The human writes raw files. The agent writes index entries and version files. Nobody edits existing version files.**

---

## The Index File — Schema and Rules

The index is the retrieval mechanism. **It contains version references only — never resume points.**

### Full schema

```markdown
# Index — <Content Name>

## Pool Metadata
type: personal_project | oss_contribution | work_experience
slug: <folder-slug>
raw_file: raw.md
current_version: <N>

## Version History

### v<N> — <jd-slug>
<YYYY-MM-DD> | <company_name>
file: versions/v<N>-<jd-slug>.md
```

### Index rules

- **One version = one entry.** Never merge. Never delete.
- **Never put points in the index.** Points go in version files only.
- **First version:** entry starts at v1.
- **Keep `current_version` in sync** with the highest version number.

---

## Version File — Schema and Rules

Each version file contains points for one JD only. Small, focused, permanent after creation.

### Full schema

```markdown
# v<N> — <jd-slug>

<dates> | <role title or project name>

<why_now_description>

- <bullet 1 — LaTeX-ready, with \textbf{} applied>
- <bullet 2>
- <bullet 3>
```

### Version file rules

- **Points are LaTeX-ready.** `\textbf{}` applied, `\%` escaped, `\&` escaped.
- **Points are final.** Never edit a version file after creation.
- **No Selection Context header.** No jd_reference, no covers, no lead_requirement — those live in idx.md.
- **No metadata beyond the schema.** No JD text, no score breakdown.

---

## Raw File — Schema by Content Type

### Personal project `raw.md`

Two formats are acceptable — the pipeline reads all fields regardless of which structure is used:

**Format A — STAR-based (from intake template):**
```markdown
# <Project Name>

## Context
**situation:** <The problem being solved and the starting state>
**task:** <What needed to be built or achieved>
**action:** <What was designed, built, and decided — include architecture choices>
**result:** <The outcome — what changed because of this work>

## Technical Scope
skills: <every technology used>
domain: <industry / problem domain>
role: <What the candidate specifically owned vs what others did>

## Dates
**date_started:** <Month YYYY>
**date_ended:** <Month YYYY | ongoing>

## Metrics
metrics: <All real numbers available. If none: "none available">
```

**Format B — Section-based (from pool-versioning schema):**
```markdown
# <Project Name>

## Context
<Full situation — the problem, constraints, starting state>

## What Was Built
<Complete description — architecture, key decisions, trade-offs>

## Technical Scope
skills: <every technology used>
domain: <industry / problem domain>
scale: <team size, data volume, users, requests — everything real>

## Role and Ownership
<What the candidate specifically designed, built, and owned vs what others did>

## All Available Metrics
<Every real number — format: what it measures — value — context>

## Date
started: <Month YYYY>
completed: <Month YYYY | ongoing>
```

**Rules:**
- Both formats are valid. The pipeline extracts facts from whichever fields are present.
- Format A is generated by the intake process. Format B is the canonical reference schema.
- If a project has no dates (user preference: no timeline on resume), the `date_started`/`date_ended` or `started`/`completed` fields may be omitted entirely. The pipeline handles missing dates gracefully — project title lines in LaTeX never show dates regardless.
- When merging multiple uploaded files for the same project, prefer Format B (section-based) as it accommodates richer narrative content.

### OSS contribution `raw.md`

```markdown
# <Repository Name> — <Short Description>

## Repository
repo: <owner/repo-name>
repo_stars: <approximate>
pr_link: <full URL to merged PR or commit>
merged: true
merge_date: <YYYY-MM-DD>

## What the Contribution Was
<Exact description of the fix, feature, or improvement>

## Technical Scope
skills: <every language, framework, or system touched>
codebase_scale: <what kind of system>
contribution_size: <rough scope>

## Validated Outcome
<What the PR description, issue, or release notes say>
<If no metric: "Merged — no metric stated">

## What This Proves as Evidence
<Human-written — what JD requirement types this can honestly prove>
```

### Work experience `raw.md`

When a company has multiple sequential roles, both roles go in ONE `raw.md`. The `dates` field shows the full span, with sub-role date ranges listed underneath. The `Everything That Was Done` section uses sub-headings for each role phase.

```markdown
# <Company Name> — <Current Title> (formerly <Previous Title>)

## Role Reality
title: <current title>
company: <company name>
dates: Mon YYYY – Present
  - Current Title: Mon YYYY – Present
  - Previous Title: Mon YYYY – Mon YYYY
employment_type: full_time | internship | part_time | contract

## Everything That Was Done

**Current Role — <Current Title> (Mon YYYY – Present):**
<current work>

**Previous Role — <Previous Title> (Mon YYYY – Mon YYYY):**
<previous work>

## All Available Metrics
<Every real number — format: what it measures — value — context>

## What This Role Can Honestly Prove
<Human-written honest assessment>
<Strong proof of: ...>
<Weak proof of: ...>
<Cannot prove: ...>
```

```markdown
# <Company Name> — <Current/Most Recent Job Title (formerly Earlier Title)>

## Role Reality
title: <current/most recent title>
company: <Company Name>
dates: <Earliest Mon YYYY – Present | Mon YYYY>
  - <Earlier Role Title>: <Mon YYYY – Mon YYYY>
  - <Current Role Title>: <Mon YYYY – Present>
team_size: <number>
reporting_to: <role title>
employment_type: full_time | internship | part_time | contract

## Everything That Was Done

**<Section Header for Earlier Role (Mon YYYY – Mon YYYY):**>
<What was done during this period>

---

**<Section Header for Current Role (Mon YYYY – Present):**>
<What is being done currently>

## Real Ownership Scope
<What the candidate actually owned end-to-end vs contributed to vs observed — can reference both periods>

## All Available Metrics
<Every real number — format: what it measures — value — context>

## What This Role Can Honestly Prove
<Human-written honest assessment — can reference both periods>
<Strong proof of: ...>
<Weak proof of: ...>
<Cannot prove: ...>
```

**Role Reality rules for multiple roles at one company:**
- `title` = current/most recent title
- `dates` = full span across all roles at this company (earliest start – Present/latest end)
- List each role with its date range as indented sub-items under `dates`
- Heading line (`#`) shows current title with former title in parentheses: `Company — Current Title (formerly Earlier Title)`
- `Everything That Was Done` uses clearly separated sections per role with `---` dividers
- The two periods should be distinguishable so the pipeline can build separate aim lists per role

---

## Version File Naming Convention

**Format:** `v<N>-<jd-slug>.md`

- `N` = simple integer, increments per content item (not global)
- `jd-slug` = 2–4 words, lowercase, hyphen-separated, max 30 chars
- Names the company + role type for at-a-glance identification

**Good:** `v1-synapse-ai-engineer.md`, `v2-buildfast-backend.md`, `v3-acme-senior-ai.md`

**Bad:** `v1-Senior AI Engineer at Synapse AI Inc March 2024.md` (spaces, too long), `v1.md` (no context), `v1-job.md` (too vague)

---

## How the Agent Reads the Pool

### During Selection (scoring pass)
1. Open `idx.md` → read `Pool Metadata` only
2. Check `type` to confirm scope
3. Scan `requirements_targeted` across all version entries — identify similar JDs
4. **Do NOT open any version file during selection.** The index is enough for scoring.

### During Re-Pointing (history check)
1. Open `idx.md` for the selected item
2. Scan all version entries → find closest match (overlapping `requirements_targeted`, similar `jd_type`, `why_now_match`)
3. Open **only that one version file** — `versions/vN-jd-slug.md`
4. Use it as the starting point for re-pointing
5. If no close match → open `raw.md`

**The agent never opens more than two files per item per run: `idx.md` + one version file (or `raw.md`).**

---

## Agent Write Operations — General Tool Rules

**`patch()` requires absolute paths.** Always use the full path from the profile root, e.g. `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/projects/slug/raw.md`. Paths like `workspace/pool/...` will silently fail with "File not found". This applies to every `patch()` call across all pool operations.

**How the Agent Writes to the Pool**

Only during the Re-Pointing step. Selection never writes. **All writes are batched into ONE execute_code call.**

### Step 1 — Determine version number

Count existing version files: `ls versions/ | wc -l` → next version = count + 1. No need to read idx.md.

### Step 2 — Write ALL version files

Single Python script writes all version files for all sections (projects + work experience).

**Version file format (minimal):**
```
# v<N> — <jd-slug>

<dates> | <role title>

<why_now_description>

- <bullet 1>
- <bullet 2>
```

No Selection Context header. No covers, no lead_requirement, no jd_reference. Just the content.

### Step 3 — Update ALL idx.md files

Single Python script appends one-line entries to each idx.md.

**Idx.md entry format (minimal):**
```
### v<N> — <jd-slug>
<YYYY-MM-DD> | <company_name>
file: versions/v<N>-<jd-slug>.md
```

No jd_type, no requirements_targeted, no why_now_match, no what_changed_from_prior. Just date, company, and file reference.

### Write rules

- **Batch ALL writes into one execute_code call.** 7+ files = 1 tool call.
- **Never edit `raw.md`.** Permanent.
- **Never edit a prior version file.** Permanent after creation.
- **Never write points into `idx.md`.** One-line reference only.
- **Write version files AND update idx.md in the same script.** No separate steps.

---

## Adding a New Item to the Pool

When a human adds a new item:

```
pool/<type>/<item-slug>/
├── raw.md          ← Human writes (required before agent can use)
├── idx.md          ← Human creates with Pool Metadata, current_version: 0
└── versions/       ← Empty folder. Agent populates on first run.
```

**Minimum valid `idx.md` on initialization:**

```markdown
# Index — <Content Name>

## Pool Metadata
type: personal_project | oss_contribution | work_experience
slug: <folder-slug>
raw_file: raw.md
current_version: 0

## Version History

(none yet)
```

**The human always initializes. The agent never creates new pool items — only writes versions and updates indexes for existing items.**

---

## Read and Write Boundaries

| File | Human | Selection Agent | Re-Pointing Agent |
|---|---|---|---|
| `raw.md` | Write | Read only | Read only |
| `idx.md` | Write (initialize) | Read only | Read + append |
| `versions/vN-jd-slug.md` | Never | Never | Write (create new) |

**No exceptions.** To correct a prior version, create `vN+1` — never edit `vN`.

---

## Traps to Avoid

1. **Writing points into `idx.md`.** Metadata only. Points go in version files.
2. **Editing a prior version file.** Create `vN+1` with the correction.
3. **Opening all version files at once.** Read index, pick one, open one.
4. **Spaces or special chars in slugs.** Lowercase, hyphen-separated, alphanumeric.
5. **Skipping `current_version` update.** Stale version numbers cause collisions.
6. **Vague `what_changed_from_prior`.** Must be specific and learnable.
7. **Agent creating a new pool item.** Human initializes. Agent only writes versions for existing items.
8. **Writing index before version file exists.** Version file first, then index.
9. **Treating OSS differently from personal projects in read/write.** Same structure, same flows. Only `raw.md` schema differs.
10. **Using the same version number globally.** Version numbers are per item, not global.
11. **Editing the `dates` field in raw.md to remove prior roles.** All roles at the same company are preserved in the raw.md. Never remove a prior role when updating dates.

---

*Pool base path: `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/`*
*This guide is the canonical reference for all pool file structure, naming, and boundaries.*


