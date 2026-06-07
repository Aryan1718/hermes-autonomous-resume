# Bullet Writing Patterns — Session Learnings (Updated June 3, 2026)

## The Rule: [Action Verb] → [What] → [How] → [Impact]

Every resume bullet must be a complete sentence-like statement starting with an action verb, followed by the system name, the technical approach, and the impact/outcome.

### Structure

```
[Action Verb] + [What (System/Tool/Feature)] + [How (Tech/Method)] + [Impact/Outcome]
```

### Good Examples (JD-Specific Tailoring)

**<WORK_EXPERIENCE_COMPANY_1> Intern — for a Healthcare AI JD:**
- "Rebuilt the <TARGET_DOMAIN> multi-agent workflow with strict RBAC/ABAC access control, orchestrating clinical data flow between <DOMAIN_TASK_1> and <DOMAIN_TASK_2> agents while enforcing per-role document boundaries"
- "Rebuilt the <DOMAIN_TASK_1> generation agent and <DOMAIN_TASK_2> mapping agent end-to-end for production <TARGET_DOMAIN> product, improving clinical documentation accuracy"

**<WORK_EXPERIENCE_COMPANY_1> Intern — for a Backend/API JD:**
- "Built FastAPI backend services for a production <TARGET_DOMAIN> platform, implementing multi-agent orchestration with RBAC/ABAC access control across clinical data agents"
- "Designed and implemented API endpoints for agent-to-agent communication, enforcing department-scoped access control and per-role document boundaries"

**<WORK_EXPERIENCE_COMPANY_1> Intern — for an AI/ML JD:**
- "Implemented multi-agent orchestration in LangGraph across planner, summarization, and analytical agents with department-scoped access control for <TARGET_DOMAIN> product"
- "Deployed and benchmarked AI workflows across 4 inference environments (OpenAI, VLLM, Ollama, Intel OPEA), building LLM inference pipeline engineering experience"

**<WORK_EXPERIENCE_COMPANY_2> — for a Backend JD:**
- "Optimized the production SaaS FastAPI backend by deploying Redis caching on AWS, reducing database load by 75% for time-sensitive order-processing workflows serving thousands of users"
- "Built FastAPI endpoints and Python backend logic for new features, implementing location-isolated traffic spike handling"

**<WORK_EXPERIENCE_COMPANY_2> — for a Cloud/Infra JD:**
- "Deployed and managed production SaaS backend on AWS, implementing Redis caching, compute resources, and firewall configuration for high-traffic order-processing workflows"
- "Built FastAPI microservices and Python backend features, deploying with auto-scaling and load balancing on AWS for thousands of concurrent users"

**<WORK_EXPERIENCE_COMPANY_3> — for a Data Engineering JD:**
- "Built a serverless data pipeline on AWS (Lambda, Glue, PySpark, S3, DynamoDB) processing 100K+ records/day for forest-fire research, reducing infrastructure cost by 6-8% versus the in-house system"
- "Developed ETL workflows using PySpark and AWS Glue, transforming and loading 100K+ daily records into S3 and DynamoDB for downstream ML model consumption"

**<WORK_EXPERIENCE_COMPANY_3> — for a Full-Stack JD:**
- "Developed a full-stack analytics application (Next.js, React, Flask, PostgreSQL, Google Maps) used by 50+ researchers/day to inspect pipeline outputs and evaluate ML model results"
- "Built interactive geospatial visualization features using React and Google Maps API, enabling 50+ daily researchers to explore forest-fire prediction model outputs"

### Bad Patterns — And How to Fix Them

**1. Noun phrase fragment (no verb)**
- ❌ "Healthcare AI multi-agent pipeline, rebuilding <DOMAIN_TASK_1>..."
- ✅ "Rebuilt the <TARGET_DOMAIN> pipeline's <DOMAIN_TASK_1> agent from scratch using Python and CrewAI..."
- Fix: Start with the action verb. The system name follows immediately after.

