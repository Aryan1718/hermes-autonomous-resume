---
name: point-creation
description: Craft reference for writing resume bullets. Defines the quality bar, STAR/XYZ/CAR method selection, and compression rules. Called into by the point-repointing skill — use this when constructing or compressing any bullet point.
version: 3.1.0
metadata:
  hermes:
    tags:
      - resume
      - writing
      - bullets
      - craft
      - reference
    category: resume-pipeline
---

# How To Create Points

This file is the `primary operating guide` for future AI sessions that create, revise, or review points.

Read this file first before drafting any new point.

> **Pipeline role:** This guide is the craft reference called into by the **Point Re-Pointing Guide**. It owns the quality bar, the STAR/XYZ/CAR method definitions, and the compression rules. It does not know about job descriptions — the **Point Re-Pointing Guide** owns the JD-targeting logic and delegates bullet construction here.

It defines:
- the quality bar
- the default workflow from raw notes to final bullet
- how to choose between `STAR`, `XYZ`, and `CAR`
- where each method usually fits
- when to open the deeper method-specific guides

Use this guide for `work experience`, `projects`, and any other writing that needs strong scannable points.

If a future section needs points for a new content type, treat this file as the default ruleset first, then adapt the output layer as needed.

The detailed method references are included as supporting files under `references/`:
- `STAR.md` — Situation → Task → Action → Result (`references/STAR.md`)
- `XYZ.md` — Accomplishment → Proof → Method (`references/XYZ.md`)
- `CAR.md` — Challenge → Action → Result (`references/CAR.md`)
- `bullet-writing-patterns.md` — Concrete before/after examples from real session feedback, including JD-specific tailoring patterns. Read THIS first when drafting bullets. (`references/bullet-writing-patterns.md`)

Open these via `skill_view(name='point-creation', file_path='references/STAR.md')` etc. when the agent needs the full method deep-dive.

**Always read `references/bullet-writing-patterns.md` before drafting bullets.** It contains the exact patterns the user approved, including JD-specific examples per role.

## Reference Convention

**Always use skill-name-only references, never hardcoded file paths.**
- ✅ `` `point-creation` `` — this skill itself
- ✅ `` `STAR.md` `` / `` `XYZ.md` `` / `` `CAR.md` `` — method deep-dives in `point-creation/references/`
- ✗ `` `skills/point-creation/SKILL.md` `` — never use hardcoded paths in procedural text

## Purpose And Quality Bar

Good points are not generic resume bullets.

They should make a reader understand:
1. **what you did** — the action you took (built, engineered, designed, rebuilt, led)
2. **what you built** — the system, tool, or solution (named clearly)
3. **what it achieved** — the outcome, impact, or result (quantified if possible, otherwise a clear "so what")

**Every bullet must be a complete sentence-like statement that starts with an action verb.** Never start with a noun phrase ("Healthcare AI pipeline..."), a number ("4 of 15..."), or a metric ("75% reduction..."). The reader needs to know what YOU did before understanding what the thing is.

The final output should be:
- easy to scan
- specific
- grounded in real context
- **action verb first, then what, then impact**
- outcome-aware — every bullet needs a result, not just an activity
- supported by actual numbers where available

### Bullet Structure

Every bullet follows this 3-part structure:

```
[Action Verb] → [What (System/Tool/Feature)] → [How + Impact/Outcome]
```

1. **Action Verb** — Built, Engineered, Developed, Designed, Rebuilt, Implemented, Led, Owned, Drove
2. **What** — the system, tool, feature, or platform you built/owned (named clearly so the reader knows what it is)
3. **Impact** — what it achieved, quantified if possible (saved time, improved accuracy, reduced cost, scaled to X users, handled Y volume). Without a number, at minimum a clear result.

