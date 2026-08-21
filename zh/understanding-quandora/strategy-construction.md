---
translation_status: pending
description: >-
  How a promising factor becomes an operating strategy — and how the full
  strategy is tested before any money is at risk.
---

{% hint style="warning" %}
本页中文内容正在审核中，以下暂时显示英文原文。
{% endhint %}

# Strategy Construction

A factor is only a signal. It says "lean long here, lean short there." A **strategy** is the operating logic wrapped around that signal: what to trade, when to enter and exit, how big, how often, and under what risk limits. Strategy construction is the step that turns a promising [factor card](factor-card.md) into something that could actually run.

### From Factor To Strategy

A factor answered _what signal should we test?_ A strategy answers a harder question:

```
How would this factor actually be traded?
```

A good-looking factor can still fail here. Sizing, costs, rebalancing, and risk rules all change the picture — a signal with a strong backtest can become unprofitable once realistic trading friction is added.

### What A Strategy Specifies

Strategy construction should make each of these explicit:

* **Market / universe** — which instruments the strategy trades
* **Entry logic** — what signal level or condition opens a position
* **Exit logic** — what closes it
* **Ranking / selection** — how candidates are chosen when there are many
* **Position sizing** — how much capital each position takes
* **Rebalance frequency** — how often the book is refreshed
* **Cost assumptions** — expected fees, spread, and slippage
* **Liquidity filters** — minimum liquidity before an instrument is tradeable
* **Risk limits** — maximum exposure, drawdown, and concentration
* **Deployment target** — where the strategy is meant to run

### Strategy Evaluation

Once the rules exist, the full strategy is tested — not just the raw factor — after realistic costs, sizing, liquidity, and risk constraints are added. Strategy evaluation reports:

**Headline metrics**

* Sharpe Ratio
* Max Drawdown
* Calmar
* Hit Rate
* Turnover

**Portfolio NAV & drawdown charts**

* Net NAV
* Gross NAV
* Drawdown
* Max DD peak
* Max DD trough

**Net vs gross performance** (with the backtest fee rate applied)

* Fee Rate (backtest parameter)
* Annual return — net and gross
* Sharpe — net and gross
* Max Drawdown
* Turnover (average per bar)
* Turnover cost (cumulative, and as return)
* Total funding return
* Periods

**Attribution & per-symbol detail**

* Single-symbol PnL
* Single-symbol PnL rank
* CS attribution overview
* Position history

It answers:

```
Does the complete strategy survive more realistic testing?
```

If it fails, it can go back to strategy construction, or all the way back to factor mining. If it passes, it can move into paper trading.

### Trust Labels

A strategy carries a trust state so its evidence level is never ambiguous:

```
Backtest only   - tested on history only
Paper-tracked   - being watched forward without real money
Live-tracked    - running with real execution under limits
Verified        - sustained evidence across conditions
Experimental    - early, low-confidence
High risk       - elevated risk profile, handle with care
```

These labels keep a promising backtest from being mistaken for a proven live strategy.

### Where This Leads

A strategy that survives evaluation can move to paper trading to be watched
forward. Next: [Paper Trading & Monitoring](paper-trading-and-monitoring.md).

Strategy composition and backtesting are available to public users. The
step-by-step product interface is reserved in the
[Strategy Tutorial](../guides/strategy-tutorial.md) and will be completed by the
plugin and Product Backend owners.
