---
translation_status: pending
description: Plain-English definitions for the quant terms used across Quandora
---

{% hint style="warning" %}
本页中文内容正在审核中，以下暂时显示英文原文。
{% endhint %}

# Glossary

Definitions are intentionally plain English. Ask your AI agent to expand any of these with examples from your own runs.

#### Research Objects

**Alpha** — A market signal that appears to predict returns beyond what general market movement (beta) explains. In Quandora, "alpha" and "factor" are used nearly interchangeably.

**Factor** — A measurable market feature turned into a score, e.g. "unusual open-interest change scaled by its volatility." Factors are the research artifact Quandora tests.

**Signal** — The output of a factor: the number per market per bar that says "lean long" or "lean short."

**Task card** — The agent's work order: what to investigate, which data headers are allowed, the forward horizon, and the task status. See [Task Card](task-card.md).

**plugin.py** — The executable form of a factor that Quandora's server can run. See [plugin.py](plugin.py.md).

**Factor card** — The structured result report: grade, evidence, caveats, next experiment. See [Factor Card](factor-card.md).

**Success / Fail** — Whether a factor passed all four required evidence checks:
IS Sharpe, absolute IS Rank IC, Health, and OOS/IS Sharpe stability.

**Grade (SSS–F)** — A cross-sectional Sharpe band. Grade describes backtest
strength separately from the Success/Fail result.

**Factor vs strategy vs deployment** — A factor is a research artifact. A strategy is a factor packaged with entry/exit rules, sizing, and risk limits. A deployment is a running instance of a strategy (paper or live).

**Trade call** — Discretionary advice on what to buy, sell, or hold. Quandora does **not** make trade calls. It runs the strategy you defined; it never tells you what to trade.

**Live trading** — An internal invitation-only capability that executes an
approved user strategy on a real account inside explicit permissions and risk
limits. It is not open to general public users and never represents Quandora's
own discretionary judgment.

#### Testing Terms

**Backtest** — Replaying history to see how a factor would have scored. Evidence about the past, not a promise about the future.

**In-sample (IS) / ALL** — In-sample is the data a factor was shaped on. ALL is the full backtest (in-sample + out-of-sample). Cards show both so you can check consistency; strong IS but weak ALL is the classic sign of overfitting.

**Walk-forward** — Repeatedly training on one window and testing on the next, marching through time — a stricter way to catch overfitting.

**Overfitting** — When a factor memorizes historical noise instead of capturing a real pattern. Looks great in-sample, fails on the full backtest.

**Forward horizon (`fwd_period`)** — How far ahead the factor is judged. Public tasks use 7 daily bars: "does today's score predict the next 7 days?"

**Blindbox** — Quandora's data rule: agents see allowed header names, never the full changing market data. Data binds server-side at evaluation. See [Our Data](our-data.md).

#### Metrics

**Sharpe ratio** — Return per unit of risk. Higher is better. Factor Success
requires IS cross-sectional Sharpe to be strictly greater than 0.8.

**IC (Information Coefficient)** — Correlation between factor scores and actual forward returns. Positive means the factor points the right way.

**Rank IC** — IC computed on rankings instead of raw values, so outliers have
less influence. Factor Success requires absolute IS Rank IC to be strictly
greater than 0.02.

**ICIR** — IC divided by its variability: is the predictive power consistent or streaky?

**WPCC** — Weighted position cross-correlation, reported alongside Mean IC and ICIR on the CS WPCC chart.

**IC decay** — How quickly the predictive edge fades as the forward horizon lengthens.

**Autocorrelation** — How similar the signal is to itself one bar later. Stable signals (high autocorrelation) are cheaper to trade than jittery ones.

**Turnover** — How much the implied portfolio changes between rebalances. High turnover means high trading costs.

**Calmar** — Annual return divided by max drawdown: return earned per unit of worst-case loss.

**Hit rate** — The share of bets that were profitable.

**Max drawdown** — The worst peak-to-trough loss over the test. The "see your downside" number.

**Net vs gross** — Gross performance is before trading costs; net is after fees, turnover cost, and funding. The gap between them is what costs eat.

**Cost viability** — Whether the factor's edge survives realistic trading
costs. It is diagnostic evidence rather than a Factor Success/Fail check. A
great signal that costs more than it earns is still not tradeable as-is.

**Regime** — The prevailing market condition (bull / bear / sideways, calm / volatile). Factor cards report the regime mix of the validation window.
