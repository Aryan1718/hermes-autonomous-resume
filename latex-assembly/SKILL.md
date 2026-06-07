---
name: latex-assembly
description: Runs after point-repointing. Assembles the final tailored resume as a compilable LaTeX file using the exact structural format. The last content step before PDF compilation.
version: 3.2.0
metadata:
  hermes:
    tags:
      - resume
      - latex
      - assembly
      - formatting
    category: resume-pipeline
---

# Resume LaTeX Assembly Guide

> **Purpose:** Assemble the final tailored resume as a LaTeX file. Runs after point-repointing, before saving the .tex file. Slots re-pointed bullets into fixed LaTeX structure — no authoring, no redesign.

**Inputs:** Tailored points from point-repointing (projects + work experience + technical_skills_update) + this guide.
**Output:** Valid, compilable `.tex` file.

**Output path:** `/opt/data/profiles/<PROFILE_SLUG>/home/<RESUMES_DIR>/<company-slug>-<YYYY-MM-DD>.tex`

---

## What This Step Is — and What It Is Not

| This step IS | This step IS NOT |
|---|---|
| Slotting re-pointed bullets into fixed LaTeX structure | Inventing new sections or layouts |
| Applying bold to keywords per the bolding rules | Deciding which projects to include (selection already did that) |
| Using `technical_skills_update` from point-repointing verbatim | Independently reordering or adding technical skills |
| Preserving exact spacing and formatting commands | Changing font sizes, margins, or document geometry |
| Outputting a valid, compilable `.tex` file | Creating a PDF (compilation is a separate step) |

---

## Document-Level Setup

Fixed — never change:

```latex
\documentclass{article}
\usepackage[top=0.2in, bottom=0.2in, left=0.3in, right=0.3in]{geometry}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{xcolor}

\hypersetup{colorlinks=true, urlcolor=blue, linkcolor=blue}
\setlength{\parindent}{0pt}

\begin{document}

\begin{center}
\thispagestyle{empty}
```

---

## Section Order

Always exactly these five sections, in this order:

```
1. Header          (name + contact)
2. Education
3. Technical Skills
4. Professional Experience
5. Projects
```

Never reorder. Never add a section. Never remove a section.

---

## Section 1: Header

```latex
\large \textbf{FULL NAME} \\
City, ST $\mid$ +1-XXX-XXX-XXXX $\mid$
\href{mailto:<CANDIDATE_EMAIL>}{<CANDIDATE_EMAIL>} $\mid$
\href{<LINKEDIN_URL>}{\textcolor{blue}{LinkedIn}} $\mid$
\href{<GITHUB_PROFILE_URL>}{\textcolor{blue}{GitHub}}
\end{center}
```

**Rules:**
- Name is ALL CAPS wrapped in `\large \textbf{}`
- City and state on the same line as name (e.g., `<CITY>, <STATE>`)
- No Portfolio link — only LinkedIn + GitHub
- Email uses `mailto:` href — no `\textcolor{blue}`
- LinkedIn and GitHub use `\textcolor{blue}{Label}`
- Separators are `$\mid$` with a space on each side
- `\end{center}` closes immediately after the contact line
- **This section is never changed by JD tailoring.** Contact details are static.

---

## Section 2: Education

**Section heading pattern** (same for every section except header):

```latex
\vspace{3mm}
\noindent \textbf{EDUCATION} \vspace{-8pt} \\
\rule{\linewidth}{0.5pt}
```

**Each entry:**

```latex
\noindent \textbf{Institution Name} \hfill \textbf{Mon YYYY – Mon YYYY} \\
\textit{Degree Name}
```

**Multiple entries:** BLANK LINE + `\vspace{1.5mm}` + BLANK LINE between each entry. The blank lines are REQUIRED — LaTeX treats them as paragraph breaks.

**After last entry:** BLANK LINE + `\vspace{3mm}` + BLANK LINE before TECHNICAL SKILLS header.

**Rules:**
- Education is **never modified** by JD tailoring. Always copied as-is.
- Degree name in `\textit{}` — no GPA/CGPA line.
- Dates use: `Mon YYYY – Mon YYYY`.

---

## Section 3: Technical Skills

**Section heading:** same pattern.

**Each skill row:**

```latex
\noindent \textbf{Category Label:} item1, item2, item3 \\
```

**Fixed categories and order:**
1. Languages
2. Frameworks
3. Databases
4. Cloud & Tools
5. Concepts

The last row (Concepts) has no trailing `\\`.

**Rules:**
- Use `technical_skills_update` from point-repointing **verbatim**.
- All 5 categories must be present.
- `&` is always escaped as `\&`.
- **Concepts row: hard limit of 6 items max.**
- Never add skills not provided by point-repointing output.

---

## Section 4: Professional Experience

**Section heading:** same pattern.

### Single role at a company:

```latex
\vspace{3mm}

{\large \noindent \textbf{Job Title $\mid$ Company Name}} \hfill \textbf{Mon YYYY – Mon YYYY}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <bullet 1>

\item <bullet 2>
\end{itemize}
}
```

