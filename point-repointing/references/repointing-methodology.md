# Repointing Methodology — Detailed

## Step 1: History Check via idx.md

For each section, `idx.md` was already loaded in the read phase. Scan its version entries. For each, look at `requirements_targeted`, `jd_type`, and `role_phase`. Compare against the current JD.

**Use history to pick a style reference, NOT a content source:**
- **Close match** (similar `jd_type`, same role_phase): optionally open that version file to see how bullets were structured. Then re-derive content from raw.md.
- **No match / `current_version: 0`**: proceed directly from raw.md. No style reference available.

**Never copy content from a prior version.** The history check is for style/formatting reference only — how long were the bullets, what verb style was used, how was formatting applied. All content comes from raw.md.

## Step 2: Detailed Re-Pointing Procedure

### 2a. Order bullets to aim list
The bullet covering the `leads: true` requirement moves to the top. Remaining bullets follow in descending priority.

### 2b. Mirror JD verb — honestly
Replace the bullet's verb with the `jd_verb` from the aim list **only when the work genuinely supports it**.

Calibration:
- JD says "architect", "own", "drive", "define" → senior verbs, *if the work was senior*
- JD says "build", "ship", "implement", "deliver" → execution verbs
- If the verb cannot be honestly mirrored, keep an accurate verb and record the gap in honesty flags

### 2c. Foreground JD-relevant metric
If the point has multiple real numbers, surface the one the JD cares about (per its quantification triggers) early in the bullet. Only real, source-supported numbers. Never invent one.

### 2d. JD-driven method override
Point Creation chooses STAR/XYZ/CAR by *story shape*. Re-pointing adds one override: **the JD gets a vote.**
- JD thick with **quantification triggers** + bullet has a strong real metric → bias toward **XYZ**
- JD's "Why Now?" is a **problem to solve** + bullet resolves that kind of challenge → bias toward **CAR**
- JD needs the **situation understood first** → **STAR**
- If story-shape and JD vote disagree, the JD vote wins for the *lead* bullet; story-shape can still govern supporting bullets.

### 2e. De-emphasize Anti-Resume flags
For any `downplay` item in the aim list: do not delete the truth, but move it down, compress it, or reframe it.

## Step 2.5: Technical Skills Update — Full Procedure

1. Read the candidate-profile's Provable Must-Haves table. These are the **only** skills that may appear.
2. For each JD `must_have` and `surface_requirement`, check whether it matches a provable skill → promote to front of its category.
3. Reorder items within ALL 5 categories so JD-relevant provable skills appear first.
4. **Concepts row: hard limit of 6 items max.** Pick the 6 most relevant to the JD.
5. Output complete reordered Technical Skills section.

```yaml
technical_skills_update:
  languages: "Python, TypeScript, JavaScript, Java, C++"
  frameworks: "React, Next.js, FastAPI, Flask, Express.js, Node.js, LangGraph, CrewAI"
  databases: "PostgreSQL, Supabase, Redis, MongoDB, DynamoDB"
  cloud_and_tools: "AWS, Docker, Docker Compose, GitHub Actions, CI/CD, Ollama, VLLM"
  concepts: "Distributed Systems, API Design, Multi-Agent Orchestration, RAG, LLM Inference, Observability"
```

**Rules:**
- Never add a skill not in the candidate-profile's Provable Must-Haves table. Reorder only.
- All 5 categories must be present even if the JD only touches one.
- Concepts row: hard limit of 6 items max.
- If the JD mentions a skill the candidate does not have, simply skip it — do not add it.
