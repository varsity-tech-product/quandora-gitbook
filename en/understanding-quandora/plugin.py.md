---
description: >-
  plugin.py is the file that contains the factor formula your AI agent wants
  Quandora to test.
---

# plugin.py

`plugin.py` is created during the factor-mining stage.

```
task card
-> agent generates plugin.py and formula
-> Quandora evaluates the factor
-> result card returns
```

The task card tells the agent what kind of factor to build. `plugin.py` is the factor implementation the agent produces.

***

#### A factor usually starts as a formula.

Example:

```
signal = ts_delta(open_interest, 4) / ts_std(open_interest, 20) * sign(return_1h)
```

This says:

```
Look for unusual open-interest change,
scale it by recent open-interest volatility,
then align it with the direction of recent return.
```

Broken down:

| Part                         | Meaning                                                       |
| ---------------------------- | ------------------------------------------------------------- |
| `open_interest`              | How many positions are open in the market.                    |
| `ts_delta(open_interest, 4)` | How much open interest changed over 4 periods.                |
| `ts_std(open_interest, 20)`  | How unusual that change is compared with the last 20 periods. |
| `sign(return_1h)`            | Whether recent price movement was positive or negative.       |
| `signal`                     | The final factor score Quandora can test.                     |

***

### Why plugin.py Exists <a href="#why-pluginpy-exists" id="why-pluginpy-exists"></a>

The formula is easy for humans to read.

`plugin.py` makes the same formula executable, so Quandora can run it against market data.

```
task card
-> agent writes formula
-> agent turns formula into plugin.py
-> Quandora evaluates plugin.py
-> result card returns
```

### What plugin.py Is Not <a href="#what-pluginpy-is-not" id="what-pluginpy-is-not"></a>

`plugin.py` is not a trading bot.

It is not:

* a buy or sell instruction
* a complete strategy
* a guarantee of profit
* a live trading system

It is just the testable formula.
