---
translation_status: pending
description: >-
  The control model behind every Quandora execution — what runs, who approves
  it, what stops it.
---

{% hint style="warning" %}
本页中文内容正在审核中，以下暂时显示英文原文。
{% endhint %}

# Safety, Risk Limits & Kill Switch

{% hint style="warning" %}
The controls on this page apply to the internal invitation-only live-trading
capability. Live trading is not open to general public users.
{% endhint %}

Everything Quandora executes runs inside a control model. This page states it plainly so there is no ambiguity about what the system can and cannot do with your capital.

### The Control Clause

```
Quandora executes the user's strategy, never its own judgment.
```

Quandora supplies the data, the tests, the risk and decay context, the evidence, the paper-trading history, and the execution rails. **Your** strategy, approvals, permissions, and limits decide what is allowed to run. This is the product promise and the compliance boundary at the same time.

### What Live Execution Requires

No strategy reaches live execution without all of the following:

* **Paper-verified evidence first** — a backtest alone is never enough
* **Explicit approval or delegated permission** — you opt in
* **Enforced risk limits** — maximum exposure, drawdown, concentration
* **Position and order constraints** — bounds on what any single order can do
* **Live monitoring** — continuous visibility into what is happening
* **Audit logs** — an immutable record of every action
* **Kill switch** — the ability to stop execution immediately

### The Kill Switch

The kill switch is not a nice-to-have. At any point you can halt execution, and the system stops acting on the strategy. Paused deployments stay visible with a clear paused state — they are not hidden or silently resumed.

### What Quandora Will Never Do

* make buy / sell / hold recommendations (that is a trade call — Quandora does not do this)
* guarantee returns or imply passive income
* treat a backtest as a promise of future performance
* ignore or override your risk limits
* execute live without your explicit permission
* touch withdrawal or fund-movement permissions

### Evidence, Not Promises

A backtest is evidence about the past. Paper trading is forward evidence. Neither is a guarantee. Quandora's job is to keep you inside an evidence loop where a decaying strategy gets paused, reviewed, and repaired — not to keep a weak strategy running.

Quandora provides research infrastructure and controlled execution rails. It is not financial advice.
