---
name: point-repointing
description: Runs after project-selection. Re-aims existing resume bullets at the current JD by changing the lead, verb, and foregrounded metric. Reads idx.md and raw.md per item, writes a new version file and updates idx.md.
version: 3.1.0
metadata:
  hermes:
    tags:
      - resume
      - tailoring
      - repointing
      - bullets
    category: resume-pipeline
---

# Point Re-Pointing Guide

> **Purpose:** Re-aim resume points at a specific JD — same truth, different target. Changes the lead, verb, and foregrounded metric. Never changes what actually happened. Run after project-selection, before latex-assembly.

**Inputs:** JD extraction artifact + 3 selected projects (with `covers` lists) + all work-experience role folders.
**Output:** JD-tailored points for all sections + `technical_skills_update`. No invented skills or metrics.

**Re-pointing is editing, not authoring.** If a bullet needs more than re-leading, re-verbing, and re-foregrounding, the honest move is a smaller claim — not a bigger one.

**Read sequence (ONCE at start):**
1. `idx.md` — version tracking only, never content source
2. `raw.md` — ONLY the relevant role/project block. Every bullet derived from raw.
3. One prior version (optional) — style reference only, never copy content.

**Pool base path:** `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/`
**`raw.md` is permanent and read-only. Never write to it.**

---

## The Re-Pointing Principle

Three variables you can move. One you cannot:

| Variable | What re-pointing does |
|---|---|
| **The lead** | Reorder so JD's highest-priority element comes first |
| **The verb** | Swap to JD's verb — honestly. "Built" → "Architected" only if work genuinely involved architecture |
| **The foregrounded metric** | Surface the number the JD cares about |
| **The truth** *(never moves)* | The work, scope, actual numbers, technologies used |

---

## Two Input Tracks

### Track A — Selected Projects
- Arrive from project-selection with `covers` list
- Folder: `POOL_DIR/projects/<slug>/` or `POOL_DIR/oss/<slug>/`
- `covers` list = direct aim instruction

### Track B — Work Experience
- Every role goes on the resume. No selection.
- Folder: `POOL_DIR/work-experience/<slug>/`
- No `covers` list — build aim list from raw.md
- Build a SEPARATE aim list for each role at the same company

---

## Step 1: Build Per-Section Aim List

**For selected projects:** Take the `covers` list as the aim list. Enrich with JD verbs. Mark highest-priority as `leads: true`.

**For work-experience roles:** Read raw.md block. List every JD requirement the role can **honestly** speak to. Tag with priority. Pull matching JD verb. Mark highest-priority as `leads: true`. Note Anti-Resume signals to downplay.

---

## Step 2: Re-Point Each Bullet

### 2a. Order to aim list
The bullet covering `leads: true` goes first. Remaining bullets follow descending priority.

### 2b. Mirror JD verb — honestly
Use the JD's verb only when work genuinely supports it. "Architect" requires architecture decisions. "Own" requires ownership scope.

**Verb Translation Reference:**
| Your Word | JD's Word (Match It) |
|---|---|
| Helped | Partnered with / Collaborated with |
| Worked on | Owned / Drove / Led |
| Made | Built / Architected / Designed |
| Improved | Optimized / Scaled / Streamlined |

### 2c. Foreground JD-relevant metric
If the bullet has multiple real numbers, surface the one the JD cares about. Only real, source-supported numbers. Never invent.

### 2d. De-emphasize Anti-Resume flags
Move flagged content down, compress, or reframe. Don't delete truth — reframe it.

### 2e. Per-Bullet Quality Checklist — RUN AFTER EACH BULLET

1. **Length:** 230-320 chars (target 250-300)? Strip LaTeX commands first.
2. **Bold terms:** At least 2 bold terms (tech, tools, metrics, key concepts)?
3. **Em dashes:** Search for `--` and `—`. If found → rewrite with commas.
4. **Problem→Action→Outcome:** All three present?
5. **Specificity:** Names specific tech, systems, exact metrics? Not generic?
6. **JD alignment:** Targets a requirement from the aim list?

