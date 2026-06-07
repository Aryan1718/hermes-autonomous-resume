---
name: candidate-profile
description: Living reference file containing the candidate's identity, target roles, provable skills, strongest signals, career direction, and hard disqualifiers. Read by jd-prefilter and jd-extraction on every run. Update when experience or preferences change.
version: 1.1.0
metadata:
  hermes:
    tags:
      - resume
      - candidate
      - profile
      - reference
    category: resume-pipeline
---

# Candidate Profile — <CANDIDATE_NAME>

> **Purpose:** Source of truth about the candidate. Read by jd-prefilter to disqualify JDs and rank survivors. Used by jd-extraction for calibration. Used by point-repointing for technical skills and honesty checks.

---

## Identity Snapshot

<CANDIDATE_NAME> is a Master's student in Computer Science at <UNIVERSITY_NAME> (GPA <GPA>, graduating <GRAD_DATE>), currently on <WORK_AUTH_STATUS>. He currently works as a **<ROLE_TITLE_2>** at <WORK_EXPERIENCE_COMPANY_1> and has hands-on production experience building AI/ML systems, backend APIs, full-stack products, SDKs/middleware, and cloud infrastructure across internships, open-source work, and independent projects.

His work spans multi-agent AI orchestration (CrewAI, LangGraph), inference pipeline engineering, RAG platforms, conversational memory middleware, access-control systems (RBAC/ABAC), healthcare AI workflows, backend API design (FastAPI, Python), cloud deployment (AWS), and DevOps/CI/CD automation. He has shipped systems in production — not just built demos — and can speak to observability, access control, scalable AI architecture, and cross-platform development from real experience.

He is actively seeking his first full-time role in <TARGET_COUNTRY> and is open to any company size, any industry, and any engineering domain where he can build, own, and ship real systems — including backend, cloud, AI/ML, DevOps, and pure software engineering roles.

**Current role:** <ROLE_TITLE_2> at <WORK_EXPERIENCE_COMPANY_1> (<CURRENT_ROLE_START_DATE> – Present). Previously <ROLE_TITLE_1> at <WORK_EXPERIENCE_COMPANY_1> (<PREVIOUS_ROLE_START_DATE> – <PREVIOUS_ROLE_END_DATE>).

---

## Target Roles

**Role titles that match:**
- Software Engineer / Software Developer
- Backend Engineer / Backend Developer
- Full-Stack Engineer / Full-Stack Developer
- AI Engineer / AI/ML Engineer / ML Engineer
- Systems Engineer (software-focused)
- DevOps Engineer / Cloud Engineer / Infrastructure Engineer
- Site Reliability Engineer (SRE) — if code/feature engineering scope is present
- Platform Engineer — if product/feature engineering scope is present
- New Grad Engineer / Associate Engineer / Junior Engineer / Junior Developer
- Software Engineering Intern (if transitioning to full-time)

**Role types that match:**
- Product engineering (building features, services, platforms)
- AI/ML systems engineering (inference, pipelines, agents, RAG)
- Backend / API engineering (REST, microservices, databases)
- Full-stack engineering (frontend + backend, React/Next.js + Python/Node.js)
- DevOps / Cloud / Infrastructure engineering (if code or product ownership is involved)
- SDK / middleware / developer tooling engineering

**Role types that do NOT match (pre-filter disqualifies):**
- Pure data science / pure ML research (no engineering component)
- Pure frontend / UI engineering with no backend scope
- QA / SDET only
- Management, non-technical, or executive roles (no engineering/technical scope)

---

## Seniority

**Targeting:** Entry-level (new grad / 0–2 yrs) and mid-level (2–4 yrs) roles.

**Pre-filter rule:** Pass if JD signals entry, new grad, junior, associate, or mid-level. Pass if seniority is unspecified. **Disqualify if JD explicitly requires 5+ years of full-time industry experience** with no flexibility stated.

