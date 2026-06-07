---
name: jd-prefilter
description: Runs when a batch of JDs arrives. Filters out irrelevant JDs using the current candidate-profile, scores survivors, and selects the top 3-5 for the full pipeline. Use this before running any other resume pipeline step.
version: 2.0.0
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

> **Purpose:** Fast gate on raw JD text + Candidate Profile. Disqualifies irrelevant JDs, scores survivors, ranks them, and hands the top 3-5 to the full pipeline. Writes nothing to any file.

**Speed is the point.** Process all JDs in one pass. Read each JD once, run four phases, move on. Deep analysis happens in the full pipeline, not here.

**Load candidate-profile once per batch.** Do not re-read it per JD.

**Deterministic:** Same JD + same profile = same result. No gut feel.

**Profile-driven:** This skill must not assume a default country, visa path, seniority, role family, or career direction. All candidate-specific judgments come from `candidate-profile`.

---

## Setup Requirement

Before using this skill, confirm that `candidate-profile` has been filled with the current candidate's real information.

- If `candidate-profile` still contains placeholders or template text, stop and ask the user to complete setup first.
- Recommended setup path: run `profile-bootstrap` to collect the candidate inputs and write `candidate-profile` consistently.
- Never infer missing candidate facts from a JD.

---

## Phase 1: Hard Disqualification

Check each JD against every disqualifier in `candidate-profile`. **Any single disqualifier fires -> immediately dropped. No scoring. Log reason.**

At minimum, evaluate the categories already defined in `candidate-profile`:

1. Geography or location scope
2. Work authorization compatibility
3. Seniority mismatch
4. Out-of-scope role family
5. Any additional candidate-specific hard constraint

**How to evaluate them:**
- **Location:** Compare the JD's stated location against the candidate's `Location` section. If the role is explicitly outside scope and no acceptable remote option exists, disqualify. If the JD is silent or ambiguous, pass unless the profile says otherwise.
- **Work authorization:** Compare the JD's explicit authorization language against the candidate's `Work Authorization` section. Ambiguous = pass. Explicit incompatibility = disqualify.
- **Experience and seniority:** Compare the JD's explicit minimums against the candidate's `Seniority` section. Preferred experience does not disqualify. Required experience that materially exceeds the candidate's supportable range does.
- **Role type:** Check title plus responsibilities against `Target Roles` and `Role types that do NOT match`. Unusual titles can still pass if the actual work fits the candidate's target scope.
- **Candidate-specific constraints:** Apply any additional hard constraints exactly as written in `candidate-profile`.

**Output:** `PASS` or `DISQUALIFIED - [reason]`. Disqualified JDs stop here.

---

## Phase 2: Binary Pass Check

Three binary questions. **All three must be YES.** A single NO -> disqualify.

### Q1 - Role type match?
Check against `Target Roles` in `candidate-profile`.

- YES if the JD's actual responsibilities match one of the candidate's in-scope role titles or role types.
- NO if the JD clearly falls into the candidate's explicit out-of-scope role types.

**Edge case:** Unusual title but description clearly describes the kind of work the candidate is targeting -> YES.

### Q2 - Seniority match?
Check against `Seniority` in `candidate-profile`.

- YES if the JD matches the candidate's stated target range or leaves seniority unspecified.
- YES if the role is a reasonable stretch that the profile explicitly allows.
- NO if the JD explicitly requires materially more experience or a materially higher level than the profile supports.

### Q3 - At least 2 provable must-haves?
Check JD required skills against the `Always Provable` tier in `candidate-profile`. Two or more matches -> YES. Zero or one -> NO.

`Provable with Framing` items do not count toward this threshold. They only count in Phase 3 scoring.

---

## Phase 3: Scoring (0-100)

Four dimensions:

| # | Dimension | Points |
|---|---|---|
| 1 | Provable Coverage | 40 |
| 2 | Career Direction Fit | 30 |
| 3 | Strongest Signal Match | 20 |
| 4 | Preferred Signal Count | 10 |

### Dimension 1 - Provable Coverage (0-40)
Count JD must-haves matching the `Always Provable` tier in `candidate-profile`:

