---
translation_status: pending
description: Plain-English definitions for the terms used across Quandora
---

{% hint style="warning" %}
本页中文内容正在审核中，以下暂时显示英文原文。
{% endhint %}


# Glossary

Definitions are intentionally plain English. Ask your AI agent to explain any
term using one exact run as an example.

## Research Objects And Skills

**Factor** — A measurable market feature turned into a score. Quandora tests
whether the score contains useful cross-sectional evidence.

**Signal** — The factor output: one value per market and bar that can be ranked
across the active universe.

**Task Card** — The structured research work order: objective, category,
allowed data headers, horizon, and research context. See [Task Card](task-card.md).

**`plugin.py`** — The executable factor definition validated and run by
Quandora. See [`plugin.py`](plugin.py.md).

**Factor Mining** — Creates, validates, and backtests a factor. It can also
browse caller-owned factor history and explicitly export a Result Bundle.

**Factor Analysis** — A read-only diagnosis of one exact factor result using
server-persisted IS evidence. It does not require a local ZIP.

**Factor Card** — The structured factor result containing Success/Fail, Health,
grade, metrics, caveats, and proposed experiments. See [Factor Card](factor-card.md).

**Success / Fail** — Whether absolute Rank IC, lag-1 autocorrelation,
cross-sectional Sharpe, and Factor Health all passed their current recorded
requirements.

**Grade (SSS–F)** — A cross-sectional Sharpe band, separate from Success/Fail.

**Strategy Building** — Selects eligible factors and submits a cross-sectional
strategy configuration for backtesting.

**Strategy Analysis** — A read-only diagnosis of one exact strategy run using
its canonical configuration, retained artifacts, and numerical chart evidence.

**Official / Mine / Shared** — Strategy factor sources. Official factors are
read-only product inventory; Mine are the caller's eligible Strategy factors;
Shared factors have been admitted to the caller's Strategy pool.

**Paper source** — A completed, owner-scoped, eligible Strategy run that can be
selected for simulated Paper Trading.

**Strategy Portfolio** — A static set of independently allocated strategy
sleeves that can be backtested and then run in Paper Trading.

**Result Bundle** — The verified ZIP exported for a completed Factor or
Strategy result. Its runtime manifest records included, pending, and omitted
items. Analysis does not depend on this ZIP.

**Live Trading** — Real-money execution. It is not part of the public Quandora
product, and this documentation does not specify an implementation or control
model for it.

## Testing Terms

**Backtest** — Replaying history to evaluate a factor or strategy. It is
evidence about the tested period, not a promise about the future.

**In-Sample (IS)** — Historical evidence in the window exposed by the current
public Factor Analysis contract.

**Out-of-sample (OOS)** — A separate held-out historical window. The current
public Factor Analysis skill does not claim OOS evidence.

**ALL** — A combined scope that includes IS. In Strategy Analysis, ALL must not
be described as pure OOS.

**Overfitting** — When a rule captures historical noise rather than a mechanism
that generalizes.

**Forward horizon (`fwd_period`)** — How far ahead factor scores are evaluated.
Current public tasks use seven daily bars.

**Data-header blindbox** — The agent sees the allowed header names while
Quandora binds changing market data server-side. See [Our Data](our-data.md).

## Factor Metrics

**Sharpe ratio** — Return per unit of variability. Current Factor Success
requires cross-sectional Sharpe to be strictly greater than `0.8`.

**Rank IC** — Correlation between factor-score rankings and forward-return
rankings. Current Factor Success requires its absolute value to be strictly
greater than `0.01`.

**Autocorrelation** — Similarity between the signal and its previous-bar value.
Current Factor Success requires lag-1 autocorrelation to be at least `0.4`.

**Health** — Recorded checks for factor-output usability, including coverage
and missingness under a declared basis. Unknown Health evidence does not pass.

**ICIR** — IC divided by its variability: a measure of consistency.

**IC decay** — How predictive evidence changes across forward horizons.

**Turnover** — How much the implied portfolio changes between rebalances.

**Calmar** — Annual return divided by maximum drawdown.

**Hit rate** — The share of observations or trades that were profitable under
the stated definition.

**Maximum drawdown** — The worst peak-to-trough decline in the evaluated path.

**Net vs gross** — Gross performance is before modeled costs; net performance
is after the applicable fee, turnover, and funding effects.

**Cost viability** — Diagnostic evidence about whether an edge survives modeled
costs. It is not a Factor Success/Fail gate.

## Paper Terms

**Paper Trading** — Simulated execution using an eligible strategy source. It
does not place live-money trades.

**Portfolio snapshot** — The current Paper balance, PnL, assets, and open or
partially open positions.

**Closed position history** — Completed net-position lifecycles. Open or
partially open positions remain in the current portfolio snapshot.

**Fill** — A simulated execution record.

**Funding** — Simulated funding transfers recorded for a Paper run.

**Stop** — A terminal action for a Paper run. A stopped run cannot be resumed;
starting again creates a new run.
