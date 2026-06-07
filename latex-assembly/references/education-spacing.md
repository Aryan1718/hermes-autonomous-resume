# Education Spacing — Detailed Rules

## The Problem

Without proper blank lines between education entries, LaTeX merges them into the same paragraph. Dates overlap with the next institution name. The rendered PDF looks squished.

## The Fix

Every education entry must be separated by:
1. A blank line (paragraph break in LaTeX)
2. A `\vspace{1.5mm}` command
3. Another blank line

## Correct Format

```latex
\noindent \textbf{<INSTITUTION_NAME_1>} \hfill \textbf{<DATE_RANGE_1>} \\
\textit{<DEGREE_1>}

\vspace{1.5mm}

\noindent \textbf{<INSTITUTION_NAME_2>} \hfill \textbf{<DATE_RANGE_2>} \\
\textit{<DEGREE_2>}
```

Note: blank line above `\vspace{1.5mm}`, blank line below it.

## After Last Education Entry

Add BLANK LINE + `\vspace{3mm}` + BLANK LINE before the TECHNICAL SKILLS section heading:

```latex
\textit{<DEGREE_2>}

\vspace{3mm}

\noindent \textbf{TECHNICAL SKILLS} \vspace{-8pt} \\
\rule{\linewidth}{0.5pt}
```

## Education is Never Modified

Education is static for the current candidate. Keep the same entries, dates, and formatting across that candidate's resumes.
- <INSTITUTION_NAME_1> | <DATE_RANGE_1> | MS in CS
- <INSTITUTION_NAME_2> | <DATE_RANGE_2> | B.Tech in CSE

