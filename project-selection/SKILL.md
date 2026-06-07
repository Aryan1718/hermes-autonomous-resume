---
name: project-selection
description: Runs after jd-extraction. Scores every personal project and OSS contribution in the pool, selects the 3 strongest picks for the JD using coverage and expert judgment, and produces a selection artifact.
version: 1.1.0
metadata:
  hermes:
    tags:
      - resume
      - project-selection
      - scoring
      - tailoring
    category: resume-pipeline
---

# Project Selection Guide

> **Purpose:** Choose the **3 strongest projects** from the pool (personal projects + OSS contributions only — NOT work experience) for this JD. Run after jd-extraction, before point-repointing.

**Inputs:** JD extraction artifact + project pool (via `pool/masters.md` unified index).
**Output:** 3 selected projects with scores, coverage lists, and selection reasoning. No files written.

**Read only `pool/masters.md` for scoring.** Do NOT open individual `raw.md` files during selection. `raw.md` is only opened during repointing for the 3 selected projects.

**Score + judge.** The numeric score measures consistency. Expert judgment overrides where experience says the numbers miss something. Neither works alone.

**Work experience is NOT selected here.** It is always on the resume and handled separately by point-repointing.

---

## Step 1: Build the Weighted Requirement Target

From the JD extraction artifact, pull:

1. Every `must_haves` item with its `priority` (A/B/C)
2. Every `surface_requirements` language, framework, database, cloud service, or tool
3. The dominant `behavioral_signals` as verb-noun pairs (e.g., "architect distributed systems", "own services in production")
4. The `scope_signals` (ownership object, production/on-call, decision authority, system complexity)
5. The `cultural_intent_signals` "Why Now?" — the actual problem this role solves

**Weight by priority:** A = 3, B = 2, C = 1.

**Read the verbs, not just the tech.** A JD that says "architect our service platform" wants someone who made platform decisions — not someone who deployed onto an existing cluster. Carry the JD's verbs into the requirement target.

---

## Step 2: Triage — Cut Before You Score

Cut projects that should never be in contention. **Cut when any one of these fires AND the project proves no `priority: A` requirement uniquely:**

- **Domain contradiction** — incompatible domain/compliance gate with nothing transferable
- **Seniority mismatch, downward** — JD wants senior ownership; project shows only ticket-level execution
- **Seniority mismatch, upward** — JD is junior IC; project leads with management framing
- **Stack contradiction** — central stack directly conflicts with a `priority: A` requirement
- **Stale with no unique value** — old AND everything it covers is covered better by something more recent

**OSS special rule:** Never apply the seniority-mismatch downward rule to OSS contributions. Merged = ownership signal. The seniority-mismatch, domain-contradiction, and stack-contradiction rules still apply to OSS.

**Record every cut** with its reason. Silent deletions are decisions no one can audit.

---

## Step 3: Score Each Project — Five-Dimension Model

| # | Dimension | Weight |
|---|---|---|
| 1 | Requirement Coverage | 35 |
| 2 | Measurable Impact | 30 |
| 3 | Seniority Match | 15 |
| 4 | Recency & Stack Currency | 10 |
| 5 | Domain Match | 10 |

### Dimension 1 — Requirement Coverage (0–35)

For each requirement-target item: is there **concrete evidence** in this project? Build the project's **coverage list** with each item tagged by priority.

| Band | Score |
|---|---|
| Multiple A items + several B/C | 30–35 |
| At least one A + some others | 20–29 |
| Only B/C items, or one A weakly | 10–19 |
| Proves little or nothing | 0–9 |

### Dimension 2 — Measurable Impact (0–30)

| Band | Score |
|---|---|
| Multiple quantified outcomes; at least one maps to a JD requirement | 26–30 |
| One strong quantified outcome relevant to the role | 17–25 |
| Qualitative outcome only, or numbers unrelated to JD | 8–16 |
| No stated outcome; only activity described | 0–7 |

**OSS impact adjustment:** A merged PR with no personal metric scores at the **floor of the 8–16 band (score: 8)**. Merged = validated outcome.

