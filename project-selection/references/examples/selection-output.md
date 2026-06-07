# Selection Output Example

Full YAML selection output from a real run, plus LaTeX display format reference.

## YAML Output Example

```yaml
jd_reference: "AI Engineer — <TARGET_COMPANY>"

requirement_target:
  - signal: "Multi-agent AI orchestration"
    exact_jd_phrase: "Build and maintain multi-agent AI systems"
    priority: A
    weight: 3
    why_now_match: true
  - signal: "LLM inference pipelines"
    exact_jd_phrase: "Inference routing and optimization"
    priority: A
    weight: 3
    why_now_match: false
  - signal: "Python"
    exact_jd_phrase: "Strong Python development skills"
    priority: B
    weight: 2
    why_now_match: false

triaged_out_projects:
  - project_id: "archify"
    reason: "Domain contradiction — AST analysis tool, no AI/ML overlap, no priority:A coverage"
  - project_id: "<PROJECT_NAME_3>"
    reason: "Stack contradiction — primary stack is MLX/Unsloth, JD asks for production Python/FastAPI"

selected_projects:
  - project_id: "ktx-yc-x25-contributions"
    title: "<OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>)"
    rank: 1
    project_type: open_source
    total_score: 82
    sub_scores: { coverage: 30, impact: 22, seniority: 12, recency: 8, domain: 10 }
    covers:
      - { signal: "Multi-agent AI orchestration", priority: A }
      - { signal: "LLM inference pipelines", priority: A }
      - { signal: "Python", priority: B }
    key_evidence: "First external contributor to YC-backed AI data agents platform (513 stars), 2 merged PRs (<PR_TITLE_1>, <PR_TITLE_2>), direct co-founder collaboration"
    selection_reason: "Anchor pick. Direct domain match for AI JD — AI data agents platform. First external contributor to YC-backed project is rare signal at new-grad level."
    judgment_overrides: "<OSS_PROJECT_NAME> <ACCELERATOR_COHORT> AI priority boost — AI data agents platform, first external contributor, direct domain match for AI JD. Domain score: 10."
    notes: "Use '<OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>)' in LaTeX title — never drop <ACCELERATOR_COHORT> label."

  - project_id: "convolayer"
    title: "<PROJECT_NAME_1>"
    rank: 2
    project_type: personal
    total_score: 71
    sub_scores: { coverage: 25, impact: 20, seniority: 10, recency: 8, domain: 8 }
    covers:
      - { signal: "Backend API at scale", priority: A }
      - { signal: "SDK/middleware engineering", priority: A }
    key_evidence: "Conversational memory middleware SDK — ChromaDB + PostgreSQL adapters, context compression, 70-80% redundant question reduction"
    selection_reason: "Gap-closer. Covers SDK/middleware engineering and backend API — both uncovered by pick #1."
    judgment_overrides: ""
    notes: ""

  - project_id: "openpr"
    title: "<PROJECT_NAME_4>"
    rank: 3
    project_type: personal
    total_score: 65
    sub_scores: { coverage: 20, impact: 18, seniority: 10, recency: 9, domain: 8 }
    covers:
      - { signal: "Backend API at scale", priority: A }
      - { signal: "Cloud/DevOps engineering", priority: B }
    key_evidence: "GitHub contribution intelligence platform — Express.js + PostgreSQL + Redis, Supabase cron jobs, background ingestion"
    selection_reason: "Closest remaining gap. Adds cloud/DevOps coverage (cron jobs, background processing) not covered by picks #1 and #2."
    judgment_overrides: ""
    notes: ""

runner_up_projects:
  - project_id: "multidoc-rag"
    title: "MultiDoc RAG"
    total_score: 68
    why_not_selected: "Covers similar ground as <OSS_PROJECT_NAME> (AI/AI agents) but without OSS validation. <OSS_PROJECT_NAME> dominates this slot."

coverage_summary:
  covered_priority_A: ["Multi-agent AI orchestration", "LLM inference pipelines", "Backend API at scale", "SDK/middleware engineering"]
  covered_priority_B: ["Python", "Cloud/DevOps engineering"]
  uncovered: []

open_questions: []
```

## LaTeX Display Format for OSS Contributions

```latex
% Personal project:
{\large \noindent \textbf{Project Name} $\mid$ \textit{Tech1, Tech2, Tech3}}

% Open source contribution:
{\large \noindent \textbf{Project Name} $\mid$ \textit{Open Source Contribution} $\mid$ \textit{Tech1, Tech2, Tech3}}
```

**Rules:**
- `Open Source Contribution` is always in `\textit{}`
- Always comes after the project name, before the tech stack
- Separators are ` $\mid$ ` on both sides
- Bullets below follow identical formatting to personal projects


