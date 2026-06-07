# Scoring Examples — JD Pre-Filter Output

Full YAML output example from a real batch run:

```yaml
batch_id: "2026-06-06-1600"
total_fetched: 8
disqualified_phase1: 3
failed_phase2: 1
scored: 4
selected_for_pipeline: 3

disqualified:
  - jd_id: "jd_001"
    company: "Acme Defense"
    title: "Software Engineer"
    phase: 1
    reason: "Requires active Secret clearance — hard disqualifier 7."

  - jd_id: "jd_004"
    company: "GlobalTech UK"
    title: "Backend Developer"
    phase: 1
    reason: "Role is London, UK only — no US remote option. Hard disqualifier 1."

  - jd_id: "jd_007"
    company: "DataCo"
    title: "Senior Data Scientist"
    phase: 2
    reason: "Question 1 failed — pure data science, no engineering scope. Question 3 also would fail: only 1 provable must-have (Python)."

scored_jds:
  - jd_id: "jd_002"
    company: "Synapse AI"
    title: "AI Engineer — New Grad"
    scores:
      provable_coverage: 38
      career_direction_fit: 30
      strongest_signal_match: 20
      preferred_signals: 9
      total: 97
    evidence:
      coverage: "Python, LangGraph, FastAPI, PostgreSQL, Redis, Docker — 6 always-provable matches."
      direction: "Fit 1 — JD explicitly mentions multi-agent orchestration and LLM inference pipelines."
      signals: "Matches signals 1 (multi-agent), 2 (inference routing), 4 (RAG platform)."
      preferred: "LangGraph, FastAPI, PostgreSQL, RAG, observability, AI-native company, AWS, OPT-friendly — 9 signals."
    decision: RUN FULL PIPELINE
    rank: 1

  - jd_id: "jd_009"
    company: "BuildFast Inc"
    title: "Backend Engineer"
    scores:
      provable_coverage: 30
      career_direction_fit: 22
      strongest_signal_match: 14
      preferred_signals: 6
      total: 72
    evidence:
      coverage: "Python, FastAPI, PostgreSQL, Redis, AWS — 5 always-provable matches."
      direction: "Fit 2 — backend at scale, high-throughput API, latency optimization focus."
      signals: "Matches signals 3 (backend API at scale), 5 (greenfield build mentioned)."
      preferred: "FastAPI, PostgreSQL, Redis, AWS, CI/CD, Python as primary language — 6 signals."
    decision: RUN FULL PIPELINE
    rank: 2

selected_pipeline_order:
  - rank: 1  jd_id: "jd_002"  score: 97   company: "Synapse AI"       title: "AI Engineer — New Grad"
  - rank: 2  jd_id: "jd_009"  score: 72   company: "BuildFast Inc"    title: "Backend Engineer"
  - rank: 3  jd_id: "jd_015"  score: 68   company: "DevCo"            title: "Software Developer"

profile_notes: []
```
