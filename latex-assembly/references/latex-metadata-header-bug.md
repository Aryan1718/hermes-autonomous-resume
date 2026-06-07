# LaTeX Metadata Header Bug — Cron Agent Anti-Pattern

## Problem

Cron agents sometimes add metadata comment lines before `\documentclass{article}`:

```latex
% Company Name — Job Title
% <CANDIDATE_NAME> — 2026-06-04
\documentclass{article}
```

This is **wrong**. The `.tex` file must start with `\documentclass{article}` on line 1.

## Detection

After writing any `.tex` file, read it back and check:
- Line 1 must be `\documentclass{article}` — NOT a comment starting with `%`
- If line 1 starts with `%`, the file is WRONG

## Fix

Remove all lines before `\documentclass`:

```bash
# Remove leading comment lines
sed -i '1,/{^% /d' file.tex
# Or more simply, remove lines 1-2 if they match the pattern:
sed -i '1,2d' file.tex  # only if lines 1-2 are the metadata header
```

## Also delete separate pattern-data files

The cron agent may also create a separate `pattern-data-YYYY-MM-DD.tex` file. This file is not a resume — delete it:

```bash
rm pattern-data-*.tex
```

## Files affected (June 4, 2026)

All 11 cron-generated resumes had this bug:
brellium, conversica, distyl, latham-watkins, lendbuzz, monticelloam, oncorps-ai, pure-storage, scowtt-fullstack, scowtt-intern, surgical-safety

All were fixed by removing lines 1-2 and verifying `\documentclass{article}` is on line 1.

## Prevention

- Trap #25 in `latex-assembly/SKILL.md` explicitly forbids metadata comment headers
- Step 10 verification now checks: "Line 1 is `\documentclass{article}` — NOT a comment"
- The assembler must NEVER add metadata comments — LaTeX begins at `\documentclass`, period

