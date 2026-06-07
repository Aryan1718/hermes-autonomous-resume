# Skill Audit Methodology

> **For the resume-pipeline-orchestrator skill and the broader pipeline skill library.** Use this when reviewing skills for quality, consistency, and context efficiency.

## Audit Checklist — 5 Categories

### 1. DUPLICATE SECTIONS (Highest Risk)
Two sections doing the same thing with **contradictory rules**. The agent will either do the work twice or pick the wrong standard.
- **How to find:** Search for overlapping section headers, repeated output format blocks, similar procedural steps
- **Fix:** Keep the more complete version, delete the other, renumber if needed
- **Example from June 5:** Step 2.5 (all 5 categories, max 6 concepts) vs Step 3.5 (Concepts only, max 7) — kept 2.5, deleted 3.5

### 2. ORPHANED DOCUMENTATION
Documentation for features **no longer used**. Wastes context, confuses the agent about what's active.
- **How to find:** Section headers/paragraphs referencing features, commands, or workflows that don't exist in the current pipeline
- **Fix:** Delete the section entirely
- **Example from June 5:** "Subagent Memory Isolation" section in orchestrator — pipeline never delegates anymore

### 3. JUMBLED NUMBERING
After removing traps/sections, numbering becomes **non-sequential** (1-10, 12-15, 18, 19, 16, 17...).
- **How to find:** List all numbered items, check for gaps and duplicates
- **Fix:** Renumber sequentially from 1 to N

### 4. CROSS-SKILL MISMATCHES
Different skills specify **different standards** for the same thing (e.g., "2–4 bolded keywords" in one skill vs "at least 2 bold terms" in another).
- **How to find:** Compare rules for the same concept across all skills in the pipeline
- **Fix:** Pick the standard that matches the cron prompt (the authoritative source), update all skills to match
- **Example from June 5:** latex-assembly said "2–4 bolded keywords," orchestrator and cron prompt said "at least 2 bold terms" — changed latex-assembly to match

### 5. BLOAT (Large Inline Blocks)
Big curl examples, JSON response shapes, or Python helper scripts **inline in the SKILL.md**. These inflate context every run regardless of whether they're needed.
- **How to find:** Code blocks >20 lines, repeated curl templates, full Python scripts
- **Fix:** Move to `references/<topic>.md`, replace inline with a compact summary + one-line pointer
- **Example from June 5:** Moved ~160 lines of API endpoint docs + 4 Python helper scripts to `references/api-reference.md`

## Fix Priority Order

1. Duplicates first (causes active quality issues)
2. Orphans second (wastes context, confusing)
3. Renumber third (cosmetic but prevents confusion)
4. Cross-skill mismatches fourth (subtle drift)
5. Bloat fifth (context optimization)

## General Principles

- **Cron prompt is authoritative** for pipeline rules. Skills add reference detail.
- **Keep SKILL.md lean** — core workflow rules inline, reference material in `references/`
- **Every reference file gets a one-line pointer** in the parent SKILL.md so agents know it exists
- **After any deletion**, renumber traps/sections immediately
- **When in doubt, read the skill** — don't assume the agent "knows" something from prior sessions
