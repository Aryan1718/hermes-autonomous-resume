# Batch Python Script Template — What Actually Worked

This documents the batch processing pattern that successfully processed 15+ JDs per run.

## Key Gotchas

1. **HOME directory**: Use `HOME=/opt/data/profiles/<PROFILE_SLUG> python3 script.py` or `cd /opt/data/profiles/<PROFILE_SLUG> && python3 script.py`
2. **f-string limitations**: Complex LaTeX in Python f-strings causes syntax errors. Build LaTeX with list concatenation (`L.append()`, `"\n".join(L)`) instead of f-strings.
3. **--- in bullets**: The LaTeX em-dash `---` triggers "Error parsing YAML" in some contexts. Use `--` or rephrase.
4. **idx.md conflicts**: idx.md files may be written by sibling subagents during batch processing. Use `write_file` (not patch) for idx.md.
5. **Version file naming**: Use `{jd-slug}.md` format. Keep it short and unique per JD.
6. **LaTeX special chars in Python strings**: Escape backslashes properly. Use raw strings `r"..."` for LaTeX commands.
7. **Variable ordering in scripts**: Python evaluates f-strings in list literals at definition time. Define `COMPANY`, `DATE`, and all f-string variables BEFORE any list that interpolates them. Defining them after the list (e.g. `idx_entries = [...]` before `COMPANY = "<TARGET_COMPANY>"`) causes NameError.

## Performance

- 15 JDs processed in ~45 minutes (first run with learning overhead)
- Mechanical steps: ~2 minutes per JD after batching
- Target for subsequent runs: <20 minutes for 15-20 JDs (mechanical only)


