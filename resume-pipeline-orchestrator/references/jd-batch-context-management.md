# JD Batch Context Management

## Problem

When fetching JDs for a batch run, the full API response (all 10 JDs) enters conversation history and stays there for the entire run. At ~2-3K chars per JD, that's 20-30K chars of permanent context overhead. By JD #10, the cumulative context includes all JD texts plus 9 JDs' worth of processing history.

## Solution: Write Batch to Temp File

After fetching, write the full response to a temp file and access one JD at a time:

```python
import json, os

# After fetch
batch = api_response['job_descriptions'][:10]  # cap at 10
with open('/tmp/jd_batch.json', 'w') as f:
    json.dump(batch, f)

# Per-JD access (only current JD text enters context)
with open('/tmp/jd_batch.json') as f:
    all_jds = json.load(f)
jd = all_jds[i]  # only this JD's data is in the variable
```

## Rules

1. Write the batch file ONCE immediately after fetching
2. NEVER reference the full fetch response again — only read from the file
3. Read ONE JD at a time using index access
4. Delete the temp file at end of run (or leave for debugging)
5. Use a run-specific filename if parallel runs are possible: `/tmp/jd_batch_<timestamp>.json`

## Context Savings

- Before: ~25K chars (all JD texts) permanent in conversation history
- After: ~2-3K chars (one JD at a time) in active context
- Net savings: ~20K+ chars across the second half of the run
