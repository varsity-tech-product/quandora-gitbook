---
translation_status: pending
description: How eligible factors become a public cross-sectional Strategy backtest.
---

{% hint style="warning" %}
本页中文内容正在审核中，以下暂时显示英文原文。
{% endhint %}


# Strategy Construction

A factor is a ranked signal. A Strategy combines one or more eligible factors
with a cross-sectional portfolio configuration and evaluates the combined
result after modeled fees and rebalancing.

## Eligible Factor Sources

Strategy Building can use:

* **Official** factors from read-only product inventory;
* **Mine** factors that belong to your eligible Strategy pool;
* **Shared** factors admitted to your Strategy pool.

All three use the same selector path when a Strategy is submitted. An external
`plugin.py` is a separate explicit import workflow and is not automatically
classified as Mine.

## Current Public Configuration

The public Strategy contract supports 1–20 factors and exposes the following
configuration boundary:

* Strategy name;
* factor selection or explicit factor weights;
* ranking;
* cross-sectional strategy type;
* start and end dates;
* initial cash;
* maker and taker fee rates;
* rebalance interval;
* attribution request.

If ranking and strategy type are omitted, the current default is a neutral
top/bottom 20% configuration. Always review the effective contract and defaults
returned in the current session before submitting.

Concepts such as a custom universe, bespoke entry/exit rules, liquidity
filters, live risk limits, or a deployment target are not current public submit
fields and should not be presented as selectable agent controls.

## Strategy Evaluation

The backtest evaluates the complete submitted configuration. Depending on
available artifacts, evidence can include:

* net and gross performance;
* NAV and drawdown paths;
* turnover and modeled costs;
* funding;
* exposure and neutrality;
* per-symbol PnL and attribution;
* position or trade history;
* bounded numerical data for the retained six-chart analysis surface.

The canonical run snapshot is the authority for the exact factor composition
and parameters. Missing artifacts stay unavailable rather than being inferred
from filenames or local files.

## Building And Analyzing Are Separate

**Strategy Building** lists factors, composes, submits, resumes, exports, and
archives supported Strategy results. **Strategy Analysis** is read-only: it
diagnoses one exact completed result and proposes controlled experiments.

An analysis proposal does not change a strategy. The user must explicitly
confirm a new Strategy Building submission.

## Where This Leads

A completed source may be eligible for simulated Paper Trading. Eligibility is
checked again when the source is selected; it is not guaranteed by a grade or
backtest status alone. Continue with the [Strategy Tutorial](../guides/strategy-tutorial.md)
or [Paper Trading Tutorial](../guides/paper-trading-tutorial.md).