**2. Number first (no context for what's being measured)**
- ❌ "Built 4 of 15 AI application blueprints using Python..."
- ✅ "Independently built 4 of 15 AI application blueprints for the Innovation Hub open-source platform using Python..."
- Fix: Name the system/platform first, then the number as supporting detail.

**3. No impact (reads like job description)**
- ❌ "Built a Python and FastAPI platform managing the LLM fine-tuning lifecycle"
- ✅ "Built a Python and FastAPI platform managing the full LLM fine-tuning lifecycle, supporting Markdown ingestion and hardware-aware training routing across MLX, Unsloth, and Colab"
- Fix: Add what the system does/what it supports — the "so what"

**4. Batch/label metadata in bullet text**
- ❌ "Delivered a <PR_TITLE_1> for a <ACCELERATOR_COHORT> platform..."
- ✅ "Delivered a <PR_TITLE_1> for <OSS_PROJECT_NAME>..."
- Fix: Project name goes in the LaTeX title line. Bullets describe the work, not company background.

**5. Missing ownership clarity**
- ❌ "Built a serverless AWS data pipeline..."
- ✅ "Independently built a serverless AWS data pipeline..." or "Led the build of..."
- Fix: Indicate solo ownership, team leadership, or contribution level.

**6. Using `--` as a clause separator (CRITICAL — zero tolerance)**
- ❌ "Rebuilding <TARGET_DOMAIN> workflow with strict RBAC/ABAC access control -- orchestrating clinical data flow between agents"
- ❌ "Optimized production SaaS backend by deploying Redis caching on AWS -- reduced database load by 75%"
- ❌ "Built serverless data pipeline on AWS processing 100K+ records/day -- reduced infrastructure cost by 6--8%"
- ✅ "Rebuilt the <TARGET_DOMAIN> workflow with strict RBAC/ABAC access control, orchestrating clinical data flow between <DOMAIN_TASK_1> and <DOMAIN_TASK_2> agents while enforcing per-role document boundaries"
- ✅ "Optimized the production SaaS backend by deploying Redis caching on AWS, reducing database load by 75% for time-sensitive order-processing workflows serving thousands of users"
- ✅ "Built a serverless data pipeline on AWS processing 100K+ records/day, reducing infrastructure cost by 6-8% versus the in-house system"
- Fix: Restructure the sentence using commas, semicolons, or a second sentence. Read the bullet aloud — if you would naturally pause and say "dash", rewrite it. NEVER use `--` anywhere in a bullet.

**7. Same bullets across different JDs (CRITICAL — must be JD-specific)**
- ❌ Using the same 2 bullets for <WORK_EXPERIENCE_COMPANY_1> Intern on every resume (<TARGET_COMPANY_1>, <TARGET_COMPANY_2>, <TARGET_COMPANY_3>, <TARGET_COMPANY_4>, <TARGET_COMPANY_5>)
- ❌ Using the same 2 bullets for <WORK_EXPERIENCE_COMPANY_2> on every resume
- ❌ Using the same 2 bullets for <WORK_EXPERIENCE_COMPANY_3> on every resume
- ✅ For a backend/API JD: Lead with FastAPI, API design, backend services
- ✅ For an AI/ML JD: Lead with LangGraph, CrewAI, LLM inference, multi-agent systems
- ✅ For a <TARGET_DOMAIN> JD: Lead with healthcare workflow, <DOMAIN_TASK_1>, <DOMAIN_TASK_2>
- ✅ For a data engineering JD: Lead with data pipeline, 100K+ records/day, PySpark
- ✅ For a cloud/infra JD: Lead with AWS deployment, caching, production environment
- Fix: Before writing ANY bullet, ask "What does THIS JD care about most from this role/project?" Then lead with that. Every version file must have a distinct `why_now_description`.

**8. Vague or generic bullets (could apply to any candidate)**
- ❌ "Built backend services" — everyone says this
- ❌ "Worked on AI systems" — too vague
- ❌ "Developed full-stack application" — no specificity
- ✅ "Built FastAPI backend services for a production SaaS platform handling thousands of orders, deployed Redis caching on AWS reducing database load by 75%"
- ✅ "Built a multi-agent AI system with LangGraph and CrewAI, implementing planner-led orchestration across clinical data agents with RBAC/ABAC access control"
- Fix: Every bullet must answer: What did you build specifically? How? What was the measurable outcome? If the bullet could appear on anyone's resume, it's too generic.

### Key Principles

1. **Action verb first** — Built, Engineered, Developed, Designed, Rebuilt, Implemented, Led, Owned
2. **System name immediately after verb** — reader knows what you built
3. **Impact always present** — numbers preferred, otherwise clear result
4. **Complete sentence, never fragment** — no noun phrases followed by commas
5. **No batch/label metadata** — no <ACCELERATOR_COHORT>, funding rounds, etc. in bullet text
6. **Ownership visible** — independently, led, owned, contributed
7. **~175 chars target** — dense but scannable
8. **Bold numbers and keywords** — \textbf{75\%}, \textbf{Python}, \textbf{FastAPI}
9. **No em dashes or double-dashes** — use commas or restructure; read aloud to check
10. **JD-specific tailoring** — every bullet must be aimed at THIS JD's priorities; never copy-paste across JDs
11. **Specific, not vague** — concrete systems, numbers, outcomes; no generic claims

### Iteration History

- **First attempt**: Made bullets start with system name → created sentence fragments
- **Second attempt**: Corrected to verb-first → proper complete sentences
- **Third attempt (June 3)**: User feedback — dashes (`--`) in every bullet, same bullets across all JDs, work experience not tailored, vague/generic language
- **Final pattern**: [Action Verb] → [What] → [How] → [Impact], JD-specific, no dashes, specific not vague
- **User confirmed**: "Do not use `-` at all in the points" + "points should focus on JD and not be vague" + "same goes with work experience"



