---
translation_status: pending
description: >-
  plugin.py is the contract-compliant factor source that an AI agent asks
  Quandora to validate and backtest.
---

{% hint style="warning" %}
本页中文内容正在审核中，以下暂时显示英文原文。
{% endhint %}


# Writing `plugin.py`

Factor Mining turns a task or custom idea into one complete `plugin.py` source:

```text
task or custom idea
-> scoped server contract
-> agent writes plugin.py and a readable formula
-> agent validates the exact complete source
-> user confirms submission
-> Quandora runs the backtest
```

## Start From The Current Contract

The server-provided construction contract is the source of truth for:

* exact `build_signal` inputs;
* supported data columns;
* forward horizon;
* required metadata and runtime sections;
* supported Python and runtime expressions;
* validation rules.

Do not copy an old signature or unsupported header from a previous run. The
agent sees allowed header names while Quandora binds changing market data
server-side.

## Formula And Source

A human-readable formula explains the mechanism. For example:

```text
signal = normalized_change(open_interest_close, 4, 20)
         * direction(one_day_return(close))
```

Plain English:

```text
Measure unusual open-interest change,
scale it by its recent behavior,
and align it with the latest price direction.
```

`plugin.py` makes that idea executable under the returned contract. The
submitted source must include the required metadata, `build_signal`, and any
declared runtime sections in the exact supported form.

## Validation Rules

The agent should:

* write one complete source file;
* keep `build_signal` parameters aligned with the returned data columns;
* return an aligned floating-point DataFrame;
* replace infinite outputs with `NaN` or a finite contract-safe fallback;
* check for materially similar factors;
* validate the complete source after every edit;
* repair only from safe structured validation diagnostics;
* submit the exact source that passed validation.

Generated factor source must not be imported, executed, or evaluated locally.
Quandora performs remote validation and evaluation.

## What `plugin.py` Is Not

`plugin.py` is not:

* a buy or sell instruction;
* a complete Strategy;
* a live trading system;
* a guarantee of profit;
* a filesystem path for the server to read.

It is the testable factor definition sent inline after validation and explicit
confirmation.

## Where The Accepted Source Goes

For a completed run, the Factor Mining-owned accepted source can be included in
the verified Result Bundle:

```text
Quandora result/factor/<factor_slug>.zip
```

The ZIP is the canonical completed local export. The agent does not create a
second extracted result tree or automatically execute the source it contains.
