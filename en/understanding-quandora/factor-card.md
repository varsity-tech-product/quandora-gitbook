---
description: >-
  The structured report for one factor result — Health, grade, evidence, risks,
  and what to test next.
---

# Factor Card

A Factor Card is the server-persisted evidence record for one exact factor
result. It turns a raw backtest into something a person or AI agent can review,
question, and compare without depending on local files.

## How To Read A Card

Read in this order:

```text
Success / Fail
-> evidence quality and Health
-> grade and continuous metrics
-> risks and caveats
-> next controlled experiment
```

## Success And Grade Are Different

| Result | Meaning |
| --- | --- |
| Success / Fail | Whether every required factor evidence check passed. |
| SSS, SS, S, A, B, C, D, F | The cross-sectional Sharpe grade relayed by the evaluation runtime. |

A factor can receive a non-F grade and still fail a required check. Read the
recorded gate evidence before interpreting the grade. See
[How Factors Are Judged](how-factors-are-judged.md) for the current semantics.

## Common Card Fields

| Field | Meaning |
| --- | --- |
| Success / Fail | Combined required-check result |
| grade and grade score | Relayed categorical and continuous rating evidence |
| factor idea and formula | What the signal is designed to capture |
| data and evaluation scope | Headers, bar size, horizon, and visible evidence window |
| Health | Coverage, missingness, output usability, and any failed Health fields |
| key metrics | Sharpe, Rank IC, autocorrelation, drawdown, turnover, and available diagnostics |
| assumptions and caveats | Conditions that may weaken the evidence |
| next experiment | A proposed controlled change, not an automatic submission |

Missing or null evidence stays unavailable; it must not be converted to zero or
treated as a pass.

## Example

For a factor evaluated on daily bars with a seven-day forward horizon:

| Field | Value | Plain English |
| --- | --- | --- |
| Success | Fail | At least one required check did not pass |
| Grade | D | Cross-sectional Sharpe falls in the D band |
| Cross-sectional Sharpe | 0.81 | Passes the strict `> 0.8` check |
| Absolute Rank IC | 0.008 | Fails the strict `> 0.01` check |
| Autocorrelation, lag 1 | 0.62 | Passes the `>= 0.4` check |
| Health | Passed | The recorded output-quality check passed |
| Max drawdown | −32% | The worst observed peak-to-trough decline |
| Turnover | 0.63 | How much the implied portfolio changed |
| Cost viability | Failed | A diagnostic warning, not a Success gate |

The concise reading is: **Fail** because absolute Rank IC missed its required
threshold; **D** because Sharpe was 0.81; and **high implementation risk** if
cost viability also failed. Those statements answer different questions.

## Server Evidence And Charts

The Factor Analysis skill reads product-safe **In-Sample (IS)** evidence for one
exact run. Depending on availability, this can include the Factor Card, Health
and rating fields, factor profile, group NAV, daily returns, simulation NAV,
simulation PnL, and inert job-linked source used only for explanation.

Do not describe this public analysis as OOS or ALL analysis. A future public
contract may expose other windows, but the current analysis surface is IS-only.

## Optional Result Bundle

Factor Analysis does not require a local archive. When Factor Mining exports a
completed result in a writable host, the canonical local output is one verified
ZIP:

```text
Quandora result/factor/<factor_slug>.zip
```

The ZIP is not automatically extracted or reconstructed. Its runtime manifest
is authoritative for the exact included, pending, and omitted items.

| Bundle state | What it means |
| --- | --- |
| Available | The verified archive is ready. |
| Partial | The archive is readable and the manifest identifies pending or omitted optional items. |
| Pending / materializing | The archive is still preparing; request the same result again later. |

A delayed bundle is not a reason to start another backtest.
