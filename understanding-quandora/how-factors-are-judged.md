---
description: >-
  The gate checks and the SSS–F grade behind every factor card — evidence, not
  promises.
---

# How Factors Are Judged

Every submitted factor gets the same treatment: Quandora binds market data server-side, runs the backtest, applies a set of gate checks, and returns a grade. The thresholds used for your run are printed in your [factor card](factor-card.md), so you can always see exactly why a factor landed where it did.

### Evaluation Windows

Factors are not judged on one block of history. The backtest splits time into windows, and the card reports both an **In-Sample** view and an **ALL** view (the full backtest = in-sample + out-of-sample) so you can check consistency:

| Window              | What it is                                                                                   |
| ------------------- | -------------------------------------------------------------------------------------------- |
| In-sample (IS)      | The period the factor is allowed to "learn" from — where the idea gets shaped.               |
| Validation          | Later data the factor has not seen. This is where overfitting shows up.                      |
| Out-of-sample (OOS) | Held-out data folded into the ALL view — the closest thing to "would this have worked live?" |

A factor that shines in-sample but falls apart across the ALL view was likely fitted to noise. The card also reports the validation window's market regime mix (bear / sideways / bull) so you can see what conditions the factor was actually tested in.

### The Gate Checks

| Check                          | Typical threshold     | What it asks                                                     |
| ------------------------------ | --------------------- | ---------------------------------------------------------------- |
| Sharpe (cross-sectional)       | ≥ 0.8                 | Is the risk-adjusted return strong enough to matter?             |
| Rank IC                        | absolute value ≥ 0.01 | Does the factor's ranking actually line up with forward returns? |
| Factor autocorrelation (lag 1) | ≥ 0.4                 | Is the signal stable from bar to bar, or just noise?             |
| Cost viability                 | pass / fail           | Does the edge survive realistic trading costs and turnover?      |
| Duplicate / similarity         | memory check          | Is this genuinely different from factors already tested?         |

Thresholds can vary by task, market, and product stage — the exact values applied to your run are always included in the factor card.

### The Grade

Instead of a pass/fail label, every evaluated factor gets a single grade:

```
SSS, SS, S, A, B, C, D   cleared the gate, strongest to weakest evidence
F                        failed the gate
```

A factor that fails the gate checks above is graded **F**. A factor that clears the gate is ranked from **D** up to **SSS** by how strong and consistent its evidence is. A low grade is not a wasted run — it becomes memory: negative evidence that stops your agent from re-testing the same dead end and points the next attempt somewhere better.

{% hint style="info" %}
A strong grade means the factor showed evidence under test conditions. It does not mean the factor will make money in the future. Backtests are evidence, not promises.
{% endhint %}