**Good examples (complete sentences with verb + what + impact):**
- ✅ "Rebuilt the healthcare AI pipeline's SOAP notes agent from scratch using Python and CrewAI, restructuring clinical output and mapping to medical codes"
- ✅ "Built 4 of 15 AI application blueprints from scratch for the Innovation Hub open-source platform using Python, CrewAI, and LangGraph, handling ongoing updates across the full catalog"
- ✅ "Enforced RBAC/ABAC access control across the FastAPI multi-agent orchestration layer, ensuring each agent accesses only authorized data"
- ✅ "Optimized the production SaaS FastAPI backend by deploying Redis on AWS, reducing database load by 75% for time-sensitive operational workflows"

**Not (fragment — starts with noun phrase, no clear action):**
- ❌ "Healthcare AI multi-agent pipeline, rebuilding SOAP notes and billing codes agents..." (no proper verb, fragment)
- ❌ "Innovation Hub open-source AI platform, independently built 4 of 15 blueprints..." (starts with noun phrase, not a sentence)

**Not (no impact — reads like a job description):**
- ❌ "Built a Python and FastAPI platform managing the LLM fine-tuning lifecycle" (what happened? so what?)
- ✅ "Built a Python and FastAPI platform managing the full LLM fine-tuning lifecycle, supporting Markdown ingestion and hardware-aware training routing across MLX, Unsloth, and Colab" (has technical depth showing scope)

**Role clarity — did you build it alone, lead a team, or contribute?**
- "Independently built..." (solo ownership)
- "Led the rebuild of..." (team leadership)
- "Owned the end-to-end..." (full responsibility)
- "Contributed to..." (team contribution)

### No Batch/Label Metadata in Bullets

Never include accelerator batch labels (e.g., "YC P25"), funding rounds, or similar metadata inside bullet text. The project name in the LaTeX title line already identifies the platform. Bullets describe the work, not the company's background.

- ✅ "Delivered a <PR_TITLE_1> for <OSS_PROJECT_NAME>, building end-to-end document ingestion..."
- ❌ "Delivered a <PR_TITLE_1> for a YC P25 platform, building..."

This file optimizes for `future AI sessions` first.

It is not limited to work experience and projects.

It should also be used for other point-driven sections unless a section has a clearly better custom format.

## Choose The Right Method

All strong points still need three ingredients:
- the challenge, reason, or context
- the implementation or ownership
- the result, payoff, or scale

The difference is `which part should lead`.

### Short Definitions

- `STAR`: lead with context and task framing when the reader needs to understand the situation before the action or result.
- `XYZ`: lead with accomplishment and proof when the visible impact or metric is the strongest part of the point.
- `CAR`: lead with the problem-solving story when the main value is how a meaningful challenge was resolved.

### Compact Comparison

| Method | Best when | Weak when |
|---|---|---|
| `STAR` | the point needs situation/task context before the action makes sense | the point is mostly a broad summary or the metric/result should obviously lead |
| `XYZ` | the point has a strong accomplishment with measurable proof or clear evidence | the point needs challenge context first or has no trustworthy proof |
| `CAR` | the point is mainly about solving a meaningful challenge or bottleneck | the point is mostly a scope summary or the main value is a metric-first accomplishment |

### Decision Rule

- Need challenge or task context first → `STAR`
- Need impact or metric first → `XYZ`
- Need problem-solving proof → `CAR`

### When To Open The Deep-Dive Files

Use this main file to choose the method.

Open the method-specific guide when:
- the point shape is clear but the draft still feels weak
- the point needs a more deliberate method-specific drafting pattern
- you need examples or step-by-step compression guidance

## Context Gathering

Do not write points from memory-first phrasing.

Write them from `context-first synthesis`.

That means:
1. read the detailed source notes
2. identify the real work areas
3. identify which numbers are real
4. identify what belongs in overview vs detail
5. write points that reflect engineering ownership, not just tool usage

## Output Layers

There are different point styles for different places a point can appear.

The three layers below are common patterns, but the same method-selection and quality rules also apply to other sections.

### A. Role Overview Points

Used in:
- homepage work section
- top of experience detail page

Purpose:
- summarize the full role surface quickly

Rules:
- 4 to 5 points is a good target for the main featured role
- each point should represent a distinct area of responsibility
- do not over-focus on one application
- use real numbers early
- broad role scope first, named examples later

