---
description: From zero to your first evidence-backed factor report in about 15 minutes.
icon: forward
---

# Quickstart

The goal: connect Quandora to your AI agent, run one research task, and read an evidence-backed factor report.

### Who This Is For

Solo systematic traders, AI power users, and market-curious builders who already use tools like Claude Code, Codex, or OpenClaw — and want their agent to work from market evidence instead of guesses.

### Before You Start

* An agent host: Claude Code, Codex, or OpenClaw
* A [Quandora account](https://app.quandora.ai/auth/signin) — authorization happens in your browser
* 10–15 minutes
* No exchange API key — the first research workflow doesn't touch trading. Authorization is browser OAuth only.

### 1. Install And Connect

Follow the [Installation Guide](installation-guide.md) for your host. Claude Code example:

```
claude plugin marketplace add varsity-tech-product/quandora-plugins
claude plugin install quandora@quandora
```

Then open `/mcp`, authenticate `quandora`, and start a new chat.

### 2. Run Your First Task

List the public research tasks:

```
/factor-mining show public tasks
```

Pick one, or let the agent choose:

```
Use Quandora Factor Mining to pick a public research task, generate a factor,
run the backtest, and give me a plain-English verdict with key metrics and risks.
```

Your agent will read the [task card](../understanding-quandora/task-card.md), check memory for duplicates, write [`plugin.py`](../understanding-quandora/plugin.py.md), and submit it. Quandora binds market data server-side and runs the backtest — mining typically takes a few minutes.

### 3. Read Your Result

The run returns a [factor card](../understanding-quandora/factor-card.md) —
verdict first, then evidence, risks, and a suggested next experiment. When your
host supports local files, it also saves charts and result files in:

```
Quandora result/factor-mining/<factor_slug>/
```

See [How Factors Are Judged](../understanding-quandora/how-factors-are-judged.md) to understand why your factor passed or failed.

### You're Done When

Your agent ran one Quandora research task and returned a report you can understand.

A rejected verdict still counts — rejections become memory and sharpen the next attempt.

{% hint style="info" %}
Factor Mining tests ideas — it does not place trades. Strategy paper trading
uses simulated orders. Live trading is a separate, internal invitation-only
capability. A Factor Card is evidence about the past, not a promise about the
future.
{% endhint %}

### Next Steps

* Browse the [research task families](../understanding-quandora/research-tasks.md)
* See what data your agent can use in [Our Data](../understanding-quandora/our-data.md)
* Learn how to [improve and rerun](../guides/improve-and-rerun.md) one factor
* New to the jargon? Keep the [Glossary](../understanding-quandora/glossary.md) open
