---
description: >-
  Watching a strategy forward without risking money — and deciding whether it's
  ready, needs a refresh, or should be retired.
---

# Paper Trading & Monitoring

Strategy paper trading is available to public users. When a strategy passes
evaluation, you can run it on live market conditions with simulated orders —
no real money at risk. The question it answers is simple and important:

```
Does the strategy keep working after the backtest?
```

A backtest describes the past. Paper trading tests whether the strategy behaves the way the backtest suggested it should, going forward. This is the main decision point in the workflow.

### What Monitoring Tracks

* **Simulated orders** — what the strategy would have done
* **Forward performance** — results on data the strategy never trained on
* **PnL and equity curve** — cumulative performance over time
* **Drawdown** — worst peak-to-trough loss so far
* **Turnover** — how much the book is churning
* **Cost drift** — whether real trading costs are eating the edge
* **Regime changes** — shifts in market conditions
* **Signal decay** — the edge weakening over time
* **Alerts** — notifications when something moves out of expected range
* **Trade-log memory** — a persistent record of what happened and why

### The Decision Point

Paper trading / monitoring is where the workflow forks.

**If the strategy stays stable**, keep monitoring it. Users with separate
invite-only access may also review the controlled
[Deployment & Live Trading](deployment-and-live-trading.md) process.

**If performance decays**, the loop restarts. Decay can mean weaker performance, larger-than-expected drawdown, rising turnover or costs, a changed market regime, or the signal drifting from its backtest behavior.

```
paper trading / monitoring detects decay
-> factor mining restarts
-> new candidate factors are generated
-> new factors are evaluated
-> the strategy is repaired, replaced, or retired
```

Quandora does not treat a decaying strategy as permanently valid. The old result becomes memory, and the agent receives a refreshed research task. The goal is not to keep a weak strategy alive — it is to keep you inside an evidence loop.

The step-by-step product interface is reserved in the
[Paper Trading Tutorial](../guides/paper-trading-tutorial.md) and will be
completed by the plugin and Product Backend owners.
