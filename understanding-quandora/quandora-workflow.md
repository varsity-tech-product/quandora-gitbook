---
description: >-
  The Quandora research workflow — from Factor Mining through strategy paper
  trading, and when the loop restarts.
---

# Quandora Workflow

Quandora turns AI-generated market ideas into tested research artifacts,
evaluated strategies, and paper-trading runs. Live trading is a separate,
internal invitation-only capability.

The public workflow starts with Factor Mining, moves through evaluation and
strategy construction, then paper-tracks the result. If performance decays, the
research loop can return to Factor Mining.

In plain English:

```
Your AI agent proposes a market idea.
Quandora makes the idea prove itself.
```

Quandora is not a trade-calling system. It is a workflow for testing whether a
market idea has evidence before capital is risked.

{% hint style="info" %}
**Available to public users:** Factor Mining, factor evaluation, Factor Cards,
strategy composition and backtesting, and strategy paper trading. Live trading
is internal invitation only and is not open to general public users. See
[Product Availability](../trust/product-availability.md).
{% endhint %}

### The System Loop

```
        +----------------------+
        | factor mining        |<----------------+
        +----------------------+                 |
                  |                              |
                  v                              |
        +----------------------+                 |
        | factor evaluation    |                 |
        +----------------------+                 |
                  |                              |
                  v                              |
        +----------------------+                 |
        | factor / strategy    |                 |
        | card                 |                 |
        +----------------------+                 |
                  |                              | performance decay
                  |                              | restarts mining
                  v                              |
        +----------------------+                 |
        | strategy             |                 |
        | construction         |                 |
        +----------------------+                 |
                  |                              |
                  v                              |
        +----------------------+                 |
        | strategy evaluation  |                 |
        +----------------------+                 |
                  |                              |
                  v                              |
        +----------------------+                 |
        | paper trading /      |-----------------+
        | monitoring           |
        +----------------------+
```

Quandora is not just a one-time backtest. It is a research loop that can keep improving when performance decays.

### Step 1: Factor Mining

Where the system searches for candidate market signals. The user or agent starts from a [research task](research-tasks.md) — liquidity fragility, trend quality, funding crowding, volatility regime, order imbalance, volume confirmation, or trading cost.

Inside factor mining, the agent:

* reads the research task
* checks the [task card](task-card.md)
* reviews allowed [data headers](our-data.md)
* checks memory for duplicates or similar ideas
* generates [`plugin.py`](plugin.py.md)
* writes a human-readable formula

Output: a factor artifact (`plugin.py` + formula). Answers: _What signal should we test?_

### Step 2: Factor Evaluation

Quandora validates the artifact, binds supported market data server-side, and runs the backtest. The agent only ever sees allowed data headers; the full market data is bound server-side.

Evaluation may include:

* Sharpe
* RankIC / IC
* ICIR
* IC win rate
* autocorrelation
* return
* max drawdown
* turnover
* cost viability

Answers: _Did this factor show useful evidence?_ — not _Will it make money in the future?_ Backtests are evidence, not promises. See [How Factors Are Judged](how-factors-are-judged.md).

### Step 3: Factor / Strategy Card

Quandora returns a [Factor Card](factor-card.md) — the trust artifact. It may include:

* grade
* factor idea
* formula
* data used
* key metrics
* assumptions
* caveats
* reason for a low grade
* suggested next experiment

Every evaluated factor receives a Success/Fail result and a Sharpe-based grade:

```
Success / Fail             required evidence checks
SSS, SS, S, A, B, C, D, F cross-sectional Sharpe grade
```

If required evidence is weak or the diagnostics show material risk, the
workflow can stop or return to mining. If the evidence supports the next
experiment, the factor can move into strategy construction.

### Step 4: Strategy Construction

Turns a promising factor into a testable trading workflow. A factor is only a signal; a strategy defines how it would be used:

* market or universe
* entry logic
* exit logic
* ranking or selection method
* position sizing
* rebalance frequency
* cost assumptions
* liquidity filters
* risk limits
* deployment target

Answers: _How would this factor become an operating strategy?_ A good-looking factor can still fail once sizing, costs, and risk rules are added. See [Strategy Construction](strategy-construction.md).

### Step 5: Strategy Evaluation

Tests the full strategy, not just the raw factor, after realistic trading rules are added. It reports:

* net vs gross performance
* drawdown
* turnover and turnover cost
* funding
* per-symbol PnL and attribution
* position history

Answers: _Does the complete strategy survive more realistic testing?_ Full metric set on the [Strategy Construction](strategy-construction.md) page.

### Step 6: Paper Trading / Monitoring

The strategy is watched forward without risking real money — a passing strategy can be deployed to paper trading in one click. Monitoring tracks:

* simulated orders
* forward performance
* PnL and equity curve
* drawdown
* turnover
* cost drift
* regime changes
* signal decay
* alerts
* trade-log memory

Answers: _Does the strategy keep working after the backtest?_ This is the main decision point. See [Paper Trading & Monitoring](paper-trading-and-monitoring.md).

### Step 7A: If Performance Decays, Restart Factor Mining

Decay can mean:

* performance weakens
* drawdown becomes larger than expected
* turnover or costs increase
* the market regime changes
* the signal stops behaving like it did in the backtest

The old result becomes memory, and the agent receives a refreshed research task:

```
paper trading / monitoring detects decay
-> factor mining restarts
-> new candidate factors are generated
-> new factors are evaluated
-> the strategy is repaired, replaced, or retired
```

This is what makes Quandora a living research loop instead of a static backtest report.

### Step 7B: If Stable, Continue Monitoring

Stable simulated performance is evidence for continued monitoring. It does not
grant access to real-money execution.

### Invite-Only Live Trading

Live trading is available only through an internal invitation and is not part
of the general public workflow. For invited users, it is not a shortcut around
research. It requires:

* human approval
* strict limits
* monitoring
* logs
* risk controls
* the ability to stop execution

This capability executes the user's approved strategy, never Quandora's own
judgment. See [Deployment & Live Trading](deployment-and-live-trading.md) and
[Safety, Risk Limits & Kill Switch](safety-risk-limits-and-kill-switch.md).

### How To Use The Workflow

Quandora runs from your local agent environment — Codex, Claude Code, Cursor, or another local agent.

```
local agent
-> Quandora plugin / skill
-> generate plugin.py and formula
-> submit to Quandora
-> server-side evaluation
-> factor card
-> strategy construction and evaluation
-> paper trading / monitoring
```

The agent creates the factor artifact locally, then submits it for evaluation. The server is the source of truth for data and grades.

### Safety Boundary

Quandora is agentic quant infrastructure. It does not provide guaranteed returns or direct buy / sell instructions.

* Backtests are evidence, not future guarantees.
* A high grade is a research output, not guaranteed profit.
* A low grade is useful negative evidence.
* A result card is not financial advice.
* Live trading is internal invitation only and requires separate authorization.

See [Safety, Risk Limits & Kill Switch](safety-risk-limits-and-kill-switch.md) for the full control model.
