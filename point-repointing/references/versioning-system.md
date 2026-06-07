# Folder-Based Versioning System

Every project, OSS contribution, and work-experience role lives in its own folder under:

```
POOL_DIR = /opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>
```

## Folder Structure

```
POOL_DIR/<type>/<item-slug>/
├── raw.md                        ← permanent context, read-only
├── idx.md                        ← index of all versions, metadata only
└── versions/
    ├── v1-<jd-slug>.md           ← points written for one specific JD
    ├── v2-<jd-slug>.md
    └── v3-<jd-slug>.md
```

Where `<type>` is one of: `projects/`, `oss/`, `work-experience/`.

## Read Principle

**Always read `raw.md` for content.** Raw is the permanent, complete source of truth. Never rely on prior version files for content — they may contain errors, role bleed, or content from a different JD targeting.

**Read once, process all sections.** Load all files at the START of the re-pointing step. Build aim lists for all sections from the single loaded context. Then process all sections. Do NOT re-read raw.md per section.

**Read scope:** For multi-role raw files (containing `## Role 1:`, `## Role 2:`, etc.), read **only the role block matching the target role_phase**. Stop reading after that role block ends.

**Read sequence (ONCE at start):**
1. `idx.md` — for every section being re-pointed. Small, metadata only. Used for version tracking, **never as a content source**.
2. `raw.md` — for every section. Read only the relevant role/project block. Every bullet must be derived from raw.md.
3. One prior version file per section — **optional**, read only for style/formatting reference. Never copy content from it verbatim.

## Write Rule

Creates one new file and updates one existing file per run per item:
- Creates `versions/v<N+1>-<jd-slug>.md` with the final re-pointed points
- Appends one new entry to `idx.md` and updates `current_version`

**Never edits `raw.md`. Never edits prior version files. Every version is permanent after creation.**

## Why This Design

A growing single file works for 3–4 versions. By version 15, it is 500+ lines — the agent loads mostly noise. The folder system keeps context clean: the index is always small, each version file contains only one JD's points. The agent's context load per item is always `idx.md` plus one file — regardless of how many JDs have been run.

## idx.md Format

```text
## Version N
date: YYYY-MM-DD
target_jd: <Company Title>
jd_slug: <slug>
current_version: N
role_phase: <role name or "default">
requirements_targeted: <comma-separated list>
```

**Preserve existing structure when appending.** Only add new version entries — never edit prior entries.

