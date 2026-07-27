---
description: Start, monitor, and stop a Quandora paper-trading strategy.
content_status: handoff
content_owner: plugin-and-product-backend
---

# Paper Trading Tutorial

Strategy paper trading is available to public users. It uses simulated orders,
so it does not place trades with real money.

The complete interface-level tutorial is being prepared. It will cover:

* choosing a completed strategy backtest;
* starting a paper-trading run;
* reading portfolio, position, fill, funding, and equity information;
* understanding pending, running, stopped, and terminal states;
* stopping a run and starting a fresh run later;
* organizing terminal history without confusing archive with deletion.

## Start From Evaluated Evidence

Paper trading starts from one completed strategy backtest. Quandora reuses that
exact strategy definition and factor composition. You may choose documented
simulation settings, but you do not rebuild the strategy or choose a different
market universe while starting the paper run.

## Understand Early And Terminal States

Immediately after submission, portfolio and equity information may still be
preparing. A temporarily unavailable portfolio is not an empty portfolio, zero
PnL, or a failed run. Wait and check the same run again.

Stopping is terminal: the same simulated book cannot be resumed. Starting the
strategy again creates a fresh paper-trading run with its own history.

Where history organization is available, archiving only hides a terminal run
from the default list. It does not stop execution, delete evidence, or make the
run resumable. An active run must be stopped before it can be archived.

For the role of simulated execution in the research process, read
[Paper Trading & Monitoring](../understanding-quandora/paper-trading-and-monitoring.md).