**Note:** The candidate currently works as a <ROLE_TITLE_2> and has approximately <YEARS_OF_EXPERIENCE> of combined internship and part-time production experience. He applies to entry and mid-level roles where his project depth, open-source contributions, and production systems compensate for years-of-experience gaps. Do not disqualify a mid-level role solely because it lists 3–4 years — only disqualify at 5+ years explicitly required.

---

## Location

**In scope:** United States only — on-site, hybrid, or remote.

**Pre-filter rule:** Pass if role is <TARGET_COUNTRY>-based (any state), <TARGET_COUNTRY>-remote, or location unspecified (assume <TARGET_COUNTRY>-remote). **Disqualify if role is explicitly outside <TARGET_COUNTRY>** (Canada-only, UK-only, EU-only, etc.) with no <TARGET_COUNTRY> option.

**State preferences:** None — all 50 states are in scope.

---

## Work Authorization

**Current status:** <WORK_AUTH_STATUS> (authorized to work in <TARGET_COUNTRY> without employer sponsorship for the OPT period).

**Future need:** Will require <FUTURE_SPONSORSHIP_TYPE> sponsorship after OPT expires.

**Pre-filter rule:**
- Pass if JD says "will sponsor" or does not mention sponsorship.
- Pass if JD says "OPT/CPT accepted."
- **Disqualify if JD explicitly says "no sponsorship now or in the future" or "must be a <TARGET_COUNTRY> citizen / permanent resident" with no exceptions.**
- If JD is ambiguous on sponsorship, **pass** — do not disqualify on ambiguity.

---

## Hard Disqualifiers

The pre-filter **immediately disqualifies** a JD if any of the following are true. Non-negotiable.

1. **Role is outside <TARGET_COUNTRY>** with no remote/US option.
2. **Explicitly no sponsorship now or ever** (citizen/PR only, no exceptions stated).
3. **Role requires 5+ years of full-time industry experience**, explicitly stated.
4. **Role is non-engineering** — pure management, pure sales, pure data analyst (no engineering scope).
5. **Role is pure frontend only** — no backend, no API, no system design scope, no DevOps/cloud scope.
6. **Role is pure ML research** — no production engineering component, academic or research lab only.
7. **Role requires an active security clearance** (Secret, TS, TS/SCI) — the candidate is not eligible.
8. **Role is QA / SDET only** — no feature or product development scope.

If a JD fails any one of these, stop — skip the JD entirely. Do not score it.

---

## Provable Must-Haves

Skills and experiences the candidate can **always honestly prove** from his projects and work experience. Used by jd-prefilter's binary check (need 2+ matches) and by point-repointing for technical skills.

### Always provable — production evidence exists

