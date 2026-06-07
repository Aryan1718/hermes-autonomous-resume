# Pool Intake — Two-File Merge Pattern

## When user uploads a main file + `_v1` file

The user frequently sends pairs:
- **Main file** (e.g. `projectname.md`) = source of truth. Contains all raw details. NEVER drop content from this file.
- **`_v1` file** (e.g. `projectname_v1.md`) = polished/portfolio-ready version. Use to enrich framing, but main file always takes precedence on facts, figures, sections, and details.

## Merge procedure

1. Use the main file as the base — every section, bullet, and detail from it must appear in `raw.md`
2. Pull improved phrasing and additional structure from the `_v1` file where it adds value
3. If content conflicts, the **main file wins**
4. Key sections most at risk of accidental loss during merge: `Differentiators`, `Impact / Outcomes`, `Key Decisions`, Architecture details, and any bulleted lists — verify all are preserved
5. The v1 file often has better: Project Summary framing, Architecture section descriptions, Deep Dive areas, cleaner differentiators

## Transformed output format

After merging, transform the content into the proper raw.md schema with `## Context`, `## Technical Scope`, `## Implementation`, `## Architecture / Flow`, `## Key Decisions`, `## Differentiators`, `## Impact / Outcomes`, `## Repository` sections.

## Slug conflict check

Before creating any folder, check whether `pool/<type-folder>/<slug>/` already exists. If it does and has version files, this slug is active — stop and report a conflict.
