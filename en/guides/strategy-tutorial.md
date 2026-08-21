---
description: Build, backtest, analyze, and export a cross-sectional Strategy.
content_status: handoff
content_owner: plugin-and-product-backend
---

# Strategy Tutorial

Strategy Building and Strategy Analysis are available to public users. The
current public workflow builds cross-sectional strategies from eligible factors.

## 1. List Eligible Factors

```text
/quandora:strategy-building list available factors
```

The first page shows eligible factors from three sources:

| Source | Meaning |
| --- | --- |
| Official | Read-only product inventory |
| Mine | Your eligible Strategy factors |
| Shared | Factors admitted to your Strategy pool |

The list is paginated and does not automatically load every page. Ask for the
next page only when you need it.

## 2. Choose The Composition

A strategy uses between 1 and 20 eligible factors. You can use equal weights or
provide explicit factor weights. Before submission, ask the agent to show the
effective configuration.

The current public configuration can include:

| Setting | Purpose |
| --- | --- |
| name | User-facing Strategy name |
| factor selection or weights | Eligible factors and their composition |
| ranking | Cross-sectional ranking rule |
| strategy type | Current cross-sectional strategy mode |
| start and end dates | Backtest window |
| initial cash | Starting simulated capital |
| maker and taker fee rates | Modeled fee assumptions |
| rebalance bars | Rebalance interval |
| attribution | Whether supported attribution output is requested |

When ranking and strategy type are omitted, the current default is a neutral
top/bottom 20% strategy. The contract returned in the current session remains
the source of truth for supported fields and defaults.

Do not assume that public submission accepts a custom universe, entry/exit
rules, liquidity filters, maximum drawdown limit, deployment target, or other
fields that are not present in that contract.

## 3. Review And Submit

```text
Use Quandora Strategy Building to combine the selected factors, show the exact
effective configuration, and ask me before submitting the backtest.
```

Check names, factors, weights, dates, capital, fees, ranking, and rebalance
settings. Submission is a mutation and requires explicit confirmation.

## 4. Monitor The Same Run

The agent follows the returned run instead of submitting a duplicate. A
terminal failure is immutable; retrying means creating a new run after an
explicit request. A completed calculation and its Result Bundle may become
ready at different times.

## 5. Analyze The Result

Use the read-only Strategy Analysis skill:

```text
/quandora:strategy-analysis analyze my latest strategy result
```

Strategy Analysis pairs the canonical run configuration with retained
artifacts and bounded numerical chart evidence. It can diagnose performance,
risk, turnover, exposure, attribution, factor combination, and Paper readiness.
It does not revise, rerun, export, or start Paper Trading.

Treat an `ALL` strategy scope as a combined scope that includes IS; it is not
pure OOS evidence.

## 6. Export The Optional Result Bundle

Ask Strategy Building to export the exact completed run. In a writable host,
the verified archive is saved as:

```text
Quandora result/strategy/<strategy_slug>.zip
```

The ZIP is retained without automatic extraction or reconstruction. Its
runtime manifest records included, pending, and omitted items.

## 7. Decide The Next Action

* Keep the result as historical evidence.
* Ask Strategy Analysis for one controlled composition or configuration experiment.
* Explicitly confirm a new Strategy Building run.
* If the source is eligible, separately confirm a simulated Paper run.

No analysis result automatically submits another backtest or starts Paper
Trading.
