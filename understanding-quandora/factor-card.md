---
description: >-
  The structured report every run returns — grade, evidence, risks, and what to
  test next.
---

# Factor Card

Every completed run returns a factor card: a structured report designed to be read by both humans and AI agents. The card is the trust artifact — it turns a raw backtest into something you can review, question, and build on.

#### How To Read A Card

Read in this order:

```
grade first
-> evidence second
-> risk / caveats third
-> next improvement fourth
```

#### The Grade

Every evaluated factor gets a single grade instead of a pass/fail label:

```
SSS, SS, S, A, B, C, D   cleared the evaluation gate, strongest to weakest evidence
F                        failed the gate
```

SSS is the strongest result and D is the weakest that still cleared the gate. A factor that fails the gate is graded F. A low grade is not a wasted run — it becomes memory that steers the next attempt. See [How Factors Are Judged](how-factors-are-judged.md) for the gate checks behind the grade.

#### Card Fields

| Field           | Meaning                                                         |
| --------------- | --------------------------------------------------------------- |
| grade           | SSS, SS, S, A, B, C, D (cleared the gate) or F (failed it)      |
| factor idea     | One-sentence explanation of what the factor tries to capture    |
| formula         | The human-readable version of the factor logic                  |
| data used       | Data headers, bar size, forward horizon, and evaluation windows |
| key metrics     | Sharpe, rank IC, autocorrelation, drawdown, turnover, and more  |
| assumptions     | What the backtest assumes                                       |
| caveats         | Why the signal may decay or fail                                |
| next experiment | What the agent or user should test next                         |

#### A Real Example

From a real run on the microstructure task — factor: "Taker Trade Size Imbalance", daily bars, 7-day forward horizon:

| Field                   | Value                              | Plain English                                            |
| ----------------------- | ---------------------------------- | -------------------------------------------------------- |
| Grade                   | D                                  | Cleared the gate, but the weakest passing tier           |
| Sharpe (CS)             | 0.81 (gate 0.8)                    | Just cleared the bar — real but not spectacular          |
| Rank IC                 | 0.012 (gate 0.01)                  | Weak but genuinely positive predictive ranking           |
| Autocorrelation (lag 1) | 0.89                               | Very stable signal, not bar-to-bar noise                 |
| Max drawdown            | −32%                               | The worst peak-to-trough loss in the backtest            |
| Turnover                | 0.63                               | How much the portfolio churns — this drives trading cost |
| Cost viable             | ❌                                  | The edge does not survive realistic trading costs        |
| Validation regime       | Bear 51% / Sideways 16% / Bull 32% | Tested across mixed market conditions                    |

Reading it the card's way: **grade** — D, it cleared the gate but sits at the weakest passing tier. **Evidence** — weak-but-real predictive power with a very stable signal. **Caveat** — it fails cost viability, so it is not tradeable as-is. **Next experiment** — reduce turnover or slow the signal down so more of the edge survives costs.

This is exactly what a factor card is for: a result that cleared the gate but still tells you the honest, load-bearing caveat before you risk anything on it.

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