| Skill / Experience | Best evidence |
|---|---|
| Python | <WORK_EXPERIENCE_COMPANY_1> (inference engine, observability pipelines), Alps (FastAPI backend), <WORK_EXPERIENCE_COMPANY_3> (AWS Lambda + PySpark), <PROJECT_NAME_3>, <PROJECT_NAME_4>, <PROJECT_NAME_1> |
| FastAPI / REST API design | <WORK_EXPERIENCE_COMPANY_2> (production SaaS backend), <PROJECT_NAME_3> |
| PostgreSQL | Alps (production DB), <PROJECT_NAME_4> (Supabase + PostgreSQL) |
| Redis | <WORK_EXPERIENCE_COMPANY_1> (caching layer), Alps (AWS Redis, 75% DB load reduction), <PROJECT_NAME_4> (Upstash Redis) |
| React / Next.js | <WORK_EXPERIENCE_COMPANY_3> (analytics dashboard), <PROJECT_NAME_4> (frontend), <WORK_EXPERIENCE_COMPANY_1> (healthcare product) |
| AWS | <WORK_EXPERIENCE_COMPANY_1> (inference routing, deployment), <WORK_EXPERIENCE_COMPANY_3> (Lambda, Glue, S3, DynamoDB), Alps (Redis on AWS) |
| Docker / Docker Compose | <WORK_EXPERIENCE_COMPANY_1> (deployment workflows), <PROJECT_NAME_4> |
| LangChain / LangGraph | <WORK_EXPERIENCE_COMPANY_1> (multi-agent orchestration), <PROJECT_NAME_3> |
| Multi-agent AI systems | <WORK_EXPERIENCE_COMPANY_1> (CrewAI + LangGraph orchestration) |
| RAG systems / vector search | <WORK_EXPERIENCE_COMPANY_1> (FinSights Q&A with document relationship retrieval), <PROJECT_NAME_3> (Markdown-to-training-data pipeline) |
| LLM inference pipelines | <WORK_EXPERIENCE_COMPANY_1> (inference routing engine, CPU/GPU/cloud switching, 4 environments) |
| Observability / monitoring | <WORK_EXPERIENCE_COMPANY_1> (LangSmith + LangFuse pipelines, 40% efficiency improvement), <PROJECT_NAME_3> (fine-tuning run tracking) |
| Healthcare / HIPAA domain | <WORK_EXPERIENCE_COMPANY_1> (healthcare AI product, SOAP notes + billing codes agent rebuild, PHI access control) |
| MongoDB | <WORK_EXPERIENCE_COMPANY_2> (production data persistence) |
| CI/CD / GitHub Actions | <WORK_EXPERIENCE_COMPANY_1> (deployment workflows, open-source blueprints), <WORK_EXPERIENCE_COMPANY_3> (scheduled AWS jobs), KTX <ACCELERATOR_COHORT> (contrib'd cross-platform CI fix) |
| TypeScript / JavaScript | <PROJECT_NAME_1>, <PROJECT_NAME_4>, <PROJECT_NAME_2>, KTX <ACCELERATOR_COHORT> |
| System design / distributed systems | <WORK_EXPERIENCE_COMPANY_1> (multi-agent orchestration at scale), <PROJECT_NAME_4> (cron jobs, geo-distributed repos), <WORK_EXPERIENCE_COMPANY_3> (serverless data pipeline) |
| SDK / middleware engineering | <PROJECT_NAME_1> (conversational memory middleware, ChromaDB + PostgreSQL adapters, context compression) |
| Cloud / DevOps engineering | <WORK_EXPERIENCE_COMPANY_3> (AWS Lambda, Glue, S3, DynamoDB pipeline), <WORK_EXPERIENCE_COMPANY_1> (inference routing, Docker, CI/CD), <PROJECT_NAME_4> (Supabase cron jobs) |
| Cross-platform development | KTX <ACCELERATOR_COHORT> (Windows pnpm fix, managed runtime smoke fix on Windows Server 2022) |
| Google Drive / Google Docs API | KTX <ACCELERATOR_COHORT> (GDrive context-source adapter, service-account auth) |
| MCP (Model Context Protocol) | <WORK_EXPERIENCE_COMPANY_1> (AccessIQ — MCP-based authorization, MCP service integration) |
| Autonomous contribution / OSS ownership | KTX <ACCELERATOR_COHORT> (first external contributor, 2 merged PRs, adapter + cross-platform fix), <OSS_PROJECT_NAME_2> (merged PR), <OSS_PROJECT_NAME_3> (merged PR) |

### Provable with framing — evidence exists but needs positioning

| Skill / Experience | Note |
|---|---|
| DynamoDB | <WORK_EXPERIENCE_COMPANY_3> (production use, cloud pipeline) |
| Node.js | <PROJECT_NAME_1> (TypeScript/Node.js SDK — production-grade) |
| GCP | Listed in skills; not the primary cloud in project evidence |
| PyTorch / LoRA | <PROJECT_NAME_3> uses MLX and Unsloth which involve PyTorch concepts, but not the central story |
| Java / C++ | Academic and listed; no production project evidence |
| Ollama / local LLM serving | <PROJECT_NAME_3> (local inference), <WORK_EXPERIENCE_COMPANY_1> (Ollama as one of 4 environments) — real but framing-dependent |
| Supabase | <PROJECT_NAME_4> (production use via PostgreSQL), <WORK_EXPERIENCE_COMPANY_1> (some internal use) |

---

## Strongest Signals

the candidate's clearest differentiators — where his evidence is deepest and most specific. When scoring a JD, a JD that asks for these signals scores higher.

**Signal 1 — Multi-agent AI systems and LLM orchestration.**
Two production-level projects (<WORK_EXPERIENCE_COMPANY_1> work, <PROJECT_NAME_3>) and direct work experience building CrewAI + LangGraph systems. This is rare at entry/mid level and is the candidate's clearest differentiator in the AI engineering space.

**Signal 2 — Inference pipeline engineering.**
The inference routing engine at <WORK_EXPERIENCE_COMPANY_1> (CPU/GPU/cloud switching, 35% latency reduction, 4 environments) is a specific, quantified, production system. Most candidates have used hosted LLMs — the candidate has built the routing layer between them.

**Signal 3 — Backend API engineering at production scale.**
<WORK_EXPERIENCE_COMPANY_2> (FastAPI + MongoDB + Redis, 75% database load reduction, 120ms latency under production traffic), <PROJECT_NAME_3> (FastAPI full-stack platform), and <PROJECT_NAME_4> (Express.js + PostgreSQL + Redis, GitHub GraphQL) provide strong, quantified backend proof.

**Signal 4 — SDK and middleware engineering.**
<PROJECT_NAME_1> — a backend-agnostic conversational memory middleware SDK (ChromaDB + PostgreSQL adapters, context compression, clarification tracking, ~70–80% redundant question reduction, stable token usage from 3 to 40+ turns). Building reusable SDKs that other developers integrate is a distinct skill from building standalone apps.

**Signal 5 — Cloud and DevOps engineering.**
<WORK_EXPERIENCE_COMPANY_3> (serverless AWS pipeline, Lambda + Glue + PySpark, 100K+ records/day, 6–8% cost reduction), <WORK_EXPERIENCE_COMPANY_1> (Docker workflows, CI/CD with GitHub Actions + Trivy + Dependabot, <PR_TITLE_2>es at KTX), <PROJECT_NAME_4> (Supabase cron jobs, background ingestion). the candidate has built and operated cloud infrastructure, not just used it.

**Signal 6 — Healthcare AI domain.**
Rebuilding SOAP notes and billing codes agents end-to-end for <WORK_EXPERIENCE_COMPANY_1>' healthcare AI product, with strict RBAC/ABAC access control around protected health information. This is domain-specific production work with real compliance constraints (PHI handling).

**Signal 7 — 0→1 product builds and greenfield ownership.**
<PROJECT_NAME_2> (AST-driven codebase understanding tool), <PROJECT_NAME_1> (memory SDK from scratch), <PROJECT_NAME_3> (full fine-tuning lifecycle platform), <PROJECT_NAME_4> (contribution intelligence platform) — the candidate has repeatedly built complete systems from nothing and can operate with ambiguity.

**Signal 8 — Open-source contribution and collaboration.**
<OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>) — first external contributor to a YC-backed project (513 stars), delivered a <PR_TITLE_1> and a <PR_TITLE_2>, actively working with the co-founder. <OSS_PROJECT_NAME_2> (merged PR). <OSS_PROJECT_NAME_3> (merged PR). Demonstrates ability to read unfamiliar codebases and contribute meaningfully.

