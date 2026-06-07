---
id: skills
title: Skill Map
sidebar_position: 2
slug: /pipeline/skills
---

# Skill map

| Skill | Role in system |
|---|---|
| `profile-bootstrap` | Onboards a real candidate and optionally fills runtime placeholders. |
| `candidate-profile` | Candidate-specific source of truth. |
| `pool-intake` | Adds new raw evidence into the pool. |
| `pool-versioning` | Defines pool structure and write boundaries. |
| `jd-prefilter` | Filters and scores incoming JDs. |
| `jd-extraction` | Extracts structured signals from a JD. |
| `project-selection` | Chooses the best supporting projects and OSS items. |
| `point-repointing` | Re-aims bullets toward the JD. |
| `point-creation` | Reference method for high-quality bullet writing. |
| `latex-assembly` | Produces the final LaTeX resume. |
| `resume-pipeline-orchestrator` | Runs the end-to-end pipeline and pushes results. |

## Design rule

The skills are intentionally composable. You should be able to understand or improve one stage without rewriting the whole pipeline at once.