**Combine title and company into ONE line:** `Title $\mid$ Company`. If the version file has them on separate lines, the assembler MUST combine them.

### Multiple roles at same company (stacked format):

```latex
\vspace{3mm}

{\large \noindent \textbf{Company Name}} \hfill \textbf{Earliest YYYY – Present}

\noindent \textbf{Most Recent Role} \hfill \textbf{Mon YYYY – Present}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <bullets for most recent role>
\end{itemize}
}

\vspace{2mm}

\noindent \textbf{Earlier Role} \hfill \textbf{Mon YYYY – Mon YYYY}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <bullets for earlier role>
\end{itemize}
}
```

**Spacing rules for stacked format:**
- **Blank line** between company header and role title
- **Blank line** between role title and `{\small` block
- `\vspace{2mm}` between roles within the same company
- `\vspace{3mm}` between **companies** (before next company's `{\large}` header)

**Rules:**
- Roles in **reverse chronological order** (most recent first).
- **Both roles always appear** regardless of JD — never drop a prior role.
- Number of bullets per role comes from point-repointing output — do not add or remove.
- No `\vspace{1mm}` between role title line and itemize block — the itemize follows directly.

---

## Section 5: Projects

**Section heading:** same pattern.

Only the 3 selected projects. Everything else is NOT included (no commented-out projects).

### Personal project:

```latex
\vspace{2mm}

{\large \noindent \textbf{Project Name} $\mid$ \textit{Tech1, Tech2, Tech3} $\mid$ \href{<GITHUB_PROFILE_URL>}{\textcolor{blue}{Link}}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <bullet 1>

\item <bullet 2>
\end{itemize}
}
```

### Open source contribution:

```latex
\vspace{2mm}

{\large \noindent \textbf{Project Name} $\mid$ \textit{Open Source Contribution} $\mid$ \textit{Tech1, Tech2, Tech3} $\mid$ \href{<GITHUB_PROFILE_URL>}{\textcolor{blue}{Link}}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <bullet 1>

\item <bullet 2>
\end{itemize}
}
```

**Rules:**
- Project name always `\textbf{}`. Tech stack always `\textit{}`.
- Separators: ` $\mid$ ` with spaces.
- **Project link is always** `\href{<GITHUB_PROFILE_URL>}{\textcolor{blue}{Link}}` — the GitHub profile, never individual project URLs.
- Always use `Link` as display text — never show the raw URL.
- `itemsep=1mm` for projects (not 1.5mm).
- `\vspace{2mm}` between entries. First project does NOT have a leading `\vspace{2mm}`.
- **Project title must match raw.md `#` heading exactly.** If raw.md has `# <OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>)`, LaTeX must show `\textbf{<OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>)}` — never simplify.
- Check `project_type` from project-selection output to pick correct format (personal vs open_source). Never guess.
- `\textit{Open Source Contribution}` always between project name and tech stack for OSS.

---

## Bolding Rules

**Bold these:**
- Technologies, tools, frameworks: `\textbf{Python}`, `\textbf{Redis}`, `\textbf{FastAPI}`
- Specific system/pattern names: `\textbf{inference routing engine}`, `\textbf{multi-agent AI system}`
- Quantified outcomes: `\textbf{35\%}`, `\textbf{100K+ records/day}`, `\textbf{220ms latency}`
- Key JD-signal phrases: `\textbf{production-grade}`, `\textbf{scalable multi-agent orchestration}`
- Each bullet should have **at least 2 bold terms**

**Do NOT bold:**
- Verbs: "Architected", "Built", "Developed"
- Filler/connective words: "using", "for", "and", "while"
- The entire bullet
- Non-technical emphasis

**Special characters in LaTeX:**
- `%` → always `\%` (bare `%` starts a comment)
- `&` → always `\&`

---

## Spacing Rules

| Location | Command |
|---|---|
| Before every section heading | `\vspace{3mm}` |
| Between heading text and rule line | `\vspace{-8pt}` (inline) |
| Between education entries | `\vspace{1.5mm}` surrounded by BLANK LINES on both sides |
| Between last education entry and TECHNICAL SKILLS | BLANK LINE + `\vspace{3mm}` + BLANK LINE |
| Between experience **companies** | `\vspace{3mm}` (before next company's `{\large}` header) |
| Between **roles within same company** | `\vspace{2mm}` (between end of one role's itemize and next role title) |
| Between company header and role title | **Blank line required** |
| Between role title and `{\small}` block | **Blank line required** |
| Between project entries | `\vspace{2mm}` |
| Between project title and bullet list | **None** — itemize follows directly |
| Bullet items (experience) | `itemsep=1mm` |
| Bullet items (projects) | `itemsep=1mm` |

---

## Agent Assembly Workflow

1. Load tailored points from point-repointing output.
2. **Fill header** — static contact details. Never changes.
3. **Fill Education** — copy as-is. Never modify.
4. **Fill Technical Skills** — use `technical_skills_update` verbatim. All 5 categories, max 6 in Concepts.
5. **Fill Professional Experience** — slot re-pointed bullets per role, most recent first.
   - Single role: combine title + company into ONE line: `Title $\mid$ Company`
   - Multiple roles: stacked format with blank lines between elements
   - Apply bolding rules to bullets
6. **Fill Projects** — 3 selected projects. Check `project_type` for format. Apply bolding rules.
7. **Verify:** every `%` → `\%`, every `&` → `\&`, all environments closed, `\end{document}` is last line.
8. **Save** — write .tex file via Python raw string script (Method A below). NEVER construct .tex inline in write_file arguments.

### Method A (preferred, MANDATORY for cron runs):

Write a Python script that generates the .tex file:

```python
content = r"""\documentclass{article}
\usepackage[top=0.2in, bottom=0.2in, left=0.3in, right=0.3in]{geometry}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{xcolor}
...
\end{document}
"""
with open("/path/to/output.tex", "w") as f:
    f.write(content)
```

Then run: `python3 /path/to/script.py`

The `r"""..."""` raw string prefix ensures backslashes are written as-is.

9. **VERIFY — read the file back. MANDATORY:**
   - **Line 1 is `\documentclass{article}`** — NOT a comment. If line 1 starts with `%`, remove all lines before `\documentclass` immediately.
   - `\documentclass{article}` appears (NOT `\\documentclass{article}`)
   - `\textbf{...}` appears (NOT `\\textbf{...}`)
   - `\item` appears (NOT `\\item`)
   - If ANY double backslashes found → replace all `\\` with `\` throughout, then re-verify.
   - **No metadata comment headers** — file starts with `\documentclass{article}`. No `% Company — Job Title` before it.

---

## Agent Behavior Rules

- **Structure is fixed.** Fill content; don't redesign.
- **Never remove a section.** If no content (shouldn't happen), leave heading + empty itemize.
- **Never invent bullets.** Only bullets from point-repointing output go in.
- **Bolding is applied at assembly.** Point-repointing output has plain text — agent applies `\textbf{}` during assembly.
- **Do NOT include commented-out non-selected projects.** Only 3 selected projects appear.
- **File must compile.** Check environments, special characters, `\end{document}`.
- **NEVER invent metadata.** Company names, dates, job titles MUST come from raw.md — never guess or fabricate.
- **Accuracy on first try.** Zero-defect output on critical steps. Follow every trap and verification step without exception.

---

## Traps to Avoid

1. **Bare `%` in bullet content.** Always `\%`.
2. **Bare `&` in content.** Always `\&`.
3. **Using `itemsep=1.5mm` for project bullets.** Projects use `1mm`.
4. **Bolding action verbs.** Never bold "Architected", "Built", "Designed".
5. **Missing `\vspace{3mm}` before section headings.** Every section needs it.
6. **Missing `\vspace{-8pt}` on section headings.** Creates too much gap.
7. **Reordering sections.** Order is fixed: Header → Education → Skills → Experience → Projects.
8. **Writing new bullets at assembly time.** This step slots in only — no authoring.
9. **Omitting `\textit{Open Source Contribution}` from OSS title lines.** Always check `project_type`.
10. **Splitting multi-role companies into separate entries.** Use stacked format — never repeat company name.
11. **Dropping a prior role at the same company.** Both roles always appear.
12. **Using `patch` on files containing LaTeX backslashes.** Patch may double backslashes. Always use `write_file` for .tex files.
13. **Hallucinated metadata.** All metadata MUST come from raw.md — never invent dates, names, or labels.
14. **Missing blank lines in stacked format.** Company header → blank → role title → blank → `{\small`. Without them, LaTeX merges paragraphs.
15. **Adding unprovable skills to Concepts row.** Max 6 items, all from point-repointing output.
16. **Stripping project title subtitles.** Match raw.md `#` heading exactly.
17. **Em dashes in bullet text.** Replace with commas during assembly if point-repointing missed any.
18. **Writing .tex via shell heredoc or echo in cron mode.** Use Python raw string script instead.
19. **Single-role company format — title and company on separate lines.** Combine into one line: `Title $\mid$ Company`.
20. **Double-backslash verification — ALWAYS check.** After writing, read back and verify single backslashes throughout.
21. **No metadata comment headers.** Line 1 MUST be `\documentclass{article}`. No `%` comments before it.
22. **Bullet length consistency — ALL bullets 230-320 chars (target 250-300).** Measure every bullet after assembly. All sections must be consistent.

---

## Closing Principle

> **Assembly is the last line of defense.** The points are final. The structure is fixed. Your job is to slot everything in correctly, verify it compiles, and push a zero-defect .tex file.

**References:**
- `references/full-latex-template.md` — Complete LaTeX template with all sections
- `references/multi-role-work-experience.md` — Stacked multi-role format with spacing rules
- `references/education-spacing.md` — Education entry spacing with examples
- `references/oss-links.md` — OSS link and title format rules
- `references/bullet-length-consistency.md` — Bullet length measurement and normalization
- `references/double-backslash-debugging.md` — Double backslash detection and fix patterns
- `references/latex-metadata-header-bug.md` — Metadata header bug description and fix



