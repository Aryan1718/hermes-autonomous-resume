---
id: installation
title: Installation
sidebar_position: 2
slug: /getting-started/installation
---

# Installation

## Step 1: Choose where Hermes will run

Before you set up the resume pipeline, decide where you want to run Hermes. There are two straightforward options for this setup.

### Option 1: Deploy Hermes on a VPS

This is the recommended approach. You can use any VPS provider, but Hermes works best when it is running on always-on infrastructure. In the reference setup for this project, Hermes runs on a Hostinger VPS.

- The main reason is Hermes's self-learning loop. For that to be useful over time, Hermes should stay up 24/7 so it can keep running, collect feedback, and improve the system over the long run.
- Use [Hostinger's Hermes Agent VPS page](https://www.hostinger.com/applications/hermes-agent?REFERRALCODE=8JYARYANPGMH) for a one-click VPS setup flow.
- This is the easiest path if you want Hermes running continuously without depending on your local machine.
- It also fits well if you plan to schedule the resume pipeline with cron and keep the system available long term.

### Option 2: Install Hermes on your own machine

If you want to run everything locally first, you can install Hermes directly on your own machine and use that as the runtime for the resume agent.

- Follow the official [Hermes installation docs](https://hermes-agent.nousresearch.com/docs/getting-started/installation).
- On macOS or Windows, Hermes recommends the Desktop installer for the easiest setup.
- For command-line only installs, the Hermes docs provide install commands for Linux, macOS, WSL2, Android Termux, and native Windows PowerShell.

## Step 2: Set up Hermes Agent

Once Hermes is installed, run:

```bash
hermes setup
```

This step is only for setting up Hermes itself. Do not configure the resume workflow yet.

During setup, use these choices for this project:

- Model provider: use [OpenRouter](https://openrouter.ai/).
- Channel or gateway: Telegram is a good default, but you can choose any supported channel that fits your setup.
- General configuration: complete the prompts Hermes gives you and confirm that the agent starts correctly once setup is done.

For the official step-by-step flow, refer to the Hermes Quickstart:

- [Hermes Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)

## Step 3: Create Hermes profiles for the two agents

A Hermes profile is a separate agent home with its own config, API keys, memory, sessions, skills, cron jobs, and gateway state. In this setup, profiles are how you run two isolated agents on the same machine.

Whether you are using a VPS or your own machine, the setup pattern is the same:

- one profile for the scraper agent
- one profile for the resume agent

If you already configured your initial Hermes agent in the `default` profile and want to keep using it for the scraper, that is fine. In that case, only create a new profile for the resume agent by cloning from `default`.

```bash
hermes profile create resume --clone
```

If you want `default` to remain your base profile and create both agents separately, create both profiles by cloning the current config:

```bash
hermes profile create scraper --clone
hermes profile create resume --clone
```

The `--clone` option copies the current profile configuration into the new profile while keeping memory and sessions separate. That gives both agents the same starting setup, but they remain isolated from each other after creation.

After the profiles are created, you can run profile-specific commands directly. For example:

```bash
scraper setup
resume setup
```

For the official Hermes profile guide, refer to:

- [Hermes Profiles Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)

## Notes

- At the end of this section, Hermes should be installed, configured, and split into the two profiles needed for this project.
- The next setup steps are scraper agent configuration and resume agent configuration.