Good overview categories:
- scope and ownership
- inference environments and benchmarking
- orchestration and security systems
- CI, quality, and security tooling
- internal product work

### B. Detailed Workstream Cards

Used in:
- experience detail page

Purpose:
- show the important work in readable chunks

Rules:
- each card should represent a major workstream
- title should be broad
- one summary sentence
- 3 strong points is the preferred pattern
- points should mix implementation and impact naturally
- only use more than 3 if the work truly needs it

Good card titles:
- `Innovation Hub Ownership`
- `Multi-Agent Orchestration`
- `Authorization and Access Control`
- `Internal Product Development`

Weak card titles:
- titles that are too long
- titles that repeat the whole explanation
- titles that over-index on a product name when the work was broader

### C. Project Overview And Detail Points

Used in:
- project descriptions
- project detail sections

Purpose:
- explain why the project matters and what makes it technically interesting

Rules:
- avoid generic `built with X, Y, Z` copy
- emphasize problem, product logic, workflow, architecture, and differentiators
- if a project title is not self-explanatory, use the first sentence to explain the actual problem solved

## Default Workflow For Future Sessions

Use this sequence unless a role or project clearly needs a custom pass:

1. read the source notes
2. identify the major workstreams
3. decide the output layer
4. choose the method per point
5. draft raw method notes
6. compress them into final, ready-to-use bullets
7. check for numbers, clarity, and repetition
8. compare overview and detail for duplication

If the content is not a role or project, keep the same sequence and replace `output layer` with the closest equivalent content layer for that section.

## Point Construction Workflow

### Step 1: Gather Raw Context

For each role or project, extract:
- the broad responsibility
- the concrete systems built
- the use case or domain
- the implementation details
- the constraints
- the reason the solution was designed that way
- the measurable outcomes

Example categories from work experience:
- platform ownership
- blueprint development
- benchmarking
- orchestration
- authorization and access control
- CI and security automation
- internal product work
- observability

Example categories from projects:
- product problem
- user workflow
- system architecture
- implementation decisions
- differentiators
- impact or why it is interesting

### Step 2: Start With Action Verb + System Name

**Every bullet starts with an action verb, followed by the system name.** This is the most important step. The reader must understand what YOU DID before anything else.

Structure: `[Action Verb] + [System/What] + [How] + [Impact]`

Ask three questions before drafting:
1. **What did I do?** → Action verb (Built, Engineered, Rebuilt, Designed, Led, Owned...)
2. **What did I build/own?** → System name (the thing itself, named clearly)
3. **What was the impact?** → Outcome (numbers preferred, otherwise clear result)

**Transform bad bullets into good ones:**

| Before (bad) | After (good) |
|---|---|
| `Rebuilding SOAP notes agents using Python and CrewAI...` (verb but no system name, no impact) | `Rebuilt the healthcare AI pipeline's SOAP notes agent from scratch using Python and CrewAI, restructuring clinical output and mapping to medical codes` |
| `Built 4 of 15 blueprints using Python...` (number first, no system name) | `Independently built 4 of 15 AI application blueprints for the Innovation Hub open-source platform using Python, CrewAI, and LangGraph, handling ongoing updates across the full catalog` |
| `Healthcare AI multi-agent pipeline, rebuilding SOAP notes...` (noun phrase fragment) | `Rebuilt the healthcare AI multi-agent pipeline's SOAP notes agent using Python and CrewAI, restructuring clinical output and mapping to medical codes` |
| `Built a Python platform managing LLM fine-tuning` (no impact) | `Built a Python and FastAPI platform managing the full LLM fine-tuning lifecycle, supporting Markdown ingestion and hardware-aware training routing across MLX, Unsloth, and Colab` |

**Role clarity:** Indicate ownership level — "Independently built...", "Led the rebuild of...", "Owned end-to-end...", "Contributed to..."

### Step 3: Separate Broad Scope From Specific Examples

