---
description: Safety boundaries for public research, backtesting, and simulated Paper Trading.
---

# Safety, Risk Limits & Kill Switch

{% hint style="warning" %}
This page does not describe a public live-trading control system. Live trading
is not part of the public Quandora product.
{% endhint %}

## Public Workflow Boundaries

* Factor Mining and Strategy Building run historical evaluations.
* Factor Analysis and Strategy Analysis are read-only.
* Paper Trading uses simulated orders and never places live-money trades.
* A Paper run starts only after explicit user confirmation.
* Stopping a Paper run is terminal and also requires explicit confirmation.
* Losses or decay do not automatically stop, restart, or modify another
  workflow.

## Evidence Safety

Backtests and Paper runs can fail, lose simulated money, or behave differently
from earlier results. A grade, Success result, or Paper PnL is evidence under a
specific scope; it is not a guarantee or approval for real-money execution.

The analysis skills preserve unavailable evidence as unavailable and separate
observations from inference. Proposed improvements remain proposals until the
user explicitly chooses a new Factor Mining or Strategy Building experiment.

## Credential Safety

Use the host-native browser OAuth flow. Never paste exchange keys, API keys,
bearer tokens, authorization codes, passwords, or other credentials into an
agent prompt. Quandora's public plugin does not require withdrawal credentials
or a user-created local MCP server.

## About Live Controls

Terms such as broker permissions, live risk limits, audit logs, or a live kill
switch require a separately approved implementation and operating contract.
This documentation intentionally makes no claim that those controls are
available to public users.

Quandora provides research and simulation infrastructure. It does not provide
financial advice or guarantee returns.
