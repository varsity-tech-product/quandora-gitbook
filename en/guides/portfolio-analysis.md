# Analyze A Portfolio

Ask whether combining the selected Strategies added value for a stated goal.
This workflow analyzes an existing backtest without submitting new experiments.

## Before You Start

Identify the exact Portfolio backtest, its actual member Strategy runs, initial
weights, and evaluation interval. State the goal and baseline before judging
results. If no goal was set beforehand, describe the review as exploratory.

Useful baselines are the core Strategy, each actual member, and an available
same-member equal-capital Portfolio. A best member selected after seeing results
can be an additional labeled reference, not a replacement for the original
baseline. A baseline that has not been run remains unavailable.

## In The Web App

1. Open the Portfolio from **Mine**, **Favorite**, or **Markets**, keeping its
   ownership or sharing context.
2. Read the selected backtest, composition, allocations, and source results.
3. Inspect its equity, return, drawdown, and other available metrics; compare
   against the BTC benchmark only when the benchmark is ready.
4. Open relevant member research. Verify common dates and cost assumptions
   before interpreting a difference as a Portfolio improvement.

## Ask Your Agent

```text
Use Quandora Portfolio Analysis on this backtest. The goal is to reduce the
core Strategy's drawdown. Compare against the actual member runs and an existing
same-member equal-capital baseline if available. Explain net return/risk,
concentration, diversification, and implementation costs where evidence permits.
Do not create missing controls or change the Portfolio.
```

A concise verdict should be one of:

| Verdict | Meaning |
| --- | --- |
| Historical evidence supports improvement | Comparable evidence supports the declared goal, with the observed tradeoffs stated |
| Risk/return tradeoff | Some dimensions improved at a named cost in others |
| No demonstrated improvement | Comparable evidence shows no goal-relevant benefit |
| Insufficient evidence | Key evidence or comparability is missing |

## What The Evidence Can And Cannot Show

Initial capital weights are not risk-contribution weights. Independent Strategy
names, standalone Sharpe ratios, or isolated charts cannot establish a
correlation matrix or market neutrality. Correlations and joint-risk measures
need aligned underlying observations and an explained calculation.

Compare net performance with compatible costs. Opposing positions do not by
themselves prove realized netting savings. A higher Sharpe alone does not prove
independent alpha, lower tail risk, or durable diversification.

To ask whether a member helped, an existing leave-one-out control can be useful.
State how the remaining capital is allocated and what else stays fixed. If the
control does not exist, propose it rather than silently running every subset.

## Done When

The analysis gives one main verdict, its decisive evidence, important gaps,
and the smallest useful next experiment. Selecting and evaluating on the same
historical sample is not out-of-sample validation. A [forward test](paper-trading-tutorial.md)
starts a separate record of actual observations.