### Dimension 3 — Seniority Match (0–15)

| Band | Score |
|---|---|
| Scope/ownership matches the JD's level closely | 12–15 |
| Adjacent level; honestly reframable | 7–11 |
| Clear mismatch with the JD's seniority signals | 0–6 |

### Dimension 4 — Recency & Stack Currency (0–10)

| Band | Score |
|---|---|
| Recent work, current/relevant stack | 8–10 |
| Moderately dated, or stack partly outdated | 4–7 |
| Old and/or on a clearly outdated stack | 0–3 |

### Dimension 5 — Domain Match (0–10)

| Band | Score |
|---|---|
| Same or closely adjacent domain | 8–10 |
| Different domain, transferable system/problem type | 4–7 |
| Unrelated domain, no transferable thread | 0–3 |

**Output of Step 3:** A scored table: five sub-scores, total, and each project's **coverage list**.

---

## Step 4: Judgment Overrides

The score proposes; judgment disposes. At these points, **expert judgment overrides the score** — record every override and its reason.

1. **"Why Now?" boost:** A project that mirrors the JD's reason-for-existing (a real monolith decomposition for a migration role, a 0→1 build for a greenfield role) is more persuasive than its coverage score shows.

2. **Seniority veto:** A high-scoring ticket-execution project for a staff-architect role loses to a lower-scoring project that shows actual architectural ownership.

3. **Redundancy is invisible to the score.** Two projects proving the same stack can both score high. Only the coverage-list comparison in Step 5 catches it.

4. **Stack-currency nuance:** For JDs that say "modernize" or name a current stack, an outdated-stack project is a larger liability than 10 points reflects.

5. **Impressive ≠ relevant.** A dazzling project exerts pull on judgment. Name the pull and resist it: if its coverage is already covered, it's a wasted slot.

6. **OSS tie-breaker:** When an OSS contribution and a personal project cover the same JD requirements equally well, judgment gives the slot to the OSS contribution (third-party validation). This is a tie-breaker only.

7. **<OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>) priority boost:** <OSS_PROJECT_NAME> is a top-tier OSS contribution — first external contributor to a YC-backed AI data agents platform (513 stars), 2 merged PRs, active co-founder collaboration. **STRONGLY PREFERRED for any AI/ML/LLM-related JD.** Domain match should score 10 for AI-related JDs.

---

## Step 5: Build the Set of 3 — Coverage, Not Ranking

**The mistake that ruins most selections: taking the top 3 by score.** The top 3 by score almost always overlap.

**Build procedure:**

1. **Pick #1 — the anchor.** Strongest blend of coverage and impact, ideally matching the "Why Now?".
2. **Pick #2 — the biggest gap-closer.** Mentally discount everything Pick #1 covers. Which remaining project adds the most new high-priority coverage?
3. **Pick #3 — close what's still open.** Repeat: which requirements are still uncovered?
4. **Gap audit.** With 3 picked, list every `priority: A` requirement still uncovered. Test swaps.

**Tie-breakers (in order):** Higher measurable impact → More recent/current stack → Closer domain match → Closer seniority match.

**When 3 projects can't cover everything:** Select the set with **maximum weighted coverage**. Record every uncovered `priority: A` item in `open_questions`. An honest gap beats a forced pick.

---

## Step 6: The Final Read — Does the Set Tell One Story?

| Problem | Fix |
|---|---|
| **Redundancy** — all 3 prove the same stack | Swap one for a runner-up covering open requirements |
| **Seniority drift** — all 3 read wrong for the JD's level | Swap toward projects matching the JD's scope |
| **Domain whiplash** — 3 unrelated domains, no thread | Prefer the set with a connecting thread |
| **Impact-blind** — no metrics for a metrics-heavy JD | Swap toward quantified projects |
| **Silent gap** — uncovered `priority: A` item, unflagged | Record in `open_questions` — never hide it |
| **Stale set** — all 3 on outdated stacks | Prefer recent, current-stack work even at small coverage cost |

A coherent set of 3 that tells one story beats a higher-scoring set that reads as scattered.

