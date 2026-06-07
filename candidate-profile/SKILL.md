---
name: candidate-profile
description: Reusable profile specification for the current candidate. This file is the source of truth for identity, target roles, provable skills, strongest signals, career direction, and hard disqualifiers. Read by jd-prefilter and jd-extraction on every run. Update it whenever the current candidate's facts or preferences change.
version: 2.0.0
metadata:
  hermes:
    tags:
      - resume
      - candidate
      - profile
      - reference
    category: resume-pipeline
---

# Candidate Profile Template

> **Purpose:** This file must describe the current candidate using only facts that are true for that person. It is read by jd-prefilter to disqualify JDs and rank survivors, by jd-extraction for calibration, and by point-repointing for technical skills and honesty checks.

> **Important:** Do not leave another person's details here. When this repository is reused, replace every candidate-specific fact in this file with the current user's own information.

---

## How to Use This File

Treat this as a living profile contract.

- Every statement should be true for the current candidate now.
- Prefer concrete evidence over generic claims.
- If a skill cannot be backed by work history, project history, OSS, coursework, or another real source, do not elevate it here.
- When facts change, update this file before running the pipeline again.

Use placeholders while setting up a new profile, then replace them with real values:

```yaml
candidate_name: <CANDIDATE_NAME>
target_country: <TARGET_COUNTRY>
current_role: <CURRENT_ROLE_TITLE>
current_company: <CURRENT_COMPANY>
years_of_experience: <YEARS_OF_EXPERIENCE>
work_authorization_status: <WORK_AUTH_STATUS>
future_sponsorship_need: <FUTURE_SPONSORSHIP_TYPE or none>
```

---

## Identity Snapshot

Write a short factual summary of the current candidate:

- current education status, if relevant
- current role and most recent prior role
- major technical themes across work and projects
- current job-search scope

**Template:**

```markdown
<CANDIDATE_NAME> is a <education or current-career summary>. They currently work as <CURRENT_ROLE_TITLE> at <CURRENT_COMPANY> and have hands-on experience across <TOP_DOMAIN_1>, <TOP_DOMAIN_2>, and <TOP_DOMAIN_3>.

Their work spans <CORE_STRENGTH_A>, <CORE_STRENGTH_B>, and <CORE_STRENGTH_C>. They have shipped real systems in <ENVIRONMENT_TYPES> and can speak concretely about <PROVABLE_SYSTEM_THEMES>.

They are currently seeking <TARGET_ROLE_SCOPE> roles in <TARGET_COUNTRY>, with openness to <LOCATION_SCOPE> and <COMPANY_STAGE_SCOPE>.
```

**Rules:**
- Keep this grounded in evidence, not aspiration.
- Do not list every technology here.
- Do not borrow wording from a previous candidate.

---

## Target Roles

List the role titles and role types that genuinely fit the current candidate.

**Role titles that match:**
- <ROLE_TITLE_OPTION_1>
- <ROLE_TITLE_OPTION_2>
- <ROLE_TITLE_OPTION_3>

**Role types that match:**
- <ROLE_TYPE_1>
- <ROLE_TYPE_2>
- <ROLE_TYPE_3>

**Role types that do NOT match (pre-filter disqualifies):**
- <OUT_OF_SCOPE_ROLE_TYPE_1>
- <OUT_OF_SCOPE_ROLE_TYPE_2>

**Rules:**
- Include adjacent titles only if the candidate has evidence for them.
- Keep this focused on what the resume can actually support.

---

## Seniority

Document the candidate's true target seniority and the matching rule.

**Template:**

```markdown
**Targeting:** <ENTRY / MID / SENIOR / mixed range>.

**Pre-filter rule:** Pass if the JD matches the candidate's target seniority or is unspecified. Disqualify only when the JD explicitly requires materially more experience than the candidate can credibly support.

**Note:** The candidate currently has <YEARS_OF_EXPERIENCE> of relevant experience across <EXPERIENCE_TYPES>. Do not over-disqualify reasonable stretch roles, but do not pretend the candidate is more senior than the evidence supports.
```

**Rules:**
- This must reflect the current candidate, not a generic new-grad assumption.
- If the candidate is senior, remove junior/new-grad framing.

---

## Location

Define the real geographic scope of the search.

**Template:**

```markdown
**In scope:** <TARGET_COUNTRY / REGIONS / remote-only / city list>.

**Pre-filter rule:** Pass if the role location matches the candidate's actual search scope or is unspecified. Disqualify if the role is explicitly outside scope with no acceptable remote option.

**Regional preferences:** <optional preferences or "None">.
```

---

## Work Authorization

