# Worked Example — Full End-to-End Re-Pointing

## Scenario: <TARGET_COMPANY> — AI Engineer (AI Foundations)

**JD focus:** Multi-agent AI orchestration, LLM inference pipelines, Python, RAG systems

### Load Phase

Extract reads idx.md + raw.md for:
- 3 selected projects: <OSS_PROJECT_NAME> <ACCELERATOR_COHORT> (covers: multi-agent AI, LLM inference, Python), <PROJECT_NAME_1> (covers: SDK/middleware, backend API), <PROJECT_NAME_4> (covers: backend API, cloud/DevOps)
- 3 work-experience roles: <WORK_EXPERIENCE_COMPANY_1> OSD, <WORK_EXPERIENCE_COMPANY_1> Intern, <WORK_EXPERIENCE_COMPANY_2>, <WORK_EXPERIENCE_COMPANY_3>

### Track A Aim Lists

**<OSS_PROJECT_NAME> <ACCELERATOR_COHORT>** (covers = multi-agent AI orchestration[A], LLM inference[A], Python[B]):
- Lead: multi-agent AI orchestration (priority A, verb: "architect" → honestly "develop and contribute" since it's an OSS contribution, not sole architecture)

**<PROJECT_NAME_1>** (covers: SDK/middleware[A], backend API[A]):
- Lead: SDK/middleware engineering (priority A, verb: "build")

**<PROJECT_NAME_4>** (covers: backend API[A], cloud/DevOps[B]):
- Lead: backend API at scale (priority A, verb: "build")

### Track B Aim Lists (built from raw.md)

**<WORK_EXPERIENCE_COMPANY_1> — <ROLE_TITLE_1> (<DATE_RANGE_1>):**
- Requirements from raw: multi-agent orchestration (A), observability (A), Python (B), cloud/CI-CD (B)
- Lead: multi-agent orchestration → verb: "develop" → foreground: 4 inference environments, LangSmith + LangFuse

**<WORK_EXPERIENCE_COMPANY_1> — <ROLE_TITLE_2> (<DATE_RANGE_2>):**
- Requirements from raw: <TARGET_DOMAIN> (A), access control/RBAC (A), frontend/React (B)
- Lead: <TARGET_DOMAIN> workflow → verb: "rebuild" → foreground: <DOMAIN_TASK_1> + <DOMAIN_TASK_2> agent

**<WORK_EXPERIENCE_COMPANY_2>:**
- Requirements from raw: backend API at scale (A), caching/Redis (A), AWS/cloud (B), latency optimization (B)
- Lead: backend API at scale → verb: "build" → foreground: 75% DB load reduction, 120ms latency

**<WORK_EXPERIENCE_COMPANY_3>:**
- Requirements from raw: data pipeline (A), cloud/serverless (A), full-stack (B)
- Lead: data pipeline → verb: "build" → foreground: 100K+ records/day, 6-8% cost reduction

### Re-Pointed Bullets (examples)

**<OSS_PROJECT_NAME> <ACCELERATOR_COHORT> — Lead bullet (multi-agent AI orchestration):**
> "Developed and contributed a <EXTERNAL_PLATFORM> integration for the open-source AI data platform <OSS_PROJECT_NAME> (500+ GitHub stars), enabling AI agents to securely ingest and retrieve knowledge from <EXTERNAL_PLATFORM> documents; recognized as the project's first external contributor"
(~280 chars, lead with capability, implementation details in supporting bullets)

**<WORK_EXPERIENCE_COMPANY_1> Intern — Lead bullet (<TARGET_DOMAIN>):**
> "Rebuilding <DOMAIN_TASK_1> and <DOMAIN_TASK_2> agents end-to-end for a <TARGET_DOMAIN> product serving thousands of clinicians, implementing strict RBAC/ABAC access control around protected health information (<REGULATED_DATA_TYPE>)"
(~250 chars, specific: product type, compliance constraint, scale)

**<WORK_EXPERIENCE_COMPANY_2> — Lead bullet (backend API scaling):**
> "Deployed a Redis caching layer on AWS with cache refresh controls for a production SaaS platform serving thousands of users, reducing database load by 75% on time-sensitive operational workflows and maintaining 120ms average response latency"
(~270 chars, named tech, specific metric, scale)

### Consistency Check

All bullets measured: 230-320 chars range. No `--` found. All have ≥2 bold terms. All have problem→action→outcome. No overlap between OSD and Intern bullets at <WORK_EXPERIENCE_COMPANY_1>. Technical Skills reordered with Multi-Agent Orchestration, RAG, LLM Inference promoted to front of Concepts row.