---

## Career Direction — Personal Why Now

The candidate is entering the workforce at the moment when AI engineering and cloud-native development are converging into a single discipline. His personal "Why Now?" maps onto multiple kinds of roles, all weighted equally:

**Fit 1 — Building AI/ML systems end-to-end.**
The work he has done and continues to do. Roles building production AI pipelines, agent systems, inference infrastructure, or AI-powered platforms. These are the highest-fit JDs — the resume is already aimed at them.

**Fit 2 — Backend and distributed systems at scale.**
Every AI project the candidate has built has a backend at its core (FastAPI, Express.js, PostgreSQL, Redis, MongoDB). Roles focused on APIs, databases, microservices, and distributed systems are a natural match.

**Fit 3 — Cloud, DevOps, and infrastructure engineering.**
<WORK_EXPERIENCE_COMPANY_3> (serverless AWS pipeline), <WORK_EXPERIENCE_COMPANY_1> (Docker, CI/CD, deployment workflows), KTX <ACCELERATOR_COHORT> (cross-platform CI/CD fixes), <PROJECT_NAME_4> (cron jobs, background processing). Roles involving cloud infrastructure, DevOps tooling, or platform engineering with a coding component are a strong fit.

**Fit 4 — SDK, middleware, and developer tooling.**
<PROJECT_NAME_1> (conversational memory middleware), <PROJECT_NAME_2> (AST-driven codebase understanding tool). Roles building reusable developer infrastructure — SDKs, middleware, CLI tools, or developer platforms — play to the candidate's ability to build for other developers.

