---
description: From zero to your first evidence-backed factor report in about 15 minutes.
icon: forward
---

# Quickstart

The goal: connect Quandora to your AI agent, run one research task, and analyze
one evidence-backed factor result.

## Who This Is For

Solo systematic traders, AI power users, and market-curious builders who use
Codex, Claude, Cursor, CodeBuddy, WorkBuddy China, or Kimi Code and want their
agent to work from market evidence instead of guesses.

## Before You Start

* A supported agent host
* A [Quandora account](https://app.quandora.ai/auth/signin)
* 10–15 minutes
* No exchange API key — this research workflow does not place trades

## 1. Install And Connect

Follow the [Installation Guide](installation-guide.md) for your host. Complete
the browser OAuth flow, then start a new chat or task so the host can discover
all five Quandora skills.

## 2. Run Your First Factor Task

List the public research tasks:

```text
/quandora:factor-mining show public tasks
```

Pick one, or let the agent choose:

```text
Use Quandora Factor Mining to pick a public research task, generate a factor,
run the backtest, and give me a short result summary.
```

Your agent reads the [task card](../understanding-quandora/task-card.md), checks
for materially similar work, writes [`plugin.py`](../understanding-quandora/plugin.py.md),
validates the complete source, and submits it. Quandora binds market data and
runs the evaluation server-side.

## 3. Analyze The Exact Result

After the run reaches a terminal state, ask for read-only analysis:

```text
/quandora:factor-analysis analyze my latest factor result
```

Factor Analysis resolves one exact run and reads its owner-scoped,
server-persisted In-Sample evidence. It does not need a local ZIP, Python
runtime, notebook, or extracted chart folder.

Read the [Factor Card](../understanding-quandora/factor-card.md) verdict,
Health evidence, grade, metrics, risks, and proposed controlled experiments.
See [How Factors Are Judged](../understanding-quandora/how-factors-are-judged.md)
for the current Success and grade semantics.

## 4. Find The Optional Export

When your host can write local files and the completed Result Bundle is ready,
Factor Mining saves one verified ZIP:

```text
Quandora result/factor/<factor_slug>.zip
```

The archive is not automatically extracted. Its manifest is authoritative for
included, pending, and omitted items. A partial bundle can still be readable;
a materializing bundle can be requested again later.

## You Are Done When

Your agent ran one task and explained one exact result using server evidence.
A failed factor still counts: negative evidence helps identify the next useful
experiment.

{% hint style="info" %}
Factor Mining and Factor Analysis do not place trades. Strategy Paper Trading
uses simulated orders. Live trading is not part of the public product. A
backtest is evidence about tested conditions, not a promise about the future.
{% endhint %}

## Next Steps

* Browse the [research task families](../understanding-quandora/research-tasks.md)
* Learn how to [improve and rerun](../guides/improve-and-rerun.md) with explicit confirmation
* Build a cross-sectional strategy with the [Strategy Tutorial](../guides/strategy-tutorial.md)
* Keep the [Glossary](../understanding-quandora/glossary.md) open for unfamiliar terms
