---
translation_status: pending
description: >-
  The structured report every run returns — grade, evidence, risks, and what to
  test next.
---

{% hint style="warning" %}
本页中文内容正在审核中，以下暂时显示英文原文。
{% endhint %}

# Factor Card

Every completed run returns a Factor Card: a structured report designed to be read by both humans and AI agents. The card is the trust artifact — it turns a raw backtest into something you can review, question, and build on.

#### How To Read A Card

Read in this order:

```
Success / Fail first
-> evidence second
-> risk / caveats third
-> next improvement fourth
```

#### Success And Grade

Every evaluated factor has a Success/Fail result and a grade:

```
Success / Fail             whether all required evidence checks passed
SSS, SS, S, A, B, C, D, F cross-sectional Sharpe grade
```

Success requires IS Sharpe, absolute IS Rank IC, Health, and OOS/IS Sharpe
stability to pass together. Grade is a separate Sharpe band. See
[How Factors Are Judged](how-factors-are-judged.md) for the exact rules.

#### Card Fields

| Field           | Meaning                                                         |
| --------------- | --------------------------------------------------------------- |
| Success / Fail  | Whether all required evidence checks passed                       |
| grade           | SSS, SS, S, A, B, C, D, or F from cross-sectional Sharpe         |
| factor idea     | One-sentence explanation of what the factor tries to capture    |
| formula         | The human-readable version of the factor logic                  |
| data used       | Data headers, bar size, forward horizon, and evaluation windows |
| key metrics     | Sharpe, rank IC, autocorrelation, drawdown, turnover, and more  |
| assumptions     | What the backtest assumes                                       |
| caveats         | Why the signal may decay or fail                                |
| next experiment | What the agent or user should test next                         |

#### Example

For a microstructure factor on daily bars with a 7-day forward horizon:

| Field                   | Value                              | Plain English                                            |
| ----------------------- | ---------------------------------- | -------------------------------------------------------- |
| Success                 | Fail                               | At least one required check did not pass                  |
| Grade                   | D                                  | Cross-sectional Sharpe falls in the D band                |
| IS Sharpe (CS)          | 0.81                               | Above the strict 0.8 Success threshold                    |
| Absolute IS Rank IC     | 0.012                              | Below the strict 0.02 Success threshold                   |
| Autocorrelation (lag 1) | 0.89                               | Very stable signal, not bar-to-bar noise                 |
| Max drawdown            | −32%                               | The worst peak-to-trough loss in the backtest            |
| Turnover                | 0.63                               | How much the portfolio churns — this drives trading cost |
| Cost viable             | ❌                                  | The edge does not survive realistic trading costs        |
| Validation regime       | Bear 51% / Sideways 16% / Bull 32% | Tested across mixed market conditions                    |

Reading it the card's way: **Success** — Fail because absolute IS Rank IC did
not exceed 0.02. **Grade** — D because cross-sectional Sharpe was 0.81.
**Caveat** — cost viability also failed, which is not a Success check but is a
strong warning against treating the factor as tradeable. **Next experiment** —
improve predictive ranking without increasing turnover.

This is exactly what a Factor Card is for: Success, grade, and practical risks
answer different questions and should be read together.

#### Charts

Each run saves its charts in two views — an **In-Sample** view and an **ALL** view (the full backtest = in-sample + out-of-sample) — so you can see whether the behavior holds up outside the data the factor was shaped on. A factor that looks strong in-sample but falls apart across the full backtest is a warning sign; that side-by-side is the consistency check.

The charts:

* **PnL** — profit and loss over the tested period
* **CS NAV** — cross-sectional net asset value curve
* **CS WPCC** — with Mean IC, Mean WPCC, and ICIR
* **IC Decay** — how the predictive edge fades as the horizon lengthens
* **Group Cumulative Return** — cumulative return split by factor buckets: do high scores outperform low scores?

#### Where Files Land

When your host supports local files, each run is archived under a stable folder named after the factor:

```
Quandora result/factor-mining/<factor_slug>/
  plugin.py
  run_summary.json
  factor_card_is.json
  factor_card_all.json
  artifact_manifest.json
  artifacts/is/*.png
  artifacts/all/*.png
```

Ask your agent to explain any field — the card is designed to be pasted into an AI conversation for critique and next steps.

Some charts or downloadable files can finish preparing after the run reaches
its terminal calculation state. A pending artifact is not necessarily absent.
Use the returned readiness state and check the same result again instead of
starting a duplicate run.
