---
id: skill-workflow
title: Skill Workflow
sidebar_position: 5
slug: /resume-agent/skill-workflow
---

# Skill Workflow

This page is the step-by-step contract map for the skills that make up the resume agent.

If you want to inspect the actual skill contracts described here, use the public source repository:

- [hermes-autonomous-resume on GitHub](https://github.com/Aryan1718/hermes-autonomous-resume)

## `candidate-profile`

**Purpose:** Candidate-specific source of truth for role scope, disqualifiers, provable skills, strongest signals, and career direction.

**When it runs:** Before every JD batch and whenever candidate facts change.

**Inputs:** Real candidate facts.

**Output:** Filled `candidate-profile/SKILL.md`.

**Writes anything?** No runtime write during orchestration; it is a maintained reference file.

**Why it matters:** All candidate-specific judgments should come from here, not from hidden assumptions in downstream skills.

## `pool-intake`

**Purpose:** Add new personal projects, OSS contributions, or work experience into the pool in the required structure.

**When it runs:** Whenever new evidence is uploaded or prepared.

**Inputs:** One source file with `type:` and required metadata.

**Output:** Initialized pool item with `raw.md`, `idx.md`, `versions/`, and where applicable a `masters.md` entry.

**Writes anything?** Yes.

**Why it matters:** Downstream skills depend on structured, validated evidence rather than loose notes.

## `pool-versioning`

**Purpose:** Define the pool folder structure, file contracts, naming rules, and read/write boundaries.

**When it runs:** As a reference whenever pool content is created, read, or updated.

**Inputs:** Existing pool structure and conventions.

**Output:** Structural rules used by other skills.

**Writes anything?** No.

**Why it matters:** It is the canonical contract for where evidence lives and which stages are allowed to write.

## `jd-prefilter`

**Purpose:** Disqualify obvious non-fits, score survivors, and decide which JDs are worth deeper processing.

**When it runs:** Immediately after the orchestrator fetches a JD batch.

**Inputs:** Raw JD text plus `candidate-profile`.

**Output:** Pass/skip decision, score, and reasons.

**Writes anything?** No.

**Why it matters:** It keeps the expensive tailoring stages focused on realistic opportunities.

## `jd-extraction`

**Purpose:** Turn one passing JD into a structured artifact of must-haves, behavior signals, scope signals, and cultural intent.

**When it runs:** After `jd-prefilter` passes a JD.

**Inputs:** Raw JD text plus `candidate-profile` for calibration.

**Output:** Structured extraction artifact.

**Writes anything?** No.

**Why it matters:** It gives selection and repointing a normalized reading of what the role actually wants.

## `project-selection`

**Purpose:** Choose the 3 strongest personal-project or OSS items for the current JD.

**When it runs:** After `jd-extraction`.

**Inputs:** JD extraction artifact plus `pool/masters.md`.

**Output:** 3 selected items, coverage lists, scores, and reasoning.

**Writes anything?** No.

**Why it matters:** It narrows the supporting evidence set before any bullet tailoring starts.

`project-selection` never selects work experience. Work experience is always included later by `point-repointing`.

## `point-repointing`

**Purpose:** Tailor bullets toward the JD without changing the underlying truth.

**When it runs:** After `project-selection`.

**Inputs:** JD extraction artifact, selected projects/OSS items, and all work-experience role folders.

**Output:** Tailored bullets, honesty flags, and `technical_skills_update`.

**Writes anything?** Yes. It writes new version files and updates `idx.md`.

**Why it matters:** This is where the resume becomes role-specific while staying grounded in real source evidence.

## `latex-assembly`

**Purpose:** Slot the tailored content into the fixed LaTeX resume structure.

**When it runs:** After `point-repointing`.

**Inputs:** Tailored projects, tailored work experience, and `technical_skills_update`.

**Output:** Final `.tex` content.

**Writes anything?** Produces the `.tex` artifact for saving.

**Why it matters:** It turns the tailored content into the exact output format the dashboard and later PDF compilation expect.

## `resume-pipeline-orchestrator`

**Purpose:** Coordinate the full run from JD fetch through self-review, push, PATCH, and logging.

**When it runs:** During normal production or operator-triggered resume generation runs.

**Inputs:** `candidate-profile`, pool content, dashboard API configuration, and all downstream skill outputs.

**Output:** Saved `.tex`, dashboard resume push, queue updates, and workflow logs.

**Writes anything?** Yes. It saves `.tex` locally and coordinates API side effects.

**Why it matters:** It is the operational entry point for the whole resume workflow.

Continue to [Run and Verify](/docs/resume-agent/run-and-verify) for the operator view of a real run.
