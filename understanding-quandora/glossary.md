---
description: Plain-English definitions for the quant terms used across Quandora
---

# Glossary

Definitions are intentionally plain English. Ask your AI agent to expand any of these with examples from your own runs.

#### Research Objects

**Alpha** — A market signal that appears to predict returns beyond what general market movement (beta) explains. In Quandora, "alpha" and "factor" are used nearly interchangeably.

**Factor** — A measurable market feature turned into a score, e.g. "unusual open-interest change scaled by its volatility." Factors are the research artifact Quandora tests.

**Signal** — The output of a factor: the number per market per bar that says "lean long" or "lean short."

**Task card** — The agent's work order: what to investigate, which data headers are allowed, the forward horizon, and the task status. See [Task Card](task-card.md).

**plugin.py** — The executable form of a factor that Quandora's server can run. See [plugin.py](plugin.py.md).

**Factor card** — The structured result report: grade, evidence, caveats, next experiment. See [Factor Card](factor-card.md).

**Grade (SSS–F)** — A factor card's verdict. Factors that clear the evaluation gate are graded SSS (strongest) down through SS, S, A, B, C, D; a factor that fails the gate is graded F.

**Factor vs strategy vs deployment** — A factor is a research artifact. A strategy is a factor packaged with entry/exit rules, sizing, and risk limits. A deployment is a running instance of a strategy (paper or live).

**Trade call** — Discretionary advice on what to buy, sell, or hold. Quandora does **not** make trade calls. It runs the strategy you defined; it never tells you what to trade.

**Live trading** — Execution of the user's approved strategy on a real account, inside explicit permissions and risk limits, with monitoring, audit logs, and a kill switch. Never Quandora's own judgment.

#### Testing Terms

**Backtest** — Replaying history to see how a factor would have scored. Evidence about the past, not a promise about the future.

**In-sample (IS) / ALL** — In-sample is the data a factor was shaped on. ALL is the full backtest (in-sample + out-of-sample). Cards show both so you can check consistency; strong IS but weak ALL is the classic sign of overfitting.

**Walk-forward** — Repeatedly training on one window and testing on the next, marching through time — a stricter way to catch overfitting.

**Overfitting** — When a factor memorizes historical noise instead of capturing a real pattern. Looks great in-sample, fails on the full backtest.

**Forward horizon (`fwd_period`)** — How far ahead the factor is judged. Public tasks use 7 daily bars: "does today's score predict the next 7 days?"

**Blindbox** — Quandora's data rule: agents see allowed header names, never the full changing market data. Data binds server-side at evaluation. See [Our Data](our-data.md).

#### Metrics

**Sharpe ratio** — Return per unit of risk. Higher is better; the evaluation gate currently looks for ≥ 0.8 cross-sectional Sharpe.

**IC (Information Coefficient)** — Correlation between factor scores and actual forward returns. Positive means the factor points the right way.

**Rank IC** — IC computed on rankings instead of raw values, so outliers don't distort it. The main "does it predict?" metric.

**ICIR** — IC divided by its variability: is the predictive power consistent or streaky?

**WPCC** — Weighted position cross-correlation, reported alongside Mean IC and ICIR on the CS WPCC chart.

**IC decay** — How quickly the predictive edge fades as the forward horizon lengthens.

**Autocorrelation** — How similar the signal is to itself one bar later. Stable signals (high autocorrelation) are cheaper to trade than jittery ones.

**Turnover** — How much the implied portfolio changes between rebalances. High turnover means high trading costs.

**Calmar** — Annual return divided by max drawdown: return earned per unit of worst-case loss.

**Hit rate** — The share of bets that were profitable.

**Max drawdown** — The worst peak-to-trough loss over the test. The "see your downside" number.

**Net vs gross** — Gross performance is before trading costs; net is after fees, turnover cost, and funding. The gap between them is what costs eat.

**Cost viability** — Whether the factor's edge survives realistic trading costs. A great signal that costs more than it earns is not tradeable.

**Regime** — The prevailing market condition (bull / bear / sideways, calm / volatile). Factor cards report the regime mix of the validation window.
