# Double-Backslash Debugging Guide

## The Problem

When writing `.tex` files, all LaTeX commands must have **single backslashes**:
- Correct: `\documentclass{article}`, `\textbf{text}`, `\item`
- Wrong: `\\documentclass{article}`, `\\textbf{text}`, `\\item`

Double backslashes cause the .tex file to be completely uncompilable.

## Root Cause

The most common cause is constructing LaTeX content as a Python string inside `write_file` tool arguments. In Python string literals, `\\` represents a single backslash. When the agent writes:

```python
content = "\\documentclass{article}\n\\usepackage..."
```

Python evaluates `\\` as `\`, but `write_file` receives the already-evaluated string. However, when the content is passed through multiple layers of string escaping (e.g., JSON serialization in tool arguments), the backslashes can get doubled.

## The Fix: Use Raw Strings

**ALWAYS use raw strings (`r"""..."""`) when constructing .tex content in Python:**

```python
content = r"""\documentclass{article}
\usepackage[top=0.2in, bottom=0.2in, left=0.3in, right=0.3in]{geometry}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{xcolor}

\hypersetup{colorlinks=true, urlcolor=blue, linkcolor=blue}
\setlength{\parindent}{0pt}

\begin{document}
...
\end{document}
"""
with open("/path/to/output.tex", "w") as f:
    f.write(content)
```

The `r` prefix tells Python to treat backslashes as literal characters — no escaping needed.

## Detection

After writing any .tex file, read it back and check:

```bash
# Check for double backslashes (should return 0 matches for commands)
grep -c '\\\\documentclass\|\\\\usepackage\|\\\\textbf\|\\\\item\|\\\\begin\|\\\\end' file.tex

# Or read the first few lines
head -5 file.tex
# Should show: \documentclass{article}
# NOT: \\documentclass{article}
```

## Fix Pattern

If double backslashes are found:

```python
with open("file.tex", "r") as f:
    content = f.read()

# Replace double backslashes with single
content = content.replace("\\\\", "\\")

with open("file.tex", "w") as f:
    f.write(content)
```

**IMPORTANT:** After fixing, re-verify. The replacement can be tricky — `\\\\` (4 chars) → `\\` (2 chars) → `\` (1 char in the actual file). Always read back and confirm.

## Prevention

1. **Method A (MANDATORY for cron runs):** Write a Python script using raw strings, then execute it
2. **Method B (interactive only):** Use `write_file` directly, then immediately read back and verify
3. **NEVER** construct .tex content inline in `write_file` arguments as a Python string without raw prefix
4. **ALWAYS** verify after writing — read the file back and check for double backslashes
