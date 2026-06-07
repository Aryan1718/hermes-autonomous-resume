# Masters File Format Reference

> **Location:** `workspace/pool/masters.md`
> **Purpose:** Unified condensed index of all personal projects AND OSS contributions for fast selection scoring. Read by project-selection skill instead of opening all raw.md files.
>
> **Replaced:** `workspace/pool/projects/master.md` (projects-only, now merged into this file).

## Entry Format — Personal Project

```markdown
## <Project Title — exact # heading from raw.md>

- **slug:** <folder-slug>
- **type:** personal_project
- **path:** workspace/pool/projects/<slug>/raw.md
- **title:** <display name — must match raw.md # heading exactly, including parenthetical labels like "(<ACCELERATOR_COHORT>)">
- **domain:** <from raw.md domain field>
- **tech:** <from raw.md skills field — comma-separated>
- **tagline:** <one-line summary of what the project does — written by agent from situation/task/action>
- **role:** <from raw.md role field>
- **bullets:**
  - <bullet 1 — key achievement with quantified impact if available>
  - <bullet 2 — technical depth or architecture highlight>
  - <bullet 3 — differentiator or outcome highlight>
```

## Entry Format — OSS Contribution

```markdown
## <Contribution Title — exact # heading from raw.md>

- **slug:** <folder-slug>
- **type:** oss_contribution
- **path:** workspace/pool/oss/<slug>/raw.md
- **title:** <display name — must match raw.md # heading exactly>
- **repo_url:** <GitHub repo URL if available>
- **domain:** <inferred from contribution context>
- **tech:** <from raw.md skills field — comma-separated>
- **tagline:** <one-line summary of the contribution — what was merged/changed>
- **role:** <contributor role — e.g. "First external contributor">
- **bullets:**
  - <bullet 1 — what was built/fixed with key technical detail>
  - <bullet 2 — impact or outcome>
  - <bullet 3 — external validation signal if applicable>
```

## Rules

- **Title must match raw.md `#` heading exactly.** If raw.md has `# <OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>)`, the masters.md title must be `<OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>)`. Never strip parenthetical labels, batch numbers, or qualifiers.
- **`path` must be the exact relative path** from the profile root to the `raw.md`. The pipeline uses this to open only selected entries during repointing.
- **Bullets are condensed** — 2-3 bullets max, each under 200 chars. These are for selection scoring, not the final resume.
- **Tagline is a single sentence** summarizing the project/contribution's purpose.
- **Update the `Entry Count`** at the bottom of masters.md when adding/removing entries (track both projects and OSS).
- **Auto-sync:** When any project's or OSS contribution's `raw.md` is edited, update the corresponding masters.md entry to match.

## Example Entry — Personal Project

```markdown
## <PROJECT_NAME_4>

- **slug:** openpr
- **type:** personal_project
- **path:** workspace/pool/projects/openpr/raw.md
- **title:** <PROJECT_NAME_4>
- **domain:** Developer Tooling
- **tech:** Next.js, TypeScript, Express.js, PostgreSQL, Supabase, GraphQL, GitHub API, Redis, Cron Jobs
- **tagline:** Full-stack contribution-intelligence platform that ranks open-source issues by quality using repo health and timeline signals
- **role:** Sole designer and full-stack builder — owned architecture, frontend, backend, ranking engine, ingestion pipeline, caching, and bookmark system
- **bullets:**
  - Built a full-stack platform using Express.js, PostgreSQL, and GitHub GraphQL that ranks actionable open-source issues using timeline signals, issue-author role classification, and repository health metrics
  - Implemented cron-based ingestion processing 20 repos per run with Redis caching and hourly cleanup over 400 stale entries for a continuously fresh issue feed
  - Combined repo-link fetching, assignment exclusion, and account-free bookmark tracking to reduce wasted contributor effort on stale or already-claimed issues
```

## Example Entry — OSS Contribution

```markdown
## <OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>)

- **slug:** ktx-yc-x25-contributions
- **type:** oss_contribution
- **path:** workspace/pool/oss/ktx-yc-x25-contributions/raw.md
- **title:** <OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>)
- **repo_url:** <GITHUB_REPO_URL>
- **domain:** AI/ML Tooling
- **tech:** TypeScript, Node.js, <EXTERNAL_PLATFORM> API, <EXTERNAL_API_2>, Service Account Auth, CLI Tooling, MCP, pnpm, OSS Collaboration
- **tagline:** First external contributor to <ACCELERATOR_COHORT> AI data agents platform — 2 merged PRs (<PR_TITLE_1> + Windows pnpm fix) + active Windows runtime investigation with co-founder
- **role:** First external contributor — delivered feature adapter integration and cross-platform bug fix as production-style work
- **bullets:**
  - Built a `gdrive` context-source adapter ingesting native Google Docs from Drive folders into Markdown with service-account auth, wired into connection schema, ingest flows, CLI setup, and tests
  - Fixed cross-platform pnpm artifact launcher on Windows by routing through `cmd.exe /d /s /c` while preserving direct execution on macOS/Linux
  - Investigating Windows managed runtime smoke failure (Issue #219) — reproduced, validated fix on clean Windows Server 2022 install, co-founder requested PR
```



