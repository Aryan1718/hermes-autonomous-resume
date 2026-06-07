# Multi-Role Raw File Convention

## When to Use This Pattern

When a candidate holds **sequential roles at the same company** (e.g., <ROLE_TITLE_1> → <ROLE_TITLE_2>), the raw.md must use the multi-role block format below. A single merged section causes content to leak across roles during re-pointing.

## File Structure

```markdown
# Company Name — Two Sequential Roles

Brief note explaining these are sequential roles. During point-repointing, read ONLY the role block matching the target role_phase.

---

## Role 1: [Title] (Date Range)

### Role Identity
- title: [exact title]
- company: [company name]
- dates: [start] – [end]

### What Was Done
[Content for this role ONLY. Never include work from the other role.]

### Ownership Scope (this role only)
[Systems, features, responsibilities owned in THIS role only]

### Technical Scope (this role only)
skills: [technologies used in this role]
domain: [domain]

### Available Metrics (this role only)
[Numbers, counts, scale — verifiable in this role only]

### What This Role Can Honestly Prove
- Strong proof of: [skills/areas this role genuinely demonstrates]
- Weak proof of: [skills mentioned but not central]
- Cannot prove: [skills this role does NOT demonstrate]

---

## Role 2: [Title] (Date Range)

### Role Identity
[Same structure as Role 1]

### What Was Done
[Content for this role ONLY.]

[... remaining sections same as Role 1 ...]
```

## Rules

1. **Each role block is self-contained.** Every section (What Was Done, Ownership, Technical Scope, Metrics, Honest Proof) must contain ONLY content from that role's time period.
2. **Never merge content across roles.** If a system (e.g., multi-agent orchestration) existed in both roles, each role's description should focus on what was *distinctive* to that phase.
3. **Separate honest proof per role.** Role 1 might prove "blueprint architecture" while Role 2 proves "<TARGET_DOMAIN> domain." Don't claim both for both.
4. **During re-pointing:** the agent reads ONLY the role block matching `role_phase`. It stops reading after that block ends.

## Real-World Example

See `/opt/data/profiles/<PROFILE_SLUG>/workspace/<POOL_DIR>/work-experience/<work-company-slug>/raw.md` — <WORK_EXPERIENCE_COMPANY_1> with <ROLE_TITLE_1> (<DATE_RANGE_1>) and <ROLE_TITLE_2> (<DATE_RANGE_2>) as two separate role blocks.

## Why This Matters

When both roles were merged in a single raw.md, re-pointing for Role 2 would load Role 1's content too, causing:
- <OSS_PROJECT_NAME> OSS bullets appearing in <WORK_EXPERIENCE_COMPANY_1> versions
- RBAC/ABAC work claimed by both roles indistinguishably
- Inability to differentiate what each role actually proved

The block format makes cross-role contamination structurally impossible.



