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
\noindent \textbf{California State University, Fullerton} \hfill \textbf{Aug 2024 – May 2026} \\
\textit{Master of Science in Computer Science}

\vspace{1.5mm}

\noindent \textbf{Institute of Computer Technology} \hfill \textbf{Jul 2019 – Jun 2023} \\
\textit{B.Tech in Computer Science Engineering}
```

Note: blank line above `\vspace{1.5mm}`, blank line below it.

## After Last Education Entry

Add BLANK LINE + `\vspace{3mm}` + BLANK LINE before the TECHNICAL SKILLS section heading:

```latex
\textit{B.Tech in Computer Science Engineering}

\vspace{3mm}

\noindent \textbf{TECHNICAL SKILLS} \vspace{-8pt} \\
\rule{\linewidth}{0.5pt}
```

## Education is Never Modified

Same 2 entries, same dates, same formatting on every resume. Copy as-is.
- California State University, Fullerton | Aug 2024 – May 2026 | MS in CS
- Institute of Computer Technology | Jul 2019 – Jun 2023 | B.Tech in CSE
