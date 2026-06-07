# Scoring Examples - JD Pre-Filter Output

Illustrative YAML output example from a batch run. Adjust the evidence and reasons to match the current candidate's actual `candidate-profile`.

```yaml
batch_id: "2026-06-06-1600"
total_fetched: 8
disqualified_phase1: 3
failed_phase2: 1
scored: 4
selected_for_pipeline: 3

disqualified:
  - jd_id: "jd_001"
    company: "Regulated Systems Co"
    title: "<OUT_OF_SCOPE_OR_RESTRICTED_ROLE_TITLE>"
    phase: 1
    reason: "JD conflicts with candidate-profile hard disqualifier: <EXACT_PROFILE_RULE>."

  - jd_id: "jd_004"
    company: "Regional Ops Ltd"
    title: "<LOCATION_CONSTRAINED_ROLE_TITLE>"
    phase: 1
    reason: "Role location is outside the candidate's allowed search scope and offers no acceptable remote option."

  - jd_id: "jd_007"
    company: "Analytics Org"
    title: "<OUT_OF_SCOPE_ROLE_TITLE>"
    phase: 2
    reason: "Question 1 failed - role scope does not match candidate-profile target roles. Question 3 also would fail: only 1 always-provable must-have matched."

scored_jds:
  - jd_id: "jd_002"
    company: "Product Systems Inc"
    title: "<HIGH_FIT_ROLE_TITLE>"
    scores:
      provable_coverage: 38
      career_direction_fit: 30
      strongest_signal_match: 20
      preferred_signals: 9
      total: 97
    evidence:
      coverage: "<SKILL_1>, <SKILL_2>, <SKILL_3>, <SKILL_4>, <SKILL_5>, <SKILL_6> - 6 always-provable matches."
      direction: "Fit 1 - JD strongly overlaps with the candidate's top-ranked career direction."
      signals: "Matches 3 strongest signals defined in candidate-profile."
      preferred: "Multiple preferred signals from candidate-profile appear directly in the JD."
    decision: RUN FULL PIPELINE
    rank: 1

  - jd_id: "jd_009"
    company: "Platform Builder LLC"
    title: "<SECONDARY_FIT_ROLE_TITLE>"
    scores:
      provable_coverage: 30
      career_direction_fit: 22
      strongest_signal_match: 14
      preferred_signals: 6
      total: 72
    evidence:
      coverage: "<SKILL_1>, <SKILL_2>, <SKILL_3>, <SKILL_4>, <SKILL_5> - 5 always-provable matches."
      direction: "Fit 2 - JD overlaps strongly with the candidate's second-ranked career direction."
      signals: "Matches 2 strongest signals from candidate-profile."
      preferred: "Several preferred signals from candidate-profile appear directly in the JD."
    decision: RUN FULL PIPELINE
    rank: 2

selected_pipeline_order:
  - rank: 1
    jd_id: "jd_002"
    score: 97
    company: "Product Systems Inc"
    title: "<HIGH_FIT_ROLE_TITLE>"
  - rank: 2
    jd_id: "jd_009"
    score: 72
    company: "Platform Builder LLC"
    title: "<SECONDARY_FIT_ROLE_TITLE>"
  - rank: 3
    jd_id: "jd_015"
    score: 68
    company: "Application Team Co"
    title: "<THIRD_FIT_ROLE_TITLE>"

profile_notes:
  - "Example: candidate-profile may need review if multiple JDs repeatedly fail on the same assumed hard constraint."
```
