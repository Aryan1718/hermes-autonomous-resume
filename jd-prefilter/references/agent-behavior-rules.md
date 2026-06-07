# Agent Behavior Rules — JD Pre-Filter

Detailed behavioral rules for each phase of the pre-filter step.

## General Rules

- **Load the profile once per batch.** Do not re-read it per JD — it is the same for all JDs in the batch.
- **Phase 1 before Phase 2 before Phase 3.** Never score a JD that failed a disqualifier or a binary check. The order is a filter funnel, not a checklist.
- **Disqualification reasons must be specific.** "Failed sponsorship check — JD says 'must be authorized to work in the US permanently, no sponsorship'" not "failed sponsorship check."
- **Scoring traces to the profile.** Every score has evidence. "Career Direction Fit: 30 — JD mentions LangGraph and multi-agent orchestration, matches Fit 1 directly" not just "30."
- **Never adjust the profile during pre-filtering.** If a JD reveals that the profile has a gap or wrong assumption, note it in the output — do not silently update the profile mid-run. Profile updates happen explicitly, with a change log entry.
- **Do not run the full pipeline on a disqualified or failed-binary JD.** Even if it looks interesting. The filters exist for a reason.

## Phase 1 Rules

- Read the Hard Disqualifiers section of candidate-profile. Check each JD against every disqualifier.
- If any single disqualifier fires, the JD is immediately dropped. Do not score it. Do not continue to Phase 2. Log it with the reason.
- For location: look for explicit non-US location with no remote clause. "London, UK" with no mention of US remote = disqualify. "Remote" or "Remote (US)" or no location = pass.
- For sponsorship: look for exact phrases like "no sponsorship", "must be authorized to work permanently", "US citizen or permanent resident required", "no OPT/CPT". Ambiguous = pass. Explicit denial = disqualify.
- For experience: look for "5+ years", "7+ years", "8+ years" in the requirements section. "3–5 years" = pass. "Minimum 5 years" = disqualify. "Preferred 5 years" = pass (preferred is not required).

## Phase 2 Rules

- All three questions must be YES to pass. A single NO disqualifies the JD — log it with which question failed.
- Q1 (role type): Check the Target Roles section of candidate-profile. When ambiguous, if the title is unusual but the description clearly describes building software systems, features, or APIs → YES. Give the benefit of the doubt on title, not on description.
- Q2 (seniority): "3–5 years preferred" → YES. "3–5 years required, minimum 3" → YES. "Minimum 5 years" → NO.
- Q3 (provable must-haves): Count only "Always provable" tier items. "Provable with framing" items do not count toward the threshold of two.

## Phase 3 Rules

- Count every JD must-have or required skill that appears in the "Always provable" tier of candidate-profile.
- For Career Direction Fit: check the Career Direction section of candidate-profile. Three fit types exist in priority order. Score based on which fit type the JD matches. Use the highest-scoring one when multiple match.
- For Strongest Signal Match: check the Strongest Signals section of candidate-profile. Five signals exist. A signal "matches" when the JD's description or requirements directly name the concept — not just shares a domain. "LLM experience" matches signal 1. "Python experience" alone does not.
- For Preferred Signal Count: check the Preferred Signals section of candidate-profile. Count how many appear in the JD. Each one is worth 1 point, capped at 10.

## Phase 4 Rules

- Sort all scored JDs by total score, highest first. Select the top 3–5 for the full pipeline.
- If the top score is ≥ 75: take top 5. If 60–74: take top 4. If < 60: take top 3 only.
- If fewer than 3 JDs scored above 40: flag the batch as low-quality and take only those above 40.
- Tie-breaking: Higher Career Direction Fit → Higher Strongest Signal Match → Higher Provable Coverage → More Preferred Signals.
- Never call PATCH /use for a skipped JD. It stays unprocessed so it can be re-evaluated after a candidate profile update.

## Log Format

**Skipped JDs:**
```json
{ "job_description_id": "{jd_id}", "status": "skipped", "message": "{company_name}: pre-filter {result}. Reason: {reason}. Score: {score}." }
```

**Profile notes:** If any JD revealed a gap or wrong assumption in candidate-profile, record it as a note for the candidate to review and update manually. The agent never edits the profile autonomously.