| Matched | Score |
|---|---|
| 6+ | 40 |
| 4-5 | 30 |
| 3 | 20 |
| 2 | 10 |

`Provable with Framing` items add 5 bonus points each, up to 10 bonus points total. Never exceed 40 total.

### Dimension 2 - Career Direction Fit (0-30)
Check the JD against the ordered `Career Direction` fits in `candidate-profile`.

| Fit | Score |
|---|---|
| Strong match to Fit 1 | 30 |
| Strong match to Fit 2 | 22 |
| Strong match to Fit 3 | 15 |
| Strong match to any later fit | 10 |
| Matches none | 5 |

Use the highest-scoring fit when multiple match. A JD that materially overlaps multiple fits may justify the top of its applicable bucket, but never exceed 30.

### Dimension 3 - Strongest Signal Match (0-20)
Check the JD against `Strongest Signals` in `candidate-profile`. Score by count matched:

| Signals matched | Score |
|---|---|
| 3+ | 20 |
| 2 | 14 |
| 1 | 7 |
| 0 | 0 |

A signal matches when the JD directly names the concept or clearly requires the same kind of work, not when it merely shares a loose domain label.

### Dimension 4 - Preferred Signal Count (0-10)
Count how many `Preferred Signals` from `candidate-profile` appear in the JD. Each = 1 point, max 10.

---

## Phase 4: Rank and Select

Sort by total score, highest first. Select top 3-5:

| Top score | How many to take |
|---|---|
| >= 75 | Top 5 |
| 60-74 | Top 4 |
| < 60 | Top 3 |
| Fewer than 3 above 40 | Take only those above 40 |

**Tie-breaking:** Higher Career Direction Fit -> Higher Strongest Signal Match -> Higher Provable Coverage -> More Preferred Signals.

**Never run the full pipeline on a disqualified or failed-binary JD.**

---

## Agent Workflow

1. Load `candidate-profile` once. Hold it for the entire batch.
2. Confirm the profile is filled for the current candidate rather than left as a template.
3. For each JD:
   - Phase 1: Hard disqualification. Stop if disqualified and log the reason.
   - Phase 2: Binary pass check. Stop if failed and log which question failed.
   - Phase 3: Score on four dimensions. Record all sub-scores with evidence.
4. Phase 4: Rank all survivors and select the top 3-5.
5. Disqualification reasons must be specific and trace to exact JD language.
6. Every score must trace to a specific section of `candidate-profile`.

---

## Standard Output

For each JD: score (0-100), four sub-scores with evidence, decision (`RUN FULL PIPELINE` or `SKIPPED` + reason), and rank.

Use the YAML output format from the pipeline.

---

## Traps to Avoid

1. **Scoring a disqualified JD.** Filters first, scoring second. Never reverse.
2. **Passing explicit authorization conflicts.** Ambiguous = pass. Explicit incompatibility with the candidate's profile = disqualify.
3. **Counting `Provable with Framing` toward the Phase 2 threshold.** Only `Always Provable` counts.
4. **Treating preferred experience as a hard seniority disqualifier.** Only explicit required minimums that exceed the profile-supported range should fire.
5. **Scoring on impression instead of the profile.** Every score traces to a specific `candidate-profile` section.
6. **Running the full pipeline on more than 5 JDs per batch.** Raise the quality threshold instead.
7. **Updating `candidate-profile` mid-run.** Observations go in `profile_notes`. Candidate updates happen explicitly.
8. **Skipping the evidence field in the output.** Scores without evidence cannot be audited.
9. **Processing phases out of order.** Phase 1 -> Phase 2 -> Phase 3 -> Phase 4. Always.
10. **Selecting fewer than 3 just because scores are low.** If 3+ scored above 40, run the pipeline on them.
11. **Trying to infer the candidate from the JD.** All candidate assumptions come from `candidate-profile`, not from guesswork.

---

## Closing Principle

> **Disqualify fast. Score honestly. Rank clearly. Hand off and move on.**

**References:**
- `references/scoring-examples.md` - Full YAML output example with scored JDs
- `references/agent-behavior-rules.md` - Detailed behavioral rules for each phase
