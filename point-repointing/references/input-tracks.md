# Two Input Tracks — Detailed Explanation

The agent re-points two kinds of content, and they arrive differently.

## Track A — Selected Projects (personal + OSS)

- **How they arrived:** chosen by the Project Selection step from the pool.
- **Folder:** `POOL_DIR/projects/<slug>/` or `POOL_DIR/oss/<slug>/`
- **`covers` list:** arrives with each pick from the Selection output.
- **Re-pointing implication:** the `covers` list is a direct instruction. Whatever requirements it names must be loud and early. The lead bullet targets the #1 priority requirement from the covers list.

## Track B — Work Experience

- **How it arrived:** not selected. Every role goes on the resume regardless.
- **Folder:** `POOL_DIR/work-experience/<slug>/`
- **No `covers` list** — nothing chose it.
- **Re-pointing implication:** Step 1 builds the missing aim list per role by reading `raw.md` and identifying what the role can honestly prove against this JD.

## Multi-Role Companies

When a raw file contains **multiple roles at the same company** (e.g., <WORK_EXPERIENCE_COMPANY_1> has <ROLE_TITLE_1> AND <ROLE_TITLE_2>):
- Build a SEPARATE aim list for each role
- Re-point each role's bullets independently
- Both roles always go on the resume
- Each role's bullets must cover DISTINCT work — no overlap
- OSD bullets → earlier phase work (blueprints, Innovation Hub, inference environments)
- Intern bullets → current phase work (<TARGET_DOMAIN>, <DOMAIN_TASK_1>, <DOMAIN_TASK_2>, frontend)
- Never let the same system appear as the lead in both roles

## The Orchestrator's Responsibility

Project selection (Step 3c) only selects from the projects and OSS pool. It has no visibility into work experience. The orchestrator is responsible for sourcing work experience folder paths from the pool and passing them alongside the selection output.

```bash
# List all work experience items in the pool
ls "$POOL_DIR/work-experience/"

# Pass each folder path to the point-repointing skill
# e.g. "$POOL_DIR/work-experience/<work-company-slug>/"
#      "$POOL_DIR/work-experience/alps-web-solutions/"
#      "$POOL_DIR/work-experience/bisag-n/"
```


