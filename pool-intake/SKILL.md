---
name: pool-intake
description: Runs when a new project, OSS contribution, or work experience file is uploaded. Creates the correct folder structure, places raw.md, generates idx.md, and validates the item is ready for the pipeline.
version: 1.0.0
metadata:
  hermes:
    tags:
      - resume
      - pool
      - intake
      - onboarding
    category: resume-pipeline
---

# Pool Intake Guide

> **Purpose:** This guide tells the agent exactly what to do when a new file is uploaded to be added to the pool. It handles all three content types — personal projects, OSS contributions, and work experience roles. It runs **before** any main pipeline step. The item is not usable by the **Project Selection Guide** or the **Point Re-Pointing Guide** until this guide has completed successfully.
>
> **Depends on:** The `pool-versioning` skill defines the folder structure, file schemas, and naming conventions this guide enforces. Read that skill first if anything here is unclear.
>
> **Pool base path:** `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/`

---

## Table of Contents

1. [What This Guide Does](#what-this-guide-does)
2. [The Type Field — How the Agent Knows What It Is](#the-type-field--how-the-agent-knows-what-it-is)
3. [Step 1: Read and Validate the Uploaded File](#step-1-read-and-validate-the-uploaded-file)
4. [Step 2: Derive the Slug](#step-2-derive-the-slug)
5. [Step 3: Create the Folder Structure](#step-3-create-the-folder-structure)
6. [Step 4: Place raw.md](#step-4-place-rawmd)
7. [Step 5: Generate idx.md](#step-5-generate-idxmd)
8. [Step 6: Create the versions/ Folder](#step-6-create-the-versions-folder)
9. [Step 7: Run the Validation Checklist](#step-7-run-the-validation-checklist)
10. [Required Fields by Type](#required-fields-by-type)
11. [Uploaded File Templates](#uploaded-file-templates)
12. [Scraper File Integration](#scraper-file-integration)
13. [Agent Intake Workflow](#agent-intake-workflow)
14. [Standard Intake Output](#standard-intake-output)
15. [Traps to Avoid](#traps-to-avoid)

---

## What This Guide Does

When you upload a file, this guide runs exactly once for that file. It does seven things in order:

1. **Reads** the uploaded file and identifies its type from the `type:` field
2. **Validates** that all required fields for that type are present
3. **Creates** the correct folder structure in the pool
4. **Places** the uploaded file as `raw.md` and generates the empty `idx.md`
5. **Creates** the empty `versions/` folder
6. **Confirms** the item is ready for the main pipeline
7. **Updates** the masters index for both `personal_project` and `oss_contribution` types (skips `work_experience`)

After this guide completes, the item exists in the pool and the main pipeline can use it. Before this guide completes, the item does not exist in the pool and cannot be selected or re-pointed.

**This guide never modifies the content of the uploaded file.** It only validates, places, and initializes. If content needs to be corrected, the human corrects the uploaded file before re-running intake.

---

## Reference Convention

**Always use skill-name-only references, never hardcoded file paths.**
- ✅ `` `pool-versioning` `` — agent resolves via `skill_view(name='pool-versioning')`
- ✅ `` `project-selection` `` — agent resolves via `skill_view(name='project-selection')`
- ✅ `` `point-repointing` `` — agent resolves via `skill_view(name='point-repointing')`
- ✗ `` `skills/pool-versioning/SKILL.md` `` — never use hardcoded paths

Use absolute paths only for system-level things: `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/`, `/opt/data/profiles/<PROFILE_SLUG>/.env`.

## The Type Field — How the Agent Knows What It Is

Every uploaded file must contain a `type:` field in its header block. This is how the agent identifies what kind of content it is without guessing from filename or reading the full document.

**The three valid values:**

```
type: personal_project
type: oss_contribution
type: work_experience
```

**Location in the file:** the `type:` field must appear within the first 10 lines of the file, in the header block before any other content sections.

**Example header block:**

```markdown
---
type: oss_contribution
name: LangChain Context Window Fix
slug: langchain-context-fix
---
```

### What happens if `type:` is missing or invalid

The agent stops immediately and returns an error:

```
INTAKE FAILED — type: field missing or invalid.
Valid values: personal_project | oss_contribution | work_experience
File: <filename>
Action required: Add a valid type: field in the first 10 lines and re-upload.
```

**Do not attempt to infer the type from filename or content. If the field is absent, stop and report the error.**

**Exception — clear contextual identification:** If the file lacks a `type:` field but the content *unambiguously* describes one type (e.g., a project description with "I built this" language, a GitHub repo URL, and personal ownership signals → `personal_project`; a merged PR link and contribution description → `oss_contribution`; a job role with company name and dates → `work_experience`), the agent may identify the type and proceed — but must state the inferred type explicitly and ask the user to confirm before finalizing intake. Example: "This appears to be a `personal_project` based on [reason]. Proceeding with that type — confirm or correct before I finalize." For two files clearly describing the same project, merge them into one raw.md during intake.

---

## Step 1: Read and Validate the Uploaded File

Read the full uploaded file. Extract the `type:` field first. Then check that all required fields for that type are present.

Required fields per type are defined in the [Required Fields by Type](#required-fields-by-type) section. A field is "present" if it exists in the file with a non-empty value. A field with a placeholder value (e.g., `TBD`, `<fill this in>`, `N/A`) counts as missing — flag it.

**If any required field is missing:**

```
INTAKE INCOMPLETE — missing required fields.
Type: <type>
Missing fields: <list each missing field>
File: <filename>
Action required: Add the missing fields and re-upload.
```

**Do not proceed to Step 2 if required fields are missing.** A pool item with incomplete raw.md data will produce weak or incorrect resume output downstream.

---

## Step 2: Derive the Slug

The slug is the folder name. It is derived in this order of preference:

1. **Use the `slug:` field if present in the file header.** This is the cleanest path — the human defined it explicitly.
2. **Derive from the `name:` field** if no `slug:` field exists: lowercase, replace spaces with hyphens, remove special characters, max 40 characters.
3. **Derive from the filename** if neither `slug:` nor `name:` is present: strip the extension and any type prefix, apply the same formatting rules.

### Slug formatting rules

- Lowercase only
- Hyphens between words, no underscores, no spaces
- Alphanumeric characters and hyphens only
- Maximum 40 characters — truncate at a word boundary if needed
- No leading or trailing hyphens

### Examples

| Input | Derived slug |
|---|---|
| `slug: langchain-context-fix` | `langchain-context-fix` |
| `name: <PROJECT_NAME_EXAMPLE>` | `<project-slug-example>` |
| `name: <WORK_EXPERIENCE_COMPANY_1> — AI/ML Intern` | `<work-company-slug>-ai-ml-intern` |
| filename `oss_fastapi_middleware_pr.md` | `fastapi-middleware-pr` |

### Slug conflict check

Before creating any folder, check whether `pool/<type-folder>/<slug>/` already exists.

- **If it does not exist:** proceed.
- **If it already exists and has no `versions/` content:** the item may have been partially initialized before. Ask the human to confirm before overwriting.
- **If it already exists and has version files:** this slug is already active in the pool. Stop and report a conflict — do not overwrite an active pool item.

```
INTAKE CONFLICT — slug already exists as an active pool item.
Slug: <slug>
Location: pool/<type-folder>/<slug>/
Action required: Either use a different slug or confirm this is a replacement (which will archive the existing item).
```

---

## Step 3: Create the Folder Structure

Create the following structure. The type determines which subfolder under `pool/`:

| Type field value | Pool subfolder |
|---|---|
| `personal_project` | `pool/projects/<slug>/` |
| `oss_contribution` | `pool/oss/<slug>/` |
| `work_experience` | `pool/work-experience/<slug>/` |

**Create exactly:**

```
pool/<type-folder>/<slug>/
├── raw.md          ← placed in Step 4
├── idx.md          ← generated in Step 5
└── versions/       ← created empty in Step 6
```

Do not create any other files or folders. Do not create subfolders inside `versions/` — that folder stays flat.

---

## Step 4: Place raw.md (or Merge and Place)

If the uploaded file already has the proper raw.md schema (with `type:` field, all required sections), copy it directly as `raw.md`.

If the uploaded file is free-form (no `type:` field, no proper schema), **transform it** into the proper raw.md format before placing:

1. Identify the type from the user's statement or from context
2. Map the free-form content to the required fields
3. **Preserve ALL original details** — never summarize, drop, or condense content during transformation
4. Write the transformed content as `raw.md` using the correct schema for that type

**Two-file project uploads (main file + `_v1` file):** The user frequently sends pairs:
- **Main file** (e.g. `projectname.md`) = source of truth. Contains all raw details. NEVER drop content from this file.
- **`_v1` file** (e.g. `projectname_v1.md`) = polished/portfolio-ready version. Use to enrich framing, but main file always takes precedence on facts, figures, sections, and details.

When both files are received for the same project, merge into one `raw.md`:
- Use the main file as the base — every section, bullet, and detail from it must appear in `raw.md`
- Pull improved phrasing and additional structure from the `_v1` file where it adds value
- If content conflicts, the **main file wins**
- Key sections most at risk of accidental loss during merge: `Differentiators`, `Impact / Outcomes`, `Key Decisions`, Architecture details, and any bulleted lists — verify all are preserved

**The raw.md is updatable.** After placement, the agent can update it directly when the user provides new info or corrections — no re-intake needed for content updates.

**Multi-role same-company entries:** If a user has held multiple sequential roles at the same company (e.g. "<ROLE_TITLE_1>" then "<ROLE_TITLE_2>"), this is ONE pool entry, not two. Both roles go in the same raw.md under:
```
dates: Earliest – Latest (or Present)
  - Role Title 1: Date Range 1
  - Role Title 2: Date Range 2
```
The `Everything That Was Done` section should have sub-sections for each role phase. The LaTeX resume will render this using the stacked format (company header → role titles underneath). Never create two separate pool folders for the same company.

---

## Step 5: Generate idx.md

Create `pool/<type-folder>/<slug>/idx.md` with the following content. This is generated by the agent — the human does not write it.

```markdown
# Index — <name from file>

## Pool Metadata
type: <type field value from raw.md>
slug: <derived slug>
raw_file: raw.md
current_version: 0

## Version History

(none yet — first version will be written by the Point Re-Pointing Guide on first pipeline run)
```

**Rules:**
- `current_version: 0` always on initialization — never set it to anything else here
- The Version History section is always empty at intake — no version entries
- The comment line in Version History is helpful for humans reading the file — keep it
- `name` in the heading comes from the `name:` field in raw.md

---

## Step 6: Create the versions/ Folder

Create an empty `versions/` folder inside the item folder:

```
pool/<type-folder>/<slug>/versions/
```

Nothing goes inside it at intake. The `point-repointing` skill will populate it on the first pipeline run that uses this item.

---

## Step 7: Run the Validation Checklist

Before declaring intake complete, verify all of the following:

```
□ raw.md exists at pool/<type-folder>/<slug>/raw.md
□ raw.md contains a valid type: field
□ raw.md contains all required fields for its type (no missing, no placeholder values)
□ idx.md exists at pool/<type-folder>/<slug>/idx.md
□ idx.md has current_version: 0
□ idx.md has an empty Version History section
□ versions/ folder exists at pool/<type-folder>/<slug>/versions/
□ versions/ folder is empty
□ No other files or folders exist in pool/<type-folder>/<slug>/
□ Slug does not conflict with any existing active pool item
```

If every box is checked: intake is complete. Output the success report.

If any box fails: intake is incomplete. Output the failure report with exactly which check failed and what the human needs to do.

---

## Step 8: Update the Masters Index

**Runs for `personal_project` AND `oss_contribution` types.** Skip this step for `work_experience`.

After successful validation (Step 7), append a new entry to `workspace/pool/masters.md` with the following fields extracted from the uploaded file:

**For `personal_project`:**

```markdown
## <Project Title from raw.md # heading>

- **slug:** <derived slug>
- **type:** personal_project
- **path:** workspace/pool/projects/<slug>/raw.md
- **title:** <display name — the # heading from raw.md>
- **domain:** <from raw.md domain field>
- **tech:** <from raw.md skills field>
- **tagline:** <one-line summary of what the project does — written by the agent from the situation/task/action content>
- **role:** <from raw.md role field>
- **bullets:**
  - <bullet 1 — key achievement with quantified impact if available>
  - <bullet 2 — technical depth or architecture highlight>
  - <bullet 3 — differentiator or outcome highlight>
```

**For `oss_contribution`:**

```markdown
## <Contribution Title from raw.md # heading>

- **slug:** <derived slug>
- **type:** oss_contribution
- **path:** workspace/pool/oss/<slug>/raw.md
- **title:** <display name — the # heading from raw.md>
- **repo_url:** <GitHub repo URL if available>
- **domain:** <inferred from contribution context>
- **tech:** <from raw.md skills field>
- **tagline:** <one-line summary of the contribution — what was merged/changed>
- **role:** <contributor role — e.g. "First external contributor">
- **bullets:**
  - <bullet 1 — what was built/fixed with key technical detail>
  - <bullet 2 — impact or outcome>
  - <bullet 3 — external validation signal if applicable>
```

**Rules:**
- The `title` field must match the `#` heading in `raw.md` exactly — this is the display name used in LaTeX.
- The `path` field must be the exact relative path from the profile root to the `raw.md` — the pipeline uses this to open only selected entries during repointing.
- Bullets are **condensed** — 2-3 bullets max, each under 200 chars. These are for selection scoring, not the final resume.
- The tagline is a **single sentence** summarizing the project/contribution's purpose.
- Update the `Entry Count` at the bottom of masters.md (track both projects and OSS).
- If masters.md does not exist, create it with the header template from `pool-versioning`.

**Auto-sync rule:** When any project's or OSS contribution's `raw.md` is edited (manually or via re-intake), the corresponding entry in `masters.md` must be updated to reflect the changes. The masters.md is the selection-facing summary — it must always match raw.md.

**Reference:** `references/master-md-format.md` for the exact entry format and rules.

---

## Required Fields by Type

### personal_project

```
type:           (must be: personal_project)
name:           (display name of the project)
slug:           (optional — derived if absent)
situation:      (the context / problem being solved)
task:           (the objective / what needed to be done)
action:         (what was built / what decisions were made)
result:         (the outcome)
skills:         (comma-separated technologies)
domain:         (industry or problem domain)
role:           (the candidate's specific role and ownership scope)
date_started:   (Month YYYY)
date_ended:     (Month YYYY or "ongoing")
metrics:        (real numbers — or explicitly "none available")
```

### oss_contribution

```
type:           (must be: oss_contribution)
name:           (short name: "RepoName — Description")
slug:           (optional — derived if absent)
repo:           (owner/repo-name)
pr_link:        (full URL to merged PR or commit)
merged:         (true or false — if false, do not intake)
merge_date:     (YYYY-MM-DD — use "unknown" if the user doesn't have the exact date; the item is still usable)
contribution:   (exact description of what changed in the codebase)
skills:         (comma-separated technologies touched)
codebase_scale: (description of the repo — size, type, significance)
validated_outcome: (what PR/issue/release notes say — or "Merged — no metric stated")
what_this_proves:  (frank assessment of which JD requirement types this can honestly prove)
```

> **Hard rule on OSS intake:** if `merged: false`, do not intake the file. Unmerged contributions are not externally validated and cannot carry the validation signal that makes OSS contributions valuable. Return an error and ask the human to re-upload once the PR is merged.

### Work experience

```
type:               (must be: work_experience)
name:               (Company Name — Job Title)
slug:               (optional — derived if absent)
title:              (exact job title — current/most recent title goes here)
company:            (company name)
dates:              (Mon YYYY – Mon YYYY or "Present"; for multiple roles, list sub-roles underneath)
                  (Example: "<CURRENT_ROLE_DATE_RANGE>" with sub-lines:
                             "  - Role Title 1: <PREVIOUS_ROLE_DATE_RANGE>"
                             "  - Role Title 2: <CURRENT_ROLE_DATE_RANGE>")
employment_type:    (full_time | internship | part_time | contract)
team_size:          (number or "unknown")
reporting_to:       (role title — not a person's name)
everything_done:    (full dump of all work — use sub-sections per role phase if multiple roles)
real_ownership:     (what was owned end-to-end vs contributed to vs observed)
metrics:            (real numbers from this role — or explicitly "none available")
what_this_proves:   (frank assessment of strong proof vs weak proof vs cannot prove)
```

**Multi-role same-company entries:** If the candidate held multiple sequential roles at the same company, this is ONE pool entry, not two. Both roles go in the same raw.md. The `dates:` field shows the overall range with sub-role date lines underneath. The `everything_done` section uses sub-sections for each role phase (e.g., "Earlier Role — <ROLE_TITLE_1> (<DATE_RANGE_1>):" and "Current Role — <ROLE_TITLE_2> (<DATE_RANGE_2>):"). The LaTeX resume renders this using the stacked format: company name as header, each role title + date underneath with its own bullet block. Never create two separate pool folders for the same company. Both roles always appear on the resume — the progression signals growth.

---

## Uploaded File Templates

Use these templates when creating a new file to upload. Copy the relevant template, fill in every field, and upload. The `type:` field must be in the header block at the top.

### Personal project template

```markdown
---
type: personal_project
name: <Project Display Name>
slug: <optional-slug-here>
---

## Context
**situation:** <The problem being solved and the starting state>
**task:** <What needed to be built or achieved>
**action:** <What was designed, built, and decided — include architecture choices>
**result:** <The outcome — what changed because of this work>

## Technical Scope
**skills:** <Python, FastAPI, PostgreSQL, Redis, ...>
**domain:** <AI tooling | backend infrastructure | full-stack product | ...>
**role:** <What the candidate specifically owned vs what others did>

## Dates
**date_started:** <Month YYYY>
**date_ended:** <Month YYYY | ongoing>

## Metrics
**metrics:** <All real numbers available. If none: "none available">
```

### OSS contribution template

```markdown
---
type: oss_contribution
name: <RepoName — Short Description of Contribution>
slug: <optional-slug-here>
---

## Repository
**repo:** <owner/repo-name>
**pr_link:** <https://github.com/owner/repo/pull/NUMBER>
## For multiple PRs to the same repo, use pr_links (plural) instead:
# **pr_links:**
#   - <https://github.com/owner/repo/pull/NUMBER_1>
#   - <https://github.com/owner/repo/pull/NUMBER_2>
**merged:** true

## For issues under active investigation (PR not yet merged):
# **issues:**
#   - https://github.com/owner/repo/issues/NUMBER
# Describe the investigation status in the contribution section:
#   "Issue #N — under discussion/testing:" or "Issue #N — PR forthcoming"
**merge_date:** <YYYY-MM-DD — use "unknown" if the exact date is not available; the item is still usable>
**codebase_scale:** <What kind of system. Approximate stars if known.>

## Contribution
**contribution:** <Exact description of what changed — merge multiple PRs into one coherent description>
**skills:** <Languages and systems touched>

## Outcome
**validated_outcome:** <What PR/issue/release notes say. If nothing: "Merged — no metric stated">

## Evidence Value
**what_this_proves:** <Frank assessment — which JD requirement types this can honestly prove>
```

### Work experience template

```markdown
---
type: work_experience
name: <Company Name — Job Title>
slug: <optional-slug-here>
---

## Role
**title:** <Exact job title>
**company:** <Company name>
**dates:** <Mon YYYY – Mon YYYY | Present>
**employment_type:** <full_time | internship | part_time | contract>
**team_size:** <Number on immediate team>
**reporting_to:** <Role title of direct manager>

## Everything Done
**everything_done:** <Full dump — messy is fine>

## Ownership
**real_ownership:** <End-to-end vs contributed vs observed>

## Metrics
**metrics:** <Every real number. If none: "none available">

## Evidence Assessment
**what_this_proves:**
- Strong proof of: <...>
- Weak proof of: <...>
- Cannot prove: <...>
```

---

## Scraper File Integration

When the LinkedIn profile scraper, company site scraper, or any other automated source generates a file for intake, the same process applies — the agent checks for the `type:` field and required fields just as it would for a manually written file. The scraper is responsible for generating a file that conforms to the correct template.

### What the scraper must produce

The scraper output must include:
- A valid `type:` field in the first 10 lines
- All required fields for that type populated with real scraped data
- No placeholder values — if the scraper cannot find a value, it writes `"not found"` rather than leaving the field empty or writing `TBD`

### The `"not found"` convention

A scraper-generated file may have fields it could not populate. These are written as `"not found"` rather than left empty. The intake agent treats `"not found"` as a present field — it passes validation. However, it flags each `"not found"` field in the intake output so the human knows which fields need manual completion before the item will score well in the pipeline.

---

## Agent Intake Workflow

Run in this exact order for every uploaded file:

1. Read the uploaded file. Extract the `type:` field from the first 10 lines.
2. If `type:` is missing or invalid — **stop. Return the type error. Do not proceed.**
3. Check all required fields for the identified type.
4. If any required field is missing or is a placeholder — **stop. Return the missing field error. Do not proceed.**
5. Derive the slug (from `slug:` field, then `name:` field, then filename).
6. Check for slug conflict in the pool.
7. If conflict exists — **stop. Return the conflict error. Do not proceed.**
8. Create the folder: `pool/<type-folder>/<slug>/`
9. Place the uploaded file as `raw.md`
10. Generate and write `idx.md` with `current_version: 0` and empty Version History
11. Create the empty `versions/` folder
12. Run the validation checklist (Step 7 above)
13. If type is `personal_project` or `oss_contribution` — update `workspace/pool/masters.md` with the new entry (Step 8). For `work_experience`, skip this step.
14. Output the intake report

### Agent behavior rules

- **Never modify the uploaded file.** It becomes raw.md as-is. Corrections go back to the human.
- **Never proceed past a blocking error.** The three blocking errors (missing type, missing required fields, slug conflict) each stop the process completely.
- **Never set `current_version` to anything other than 0 at intake.** The pipeline writes the first version, not the intake process.
- **Never create version files at intake.** The `versions/` folder is always empty after intake.
- **Treat `"not found"` as present but flagged.** It passes validation; it gets a warning in the output.
- **Treat `unknown` for `merge_date` as present but flagged.** Item is usable; add a warning so the user knows to fill it in later.
- **One uploaded file = one intake run.** If the human uploads three files at once, run intake three times independently — once per file.

---

## Standard Intake Output

### Success

```yaml
intake_status: COMPLETE
file: <original filename>
type: personal_project | oss_contribution | work_experience
slug: <derived slug>
location: pool/<type-folder>/<slug>/

files_created:
  - pool/<type-folder>/<slug>/raw.md
  - pool/<type-folder>/<slug>/idx.md
  - pool/<type-folder>/<slug>/versions/   (empty)

warnings: []

next_step: >
  This item is now available in the pool.
  It will be considered by the Project Selection Guide on the next pipeline run.
  The Point Re-Pointing Guide will write the first version file
  (versions/v1-<jd-slug>.md) on the first run that selects this item.
```

### Success with warnings (scraper fields not found)

```yaml
intake_status: COMPLETE_WITH_WARNINGS
file: <original filename>
type: oss_contribution
slug: langchain-context-fix
location: pool/oss/langchain-context-fix/

files_created:
  - pool/oss/langchain-context-fix/raw.md
  - pool/oss/langchain-context-fix/idx.md
  - pool/oss/langchain-context-fix/versions/   (empty)

warnings:
  - field: codebase_scale
    value: "not found"
    impact: "Item will score lower on Domain Match until populated"
    action: "Edit raw.md and add the codebase description manually"
  - field: validated_outcome
    value: "not found"
    impact: "Item will score at the impact floor (8/30) until a real outcome is added"
    action: "Check the PR description and release notes; edit raw.md with the outcome"

next_step: >
  This item is usable in the pipeline but will underperform on scoring
  until the warned fields are filled in. Edit raw.md directly to add them.
  No re-intake is needed after editing raw.md — the pipeline reads raw.md live.
```

### Failure — missing type field

```yaml
intake_status: FAILED
file: <original filename>
error: MISSING_TYPE_FIELD
message: >
  The type: field was not found in the first 10 lines of the file.
  Valid values: personal_project | oss_contribution | work_experience
action_required: >
  Add a type: field to the file header block and re-upload.
```

### Failure — missing required fields

```yaml
intake_status: FAILED
file: <original filename>
type: work_experience
error: MISSING_REQUIRED_FIELDS
missing_fields:
  - real_ownership
  - what_this_proves
message: >
  The above fields are required for type: work_experience but were not found
  or contained placeholder values.
action_required: >
  Add the missing fields to the file and re-upload.
```

### Failure — unmerged OSS contribution

```yaml
intake_status: FAILED
file: <original filename>
type: oss_contribution
error: UNMERGED_CONTRIBUTION
message: >
  merged: false — this contribution has not been merged into the repository.
  Unmerged contributions cannot be added to the pool because they lack
  external validation.
action_required: >
  Re-upload this file after the PR is merged and update:
    merged: true
    merge_date: <YYYY-MM-DD>
```

### Failure — slug conflict

```yaml
intake_status: FAILED
file: <original filename>
slug: <project-slug-example>
error: SLUG_CONFLICT
existing_location: pool/projects/<project-slug-example>/
existing_versions: 3
message: >
  A pool item with this slug already exists and has active version history.
action_required: >
  Option A: Use a different slug.
  Option B: If this is a genuine replacement, manually archive the existing folder.
```

---

## Traps to Avoid

1. **Inferring type from filename.** The `type:` field in the file header is the only valid source.
2. **Proceeding past a blocking error.** All three blocking errors stop the process completely.
3. **Setting `current_version` to anything other than 0.** The pipeline writes versions. Intake only initializes.
4. **Writing anything into the `versions/` folder at intake.** It is always empty after intake.
5. **Modifying the uploaded file's content.** The agent reads it and places it. It does not edit it.
6. **Running intake on an unmerged OSS contribution.** The merged state is the validation signal.
7. **Treating a `"not found"` scraper value as a blocking error.** It is a warning, not a failure.
8. **Skipping the slug conflict check.** Silently overwriting an active pool item destroys accumulated point history.
9. **Running intake more than once for the same file.** The conflict check will catch it.
10. **Leaving the `versions/` folder absent.** It must exist and be empty.
11. **Accepting a free-form file without a `type:` field and guessing the type.** If the uploaded file has no `type:` header (e.g. a free-form markdown resume or notes file), do NOT guess the type. Stop and ask the user: "This file doesn't have a `type:` field. Is this a personal_project, oss_contribution, or work_experience? Please add `type: <value>` to the header and re-upload, or tell me and I'll transform it into the proper raw.md format."
12. **Combining multiple OSS PRs to the same repo.** When the user has multiple merged PRs for the same repository, combine them into a single pool entry rather than creating separate ones. Use the repo name as the project name, list all PR links under `pr_links:`, and merge the contribution descriptions into one coherent entry. This creates a stronger narrative (shows repeated meaningful contribution to one project) and saves resume project slots for other work. Archive the individual entries if they were already created separately. See `references/combined-oss-pr-same-repo.md` for a worked example.

14. **Project title convention for `raw.md` `#` heading.** The first heading in `raw.md` becomes the project title on the resume. Keep it **concise** — just the project/repo name and any notable branding. Do NOT include descriptive subtitles, contribution summaries, or technology lists in the title. The `What Changed` section exists for details.
    - ✅ `# <OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>)` — clean, recognizable, concise
    - ✅ `# <OSS_PROJECT_NAME_2> — Server URL Edit Fix` — repo + brief context if needed for disambiguation
    - `# <OSS_PROJECT_NAME> — <EXTERNAL_PLATFORM> Adapter + Windows Fix + Runtime Smoke Fix` — contribution details belong in body, not title
    - ✗ `# <OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>) — <EXTERNAL_PLATFORM> Context Source + Windows Build Fix + Runtime Smoke Fix` — too long; all contributions described in detail below

13. **Transforming free-form content into raw.md without preserving all data.** When a file comes in without the proper schema, the agent must transform it into the raw.md format while preserving ALL original details — responsibilities, metrics, dates, skills, links, `Differentiators`, `Impact / Outcomes`, `Key Decisions`, and bulleted lists. Never summarize or drop content during transformation. Key sections most at risk: `Differentiators`, `Impact / Outcomes`, `Key Decisions` — explicitly verify these are present after every merge or transformation.

13b. **Dropping content from the main upload file when a `_v1` companion is present.** When two files arrive for the same project (e.g. `project.md` + `project_v1.md`), the main file is the source of truth. The `_v1` file enriches but never replaces. After writing `raw.md`, cross-check: every bullet from the main file's `Problem`, `What It / What the contribution was`, `Implementation`, `Architecture`, `Key Decisions`, `Differentiators`, and `Impact / Outcomes` sections must be present in `raw.md`. If anything from the main file was lost during merge, restore it before declaring intake complete.

13. **Creating a second pool entry for the same company.** If a user held two sequential roles at the same company, both roles go in ONE raw.md entry with a date range covering the full period and sub-role date ranges listed underneath. Never create two separate pool folders (e.g., `<work-company-slug>` and `<work-company-slug>-intern`). The multi-role stacked format belongs in a single `raw.md`.

12. **Combining multiple OSS PRs to the same repo.** When the user has multiple merged PRs for the same repository, combine them into a single pool entry rather than creating separate ones. Use the repo name as the project name, list all PR links under `pr_links:`, and merge the contribution descriptions into one coherent entry. This creates a stronger narrative (shows repeated meaningful contribution to one project) and saves resume project slots for other work. Archive the individual entries if they were already created separately.

13. **Using `patch` without absolute paths.** The `patch()` tool requires **absolute paths** (e.g. `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/...`). Relative paths like `workspace/pool/...` will fail with "File not found". Always construct the full path from the profile root. This applies to ALL `patch()` calls, not just file edits — every file operation through `patch()` needs an absolute path.

13a. **Using `patch` on lines containing LaTeX backslashes inside markdown code blocks.** The `patch` tool may double backslashes in the actual file content. Always verify by reading the file after patching, and use `sed` via terminal or `write_file` to fix any doubled backslashes. Prefer `write_file` over `patch` for lines containing LaTeX commands within markdown tables or code blocks.

14. **Forgetting to update `pool/masters.md` after intake or raw.md edit.** After every successful intake AND after every manual raw.md edit, the agent MUST update `workspace/pool/masters.md` with the item's condensed entry — title, type, path, slug, domain, tech stack, role, 2-3 bullets. Masters.md is the fast-lookup index for project selection — if it's stale, selection quality degrades. Applies to both `personal_project` and `oss_contribution` entries. See `references/master-md-format.md` for the exact schema.

---

*This guide runs once per uploaded file, before any main pipeline step. After successful intake, the item is available to the `project-selection` skill and the `point-repointing` skill. Pool structure is governed by the `pool-versioning` skill.*




