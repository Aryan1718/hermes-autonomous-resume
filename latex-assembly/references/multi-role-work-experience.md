# Multi-Role Work Experience — LaTeX Format Reference

## When to Use the Stacked Format

Use the stacked multi-role format when a candidate held **multiple sequential roles at the same company**. Both roles always appear on the resume — never drop or hide the earlier role. The progression signals growth.

**Do NOT split roles at the same company into separate `Title | Company` entries.** That repeats the company name and looks like two unrelated entries.

## LaTeX Output Format

```latex
%--- PROFESSIONAL EXPERIENCE ---
\vspace{3mm}
\noindent \textbf{PROFESSIONAL EXPERIENCE} \vspace{-8pt} \\
\rule{\linewidth}{0.5pt}

% Multi-role company (stacked format):
\vspace{3mm}

{\large \noindent \textbf{Company Name}} \hfill \textbf{Earliest YYYY – Present}

\noindent \textbf{Most Recent Role Title} \hfill \textbf{Mon YYYY – Present}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <bullets for most recent role>
\end{itemize}
}

\vspace{2mm}

\noindent \textbf{Earlier Role Title} \hfill \textbf{Mon YYYY – Mon YYYY}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <bullets for earlier role>
\end{itemize}
}

% Single-role company (default format):
\vspace{3mm}

{\large \noindent \textbf{Job Title (Role) $\mid$ Company Name}} \hfill \textbf{Mon YYYY – Mon YYYY}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <bullets>
\end{itemize}
}
```

## Spacing Rules

| Location | Command |
|---|---|
| Between **companies** | `\vspace{3mm}` (before next company's `{\large ...}` header) |
| Between **roles within same company** | `\vspace{2mm}` (between end of one role's itemize and next role title) |
| Between role title and bullet list | **None** — itemize follows directly |
| Between company header and role title (stacked format) | **Blank line required** — LaTeX needs a paragraph break between the `{\large \noindent \textbf{Company}}` header and the `\noindent \textbf{Role Title}` line. Without the blank line, both lines render in the same paragraph, merging dates and titles. |
| Between role title and `{\small}` block (stacked format) | **Blank line required** — separate the role title line from the `{\small}` group starter with a blank line for proper LaTeX paragraph spacing. |
| Experience bullet items | `itemsep=1mm` |

## Real Example — <WORK_EXPERIENCE_COMPANY_1>

```latex
\vspace{3mm}

{\large \noindent \textbf{<WORK_EXPERIENCE_COMPANY_1>}} \hfill \textbf{Jan 2026 – Present}

\noindent \textbf{<ROLE_TITLE_2>} \hfill \textbf{May 2026 – Present}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item Built multi-agent workflow orchestration for a <TARGET_DOMAIN> product, enforcing role and attribute-based access control for cross-agent information sharing.
\item Rebuilt the <DOMAIN_TASK_1> generation agent, restructuring clinical information processing and structured output formatting.
\item Rebuilt the <DOMAIN_TASK_2> agent that maps clinical documentation to appropriate medical codes.
\item Resolved frontend bugs and improved reliability of the user-facing workflow interface.
\end{itemize}
}

\vspace{2mm}

\noindent \textbf{<ROLE_TITLE_1>} \hfill \textbf{Jan 2026 – Apr 2026}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item Managed the open-source Innovation Hub repository (15-blueprint AI platform), independently built 4 blueprints from scratch and maintained updates across the full set.
\item Built FinSights (finance document summarization) and Audify (document-to-podcast with configurable voices) from scratch using Python, FastAPI, and React.
\item Built <SYSTEM_NAME_1> (RBAC/ABAC authorization MCP service) and <SYSTEM_NAME_2> (multi-agent transport system) using CrewAI, LangGraph, and MCP.
\item Implemented multi-agent orchestration in LangGraph with planner, summarization, and analytical agents across department-scoped access rules.
\end{itemize}
}
```

## How the Pipeline Detects Multi-Role Entries

The `raw.md` for a multi-role company has sub-roles listed under `dates`:

```markdown
dates: Jan 2026 – Present
  - <ROLE_TITLE_1>: Jan 2026 – Apr 2026
  - <ROLE_TITLE_2>: May 2026 – Present
```

The `Everything That Was Done` section has sub-sections for each role phase. The LaTeX assembler reads this structure and generates the stacked format automatically.

## Key Rules

1. **Both roles always appear** — never drop the earlier role, regardless of JD
2. **Company name appears once** as the `\large` header
3. **Each role gets its own** `\noindent \textbf{Role Title}` line with dates and bullet block
4. **Reverse chronological order** — most recent role first
5. **Never use** `\textbf{Title $\mid$ Company}` for each role separately — that's the single-role format
6. **No `\vspace{1mm}`** between role title and itemize — it follows directly


