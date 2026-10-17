# Analyze A Factor

Decide whether a factor's recorded behavior supports its hypothesis, and what
one experiment could clarify next. This is a read-only backtest workflow.

## Before You Start

Choose one owned factor run or an active Official factor result you can access.
Use a result link or exact selection when names repeat. Factor Analysis uses
saved **In-Sample (IS)** evidence; it does not claim unseen OOS performance or
require a local ZIP.

## In The Web App

1. Open **Research → Factors** and select the relevant library or folder.
2. Open the factor and identify the result you intend to analyze.
3. Read [Success/Fail, Health, and grade](../understanding-quandora/how-factors-are-judged.md)
   separately. A completed run is not necessarily a successful factor, and a
   grade alone does not determine Strategy eligibility.
4. Read the metrics and available charts together: predictive direction,
   stability, coverage, turnover, and costs may tell different parts of the story.

## Ask Your Agent

```text
Use Quandora Factor Analysis on this result. Explain the hypothesis and the
recorded IS evidence, including Health, Rank IC, autocorrelation, Sharpe,
turnover, and modeled costs where available. Separate observations from
inferences. Propose one experiment without running it.
```

The Agent should explain which exact result it used, what is unavailable, and
what evidence would distinguish its preferred explanation from alternatives.
It should not fetch or infer private source for an Official factor.

## Done When

The conclusion connects the factor's mechanism to recorded evidence and names
its limitations. Missing Health or other required evidence remains unknown.
Costs are diagnostic evidence, not an additional Success/Fail gate.

To test an improvement, use [Improve and Rerun](improve-and-rerun.md). To combine
factors, use [Strategy Building](strategy-tutorial.md), which checks the actual
eligible factor pool again.
