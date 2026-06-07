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

\large \textbf{ARYAN PANDIT} \\
Fullerton, CA $\mid$ +1-714-519-7675 $\mid$
\href{mailto:<CANDIDATE_EMAIL>}{<CANDIDATE_EMAIL>} $\mid$
\href{<LINKEDIN_URL>}{\textcolor{blue}{LinkedIn}} $\mid$
\href{<GITHUB_PROFILE_URL>}{\textcolor{blue}{GitHub}}
\end{center}

%--- EDUCATION ---
\vspace{3mm}
\noindent \textbf{EDUCATION} \vspace{-8pt} \\
\rule{\linewidth}{0.5pt}

\noindent \textbf{California State University, Fullerton} \hfill \textbf{Aug 2024 – May 2026} \\
\textit{Master of Science in Computer Science}

\vspace{1.5mm}

\noindent \textbf{Institute of Computer Technology} \hfill \textbf{Jul 2019 – Jun 2023} \\
\textit{B.Tech in Computer Science Engineering}

\vspace{3mm}

%--- TECHNICAL SKILLS ---
\noindent \textbf{TECHNICAL SKILLS} \vspace{-8pt} \\
\rule{\linewidth}{0.5pt}

\noindent \textbf{Languages:} Python, TypeScript, JavaScript, Java, C++ \\
\textbf{Frameworks:} React, Next.js, FastAPI, Flask, Node.js, LangGraph, CrewAI \\
\textbf{Databases:} PostgreSQL, Redis, MongoDB, DynamoDB \\
\textbf{Cloud \& Tools:} AWS, Docker, Docker Compose, GitHub Actions, CI/CD, Ollama, VLLM \\
\textbf{Concepts:} API Design, Distributed Systems, Multi-Agent Orchestration, RAG, LLM Inference, Observability

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

% Multi-role stacked example (<WORK_EXPERIENCE_COMPANY_1>):
\vspace{3mm}

{\large \noindent \textbf{<WORK_EXPERIENCE_COMPANY_1>}} \hfill \textbf{Jan 2026 – Present}

\noindent \textbf{<ROLE_TITLE_2>} \hfill \textbf{May 2026 – Present}

{\small
\begin{itemize}[noitemsep, nolistsep, leftmargin=*, itemsep=1mm]
\item <tailored bullet 1>

\item <tailored bullet 2>
\end{itemize}
}

\vspace{2mm}

\noindent \textbf{<ROLE_TITLE_1>} \hfill \textbf{Jan 2026 – Apr 2026}

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

- Header contact details are STATIC — never change across resumes
- Education is STATIC — same entries on every resume
- Technical Skills changes per JD (from `technical_skills_update`)
- Professional Experience bullets change per JD (from point-repointing)
- Projects change per JD (3 selected projects from project-selection)
- Always verify: single backslashes, line 1 = `\documentclass{article}`, no metadata headers