**Fix BEFORE moving to next bullet. Do NOT batch-write then check.**

---

## Step 2.5: Update Technical Skills Section

Produce `technical_skills_update` for the LaTeX assembler:

1. Read candidate-profile's Provable Must-Haves table. **Only these skills may appear.**
2. For each JD must-have/surface-requirement, check if it matches a provable skill → promote to front of its category.
3. Reorder items within ALL 5 categories (Languages, Frameworks, Databases, Cloud & Tools, Concepts) so JD-relevant skills appear first.
4. **Concepts row: hard limit of 6 items max.**
5. Output all 5 categories. Never add a skill not in the profile.

---

## Step 3: Honesty Gate

For any JD requirement a section **cannot honestly support**, record a flag:

```yaml
honesty_flags:
  - requirement: "<JD requirement>"
    section: "<where the gap showed up>"
    note: "<what is missing>"
```

**Never invent a bullet to fill a gap.** A recorded honesty flag beats fabricated content.

---

## Step 4: Section Read — HARD GATE (Blocking)

### 4a — Lead bullet check:
- Lands the JD's top requirement?
- Verb honest and calibrated to JD seniority?
- Right numbers foregrounded?
- **230-320 chars?**
- No em dashes? Numbers and keywords bolded?
- Problem→Action→Outcome?

### 4b — Supporting bullets check:
- Each covers a *different* requirement from lead?
- Within point budget?
- **Each 230-320 chars?**
- No em dashes, bolded, keywords bolded?

### 4c — Cross-section check:
- Every honesty flag recorded?
- No two sections saying the same thing?
- Resume sounds like the JD's world?

### 4d — FINAL VERIFICATION (LAST before write-back):

**Search EVERY bullet for `--`.** If ANY found → REWRITE IMMEDIATELY. Use commas. Zero tolerance.

**Measure EVERY bullet.** Under 230 → expand. Over 320 → compress. Target 250-300.

**Count bullets per section.** Cloud2 OSD=3, SWE Intern=2, Alps=2, <WORK_EXPERIENCE_COMPANY_3>=2. Projects=2 each (KTX=3). Total max=16. Over budget → compress.

**Do NOT proceed with failing bullets. Fix or skip.**

---

## Point Budget Per Section

### Work Experience
| Section | Max Bullets |
|---|---|
| <WORK_EXPERIENCE_COMPANY_1> — <ROLE_TITLE_1> (<DATE_RANGE_1>) | **3** |
| <WORK_EXPERIENCE_COMPANY_1> — <ROLE_TITLE_2> (<DATE_RANGE_2>) | **2** |
| <WORK_EXPERIENCE_COMPANY_2> | **2** |
| <WORK_EXPERIENCE_COMPANY_3> | **2** |

### Projects
| Project | Max Bullets |
|---|---|
| <OSS_PROJECT_NAME> (if selected) | **3** |
| All other selected projects | **2** (expand to 3 only if 3+ unique priority:A requirements) |

### Fit within budget
- Compress related contributions into one bullet. Use semicolons for closely related items.
- **Never exceed budget.** One page only.

---

## Step 5: Write Back — BATCHED (ONE execute_code call)

Python script writes ALL version files and updates ALL idx.md files in one call.

**Version file format:**
```
# v<N> — <jd-slug>

<dates> | <role title or project title>

<why_now_description>

- <bullet 1>
- <bullet 2>
- <bullet 3>
```

**Project title rule:** Must match the `#` heading in raw.md exactly. If raw.md has `# <OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>)`, version file must show `<OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>)` — never simplify.

**Version number** = count of existing version files + 1. No need to read idx.md.

**Batch ALL writes:** Version files + idx.md updates = 1 tool call, not 12.

---

## Standard Output

