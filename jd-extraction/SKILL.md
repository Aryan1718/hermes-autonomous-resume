---
name: jd-extraction
description: Runs after the jd-prefilter skill selects a JD. Deeply extracts must-haves, behavioral signals, scope signals, and cultural intent from a job description into a structured artifact used by downstream skills.
version: 1.1.0
metadata:
  hermes:
    tags:
      - resume
      - job-search
      - extraction
      - jd-analysis
    category: resume-pipeline
---

# JD Extraction Guide

> **Purpose:** Decode a JD into a structured artifact (must-haves, behavioral signals, scope signals, cultural intent). This artifact is consumed by project-selection and point-repointing. Run after jd-prefilter, before project-selection.

**Two inputs:** Raw JD text + candidate-profile skill (for calibration only — the extraction is about what the JD says, not whether the candidate matches).

**Output:** One normalized extraction artifact. No files written.

**Decode, don't copy.** A JD is a human document written under pressure. Your job is to extract what they actually want, categorize it, and flag what's explicit vs. inferred.

---

## Layer 0: Hard Screens

Extract gating filters before deeper analysis. These are binary constraints that can remove a candidate regardless of fit.

**Hard-screen items:**
- Work authorization / visa requirements
- Location, timezone, remote/hybrid/on-site expectations
- Travel requirements
- Security clearance or background constraints
- Degree requirements that appear strict
- Years of experience floors
- Required management scope
- Required customer-facing or stakeholder-facing scope
- Industry or regulatory requirements (healthcare, fintech, gov)

**Labels:** Classify each as `explicit constraint`, `likely constraint`, or `context signal`. If ambiguous, mark as ambiguous — don't upgrade to hard requirement.

---

## Extraction Procedure

Read the JD **three times**, each pass looking for different things:

### Pass 1 — Surface (Hard Requirements)
**Look for:** Tools, software, platforms, certifications, years of experience, degrees, methodologies.
**Capture:** Bulleted list. These are non-negotiable for ATS systems.

### Pass 2 — Behavioral (How They Work)
**Look for:** Action verbs ("drive," "own," "execute," "collaborate"), working style cues ("fast-paced," "ambiguous," "structured"), decision-making language ("data-driven," "consensus-building").
**Capture:** These verbs reveal how the company expects work to get done. Carry the JD's exact verbs into the artifact — project-selection and repointing will mirror them.

### Pass 3 — Cultural/Intent (The Real Why)
**Look for:** What problem is this role solving? What is broken, missing, or growing? What does success look like in 6–12 months?
**Capture:** The "Why Now?" diagnosis — the actual reason this role exists.

---

## Must-Haves vs. Nice-to-Haves vs. Filler

**Bucket 1: Non-Negotiables (Must-Haves)**
- Mentioned 2+ times, or in the job title, or under "minimum qualifications" / "required"
- MUST appear on the resume, ideally in the top third

**Bucket 2: Preferred (Nice-to-Haves)**
- Mentioned once, under "preferred" / "bonus" / "nice to have"
- Include if genuinely matched. Skip if not.

**Bucket 3: Filler**
- Generic corporate language: "team player," "passionate," "fast-paced environment"
- Ignore for keyword extraction. Mirror tone only.

---

## Verb and Noun Mirroring

Extract every verb-noun pair from the JD's responsibilities section. These are the exact phrases project-selection and repointing will use.

**Verb Translation Reference:**
| Your Word | JD's Word (Match It) |
|---|---|
| Helped | Partnered with / Collaborated with |
| Worked on | Owned / Drove / Led |
| Made | Built / Architected / Designed |
| Improved | Optimized / Scaled / Streamlined |
| Talked to customers | Conducted user research / Gathered customer insights |

---

## Seniority Calibration

Extract the JD's expected level from verbs and scope cues:

