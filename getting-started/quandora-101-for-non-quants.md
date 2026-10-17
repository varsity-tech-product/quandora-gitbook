# Quandora 101

Quandora helps you test a trading idea, understand its evidence, and observe it
under new conditions. You can work in the web app, through an AI Agent, or both.

## Four Objects To Understand

| Object | Plain-language meaning | Example |
| --- | --- | --- |
| Factor | A rule that gives markets scores | Rank markets using a liquidity-related signal |
| Strategy | A trading rule built from factor scores | Combine two eligible factors and select top/bottom-ranked markets |
| Portfolio | One or more Strategies with initial capital allocations | Allocate 70% to a core Strategy and 30% to a complementary one |
| Account and run | Where a Portfolio is observed forward | Start a Simulation and inspect its positions and fills |

Examples explain the objects, not recommended investments or optimal settings.
A name is only a label: different objects can share a name. A saved definition
and a particular run let you identify exactly what was tested.

## Three Different Questions

**Does the idea show useful historical evidence?** Mine and analyze a Factor.

**Does a complete rule or combination work under its test assumptions?** Build
and analyze a Strategy, then a Portfolio when appropriate.

**What has happened since the run started?** Analyze Simulation or authorized
Live evidence through Portfolio Trading Analysis.

These questions use different evidence. A Factor grade does not establish that
a Portfolio is useful. A backtest does not prove future performance. Simulation
execution and actual Live execution are also different observations.

## What An Agent Adds

An Agent can turn a hypothesis into factor code, run authorized research,
explain saved results, and carry out supported account operations when asked.
It should identify the exact evidence, preserve missing data as missing, and
separate its interpretation from what the product actually recorded.

You can use the web app to browse results and build Strategies or Portfolios
without writing code. Tutorials offer both routes where supported. Start with
[Choose Your Path](choose-your-path.md) or the
[Workflow Map](../understanding-quandora/quandora-workflow.md).