**Fit 5 — Healthcare AI and regulated domains.**
Rebuilding production healthcare agents with PHI access control at <WORK_EXPERIENCE_COMPANY_1>. Roles in healthtech or other regulated industries where data privacy and compliance matter.

**Fit 6 — Taking a product from 0 to 1.**
Most of the candidate's major projects were greenfield builds with no existing foundation. He is comfortable with ambiguity and building structure from scratch. Startup or early-stage roles with a 0→1 mandate are a good fit.

**Scoring note:** When ranking JDs, all six fit types are weighted equally. A JD that matches any of these scores proportionally. A JD that matches multiple fits scores highest. A JD that matches none of these is a weak fit even if it passes the binary disqualifiers.

---

## Preferred Signals

Not gates — a JD does not fail if they are absent. But their presence raises a JD's score during ranking. Each preferred signal present adds one point to the JD's score.

**AI / ML signals:**
- Mentions LLM, AI agents, RAG, vector search, or inference pipelines
- Mentions LangChain, LangGraph, CrewAI, or similar orchestration frameworks
- Mentions fine-tuning, model training, or dataset generation

**Backend / systems signals:**
- Mentions Python as the primary backend language
- Mentions FastAPI, Express.js, or Django
- Mentions PostgreSQL, Redis, MongoDB, or DynamoDB specifically
- Mentions system design, distributed systems, or microservices

**Cloud / DevOps signals:**
- Mentions AWS, Docker, or cloud infrastructure
- Mentions CI/CD, GitHub Actions, Terraform, or infrastructure-as-code
- Mentions DevOps, cloud engineering, or platform engineering (with coding)

**Full-stack signals:**
- Mentions React, Next.js, or TypeScript
- Mentions full-stack or full-lifecycle development

**Domain signals:**
- Mentions healthcare, healthtech, HIPAA, or regulated data
- Mentions MCP, SDK, middleware, or developer tooling

**Culture / stage signals:**
- Mentions 0→1, greenfield, or "build from scratch"
- Role is at a startup or early-stage company
- Role is at a company building AI-native products or tooling
- OPT/sponsorship-friendly language present

---

## Industry Restrictions

**None.** The candidate applies across all industries. No sector is excluded.

---

## Compensation

**Expectation:** US market rate for entry-to-mid-level software engineering roles.

**Pre-filter rule:** Do not disqualify on compensation. If a JD lists a salary range, pass regardless — compensation is negotiated at offer stage, not filtered at JD stage.

---

**References:**
- `references/update-protocol.md` — How to update this profile (for manual maintenance only)
- `references/change-log.md` — Historical change log