Do not lead with product names if the actual work was broader than the product name.

Bad pattern:
- leading with `OmniRoute`, `AccessIQ`, or `Innovation Hub` before the reader even knows what kind of work was done

Better pattern:
- first describe the broader capability
- then use the product or blueprint as the example inside the point

Example:

Instead of:
- `Built OmniRoute for transportation using multiple agents`

Prefer:
- `Designed a multi-agent blueprint for a transportation use case...`

Why:
- the reader understands the engineering work first
- the product name becomes supporting context, not the main idea

### Step 4: Decide The Output Layer First

Before drafting any point, decide whether it belongs to:
- a role overview
- a detailed workstream card
- a project overview
- a deep-dive project section

The same raw note may become different points at different layers.

Overview points should stay broader.

Detail points should carry more implementation logic and more context.

### Step 5: Choose The Drafting Method

Do not default to one formula for every point.

Choose the method that matches the story shape:
- use `STAR` when the point needs situation or task framing
- use `XYZ` when the result or metric should lead
- use `CAR` when the point is mainly about challenge-solving

Even when using different methods, every final point should still answer:
- why this work existed
- what was done
- what changed or mattered

If the method choice is unclear, use this rule:
- if the point feels empty without setup, start with `STAR`
- if the point already has a strong proof statement, start with `XYZ`
- if the point is really about resolving a bottleneck or risk, start with `CAR`

### Step 6: Compress The Draft Into Final Writing

The final point should not expose the method mechanically.

Do not write obvious template prose.

Prefer compressed bullets that preserve:
- the system/feature name (first)
- the action taken
- the payoff

Weak patterns:
- just listing tools
- just naming a project
- just saying `worked on`
- just describing an implementation without saying why it mattered
- **starting with a verb** ("Rebuilding...", "Built...", "Implemented...") without naming the system first
- **starting with a number** ("4 of 15...", "75%...") without context for what's being measured

Bad examples:
- `Used Python, FastAPI, and Redis`
- `Worked on OmniRoute`
- `Implemented caching`
- `Rebuilding SOAP notes agents using Python and CrewAI`
- `Built 4 of 15 blueprints from scratch using Python`
- `75% reduction in database load using Redis`

Good examples:
- `Healthcare AI pipeline for clinical documentation, rebuilding SOAP notes and billing codes agents end-to-end using Python and CrewAI`
- `Innovation Hub open-source AI platform, independently built 4 of 15 blueprints from scratch using Python, CrewAI, and LangGraph`
- `Production SaaS backend, deployed Redis caching on AWS reducing database load by 75% for time-sensitive workflows`

### Step 7: Surface Numbers Early (After Context)

Once the system is named, use numbers to quantify scope and impact. But numbers come **after** the system name, never before.

- ✅ `Innovation Hub platform, built 4 of 15 blueprints...` (system first, then number)
- ❌ `Built 4 of 15 blueprints...` (number first, no context)

### Step 8: Decide What To Omit

The goal is not to preserve every raw note line by line.

The goal is to preserve the important meaning.

Keep:
- ownership
- architecture decisions
- constraints
- reusable patterns
- scale
- impact

Omit or compress:
- repeated mentions of the same tool
- low-signal filler wording
- duplicate explanations across overview and detail
- product names when they do not add understanding
- batch/accelerator labels (YC P25, etc.) — these belong in the LaTeX title line, not the bullet

## Method Mapping By Point Type

Use these defaults to reduce ambiguity.

### Role Overview Points

Default:
- broad synthesis first

Usually strongest with:
- selective `XYZ` when a metric or visible proof should lead
- selective `CAR` when a meaningful bottleneck or intervention explains the role well

Use `STAR` sparingly:
- only when one overview point really needs context to make sense

### Detailed Workstream Card Points

Default:
- heavy `STAR` or `CAR`

Why:
- these points usually need workstream context, constraints, and problem-solving logic

Use `XYZ` selectively:
- when one bullet should quickly prove the value of the workstream

### Project Overview Points

Default:
- broad synthesis first

