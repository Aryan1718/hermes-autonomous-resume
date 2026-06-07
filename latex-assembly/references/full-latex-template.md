# Full LaTeX Template

Complete LaTeX template with all sections. Use this as the structural reference when assembling resumes.

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

\large \textbf{<CANDIDATE_NAME>} \\
<CITY>, <STATE> $\mid$ <PHONE_NUMBER> $\mid$
\href{mailto:<CANDIDATE_EMAIL>}{<CANDIDATE_EMAIL>} $\mid$
\href{<LINKEDIN_URL>}{\textcolor{blue}{LinkedIn}} $\mid$
\href{<GITHUB_PROFILE_URL>}{\textcolor{blue}{GitHub}}
\end{center}

%--- EDUCATION ---
\vspace{3mm}
\noindent \textbf{EDUCATION} \vspace{-8pt} \\
\rule{\linewidth}{0.5pt}

\noindent \textbf{<INSTITUTION_NAME_1>} \hfill \textbf{<DATE_RANGE_1>} \\
\textit{<DEGREE_1>}

\vspace{1.5mm}

\noindent \textbf{<INSTITUTION_NAME_2>} \hfill \textbf{<DATE_RANGE_2>} \\
\textit{<DEGREE_2>}

\vspace{3mm}

%--- TECHNICAL SKILLS ---
\noindent \textbf{TECHNICAL SKILLS} \vspace{-8pt} \\
\rule{\linewidth}{0.5pt}

\noindent \textbf{Languages:} <LANGUAGE_1>, <LANGUAGE_2>, <LANGUAGE_3> \\
\textbf{Frameworks:} <FRAMEWORK_1>, <FRAMEWORK_2>, <FRAMEWORK_3> \\
\textbf{Databases:} <DATABASE_1>, <DATABASE_2>, <DATABASE_3> \\
\textbf{Cloud \& Tools:} <TOOL_1>, <TOOL_2>, <TOOL_3> \\
\textbf{Concepts:} <CONCEPT_1>, <CONCEPT_2>, <CONCEPT_3>, <CONCEPT_4>, <CONCEPT_5>, <CONCEPT_6>

%--- PROFESSIONAL EXPERIENCE ---
\vspace{3mm}
\noindent \textbf{PROFESSIONAL EXPERIENCE} \vspace{-8pt} \\
\rule{\linewidth}{0.5pt}

% Single role example:
\vspace{3mm}

{\large \noindent \textbf{Job Title $\mid$ Company Name}} \hfill \textbf{Mon YYYY – Mon YYYY}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <tailored bullet 1>

\item <tailored bullet 2>
\end{itemize}
}

% Multi-role stacked example (<COMPANY_NAME>):
\vspace{3mm}

{\large \noindent \textbf{<COMPANY_NAME>}} \hfill \textbf{<OVERALL_DATE_RANGE>}

\noindent \textbf{<MOST_RECENT_ROLE_TITLE>} \hfill \textbf{<MOST_RECENT_ROLE_DATE_RANGE>}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <tailored bullet 1>

\item <tailored bullet 2>
\end{itemize}
}

\vspace{2mm}

\noindent \textbf{<EARLIER_ROLE_TITLE>} \hfill \textbf{<EARLIER_ROLE_DATE_RANGE>}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <tailored bullet 1>

\item <tailored bullet 2>

\item <tailored bullet 3>
\end{itemize}
}

%--- PROJECTS ---
\vspace{3mm}
\noindent \textbf{PROJECTS} \vspace{-8pt} \\
\rule{\linewidth}{0.5pt}

% Personal project:
\vspace{2mm}

{\large \noindent \textbf{Project Name} $\mid$ \textit{Tech1, Tech2, Tech3} $\mid$ \href{<GITHUB_PROFILE_URL>}{\textcolor{blue}{Link}}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <tailored bullet 1>

\item <tailored bullet 2>
\end{itemize}
}

% Open source contribution:
\vspace{2mm}

{\large \noindent \textbf{Project Name} $\mid$ \textit{Open Source Contribution} $\mid$ \textit{Tech1, Tech2, Tech3} $\mid$ \href{<GITHUB_PROFILE_URL>}{\textcolor{blue}{Link}}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <tailored bullet 1>

\item <tailored bullet 2>
\end{itemize}
}

\end{document}
```

## Template Rules

- Header contact details are STATIC for the current candidate — never change across that candidate's resumes
- Education is STATIC for the current candidate — same entries on every resume
- Technical Skills changes per JD (from `technical_skills_update`)
- Professional Experience bullets change per JD (from point-repointing)
- Projects change per JD (3 selected projects from project-selection)
- Always verify: single backslashes, line 1 = `\documentclass{article}`, no metadata headers


