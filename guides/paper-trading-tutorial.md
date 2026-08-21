---
description: Start, monitor, inspect, and stop a Quandora simulated Paper run.
content_status: handoff
content_owner: plugin-and-product-backend
---

# Paper Trading Tutorial

Paper Trading uses simulated orders and never places live-money trades. It
starts from an existing eligible Strategy result; factor selection and Strategy
backtesting remain in Strategy Building.

## 1. Select An Eligible Source

```text
/quandora:paper-trading start a paper run
```

If you did not specify an exact source, the agent lists your eligible Paper
sources. Select one returned source instead of guessing an identifier.

A source must be owner-scoped, completed, successfully submitted,
cross-sectional, and reconstructable by the service. A preflight result can be:

* **eligible** — safe checks passed, with final validation still performed at submission;
* **provider validation required** — eligibility could not yet be confirmed;
* **ineligible** — the returned reason explains why the source cannot be used.

If no eligible source exists, return to [Strategy Building](strategy-tutorial.md).

## 2. Confirm The Paper Run

Before submission, review and explicitly confirm:

* the exact source and safe Strategy label;
* optional initial balance;
* optional start date;
* optional leverage.

The Paper skill does not accept a custom symbol list or universe policy.
Quandora selects and freezes the simulation universe downstream.

## 3. Monitor Lifecycle From Run Detail

After submission, monitor the same run through its detail state. Do not create a
second run because an early portfolio or equity response is still preparing.

Ask naturally or use:

```text
/quandora:paper-trading show my current Paper PnL
```

Available reads can include:

* current portfolio, assets, PnL, and open positions;
* closed net-position lifecycles;
* simulated fills;
* funding records;
* fixed-lookback equity curves;
* bounded strategy code for inspection.

Open or partially open positions belong to the current portfolio snapshot. The
position-history view contains only closed net-position lifecycles.

## 4. Read Equity Curves Carefully

Current fixed lookbacks are `7D`, `30D`, `90D`, `180D`, `1Y`, and `3Y`. Before
the Paper run's live simulation period begins, the curve can contain explicit
zero padding. That padding means “before this run,” not zero historical loss or
missing market data.

## 5. Stop Only When You Mean It

Stopping is a terminal mutation and requires explicit confirmation. A stopped
Paper run cannot be resumed. Starting the same source again creates a fresh run
with separate history.

The current public agent workflow does not expose Paper archive, unarchive, or
resume actions. Do not describe hiding history as a way to stop execution.

## Strategy Portfolio Paper

Paper Trading also supports a Strategy Portfolio made from static,
independently allocated Strategy sleeves. The workflow is:

```text
create or revise the Portfolio definition
-> backtest the Portfolio
-> inspect the result
-> explicitly confirm a Portfolio Paper run
-> monitor or stop that exact run
```

Creating factors or individual Strategy backtests still belongs to Strategy
Building.

## No Automatic Repairs

Losses, drawdown, or suspected decay never authorize the agent to stop a run,
mine another factor, revise a Strategy, or start another workflow. The agent can
report evidence and propose a handoff; the user decides and confirms the next
action.
