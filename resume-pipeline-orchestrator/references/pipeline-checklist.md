# Pipeline Speed & Quality Checklist

> **Purpose:** Run this checklist after every pipeline execution. Target: <20 min, zero quality issues.

## Timing Checkpoint

| Step | Target | Actual | Status |
|------|--------|--------|--------|
| Fetch + prefilter | <3 min | | |
| JD extraction | <3 min | | |
| Project selection | <5 min | | |
| Read 3 raw.md files | <3 min | | |
| Re-pointing + version writes | <5 min | | |
| LaTeX assembly | <3 min | | |
| Push + mark + log | <2 min | | |
| **TOTAL** | **<20 min** | | |

## Quality Gate — Bullets

- [ ] No em dashes (`--` or `—`) in any bullet
- [ ] Every bullet has: problem → action → outcome
- [ ] Numbers bolded (`\textbf{75\%}`)
- [ ] Keywords/tools bolded (`\textbf{FastAPI}`, `\textbf{LangGraph}`)
- [ ] ~175 chars per bullet (not counting LaTeX commands)
- [ ] No invented skills or metrics

## Quality Gate — Format

- [ ] Version files: header + bullets only (no `---`, no LaTeX commands)
- [ ] idx.md: existing structure preserved, new `## Version N` block appended
- [ ] .tex file: all `%` escaped as `\%`, all `&` as `\&`
- [ ] .tex file: starts with `\documentclass`, ends with `\end{document}`
- [ ] No commented-out projects in output

## Efficiency Gate

- [ ] read_file calls: 6 max (3 selected + 3 work-exp)
- [ ] Version writes: batched in ONE execute_code call
- [ ] idx.md updates: batched in same execute_code call
- [ ] delegate_task NOT used for full pipeline
- [ ] .tex written via write_file (not patch)