| JD Language | Expected Level | Resume Tone |
|---|---|---|
| "Own the roadmap," "Define strategy" | Senior / Lead | "Owned," "Defined," "Architected" |
| "Contribute to roadmap," "Support strategy" | Mid-level | "Contributed," "Supported," "Drove parts of" |
| "Execute on plans," "Deliver tasks" | Junior | "Executed," "Delivered," "Implemented" |
| "Mentor junior team members" | Senior IC | Show leadership without "managed X reports" |
| "Manage a team of N" | Manager | Lead with people-management metrics |

Calibrate honestly. Using senior verbs for a mid-level role reads as inflated.

---

## Quantification Trigger Scan

Scan the JD for outcome-oriented words. These signal the company values measurable results:

**Trigger words:** "scale," "grow," "expand," "optimize," "improve," "reduce," "drive revenue," "cut costs," "increase efficiency," "accelerate"

If any triggers appear, the JD cares about numbers. Repointing should foreground metrics.

---

## Anti-Resume Extraction

Extract signals about what the candidate should **remove or downplay**:

| JD Signal | What to Remove or Downplay |
|---|---|
| Emphasis on startup speed | Long tenures at slow enterprises (compress) |
| Deep specialization required | "Jack of all trades" framing; remove unrelated roles |
| No mention of management | People-management bullets (lead with IC work) |
| Heavy technical depth | Soft-skill-heavy bullets at the top |
| Customer-facing focus | Internal-only project descriptions |
| IC role | "Managed a team of N" as the lead bullet |

---

## Standard Extraction Output

### Required sections

- `hard_screens`
- `surface_requirements`
- `behavioral_signals`
- `scope_signals`
- `cultural_intent_signals`
- `must_haves`
- `preferred`
- `filler_or_tone`
- `open_questions`

### Per-item fields

| Field | Description |
|---|---|
| `signal` | The extracted signal text |
| `category` | Which section it belongs to |
| `priority` | `A` (critical/gating), `B` (important), `C` (context/tone) |
| `exact_jd_phrase` | The exact wording from the JD |
| `normalized_meaning` | What it means in plain terms |
| `explicit_or_inferred` | Directly stated or inferred |
| `confidence` | `explicit`, `high-confidence inference`, `medium-confidence inference`, `low-confidence inference` |
| `notes` | Any additional context |

### Priority labels
- `A` = critical or gating
- `B` = important but not gating
- `C` = useful context or tone

---

## Agent Behavior Rules

- Prefer exact JD language before summarizing in your own words.
- Separate facts from interpretations.
- Do not infer candidate fit during extraction. Do not start rewriting bullets.
- If the JD is vague, preserve uncertainty instead of inventing specificity.
- Label every non-obvious conclusion as `explicit`, `supported inference`, or `low-confidence inference`.

---

## Common Mistakes to Avoid

1. **Keyword stuffing.** Putting every JD term in a skills section without integrating into bullets. ATS catches it; humans hate it.
2. **Faking experience.** Adding a tool you don't know because it's in the JD.
3. **Copying the JD verbatim.** Mirroring is not plagiarism. Rephrase using their verbs but your context.
4. **Ignoring tone.** A casual startup JD deserves a slightly less stiff resume. A formal enterprise JD deserves more polish.
5. **Over-tailoring for ATS only.** Real humans read these resumes too. Optimize for both.
6. **Forgetting the Anti-Resume Check.** Most people only add. Remove ruthlessly.
7. **Calibrating up too far.** Using senior verbs for a mid-level role reads as inflated.
8. **Treating the JD as a wishlist.** It's a diagnosis of a problem. Solve the problem in their framing.

---

## Closing Principle

> **A tailored resume is not a resume with the right keywords. It is a resume that tells the hiring manager: "I have already solved your problem before."**

**References:**
- `references/three-layer-read.md` — Detailed three-layer read methodology with examples
- `references/why-now-diagnosis.md` — "Why Now?" trigger table and diagnosis examples
- `references/must-haves-vs-filler.md` — Bucketing methodology with examples
- `references/hidden-stack-inference.md` — Hidden stack inference table
- `references/workflow-checklist.md` — Phase-by-phase workflow checklist
