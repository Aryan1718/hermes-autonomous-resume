# Quality Verification Checklist for .tex Files

## Run this verification AFTER saving each .tex file and BEFORE pushing to dashboard.

### 1. Double-Backslash Check
head -5 resume.tex | grep '\\\\documentclass' && echo "FAIL: double backslash" && exit 1

### 2. Bullet Count Check
BULLET_COUNT=$(grep -c '\\item' resume.tex)
if [ "$BULLET_COUNT" -lt 14 ]; then
  echo "FAIL: only $BULLET_COUNT bullets, expected 14+"
  exit 1
fi

### 3. Bullet Length Check (MIN 300 chars per bullet, target 350-500)
python3 -c "
import re
with open('resume.tex') as f:
    content = f.read()
bullets = re.findall(r'\\item\\s+(.*?)(?=\\n\\n|\\n\\item|\\end{itemize})', content, re.DOTALL)
bullets = [b.strip().replace(chr(10), ' ') for b in bullets if len(b.strip()) > 20]
if not bullets:
    print('FAIL: no bullets'); exit(1)
avg = sum(len(b) for b in bullets) / len(bullets)
short = [i+1 for i, b in enumerate(bullets) if len(b) < 300]
print(f'Bullets: {len(bullets)}, Avg: {avg:.0f}')
if short: print(f'FAIL: bullets {short} under 300 chars'); exit(1)
if avg < 350: print(f'FAIL: avg {avg:.0f} below 350'); exit(1)
print('OK')
"

### 4. No Em Dashes in Bullets
grep '\\item.*--.*' resume.tex && echo "FAIL: em dash in bullet" && exit 1

## If ANY check fails:
1. DO NOT push the resume
2. Fix the issue (regenerate bullets, fix formatting, etc.)
3. Re-verify before pushing
