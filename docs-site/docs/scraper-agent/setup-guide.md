---
id: setup-guide
title: Setup Guide
sidebar_position: 2
slug: /scraper-agent/setup-guide
---

import SourceRepoNote from '@site/src/components/SourceRepoNote';

# Scraper Agent Setup Guide

This section is for scraper-agent-specific setup only.

Use this guide to configure the Hermes profile that handles job scraping, scheduling, and upstream job-description collection for the resume workflow.

## Profile model

Run the scraper in a dedicated Hermes profile such as `scraper`.

Do not run it in the same Hermes profile as the resume agent. The scraper profile should stay isolated because it owns:

- scraping credentials
- scraper ingest secrets
- browser automation dependencies
- cron scheduling for job collection

The resume profile should stay focused on `candidate-profile`, pool content, and `resume-pipeline-orchestrator`.

## Files in this repo

The current scraper files are:

- `scraper/jobright.py`
- `scraper/tiny_fish_job_description.py`
- `scraper/.env.example`

The repository currently gives you the scraper scripts and the env template. The Hermes wrapper skill for prompts like `scrape 20 jobs` should be created inside the dedicated scraper profile.

`jobright.py` is the main batch-ingest scraper. It logs into Jobright, collects jobs, opens each detail page in the same browser session, and posts those jobs to the dashboard ingest endpoint.

`tiny_fish_job_description.py` is a utility fetcher for individual job-description URLs. It requires a paid Tiny Fish API key and writes Markdown output locally.

## Environment configuration

Create a real `.env` file for the scraper profile based on `scraper/.env.example`.

Current variables:

```env
JOBRIGHT_EMAIL=""
JOBRIGHT_PASSWORD=""
TINYFISH_API_KEY=your_tinyfish_api_key_here
SCRAPER_INGEST_URL="https://your-dashboard.example.com/api/job-descriptions"
SCRAPER_INGEST_SECRET=your_scraper_ingest_secret_here
```

Rules:

- keep real values out of git
- set `SCRAPER_INGEST_URL` to your real dashboard ingest endpoint
- set `SCRAPER_INGEST_SECRET` to the backend secret or token used for scraper ingestion
- only set `TINYFISH_API_KEY` if you plan to use Tiny Fish

## Jobright scraper usage

Use `jobright.py` when you want to collect a batch of Jobright jobs and ingest them into the dashboard queue.

Typical manual commands:

```bash
python scraper/jobright.py --xvfb --jobs 20
python scraper/jobright.py --xvfb --jobs 5 --debug
python scraper/jobright.py --xvfb --jobs 3 --dry-run
```

Operational notes:

- `--jobs` controls target batch size
- `--xvfb` is the normal VPS mode because the scraper is not reliably usable as a true headless browser flow
- `--dry-run` collects links without scraping job details
- `--debug` helps when the site layout or login flow changes

## Tiny Fish usage

Use `tiny_fish_job_description.py` when you already have a specific job URL and want to fetch its content outside Jobright.

Example:

```bash
python scraper/tiny_fish_job_description.py --url https://example.com/job/123
```

Important tradeoff:

- Tiny Fish is more general but paid
- Jobright is free but limited to the Jobright platform

## Hermes skill pattern

For day-to-day operation, add a scraper skill inside the scraper Hermes profile that acts as a thin wrapper around the script.

The intended operator experience is:

- you tell Hermes `scrape 20 jobs`
- the scraper profile invokes the Jobright scraper skill
- the skill runs the correct command for that environment

That wrapper skill should:

- accept the requested job count
- run `scraper/jobright.py` with `--xvfb` in VPS environments
- use the scraper profile's env file and secrets
- report how many jobs were ingested, skipped, or failed

This is the preferred path over manually typing the full Python command every time.

Keep the division clear:

- repository assets: scraper scripts, env template, docs
- scraper profile asset: the Hermes skill that invokes those scripts

## Cron mode

The scraper profile is a good cron target because it is isolated from the resume agent and can run independently.

Typical operating pattern:

1. schedule the scraper profile in the morning
2. ingest fresh jobs into the dashboard queue
3. run the resume profile later against those queued JDs

This separation makes failures easier to diagnose. If scraping breaks, resume generation is still isolated. If resume generation breaks, scraping can continue to keep the queue fresh.

## VPS requirement

The current Jobright scraper uses browser automation and should not be documented as a pure headless flow.

For VPS deployment:

- install Hermes on the VPS
- use the dedicated scraper profile there
- make sure the machine can provide a browser display context
- run the scraper with `--xvfb`

If you are using the reference always-on Hermes VPS setup, this scraper belongs there rather than on a laptop that may go offline.

<SourceRepoNote>
  If you want the actual scraper files behind this setup guide, use the public source repository.
</SourceRepoNote>
