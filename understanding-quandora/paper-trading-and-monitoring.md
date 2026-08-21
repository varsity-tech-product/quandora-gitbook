---
description: >-
  Monitor a strategy with simulated orders, inspect its evidence, and decide
  the next action yourself.
---

# Paper Trading & Monitoring

Strategy Paper Trading is available to public users. It reuses an eligible,
completed Strategy result and runs simulated orders without risking real money.

The question is:

```text
How is this exact Strategy source behaving in simulation now?
```

Paper evidence does not prove future or live-money performance.

## What You Can Inspect

The current public Paper workflow can expose:

* run lifecycle and safe source information;
* current balance, assets, PnL, and portfolio positions;
* closed net-position lifecycles;
* simulated fills and funding;
* fixed-lookback equity curves;
* bounded strategy code;
* terminal stop after explicit confirmation.

The portfolio snapshot is the source for open and partially open positions.
Closed position history contains completed net-position lifecycles only.

Fixed-lookback equity views are `7D`, `30D`, `90D`, `180D`, `1Y`, and `3Y`.
Pre-run dates can be represented by explicit zero padding so the requested
window remains fixed; that padding is not simulated performance.

## Monitoring Is Evidence, Not Automation

Use the detail state to follow one exact run. A temporarily unavailable
portfolio is not proof of zero PnL, an empty portfolio, or a failed run. Check
the same run again instead of rapidly polling or submitting a duplicate.

The public skill does not promise automatic alerts, autonomous regime
classification, automatic signal-decay decisions, or an agent-maintained trade
story. Interpret only the evidence that the service returns.

## User-Controlled Decision Point

If the evidence is stable, you can keep monitoring. If losses, drawdown, or
unexpected behavior appear, you can:

* inspect fills, funding, positions, equity, and code;
* stop the Paper run after explicit confirmation;
* ask Strategy Analysis for a read-only diagnosis of the source result;
* choose a controlled Strategy Building experiment;
* return to Factor Analysis or Factor Mining when the evidence supports it.

Nothing happens automatically. Paper Trading does not stop itself, revise a
Strategy, restart Factor Mining, or submit a replacement run because a metric
changed.

For the exact procedure, see the [Paper Trading Tutorial](../guides/paper-trading-tutorial.md).