Use `XYZ` only when visible impact exists:
- metrics
- usage
- clear performance gain
- obvious proof of value

Use `STAR` or `CAR` only if the project overview needs a problem-first explanation to be understandable.

### Deep-Dive Project Sections

Default:
- choose among all three based on story shape

Good heuristics:
- subsystem or workflow story → `STAR`
- measurable improvement → `XYZ`
- hard challenge or design tradeoff → `CAR`

## Formatting Rules For Strong Points

### Bullet Format Rules — ALL points must follow these

**0. Action verb first.** Every bullet must start with an action verb (Built, Engineered, Developed, Designed, Rebuilt, Implemented, Led, Owned, Drove), followed by the system name. Never start with a noun phrase ("Healthcare AI pipeline..."), a number ("4 of 15..."), or a metric ("75% reduction..."). Every bullet must be a complete sentence-like statement, not a fragment. Pattern: `[Verb] + [What] + [How] + [Impact]`.

**1. No em dashes.** Never use `—` (em dash, U+2014) or `--` (double-dash) anywhere in resume bullets. This includes using `--` as a separator between clauses (e.g., "Built X -- doing Y"). Use commas, semicolons, or restructure the sentence. Read every bullet aloud — if you would naturally pause and say "dash", rewrite it. Zero tolerance.

**2. Bold numbers.** Every number, metric, or quantitative outcome must be wrapped in `\\textbf{}`. This includes percentages, counts, time measurements, and scale numbers. Examples: `\\textbf{75\\%}`, `\\textbf{100K+ records/day}`, `\\textbf{50+ daily users}`, `\\textbf{40}`, `\\textbf{18}`.

**3. Bold keywords.** Wrap JD-relevant technologies, tools, and skills in `\\textbf{}`. This includes frameworks (FastAPI, React), languages (Python, TypeScript), databases (PostgreSQL, Redis, MongoDB), cloud services (AWS, Supabase), and key concepts (GraphQL, RBAC, multi-agent). Each bullet should have 2--4 bolded keywords.

**4. Target length: ~175 characters.** Every bullet should land around 175 characters. This creates visual uniformity and a dense, information-rich feel. If a bullet is over 220 characters, compress. If under 140, expand with more context or a metric.

**5. Tell a story with impact.** Each bullet must answer: what did you do, what did you build, and what was the result? Without an impact/outcome, the bullet reads like a job description, not an achievement. Every bullet needs a "so what."

**6. Role clarity.** Indicate ownership: "Independently built...", "Led...", "Owned end-to-end...", "Contributed to..."

**7. No batch/label metadata.** Never include accelerator labels (YC P25), funding rounds, or similar metadata in bullet text. These belong in the LaTeX title line.

**8. No em dashes.** (Reiterated for emphasis) Never use `—` or `--` anywhere. Read every bullet aloud — if you'd say "dash", rewrite with comma/semicolon/new sentence.

**9. JD-specific tailoring required.** Bullets must be aimed at the specific JD's priorities. The same role/project should emphasize DIFFERENT aspects depending on the JD's focus. Before writing any bullet, ask: "What does THIS JD care about most from this role/project?" Then lead with that. Never copy-paste the same bullets across different JDs. See `references/bullet-writing-patterns.md` for JD-specific examples per role.

**10. Specific, not vague.** Every bullet must answer: What did you build specifically? How? What was the measurable outcome? "Built backend services" is vague. "Built FastAPI backend for production SaaS handling thousands of orders on AWS" is specific. If the bullet could appear on anyone's resume, it's too generic. Concrete system names, specific numbers, clear outcomes.

### Role Overview Point Format

Overview points should:
- be broad
- be dense
- cover one main slice of the role
- usually fit in one sentence

Example:
- `Owned a 15-blueprint AI application platform, independently built 4 blueprints, and handled ongoing updates, fixes, and new feature work across the broader set.`

### Detailed Card Summary Format

Each card should have:
- a title
- one summary sentence

The summary should answer:
- what was built
- why it was built that way

