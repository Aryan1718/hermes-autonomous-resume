---
id: feedback-loop
title: Feedback Loop
sidebar_position: 2
slug: /architecture/feedback-loop
---

# Feedback loop

Hermes is not just a one-shot resume generator. The point of the larger system is that outputs feed back into better future runs.

## Feedback sources

- accept or reject decisions on generated resumes
- comments on weak bullets or missing evidence
- repeated JD failure patterns
- signals that the candidate profile is stale

## What feedback should improve

- `candidate-profile` accuracy
- pool completeness
- stricter or better `jd-prefilter` rules
- stronger project selection
- clearer quality gates before pushing resumes

## Important boundary

Feedback should not silently mutate candidate truth in the middle of a run. Broad profile changes should go through explicit setup or refresh steps so the system stays auditable.
