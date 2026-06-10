---
id: overview
title: Overview
sidebar_position: 1
slug: /resume-agent/overview
---

# Resume Agent Overview

The resume agent is responsible for reading candidate context, processing job descriptions, running the resume pipeline, and producing tailored resume outputs.

In this setup, the resume agent runs as its own Hermes profile so it stays isolated from the scraper agent. That keeps resume-generation logic, skills, prompts, and runtime settings separate from scraping concerns.

If you kept `default` for scraping, use the `resume` profile here. If you created both `scraper` and `resume` as separate profiles, continue all resume-specific work in the `resume` profile.
