# Agent Behavior Rules - JD Pre-Filter

Detailed behavioral rules for each phase of the pre-filter step.

## General Rules

- **Load the profile once per batch.** Do not re-read it per JD. It is the same for all JDs in that batch.
- **Phase 1 before Phase 2 before Phase 3.** Never score a JD that failed a disqualifier or a binary check. The order is a filter funnel, not a checklist.
- **Disqualification reasons must be specific.** Cite the exact JD language and the exact profile rule that fired.
- **Scoring traces to the profile.** Every score needs evidence from both the JD and the relevant `candidate-profile` section.
- **Never adjust the profile during pre-filtering.** If a JD reveals that the profile has a gap or wrong assumption, note it in the output. Do not silently update the profile mid-run.
- **Do not run the full pipeline on a disqualified or failed-binary JD.** Even if it looks interesting.
- **Do not operate on placeholder profiles.** If `candidate-profile` still contains setup placeholders or obvious template text, stop and ask the user to complete setup first.

## Phase 1 Rules

- Read the `Hard Disqualifiers` section of `candidate-profile`. Check each JD against every disqualifier.
- If any single disqualifier fires, the JD is immediately dropped. Do not score it. Do not continue to Phase 2. Log the exact reason.
- For location: compare the JD's location against the candidate's actual `Location` scope. Explicitly out of scope with no acceptable remote option = disqualify. Silent or ambiguous = pass unless the profile says otherwise.
- For work authorization: compare the JD's explicit authorization restrictions against the candidate's `Work Authorization` section. Ambiguous = pass. Explicit incompatibility = disqualify.
- For experience: compare the JD's explicit minimums against the candidate's `Seniority` section. Preferred experience does not disqualify. Required experience that materially exceeds the candidate's supportable range does.
- For role family: compare title plus scope against `Target Roles` and `Role types that do NOT match`. Use the actual responsibilities, not just the title string.
- For candidate-specific constraints: apply any additional profile constraints exactly as written. Do not invent new ones.

## Phase 2 Rules

- All three questions must be YES to pass. A single NO disqualifies the JD. Log which question failed.
- Q1 (role type): Check the `Target Roles` section of `candidate-profile`. When ambiguous, if the title is unusual but the description clearly matches the candidate's target work, answer YES.
- Q2 (seniority): Use the `Seniority` section of `candidate-profile`. Unspecified seniority = YES. Reasonable stretch roles = YES if the profile allows them. Materially more senior than the profile supports = NO.
- Q3 (provable must-haves): Count only `Always Provable` items. `Provable with Framing` items do not count toward the threshold of two.

## Phase 3 Rules

- Count every JD must-have or required skill that appears in the `Always Provable` tier of `candidate-profile`.
- For Career Direction Fit: check the ordered `Career Direction` section of `candidate-profile`. Reward earlier fits more heavily. Use the highest matching fit when multiple apply.
- For Strongest Signal Match: check the `Strongest Signals` section of `candidate-profile`. A signal matches when the JD directly names the concept or clearly requires the same kind of work, not when it merely overlaps by domain.
- For Preferred Signal Count: check the `Preferred Signals` section of `candidate-profile`. Count how many appear in the JD. Each one is worth 1 point, capped at 10.

## Phase 4 Rules

- Sort all scored JDs by total score, highest first. Keep the ranking for visibility and auditability.
- Handoff is threshold-based in the current orchestrator contract:
  - `score >= 40` -> `RUN FULL PIPELINE`
  - `score < 40` -> `SKIPPED`
- Disqualified and failed-binary JDs are always `SKIPPED` regardless of numeric score.
- Tie-breaking: Higher Career Direction Fit -> Higher Strongest Signal Match -> Higher Provable Coverage -> More Preferred Signals.
- Never call the downstream pipeline for a skipped JD. It stays unprocessed so it can be re-evaluated after a profile update.

## Log Format

**Skipped JDs:**
```json
{ "job_description_id": "{jd_id}", "status": "skipped", "message": "{company_name}: pre-filter {result}. Reason: {reason}. Score: {score}." }
```

**Profile notes:** If any JD revealed a gap or wrong assumption in `candidate-profile`, record it as a note for the candidate to review and update manually. The agent never edits the profile autonomously.
