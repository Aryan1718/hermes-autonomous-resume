# Hidden Stack Inference

JDs often list one tool but assume you know the ecosystem around it. Read between the lines.

## Inference Table

| JD Mentions | Likely Also Used (Even If Unstated) |
|---|---|
| Salesforce | SOQL, Apex, Sales Cloud, Service Cloud |
| AWS | EC2, S3, Lambda, CloudWatch, IAM |
| React | JavaScript/TypeScript, Redux or Context, Webpack/Vite |
| Tableau | SQL, data modeling, possibly Snowflake/BigQuery |
| HubSpot | CRM workflows, marketing automation, possibly Marketo adjacency |

**Rule:** If you have honest experience with the adjacent stack, **include it**. It signals depth. But do not fabricate.

## How to Extract

During Pass 1 (surface scan), when you identify a major tool/platform, check whether the candidate has experience with the surrounding ecosystem. Add these as `surface_requirements` with `confidence: high-confidence inference` and `explicit_or_inferred: supported inference`.

Only infer adjacent tools — never infer the core requirement itself. If the JD says "Python," don't infer "Django" unless the JD also mentions web frameworks.
