---
description: Build and evaluate a strategy from Quandora factors.
content_status: handoff
content_owner: plugin-and-product-backend
---

# Strategy Tutorial

Strategy composition and backtesting are available to public users.

The complete interface-level tutorial is being prepared. It will cover:

* finding factors that are ready to be selected for a strategy;
* validating or importing one of your own factors when it is not yet selectable;
* selecting and combining eligible factors;
* reviewing strategy parameters before submission;
* deciding whether to create, revise, fork, or rerun;
* running one exact strategy version through a backtest;
* reading status, performance, risk, and artifact results;
* revising a strategy without losing its earlier definitions or evidence.

## Choose The Right Action

| Your intent | Choose |
| --- | --- |
| Build an independent strategy | **Create** — start a new strategy at Version 1 |
| Improve the same strategy | **Revise** — add a new immutable version to its history |
| Explore a separate strategy from an existing version | **Fork** — start a new Strategy at Version 1 with visible lineage |
| Test an unchanged strategy again | **Rerun** — create a new run without creating a new version |

Factor selection, weights, ranking, strategy type, and rebalance rules define
what the strategy is. Test dates, starting balance, and test-only assumptions
belong to an individual run. Changing run settings should not silently create a
new strategy definition.

## What To Expect From A Run

A submitted strategy run moves through a lifecycle before its final result and
downloadable artifacts are ready. A completed calculation and a complete
artifact archive may become ready at different times. Show a pending state
rather than treating a not-yet-ready file as missing.

If submission confirmation is interrupted, do not immediately submit a second
copy. First ask the product or your agent to reconcile the original attempt.

For the product concepts and evaluation outputs, read
[Strategy Construction](../understanding-quandora/strategy-construction.md).
