# LaTeX Backslash Escaping — Known Issue & Fix

## The Bug

When writing `.tex` files, backslashes can get doubled:
- **Wrong:** `\\documentclass{article}` (double backslash — won't compile)
- **Correct:** `\documentclass{article}` (single backslash)

This happened in the June 4, 2026 cron run — 6 out of 12 generated `.tex` files had every LaTeX command double-escaped. The files were: brellium, pure-storage, monticelloam, latham-watkins, oncorps-ai, scowtt-intern.

## Root Cause

The `.tex` content string was passed through a path that double-escaped backslashes before writing. This can happen when:
1. Content is serialized/deserialized through JSON (which escapes `\` as `\\`)
2. Content is written via a method that applies an extra layer of escaping
3. The `patch` tool is used on files containing LaTeX (known issue — trap #15)

## Prevention

1. **Always use `write_file` for `.tex` files** — never `patch`
2. **After writing, read the file back** and verify single backslashes
3. **Quick check:** `grep -c '\\\\documentclass' file.tex` should return 0 (no matches)

## Fix (if found broken)

```bash
python3 -c "
import sys
fpath = sys.argv[1]
with open(fpath, 'r') as f:
    content = f.read()
# Replace double backslashes with single
fixed = content.replace('\\\\\\\\', '\\\\')
with open(fpath, 'w') as f:
    f.write(fixed)
print(f'Fixed: {fpath}')
" file.tex
```

Or for all files at once:
```bash
for f in *.tex; do
  python3 -c "
with open('$f', 'r') as fh: c = fh.read()
with open('$f', 'w') as fh: fh.write(c.replace('\\\\\\\\', '\\\\'))
"
done
```

## Verification Checklist (after every .tex write)

- [ ] `\documentclass` — single backslash
- [ ] `\usepackage` — single backslash
- [ ] `\begin` / `\end` — single backslash
- [ ] `\textbf` / `\textit` — single backslash
- [ ] `\item` — single backslash
- [ ] `\vspace` / `\hfill` / `\rule` — single backslash
- [ ] `\\` (line break) — exactly two backslashes (not four)
- [ ] `\&` and `\%` — single backslash (escaped special chars)
