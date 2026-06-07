# Candidate Profile Update Protocol

## When to Update

Update the candidate profile whenever any of the following changes:

- current role or role history
- location scope
- work authorization
- target seniority
- target role families
- provable skills or strongest signals
- hard disqualifiers
- compensation constraints, if used

## Major Overhaul Protocol

1. **Re-read all pool `raw.md` files** before editing. Do not carry forward facts from an older profile if the pool evidence no longer supports them.
2. **Collect clarifications in one batch** after reading. Ask only for missing or ambiguous facts.
3. **Cross-check dates and constraints** against what the current candidate actually said. Do not inherit geography, authorization, or seniority assumptions from a previous user.
4. **After writing the profile, scan generated resumes** in `home/<RESUMES_DIR>/` for stale facts if historical outputs are meant to stay aligned.
5. **Update any persistent memory or notes** your environment uses so stale profile facts do not keep resurfacing.

## Bulk Refresh Protocol

When the user asks to refresh or overhaul the profile:

1. **Read all source data first.** Load every relevant `raw.md` from `workspace/pool/`.
2. **Identify stale or missing profile fields.** Focus on facts that affect filtering, ranking, or tailoring.
3. **Confirm the intended changes.** Summarize what will change before writing if the update is broad or risky.
4. **Execute edits in one pass.** Keep the profile internally consistent.
5. **Update the change log.** Append one entry covering what changed and why.

## Reusability Check

Before considering the profile update complete, verify that:

- no stale facts from a previous candidate remain
- examples are either generic templates or truly belong to the current candidate
- downstream skills will not inherit another person's seniority, geography, or authorization rules