Example:
- `Designed a multi-agent blueprint for a transportation use case to show how planner-based routing, controlled agent communication, and cross-inference reliability could work in a practical workflow.`

### Detailed Card Point Format

Each card should preferably have 3 points:
1. implementation framing
2. key implementation details or constraints
3. impact or why it mattered

Example:
- `Used a transportation use case to design a broader multi-agent blueprint with CrewAI, where a planner agent routed requests across task-specific agents instead of pushing every request through the same reasoning path.`
- `Implemented an intent taxonomy, low-confidence clarification handling, and selective agent-to-agent communication so the workflow stayed controlled, avoided unnecessary LLM calls, and reduced token and context waste.`
- `This made the blueprint easier to benchmark across different inference environments because the orchestration logic was structured, portable, and not dependent on one model or serving setup to work well.`

## Quality Checklist

Before finalizing points, check:
- **Does the bullet start with an action verb?** (Gate check — if it starts with a noun phrase like "Healthcare AI pipeline..." or a number like "4 of 15..." or a metric like "75%...", rewrite to start with a verb like "Built", "Rebuilt", "Engineered")
- **Is it a complete sentence, not a fragment?** (Gate check — "Healthcare AI pipeline, rebuilding..." is a fragment. "Rebuilt the healthcare AI pipeline's agent..." is a sentence)
- **Does it have an impact/outcome?** (Gate check — "Built a Python platform" is activity. "Built a Python platform, supporting X and achieving Y" is achievement. Every bullet needs a "so what")
- **Is ownership clear?** ("Independently built", "Led", "Owned end-to-end" — not invisible)
- Does the overview represent the full role, not just one project?
- Are numbers included where available?
- **No em dashes anywhere.** (Gate check — read aloud, if you'd say "dash", rewrite)
- **All numbers bolded.** (Gate check)
- **Target ~175 chars per bullet.** (Gate check)
- **No batch/label metadata in bullets.** No YC P25, funding rounds, etc.
- **Is this bullet JD-specific?** (Gate check — could this exact bullet appear on a resume for a completely different JD? If yes, it's too generic. Rewrite to emphasize what THIS JD cares about.)
- **Is this bullet specific, not vague?** (Gate check — does it name concrete systems, numbers, outcomes? Or could it apply to any candidate?)

## Examples From This Portfolio

### Good Transformation 1

From:
- `OmniRoute multi-agent orchestration for transportation workflows`

To:
- `Multi-Agent Orchestration`

Why it improved:
- broader
- focuses on capability
- easier for unfamiliar readers

### Good Transformation 2

From:
- `AccessIQ and deterministic authorization before LLM execution`

To:
- `Authorization and Access Control`

Why it improved:
- broader
- clearer
- less product-name dependent

### Good Transformation 3

From:
- platform-specific first-line wording

To:
- `Built and maintained AI applications across multiple inference environments, with work spanning blueprint development, benchmarking, orchestration, and internal product features.`

Why it improved:
- explains the work before naming internal platforms
- creates a stronger first impression

## If Creating A New Revision File

If a role needs careful refinement, create a dedicated revision note such as `c2l_v1.md`.

That file should contain:
- current overview points
- final card titles
- final summaries
- final bullets
- why each section was written that way
- references back to the source markdown

This is useful because it preserves:
- copy decisions
- reasoning
- future edit context

## Final Principle

The best points should make a reader understand:
- what the work actually was
- why the implementation was thoughtful
- why it mattered

They should not read like:
- tool dumps
- vague resume filler
- internal jargon without explanation
- random project-name lists
- AI-generated prose with em dashes
- the same generic bullets copy-pasted across every resume

Write for understanding first, aim for ~175 characters, bold all numbers and keywords, tell a mini-story in every bullet. Every bullet must be JD-specific — aimed at what THIS JD cares about most. Be specific, not vague. No dashes ever.

Write for understanding first.
Then choose the right method.
Then compress for clarity.
Then surface numbers for credibility.
Aim for ~175-200 characters per bullet with context-first framing.