---

## Standard Output

**Per selected project:**
- `project_id`, `title`, `rank` (1–3)
- `project_type`: `"personal"` or `"open_source"`
- `total_score` and five `sub_scores`
- `covers`: requirement-target items proven, each with priority
- `key_evidence`: specific content that drove the score
- `selection_reason`: why it earned the slot, explicitly naming unique coverage vs. other picks
- `judgment_overrides`: any overrides with reasons
- `notes`: caveats, framing flags

**Also output:**
- `triaged_out_projects`: cuts with reasons
- `runner_up_projects`: next-best not selected
- `coverage_summary`: what's covered, any gaps (especially uncovered `priority: A` items)

---

## Agent Workflow

1. Read `pool/masters.md` — unified index with ALL entries. Do NOT open individual `raw.md` files.
2. Build the **weighted requirement target** including verbs and "Why Now?".
3. **Triage** the pool; cut doomed projects. Record every cut with reason.
4. **Score** every surviving project on the five-dimension model. Record sub-scores, totals, coverage lists.
5. Apply **judgment overrides**. Record each override and its reason.
6. **Build the set of 3** by anchor-then-gap-closer on marginal coverage. Run the gap audit.
7. Do the **final read**; swap picks if the set is incoherent.
8. Produce the selection artifact.

**Rules:**
- Select, score, and explain only. Never rewrite.
- Score and judge against evidence actually in masters.md. Never infer unstated skills.
- Every judgment override must be recorded with its reason.
- A named gap beats a hidden one. Always record uncovered `priority: A` items in `open_questions`.
- Be deterministic — same JD + same pool = same scores + same 3 picks.
- Do NOT include work experience in selection. Only read from `pool/masters.md`.

---

## Traps to Avoid

1. **Picking the top 3 by score.** They overlap. Build for *marginal* coverage.
2. **Picking the impressive project.** Flashy ≠ relevant. Zero `priority: A` coverage = no slot.
3. **Honoring the candidate's favorite.** Pride is not relevance. The JD chooses.
4. **Matching tech, ignoring verbs.** "Deployed onto Kubernetes" ≠ "architected the platform."
5. **Faking coverage.** Coverage needs evidence, not topic-adjacency.
6. **Inventing metrics.** A missing number is information. Record it; never fill it.
7. **Unexplained judgment overrides.** Every override reason must be in `notes`.
8. **Hiding a gap.** An unflagged uncovered `priority: A` is the worst possible output.
9. **Seniority blindness.** Wrong-scoped projects undermine the resume's framing.
10. **Domain whiplash.** Three unrelated domains. The set should read as one story.
11. **Stale-stack blindness.** Recency is only 10 points but the liability is larger.
12. **Rewriting during selection.** Not this step's job. Select, score, explain, hand off.
13. **Non-determinism.** Same JD + same pool must yield same output on re-run.
14. **Giving OSS automatic priority.** The tie-breaker only applies when coverage is genuinely equal.
15. **Applying seniority-mismatch downward to OSS.** Merged is the ownership signal.
16. **Scoring no-metric OSS at 0–7 impact.** Merged = validated outcome. Floor is 8.
17. **Including work experience in project selection.** Work experience is NOT a project.
18. **Reading from `pool/work-experience/` during selection.** Only read from `pool/masters.md`.
19. **Opening individual `raw.md` files during selection.** Use `pool/masters.md` for all scoring.
20. **Letting masters.md go stale.** When any `raw.md` is edited, the corresponding entry in `pool/masters.md` must be updated to match.

---

## Closing Principle

> **A well-chosen set of 3 is not the candidate's three highest-scoring projects. It is the three projects that, standing together, make an engineering hiring manager believe the candidate has already built the exact system this JD describes.**

Score for consistency. Let judgment override where experience demands it. Build the set on marginal coverage, not the leaderboard. Read the three as one story. Flag every gap honestly.

**References:**
- `references/expert-thinking.md` — How an expert thinks about project selection
- `references/examples/selection-output.md` — Full YAML selection output example with LaTeX display format

