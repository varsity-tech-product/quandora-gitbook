---
translation_status: pending
description: The current boundary between public Quandora workflows and real-money execution.
---

{% hint style="warning" %}
本页中文内容正在审核中，以下暂时显示英文原文。
{% endhint %}


# Deployment & Live Trading

{% hint style="warning" %}
Live trading is not part of the public Quandora product. Public accounts can use
Factor Mining, Factor Analysis, Strategy Building, Strategy Analysis, and
simulated Paper Trading. None of those results grants real-money execution.
{% endhint %}

## What The Public Product Supports

The public workflow produces historical or simulated evidence:

```text
Factor Mining -> Factor Analysis
-> Strategy Building -> Strategy Analysis
-> simulated Paper Trading
```

Factor and Strategy backtests describe tested historical conditions. Paper
Trading uses simulated orders. These workflows do not connect a public user to
a broker or exchange for real-money execution.

## What This Documentation Does Not Claim

This public documentation does not specify a live-trading implementation,
broker permission model, launch procedure, supported venue, risk-limit schema,
or operational control system. Do not infer those capabilities from a factor
grade, strategy result, Paper run, plugin tool, or account state.

If real-money execution becomes a documented public capability, Quandora will
publish a separately reviewed availability, authorization, risk, monitoring,
and support contract before users are asked to rely on it.

## User Safety Boundary

Quandora research outputs are not financial advice, guaranteed returns, or
instructions to buy, sell, hold, size, or close a position. Users remain
responsible for decisions made outside the public research and simulation
workflow.

For the currently documented boundary, see [Product Availability](../trust/product-availability.md)
and [Safety, Risk Limits & Kill Switch](safety-risk-limits-and-kill-switch.md).
