---
description: >-
  The controlled bridge from paper evidence to live execution — your approved
  strategy inside explicit permissions and limits.
---

# Deployment & Live Trading

{% hint style="warning" %}
Live trading is internal invitation only and is not open to general public
users. Public accounts can use Factor Mining, strategy backtesting, and strategy
paper trading, but those results do not grant live-trading access.
{% endhint %}

For invited users, deployment is the stage after a strategy has been researched,
evaluated, paper-tracked, and separately approved for real-money execution.

Invite-only live trading can execute the user's approved strategy, never its
own judgment. That distinction is the whole point:

```
Trade call     = "you should buy / sell / hold this."
Execution rail = "run the strategy you approved, inside the limits you set."
```

The invite-only capability provides execution rails. It does not make
discretionary trade calls.

### Where Deployment Fits

The live workflow comes after evidence:

```
factor mining
-> factor evaluation
-> factor / strategy card
-> strategy construction
-> strategy evaluation
-> paper trading / monitoring
-> supervised deployment
-> live trading inside limits
```

Live trading is not a shortcut around research. It is the controlled final stage of the workflow.

### What A Deployment Contains

A deployment makes the operating state explicit:

* strategy name and version
* market / instrument universe
* entry and exit rules
* position sizing
* rebalance or execution frequency
* cost and slippage assumptions
* risk limits
* broker or exchange connection
* permission scope
* monitoring destination
* audit log
* kill switch

You should always be able to answer:

```
What strategy is running?
What account or venue can it touch?
What is the maximum allowed risk?
How do I stop it?
Where do I see what happened?
```

### Permission Scope

The connection to your broker or exchange is stated explicitly before launch:

* **Read-only access** — Quandora can see the account but not trade
* **Manual approval** — every order requires your confirmation
* **Delegated execution** — the strategy trades within pre-set limits you approved

Quandora never implies withdrawal permission. Execution access is not the same as fund access.

### Required Controls

Live trading requires:

* paper-verified evidence first
* explicit approval or delegated permission
* enforced risk limits
* order and position constraints
* live monitoring
* audit logs
* kill switch

### If A Strategy Decays

Monitoring does not treat a live strategy as permanently valid. If performance decays, risk limits are breached, or market behavior changes:

```
deployment is paused or stopped
-> report explains what changed
-> strategy is reviewed
-> the research loop restarts
-> factor mining searches for a repair or replacement
```

### What Quandora Does Not Do

Quandora does not:

* guarantee returns
* provide financial advice
* tell you what to buy, sell, hold, size, or close
* turn a backtest into a promise
* ignore user-defined risk limits
* run live trading without explicit permission

### The Control Clause

```
Quandora executes the user's strategy, never its own judgment.
```

The practical meaning:

```
user strategy
-> paper evidence
-> explicit permission
-> enforced limits
-> monitored execution
-> logs and kill switch
```

Deployment is the controlled bridge from paper evidence to live execution. See [Safety, Risk Limits & Kill Switch](safety-risk-limits-and-kill-switch.md) for the full control model.
