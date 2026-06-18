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

The scraper implementation in this repository is built around two scraper scripts:

- `jobright` scraper for collecting jobs from the Jobright platform
- `tinyfish` scraper for collecting jobs from general job boards

Both implementations are available in the repository:

- [hermes-autonomous-resume on GitHub](https://github.com/Aryan1718/hermes-autonomous-resume)

You are not limited to these two scrapers. You can also build your own scraper as long as it collects the required job data and pushes it into the backend in the format expected by the rest of the system.

## How the scraper flow works

The operating model is straightforward:

- the scraper agent runs in the morning
- it collects around 20 jobs
- it stores those jobs in the backend database with the required metadata
- the resume agent later fetches unused jobs from that database and runs the resume pipeline on them

This makes the scraper agent the ingestion layer for the whole system. Its job is not to generate resumes. Its job is to continuously keep the job queue fresh, structured, and ready for downstream processing.

## Backend integration

To make this work in your own setup, you will need backend endpoints for storing scraped jobs, marking job state, and serving unused jobs back to the resume agent. Those backend contracts are documented in the API reference:

- [API Reference Overview](/docs/api-reference)
