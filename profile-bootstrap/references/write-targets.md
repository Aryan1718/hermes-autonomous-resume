# Write Targets

Only use this file when the user wants runtime/environment placeholders filled in addition to `candidate-profile`.

## Candidate-Required Target

- `candidate-profile/SKILL.md`

## Optional Runtime Targets

Use these only when the corresponding value was provided by the user.

### Profile Storage Placeholders

- `<PROFILE_SLUG>`
- `<POOL_DIR>`
- `<RESUMES_DIR>`

Common locations:
- `resume-pipeline-orchestrator/SKILL.md`
- `resume-pipeline-orchestrator/scripts/push_resume.py`
- `resume-pipeline-orchestrator/references/api-reference.md`
- `resume-pipeline-orchestrator/references/api-helper-scripts.md`
- `resume-pipeline-orchestrator/references/batch-processing-pattern.md`
- `resume-pipeline-orchestrator/references/push-verification.md`
- `pool-intake/SKILL.md`
- `pool-versioning/SKILL.md`
- `point-repointing/SKILL.md`

### Dashboard API Placeholders

- `<DASHBOARD_BASE_URL>`
- `<DASHBOARD_API_KEY_ENV>`

Common locations:
- `resume-pipeline-orchestrator/SKILL.md`
- `resume-pipeline-orchestrator/scripts/push_resume.py`
- `resume-pipeline-orchestrator/references/api-reference.md`
- `resume-pipeline-orchestrator/references/api-helper-scripts.md`

## Rules

- Replace only the placeholders the user asked to personalize.
- Do not replace generic candidate-content placeholders inside template examples unless the task is specifically to write the live candidate profile.
- After edits, scan the touched files for the exact placeholders you intended to replace.
