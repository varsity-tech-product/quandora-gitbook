---
translation_status: pending
description: >-
  Five public Quandora skills, their evidence boundaries, and the explicit
  confirmations between them.
---

{% hint style="warning" %}
本页中文内容正在审核中，以下暂时显示英文原文。
{% endhint %}


# Quandora Workflow

Quandora separates creation from analysis and historical testing from
simulation. The public workflow is implemented through five skills:

```text
Factor Mining -> Factor Analysis -> Strategy Building
      ^                |                   |
      +-- user-approved factor experiment-+

Strategy Building -> Strategy Analysis -> Paper Trading
        ^                    |
        +-- user-approved strategy experiment
```

Analysis is read-only. A proposed factor experiment returns to Factor Mining; a
composition or configuration experiment returns to Strategy Building. Paper
Trading begins only after a separate explicit confirmation.

{% hint style="info" %}
All five skills are available to public users. Paper Trading is simulated.
Live trading is not part of the public product. See
[Product Availability](../trust/product-availability.md).
{% endhint %}

## 1. Factor Mining

Factor Mining starts from a public [Research Task](research-tasks.md) or a
custom idea. The agent reads the server contract, creates and validates a
contract-compliant [`plugin.py`](plugin.py.md), checks for materially similar
work, submits the exact validated source, and follows the returned run.

Output: one factor result and, when requested and available, one verified
Result Bundle ZIP.

## 2. Factor Analysis

Factor Analysis selects one exact run and reads owner-scoped,
server-persisted IS evidence. It diagnoses the [Factor Card](factor-card.md),
Health, rating fields, chart data, and inert source when needed.

Output: observations, inferences, alternatives, risks, and controlled
experiments. It does not submit or modify anything.

## 3. Strategy Building

Strategy Building lists eligible Official, Mine, and Shared factors. It composes
a public cross-sectional Strategy, shows the effective configuration, obtains
confirmation, submits the backtest, follows the same run, and can explicitly
export its verified Result Bundle.

Output: one canonical Strategy run with its exact factors and parameters.

## 4. Strategy Analysis

Strategy Analysis selects one exact run, reads its canonical configuration and
retained artifacts, and uses bounded numerical chart evidence for diagnosis.

Output: performance, risk, turnover, exposure, attribution, factor-combination,
and Paper-readiness analysis. It does not submit a new Strategy or Paper run.

## 5. Paper Trading

Paper Trading selects an eligible completed Strategy source and obtains a
separate confirmation before starting simulated execution. It can inspect the
current portfolio, closed positions, fills, funding, equity, and bounded code,
and it can stop the run after explicit confirmation.

Output: simulated execution evidence. A stopped run is terminal and cannot be
resumed.

## Explicit Handoffs

| From | To | Required user decision |
| --- | --- | --- |
| Factor Analysis | Factor Mining | Choose a proposed factor experiment and confirm a new run |
| Factor or Strategy evidence | Strategy Building | Choose eligible factors and confirm the exact configuration |
| Strategy Analysis | Strategy Building | Choose a proposed composition/configuration experiment |
| Eligible Strategy source | Paper Trading | Confirm the exact source and simulation settings |
| Paper evidence | Any research skill | Choose the next action; no automatic restart or repair |

## Local Outputs

Analysis does not depend on local files. In writable hosts, explicit completed
exports use:

```text
Quandora result/factor/<factor_slug>.zip
Quandora result/strategy/<strategy_slug>.zip
```

Each verified ZIP remains intact and is not automatically extracted or rebuilt.
Its runtime manifest is the authority for included, pending, and omitted items.

## Safety Boundary

Backtests and simulated Paper runs are evidence under defined conditions. They
are not future-return guarantees, financial advice, or permission for
real-money execution. Missing evidence remains missing, analysis remains
read-only, and mutations require explicit confirmation.
