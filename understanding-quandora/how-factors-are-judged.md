---
description: >-
  The current Success checks and SSS–F grade behind a Factor Card — evidence,
  not promises.
---

# How Factors Are Judged

Every submitted factor is evaluated on server-bound market data. Read the two
headline results separately:

* **Success or Fail** asks whether every required evidence check passed.
* **Grade** reports a cross-sectional Sharpe band.

The evaluation runtime owns these semantics. The Factor Card's recorded values,
thresholds, Health evidence, and failure reasons are authoritative for the
exact run.

## Current Public Evidence Scope

The Factor Analysis skill currently reads product-safe **In-Sample (IS)**
evidence. It does not claim OOS or ALL evidence. IS is historical evidence and
does not predict future or simulated performance.

## Success Or Fail

A cross-sectional factor succeeds only when all four current checks pass:

| Check | Success condition | What it asks |
| --- | --- | --- |
| Absolute Rank IC | `> 0.01` | Is the ranking relationship strong enough? |
| Autocorrelation, lag 1 | `>= 0.4` | Is the signal sufficiently persistent from one bar to the next? |
| Cross-sectional Sharpe | `> 0.8` | Was risk-adjusted cross-sectional performance strong enough? |
| Factor Health | Passed | Was the factor output sufficiently complete and usable under the recorded Health basis? |

The Rank IC and Sharpe checks use strict greater-than comparisons;
autocorrelation includes the threshold. Unknown, unavailable, or non-finite
required evidence does not pass.

Cost viability, turnover, drawdown, and other diagnostics remain important,
but they do not independently determine Factor Success or Fail.

## Health And Coverage

Health checks factor values within the active universe. A symbol's active span
runs from its first valid value through its last valid value; cells outside that
span do not count against active coverage.

The card can record Health metrics, their thresholds, the coverage basis, and
the exact failed fields. Treat missing or `null` Health evidence as unknown, not
as passed. When comparing two runs, compare Health directly only when their
windows, active-universe definitions, missing-value handling, and thresholds
match.

## Grade

The grade bands use cross-sectional Sharpe:

| Cross-sectional Sharpe | Grade |
| --- | --- |
| `< 0.8` | F |
| `0.8 – < 1.2` | D |
| `1.2 – < 1.4` | C |
| `1.4 – < 1.6` | B |
| `1.6 – < 1.8` | A |
| `1.8 – < 2.0` | S |
| `2.0 – < 2.2` | SS |
| `>= 2.2` | SSS |

The grade is relayed evidence, not a promotion decision. It does not override a
failed required check and does not say that a factor is ready for real-money
trading.

{% hint style="info" %}
A successful factor showed evidence under the tested conditions. A backtest is
evidence about the past, not a guarantee of future returns.
{% endhint %}
