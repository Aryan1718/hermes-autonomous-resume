---
name: jd-prefilter
description: Runs when a batch of JDs arrives. Filters out irrelevant JDs using hard disqualifiers, scores survivors, and selects the top 3-5 for the full pipeline. Use this before running any other resume pipeline step.
version: 1.1.0
metadata:
  hermes:
    tags:
      - resume
      - job-search
      - filtering
      - scoring
    category: resume-pipeline
---

# JD Pre-Filter and Scoring Guide

> **Purpose:** Fast gate on raw JD text + Candidate Profile. Disqualifies irrelevant JDs, scores survivors, ranks, hands top 3–5 to the full pipeline. Writes nothing to any file.

**Speed is the point.** Process all JDs in one pass. Read each JD once, run four phases, move on. Deep analysis happens in the full pipeline — not here.

**Load candidate-profile once per batch.** Do not re-read it per JD.

**Deterministic:** Same JD + same profile = same result. No gut feel.

---

## Phase 1: Hard Disqualification

Check each JD against every disqualifier. **Any single disqualifier fires → immediately dropped. No scoring. Log reason.**

1. Role is outside the US with no remote/US option
2. Explicitly no sponsorship now or ever (citizen/PR only)
3. Role requires 5+ years of full-time industry experience, explicitly stated
4. Role is non-engineering (pure management, sales, or analyst with no engineering scope)
5. Role is pure frontend only — no backend, API, or system design scope
6. Role is pure ML research — no production engineering component
7. Role requires an active security clearance

**How to check each one:**
- **Location:** Non-US with no remote clause = disqualify. "Remote" or "Remote (US)" or no location = pass.
- **Sponsorship:** Exact phrases like "no sponsorship", "must be authorized permanently", "no OPT/CPT" = disqualify. Ambiguous = pass.
- **Experience:** "5+ years required" = disqualify. "3–5 years" or "preferred 5 years" = pass.
- **Role type:** Check title + first paragraph. "Data Analyst", "Product Manager" with no engineering scope = disqualify.
- **Pure frontend:** Entire stack is UI/CSS/design with no backend/API/database = disqualify.
- **Pure ML research:** "PhD required", "research scientist", "publish papers", "no production scope" = disqualify.
- **Security clearance:** "Secret", "Top Secret", "TS/SCI" = disqualify.

**Output:** `PASS` or `DISQUALIFIED — [reason]`. Disqualified JDs stop here.

---

## Phase 2: Binary Pass Check

Three binary questions. **All three must be YES.** A single NO → disqualify.

### Q1 — Role type match?
Check against Target Roles in candidate-profile. Matches: Software Engineer/Developer, Backend Engineer, Full-Stack Engineer, AI/ML Engineer, Systems Engineer (software), DevOps/Cloud Engineer, Platform Engineer (with code), New Grad/Associate/Junior Engineer.

Not matching: pure DevOps, pure QA, pure data science, pure research, pure frontend, non-technical.

**Edge case:** Unusual title but description clearly describes building software systems → YES.

### Q2 — Seniority match?
Check against Seniority in candidate-profile.

- Entry-level, new grad, junior, associate, 0–2 years → YES
- Mid-level, 2–4 years → YES
- Unspecified → YES
- Senior, 5+ years explicitly required → NO
- Staff, principal, lead, director, manager → NO

### Q3 — At least 2 provable must-haves?
Check JD required skills against "Always provable" tier in candidate-profile. Two or more matches → YES. Zero or one → NO.

**"Provable with framing" items do NOT count toward this threshold.** They only count in Phase 3 scoring.

---

## Phase 3: Scoring (0–100)

Four dimensions:

| # | Dimension | Points |
|---|---|---|
| 1 | Provable Coverage | 40 |
| 2 | Career Direction Fit | 30 |
| 3 | Strongest Signal Match | 20 |
| 4 | Preferred Signal Count | 10 |

### Dimension 1 — Provable Coverage (0–40)
Count JD must-haves matching "Always provable" tier in candidate-profile:

| Matched | Score |
|---|---|
| 6+ | 40 |
| 4–5 | 30 |
| 3 | 20 |
| 2 | 10 |

"Provable with framing" items add 5 bonus points each (max 10 bonus). Never exceeds 40 total.

### Dimension 2 — Career Direction Fit (0–30)
Check JD against Career Direction fits in candidate-profile:

| Fit | Score |
|---|---|
| Fit 1 — Building AI/ML systems end-to-end | 30 |
| Fit 2 — Backend systems at scale | 22 |
| Fit 3 — Taking a product from 0 to 1 | 15 |
| Matches none | 5 |

Use the highest-scoring fit when multiple match.

### Dimension 3 — Strongest Signal Match (0–20)
Check JD against Strongest Signals in candidate-profile. Score by count matched:

| Signals matched | Score |
|---|---|
| 3+ | 20 |
| 2 | 14 |
| 1 | 7 |
| 0 | 0 |

A signal matches when the JD directly names the concept — not just shares a domain.

### Dimension 4 — Preferred Signal Count (0–10)
Count how many Preferred Signals from candidate-profile appear in the JD. Each = 1 point, max 10.

---

## Phase 4: Rank and Select

Sort by total score, highest first. Select top 3–5:

| Top score | How many to take |
|---|---|
| ≥ 75 | Top 5 |
| 60–74 | Top 4 |
| < 60 | Top 3 |
| Fewer than 3 above 40 | Take only those above 40 |

**Tie-breaking:** Higher Career Direction Fit → Higher Strongest Signal Match → Higher Provable Coverage → More Preferred Signals.

**Never run the full pipeline on a disqualified or failed-binary JD.**

---

## Agent Workflow

1. Load `candidate-profile` skill once. Hold for entire batch.
2. For each JD:
   - Phase 1: Hard disqualification. Stop if disqualified — log reason.
   - Phase 2: Binary pass check. Stop if failed — log which question.
   - Phase 3: Score on four dimensions. Record all sub-scores with evidence.
3. Phase 4: Rank all survivors, select top 3–5.
4. Disqualification reasons must be specific (trace to exact JD language).
5. Every score traces to a specific section of candidate-profile — no guessing.

---

## Standard Output

For each JD: score (0–100), four sub-scores with evidence, decision (RUN FULL PIPELINE or SKIPPED + reason), rank.

Use the YAML output format from the pipeline.

---

## Traps to Avoid

1. **Scoring a disqualified JD.** Filters first, scoring second. Never reverse.
2. **Passing ambiguous sponsorship.** Ambiguous = pass. Only explicit denial disqualifies.
3. **Counting "provable with framing" toward Phase 2 threshold.** Only "always provable" counts.
4. **Treating "preferred 5 years" as a hard seniority disqualifier.** Only "required" or "minimum" fires.
5. **Scoring on impression instead of the profile.** Every score traces to a specific candidate-profile section.
6. **Running the full pipeline on more than 5 JDs per batch.** Raise quality threshold instead.
7. **Updating candidate-profile mid-run.** Observations go in `profile_notes`. Candidate updates manually.
8. **Skipping the evidence field in the output.** Scores without evidence cannot be audited.
9. **Processing phases out of order.** Phase 1 → Phase 2 → Phase 3 → Phase 4. Always.
10. **Selecting fewer than 3 just because scores are low.** If 3+ scored above 40, run the pipeline on them.

---

## Closing Principle

> **Disqualify fast. Score honestly. Rank clearly. Hand off and move on.**

**References:**
- `references/scoring-examples.md` — Full YAML output example with scored JDs
- `references/agent-behavior-rules.md` — Detailed behavioral rules for each phase
