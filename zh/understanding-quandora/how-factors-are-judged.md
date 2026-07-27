---
translation_status: pending
description: >-
  The Success checks and SSS–F grade behind every Factor Card — evidence, not
  promises.
---

{% hint style="warning" %}
本页中文内容正在审核中，以下暂时显示英文原文。
{% endhint %}

# How Factors Are Judged

Every submitted factor is evaluated on server-bound market data and returns a
Factor Card. Read two results separately:

* **Success or Fail** asks whether the factor cleared every required evidence
  check.
* **Grade** ranks the factor by its cross-sectional Sharpe after the required
  checks have been evaluated.

## Evaluation Windows

The backtest separates the period used to shape the factor from later held-out
evidence.

| Window | What it is |
| --- | --- |
| In-sample (IS) | The period used to develop and evaluate the original factor idea. |
| Out-of-sample (OOS) | A later held-out period used to check whether the evidence remained stable. |
| ALL | The full backtest view containing both IS and OOS periods. |

OOS evidence is still historical evidence. It is not the same as live or
paper-trading performance.

## Success Or Fail

A cross-sectional factor is successful only when all four checks pass:

| Check | Success condition | What it asks |
| --- | --- | --- |
| IS Sharpe | `> 0.8` | Was in-sample risk-adjusted performance strong enough? |
| Absolute IS Rank IC | `> 0.02` | Did the ranking have enough predictive relationship with forward returns? |
| Health | Passed | Was the factor output sufficiently complete and usable? |
| OOS/IS Sharpe | `> 0.5` | Did held-out Sharpe retain more than half of IS Sharpe? |

These conditions use strict greater-than comparisons. A value equal to the
threshold does not pass.

Cost viability, turnover, drawdown, and autocorrelation remain important
diagnostic evidence, but they do not determine Factor Success or Fail.

## Health And Active-Universe Coverage

Health checks the factor values inside the active universe. For each symbol,
its active span runs from its first valid value through its last valid value.
Cells outside that span do not count against coverage.

Coverage is calculated per timestamp as valid active symbols divided by active
symbols, then averaged across timestamps that contain active symbols. It is not
the percentage of non-empty cells across the complete raw signal matrix.

The Factor Card may show the individual Health metrics and the reason a Health
check failed. Treat unavailable Health evidence as not passing the Success
requirement.

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
| `≥ 2.2` | SSS |

Grade describes the strength of one backtest result. It does not override a
failed Success check and does not say that a factor is ready for real-money
trading.

{% hint style="info" %}
A successful factor showed evidence under the tested conditions. It does not
guarantee future returns. Backtests are evidence, not promises.
{% endhint %}
