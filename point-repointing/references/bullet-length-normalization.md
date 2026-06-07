# Bullet Length Normalization Guide

## Target Range

**250-300 characters per bullet** (excluding LaTeX formatting commands like `\textbf{}`).

- **Hard minimum:** 230 chars — bullets shorter than this look sparse and leave gaps
- **Hard maximum:** 320 chars — bullets longer than this break the resume layout by taking up too much vertical space

## Why This Matters

Inconsistent bullet lengths cause uneven vertical spacing in the rendered PDF. Long bullets push content down, short bullets leave gaps. When mixed, the resume looks unprofessional and can spill onto a second page.

## Reference Example (~285 chars)

```
Deployed a Redis caching layer on AWS with cache refresh controls for a production SaaS platform serving thousands of users, reducing database load by 75% on time-sensitive operational workflows and improving response consistency during traffic spikes.
```

This is the ideal: specific technology names, clear problem→action→outcome, quantified impact, consistent length.

## How to Normalize

### If a bullet is too short (< 230 chars):
- Add specific technology names (e.g., "built a caching layer" → "built a Redis caching layer on AWS")
- Add quantified metrics (e.g., "improved performance" → "reducing database load by 75%")
- Add context about scale (e.g., "for a production platform" → "for a production SaaS platform serving thousands of users")
- Add the "why" or "so what" (e.g., "reducing database load" → "reducing database load on time-sensitive operational workflows")

### If a bullet is too long (> 320 chars):
- Remove redundant phrases (e.g., "in order to" → "to")
- Combine related clauses with commas instead of separate phrases
- Shorten lists (e.g., list 3 items instead of 5)
- Remove filler words ("various", "multiple", "several", "different")
- Split into two shorter bullets if the content genuinely covers two distinct contributions

### Cross-section consistency:
After normalizing individual bullets, compare average lengths across sections:
- Work experience bullets should be similar length to project bullets
- No section should average 300+ chars while another averages 220
- If one section is systematically longer, compress those bullets slightly

## Measurement

Count characters excluding LaTeX commands:
```python
import re
bullet_text = r"\item Deployed a \textbf{Redis} caching layer..."
# Strip LaTeX commands for length measurement
clean = re.sub(r'\\[a-z]+\{[^}]*\}', '', bullet_text)
clean = clean.replace('\\item ', '').strip()
length = len(clean)
```

Or simply: copy the bullet text (without `\item` and without `\textbf{}` wrappers) and count characters.