```yaml
jd_reference: "Role Title — Company"

projects:
  - project_id: "P1"
    title: "Project Name"
    points:
      - "<bullet 1 — lead, targets JD #1 priority>"
      - "<bullet 2>"

work_experience:
  - role: "<ROLE_TITLE_2>"
    company: "<WORK_EXPERIENCE_COMPANY_1>"
    date: "<CURRENT_ROLE_DATE_RANGE>"
    points:
      - "<bullets for this role>"

honesty_flags:
  - requirement: "<JD requirement>"
    section: "<section>"
    note: "<what is missing>"

technical_skills_update:
  languages: "Python, TypeScript, JavaScript, Java, C++"
  frameworks: "React, Next.js, FastAPI, Flask, Node.js, LangGraph, CrewAI"
  databases: "PostgreSQL, Redis, MongoDB, DynamoDB"
  cloud_and_tools: "AWS, Docker, GitHub Actions, CI/CD, Ollama, VLLM"
  concepts: "API Design, Distributed Systems, Multi-Agent Orchestration, RAG, LLM Inference, Observability"
```

---

## Key Rules

- **Always read raw.md for content.** Every bullet derived from raw — never from memory or prior versions.
- **Never write to raw.md.** Permanent and read-only.
- **Never edit prior version files.** Each is permanent after creation.
- **Re-aim, don't re-author.** No basis in raw or versions = point-creation task, not repointing.
- **Be deterministic.** Same JD + same inputs = same output.
- **Work experience bullets must be tailored to the JD** — just like project bullets. Different JD = different emphasis. Lead with what THIS JD cares about from this role.
- **Project bullets must be tailored to the JD** — same project, different JD = different bullets. Lead targets JD #1 priority.

---

## Traps to Avoid

1. Not reading raw.md for content — always derive from raw, never prior versions.
2. Writing to raw.md — permanent and read-only.
3. Editing prior version files — each is permanent.
4. Re-authoring instead of re-aiming.
5. Inflating the verb — senior verb for junior work reads as inflated.
6. Inventing a metric — only real, source-supported numbers.
7. Burying the requirement a project was selected for — if covers says "distributed systems", that must lead.
8. Same bullets across different JDs — project AND work-experience bullets must be tailored.
9. Generic bullets — "Built a scalable platform" is too vague. Add specific tech, metrics, outcomes.
10. Priority:A gap left silent — always record honesty flags.
11. Exceeding point budget — compress, never add a page.
12. Overlapping role bullets at same company — OSD and Intern bullets must tell different stories.
13. Not updating Technical Skills — must produce `technical_skills_update` with all 5 categories.
14. Inventing concepts — Concepts row limited to honest, provable skills only. Max 6.
15. Stripping project titles — preserve raw.md `#` heading exactly in version files.
16. No `--` in any bullet — ZERO TOLERANCE. Use commas, restructure. Check every bullet.
17. Bullet length outside 230-320 — measure every bullet after writing.
18. Inconsistent length across sections — all sections must be visually balanced.
19. Bullet ownership — end with what YOU achieved, not what others did ("co-founder confirming" → "identifying root cause").
20. Lead with implementation — sell capability first, implementation second. "Enabling AI agents to securely ingest" not "Built an adapter with auth".

---

## Closing Principle

> **A re-pointed resume is not a rewritten resume. It is the candidate's real work — every project, every role, every honest number — turned so the part facing the hiring manager is the part this job description asked for.**

Aim, don't author. Mirror the JD's verbs honestly. Foreground the metric this JD cares about. Lead with what was selected. Flag every gap instead of filling it with fiction.

**References:**
- `references/versioning-system.md` — Folder-based versioning system, read/write procedures
- `references/point-creation-relation.md` — Relationship to point-creation skill, lazy-loading strategy
- `references/input-tracks.md` — Two input tracks (A/B) detailed explanation
- `references/repointing-methodology.md` — Detailed repointing methodology with examples
- `references/worked-example.md` — Full worked example end-to-end
- `references/cron-failure-patterns.md` — Documented failure patterns from cron runs


