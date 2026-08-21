---
description: A research task tells the agent what kind of market pattern to test.
---

# Research Tasks

Research tasks are the starting point for a Quandora run.

They give your AI agent a focused market behavior to investigate, instead of asking it to "find alpha" from a blank prompt. A task turns a broad trading question into a structured research job with a goal, allowed data fields, hints, and an evaluation horizon.

***

### Why Research Tasks Matter <a href="#why-research-tasks-matter" id="why-research-tasks-matter"></a>

AI agents are good at generating ideas, but finance research needs more than ideas. A useful trading idea needs a clear question, usable data, testable logic, and a way to decide whether the result is strong or weak.

Research tasks give the agent those rails.

Instead of starting with:

```
Find me a good trading strategy.
```

Quandora starts with a narrower job:

```
Find a testable factor that detects liquidity fragility before volatility expands.
```

That difference matters. A narrow task helps the agent produce something Quandora can evaluate: a factor artifact, a formula, and a result card.

***

### Current Research Task Grouping <a href="#current-research-task-families" id="current-research-task-families"></a>

Quandora research tasks are grouped by the kind of market behavior they ask the agent to investigate.

#### Market Microstructure And Liquidity Fragility <a href="#market-microstructure-and-liquidity-fragility" id="market-microstructure-and-liquidity-fragility"></a>

This task asks whether a market is becoming fragile.

It looks for signs that liquidity is weakening, price is becoming easier to move, or liquidation cascades may create unstable conditions. The agent may study volume, taker flow, open interest, funding, liquidations, and premium data to create a testable liquidity-fragility factor.

Plain-English question:

```
Is the market becoming easier to push around?
```

#### Volatility Regime And Risk Compensation <a href="#volatility-regime-and-risk-compensation" id="volatility-regime-and-risk-compensation"></a>

This task asks whether the market is moving into a different volatility regime.

It looks for panic, squeeze setups, volatility expansion, and changing risk conditions. The agent tries to detect whether the market is becoming calmer, more explosive, or more unstable.

Plain-English question:

```
Is the market environment changing?
```

#### Order Imbalance And Persistent Pressure <a href="#order-imbalance-and-persistent-pressure" id="order-imbalance-and-persistent-pressure"></a>

This task asks whether there is persistent buy or sell pressure.

It looks for accumulation, distribution, trend continuation, and one-sided market pressure. The agent studies whether buyers or sellers are consistently dominating over time.

Plain-English question:

```
Is one side of the market quietly taking control?
```

#### Aggressive Order Flow And Informed Trading <a href="#aggressive-order-flow-and-informed-trading" id="aggressive-order-flow-and-informed-trading"></a>

This task asks whether aggressive traders are pushing the market in one direction.

It looks at taker flow, aggressive volume, short-term drift, and possible signs of informed capital. The agent studies whether fast market participants are leaving a useful footprint.

Plain-English question:

```
Are aggressive traders telling us something before price fully reacts?
```

#### Funding, Premium And Positioning Crowding <a href="#funding-premium-and-positioning-crowding" id="funding-premium-and-positioning-crowding"></a>

This task asks whether leverage is becoming crowded or unstable.

It looks for funding reversals, premium deviations, crowded positioning, and trend exhaustion. The agent studies whether too many traders are leaning the same way.

Plain-English question:

```
Is the trade becoming too crowded?
```

#### Price Momentum And Trend Quality <a href="#price-momentum-and-trend-quality" id="price-momentum-and-trend-quality"></a>

This task asks whether a trend is clean enough to trust.

It looks for trend-following factors with quality filters such as smoothness, volume confirmation, and flow support. The agent studies whether price movement is persistent or just noisy.

Plain-English question:

```
Is this a real trend or just random movement?
```

#### Volume Shock And Trend Confirmation <a href="#volume-shock-and-trend-confirmation" id="volume-shock-and-trend-confirmation"></a>

This task asks whether unusual volume confirms a price move.

It looks for abnormal volume, information arrival, and whether market activity supports or rejects a move. The agent studies whether a price move has real participation behind it.

Plain-English question:

```
Did volume confirm the move?
```

#### Liquidity Premium And Trading Cost <a href="#liquidity-premium-and-trading-cost" id="liquidity-premium-and-trading-cost"></a>

This task asks whether a signal is still useful after trading costs.

It looks for slippage risk, liquidity collapse, trading cost, and impact-adjusted liquidity. The agent studies whether an idea is practical after accounting for the cost of actually trading it.

Plain-English question:

```
Does the idea survive real trading friction?
```
