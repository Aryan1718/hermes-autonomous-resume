# Batch Write-Back Script

## Pattern: Write ALL version files + update ALL idx.md in ONE execute_code call

After re-pointing all sections, collect all version content and idx.md appends, then write everything in a single Python script via execute_code.

```python
import os

POOL_DIR = "/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>"
JD_SLUG = "<jd-slug>"  # e.g., "jane-street-software-engineer"
DATE = "<YYYY-MM-DD>"

# --- VERSION FILES ---
# Determine version number: count existing version files + 1
sections = [
    # (relative_folder, content)
    ("work-experience/<work-company-slug>",
     f"# v{N} — {JD_SLUG}\n\n<CURRENT_ROLE_DATE_RANGE> | <ROLE_TITLE_1>\n\n<why_now>\n\n- <bullet 1>\n- <bullet 2>\n- <bullet 3>"),
    ("work-experience/alps-web-solutions",
     f"# v{N} — {JD_SLUG}\n\nDec 2023 – Jun 2024 | Software Developer\n\n<why_now>\n\n- <bullet 1>\n- <bullet 2>"),
    # ... add all 7 sections here
]

for folder, content in sections:
    ver = len(os.listdir(os.path.join(POOL_DIR, folder, "versions"))) + 1
    path = os.path.join(POOL_DIR, folder, "versions", f"v{ver}-{JD_SLUG}.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content.format(N=ver))
    print(f"WROTE: {path}")

# --- IDX.MD UPDATES ---
import re

idx_updates = [
    ("work-experience/<work-company-slug>",
     f"### v{N} — {JD_SLUG}\n{DATE} | <company_name>\nfile: versions/v{N}-{JD_SLUG}.md\n"),
    # ... add all idx updates
]

for folder, entry in idx_updates:
    path = os.path.join(POOL_DIR, folder, "idx.md")
    with open(path, "r") as f:
        content = f.read()
    # Find the last version entry and insert after it
    lines = content.split("\n")
    last_ver_idx = None
    for i, line in enumerate(lines):
        if line.startswith("### v"):
            last_ver_idx = i
    if last_ver_idx is not None:
        # Find blank line after this version block
        for j in range(last_ver_idx + 1, len(lines)):
            if lines[j].strip() == "":
                lines.insert(j + 1, entry)
                break
    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(f"UPDATED: {path}")
```

## Key Points
- **ONE tool call** for all writes (version files + idx.md updates)
- **Version number**: `len(os.listdir("versions/")) + 1` — no need to read idx.md
- **idx.md update**: append entry after last `### vN` block — no full file rewrite needed
- **Do NOT write one at a time** — each write_file call adds to context and slows the run


