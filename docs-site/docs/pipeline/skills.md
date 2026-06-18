---
id: skills
title: Skill Map
sidebar_position: 2
slug: /pipeline/skills
---

# Skill map

For step-by-step operational usage, use [Resume Agent > Skill Workflow](/docs/resume-agent/skill-workflow). This page remains the compact map.

| Skill | Role in system |
|---|---|
| `profile-bootstrap` | Setup skill for candidate onboarding and runtime placeholders. |
| `candidate-profile` | Setup artifact and source of truth for candidate-specific decisions. |
| `pool-intake` | Setup skill for adding raw evidence into the pool. |
| `pool-versioning` | Setup contract for pool structure and write boundaries. |
| `resume-pipeline-orchestrator` | Normal runtime entry point for JD processing. |
| `jd-prefilter` | Runtime gate that filters, scores, and skips or passes JDs. |
| `jd-extraction` | Runtime stage that extracts structured JD signals. |
| `project-selection` | Runtime stage that selects projects and OSS evidence only. |
| `point-repointing` | Runtime stage that tailors selected projects plus all work experience. |
| `point-creation` | Reference method for high-quality bullet writing. |
| `latex-assembly` | Runtime stage that assembles the final LaTeX resume. |

## Design rule

The skills are intentionally composable. You should be able to understand or improve one stage without rewriting the whole pipeline at once.

Normal usage is: run `resume-pipeline-orchestrator`, not each downstream runtime skill by hand. Individual stages are mainly for debugging or internal iteration.
