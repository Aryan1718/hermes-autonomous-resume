# OSS Project Link Reference

## <OSS_PROJECT_NAME>
- **Title**: `<OSS_PROJECT_NAME> (<ACCELERATOR_COHORT>)` — note: <ACCELERATOR_COHORT>, not P25
- **Repo URL**: `<GITHUB_REPO_URL>`
- **Display**: When selected, show as 4th part of title line: `\href{<GITHUB_REPO_URL>}{\textcolor{blue}{Link}}`

## General Rule
- Open source contributions with a `repo_url` field in `raw.md` should display a link in the LaTeX title line
- Format: `\textbf{Name} $\mid$ \textit{Open Source Contribution} $\mid$ \textit{Tech} $\mid$ \href{url}{\textcolor{blue}{Link}}`
- If no `repo_url` is present, omit the 4th part


