# Bullet Length Consistency Check

## Target Range

**250-300 characters per bullet** (excluding LaTeX formatting commands like `\textbf{}`).

- **Hard minimum:** 230 chars — bullets shorter than this look sparse
- **Hard maximum:** 320 chars — bullets longer than this break the resume layout

## Why This Matters

Inconsistent bullet lengths cause uneven vertical spacing in the rendered PDF. When some bullets are 400+ chars and others are 200 chars, the resume looks unbalanced and can spill onto a second page.

## Reference Example (~285 chars)

```
Deployed a Redis caching layer on AWS with cache refresh controls for a production SaaS platform serving thousands of users, reducing database load by 75% on time-sensitive operational workflows and improving response consistency during traffic spikes.
```

## Assembly-Time Check

After assembling the .tex file, measure every bullet:

```python
import re

with open("/path/to/resume.tex") as f:
    content = f.read()

# Extract bullets
bullets = re.findall(r'\\item (.+?)(?=\\item|\\end\{document\})', content, re.DOTALL)

for i, b in enumerate(bullets):
    # Strip LaTeX commands for measurement
    clean = re.sub(r'\\[a-z]+\{[^}]*\}', '', b)
    clean = clean.strip().replace('\n', ' ')
    length = len(clean)
    
    if length < 230:
        print(f"Bullet {i+1}: TOO SHORT ({length} chars)")
    elif length > 320:
        print(f"Bullet {i+1}: TOO LONG ({length} chars)")
    else:
        print(f"Bullet {i+1}: OK ({length} chars)")
```

## Cross-Section Consistency

After measuring individual bullets, compare averages:
- Work experience bullets should be similar length to project bullets
- No section should average 300+ chars while another averages 220
- If inconsistent, normalize by compressing longer bullets or expanding shorter ones

## Fix

If a bullet is outside the 230-320 range:
- **Too short:** Add specific technology names, metrics, scale numbers, or clearer problem→action→outcome
- **Too long:** Remove redundant phrases, combine clauses, shorten lists, remove filler words

Do NOT push a resume with inconsistent bullet lengths.
