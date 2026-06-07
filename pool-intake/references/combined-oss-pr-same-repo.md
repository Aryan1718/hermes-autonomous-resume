# Reference: Combining Multiple OSS PRs to Same Repo

## When to Combine
When a candidate has multiple merged PRs for the same repository, combine them into a single pool entry instead of creating separate ones.

**Why:**
- Stronger narrative: shows repeated meaningful contribution to one project
- Saves resume project slots (only 3 available)
- YC/startup branding appears once, not diluted
- Example: 2 PRs to <OSS_PROJECT_NAME> → one entry, not two

## How to Combine

1. Use the repo name as the project name (include metadata like YC batch in the heading)
2. List all PR links under `pr_links:` (plural)
3. Merge contribution descriptions into one coherent `What the Contribution Was` section
4. Keep each PR's specific changes as sub-bullets under `What Changed`
5. Merge skills, outcomes, and evidence assessment

## Example raw.md Heading
```markdown
# <OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>) — Google Drive Context Source + Windows Build Fix
```

## Example pr_links Field
```markdown
pr_links:
  - <PR_URL_1>
  - <PR_URL_2>
```

## Tracking Active Issue Investigations

When you have merged PRs AND an active issue investigation in progress on the same repo:

1. List merged PRs under `pr_links:` (plural)
2. Add an `issues:` field with links to active issues
3. In the `What Changed` section, add a sub-section for the active issue with status:
   - "Issue #N — under discussion/testing:" for issues being investigated
   - "Issue #N — PR forthcoming" when the maintainer has asked for a PR
4. `merged:` stays `true` if at least one PR has merged (the entry is externally validated)
5. The contribution description should mention both the merged work and the active investigation

**Why:** Shows ongoing engagement with the project and collaboration with maintainers. Once the PR merges, update the entry to move the issue from "investigation" to a merged PR in `pr_links`.

## What Not to Do
- Don't create two folders: `ktx-google-drive-context-source/` and `ktx-windows-pnpm-artifacts-fix/`
- Don't let the same company name appear twice in the Projects section
- If already created separately, archive the individual entries (prefix with `_archived-`) and create the combined one

## Real-World Example from This Session
See: `pool/oss/ktx-yc-x25-contributions/raw.md`
Archived: `_archived-ktx-google-drive-context-source/`, `_archived-ktx-windows-pnpm-artifacts-fix/`