State only the current candidate's real authorization constraints.

**Template:**

```markdown
**Current status:** <WORK_AUTH_STATUS>.

**Future need:** <FUTURE_SPONSORSHIP_TYPE / none / unknown>.

**Pre-filter rule:**
- Pass if the JD is compatible with the candidate's current and future authorization.
- Disqualify if the JD explicitly rules the candidate out on authorization grounds.
- If the JD is ambiguous, prefer pass unless the restriction is explicit.
```

**Rules:**
- Do not hard-code a specific visa path, citizenship restriction, or any other authorization path unless true for the current candidate.

---

## Hard Disqualifiers

List the rules that immediately eliminate a JD for the current candidate.

**Required categories to consider:**
1. Geography
2. Work authorization
3. Seniority mismatch
4. Out-of-scope role family
5. Candidate-specific hard constraints

**Template:**

```markdown
1. Role is outside <LOCATION_SCOPE> with no acceptable remote option.
2. JD explicitly blocks the candidate's work authorization path.
3. JD requires materially more experience than the candidate can credibly support.
4. Role is outside the candidate's technical scope.
5. <Any additional hard constraint that is actually true for this candidate>.
```

**Rules:**
- Every disqualifier must be candidate-specific and defensible.
- Do not inherit hard disqualifiers from another profile.

---

## Provable Must-Haves

This is the skill inventory the pipeline is allowed to trust.

### Always Provable

List skills and experiences the current candidate can consistently prove from real evidence.

| Skill / Experience | Best evidence |
|---|---|
| <SKILL_1> | <WORK / PROJECT / OSS evidence> |
| <SKILL_2> | <WORK / PROJECT / OSS evidence> |
| <SKILL_3> | <WORK / PROJECT / OSS evidence> |

### Provable with Framing

List skills that are real but should not be overemphasized unless the evidence is thinner or more indirect.

| Skill / Experience | Note |
|---|---|
| <SKILL_A> | <why it is real but secondary> |
| <SKILL_B> | <why it is real but secondary> |

**Rules:**
- Evidence should point to raw project/work facts, not vague self-descriptions.
- If a skill exists only in a keyword list and nowhere else, it does not belong in Always Provable.
- point-repointing may only promote skills that are truly supported here.

---

## Strongest Signals

Document the candidate's differentiators: the signals where evidence is deepest, clearest, and most defensible.

Use this format:

```markdown
**Signal 1 — <SIGNAL_NAME>.**
<Why this is one of the candidate's strongest signals. Mention the proof sources and what makes the evidence unusually credible or differentiated.>
```

**Rules:**
- Prioritize evidence depth, not trendiness.
- A strong signal should help rank JDs, not just decorate the profile.
- Remove stale signals when the candidate's portfolio changes.

---

## Career Direction

Explain what kinds of roles make sense for this candidate and why.

Use this format:

```markdown
**Fit 1 — <FIT_TYPE>.**
<Why this type of role fits the candidate's real evidence and trajectory.>
```

**Scoring note:** When ranking JDs, reward real overlap with these fit types. A JD that matches multiple fits should score higher than one that barely clears the binary gates.

**Rules:**
- This section should reflect genuine direction, not every possible role the market contains.
- Avoid first-person narrative; write it as an evaluator-facing profile.

---

## Preferred Signals

These are not gates. They are score-raisers.

Group them by area relevant to the candidate, for example:

- domain signals
- backend/system signals
- cloud/devops signals
- AI/ML signals
- frontend/full-stack signals
- culture/stage signals

**Template:**

```markdown
**<SIGNAL_GROUP_NAME>:**
- <signal phrase or concept>
- <signal phrase or concept>
```

**Rules:**
- Only include signals the candidate can respond to meaningfully if selected.
- Do not add a signal group just because it was useful for a previous candidate.

---

## Industry Restrictions

Document any true industry constraints.

**Template:**

```markdown
**None.** The candidate applies across all industries.
```

or

```markdown
**Restricted.** The candidate is not targeting <INDUSTRY_1>, <INDUSTRY_2>, because <REAL_REASON>.
```

---

## Compensation

Only include this if compensation expectations materially affect filtering or job-search strategy.

**Template:**

```markdown
**Expectation:** <COMPENSATION_EXPECTATION or "not used as a filter">.
```

---

## Maintenance Rules

- Re-read pool `raw.md` files before major profile rewrites.
- Update this file whenever the candidate adds a new role, ships a major project, changes work authorization, changes target geography, or narrows/widens role scope.
- If this file changes materially, review generated resumes for stale facts.
- Keep the profile consistent with pool content; the pool is the evidence base.

