---
id: overview
title: Overview
sidebar_position: 1
slug: /scraper-agent/overview
---

# Scraper Agent Overview

The scraper agent is responsible for collecting job descriptions and handing them off to the rest of the resume pipeline.

In this system, the scraper agent runs as its own Hermes profile so it stays isolated from the resume agent. That separation makes it easier to manage scraping-specific prompts, runtime values, schedules, and ingestion logic without affecting resume generation directly.

## Available scrapers

The scraper implementation in this repository is built around two scraper scripts with different tradeoffs:

- `jobright` scraper: free, but only scrapes jobs from Jobright
- `tinyfish` scraper: paid, requires a Tiny Fish API key, but can fetch content from general job-description URLs outside Jobright

Both implementations are available in the public repository under `scraper/`:

- `scraper/jobright.py`
- `scraper/tiny_fish_job_description.py`

Source repository:

- [hermes-autonomous-resume on GitHub](https://github.com/Aryan1718/hermes-autonomous-resume)

You are not limited to these two scrapers. You can also build your own scraper as long as it collects the required job data and pushes it into the backend in the format expected by the rest of the system.

## How the scraper flow works

The operating model is straightforward:

- the scraper agent runs in its own Hermes profile, usually on a morning cron
- it collects a batch of jobs
- it stores those jobs in the dashboard/backend queue
- the resume agent later fetches unused jobs from that database and runs the resume pipeline on them

This makes the scraper agent the ingestion layer for the whole system. Its job is not to generate resumes. Its job is to continuously keep the job queue fresh, structured, and ready for downstream processing.

## Normal ways to use it

There are two normal operating modes:

- manual run: ask the scraper Hermes profile to scrape a batch now
- scheduled run: let cron invoke the scraper profile automatically

Recommended operator pattern:

- keep the scraper in a dedicated Hermes profile such as `scraper`
- add a scraper skill in that profile that maps prompts like `scrape 20 jobs` to the correct script invocation
- keep the scraper scripts and env template from this repository available inside that scraper profile's workspace
- keep the resume pipeline in a separate Hermes profile such as `resume`

That separation is intentional. The scraper profile owns browser automation, scraping credentials, ingest secrets, and cron scheduling. The resume profile owns candidate truth, evidence selection, resume generation, and dashboard resume pushes.

Current scraper-side assets in this repository are:

- `scraper/jobright.py`
- `scraper/tiny_fish_job_description.py`
- `scraper/.env.example`
- the documented pattern for a scraper-profile wrapper skill

## Jobright vs Tiny Fish

Use `jobright.py` when:

- you want a free source of jobs
- you are specifically scraping Jobright recommendations
- you want to ingest batches directly into the dashboard queue

Use `tiny_fish_job_description.py` when:

- you already have a specific job URL
- the job is not on Jobright
- you are willing to pay for Tiny Fish API access

Important limitation:

- `tiny_fish_job_description.py` fetches page content and saves Markdown locally
- `jobright.py` is the scraper that currently logs in, collects jobs, and posts them into the dashboard ingest endpoint

## VPS and headless note

The current Jobright scraper should not be treated as a true headless scraper. In the repository it runs with browser automation and `headless=False`.

For VPS use:

- run it on a VPS where Hermes is installed in the dedicated scraper profile
- use a virtual display such as `Xvfb`
- invoke the script with `--xvfb` so the browser has a display context

If you want always-on automation, the VPS setup is the right place for the scraper agent. Local runs are fine for testing, but cron-based scraping belongs on the scraper profile's VPS environment.

## Backend integration

To make this work in your own setup, you will need backend endpoints for storing scraped jobs, marking job state, and serving unused jobs back to the resume agent. Those backend contracts are documented in the API reference:

- [API Reference Overview](/docs/api-reference)
