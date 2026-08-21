---
description: A task card is the structured research work order used by Factor Mining.
---

# Task Card

A task card tells the agent what market behavior to investigate, which data
headers it may use, what forward horizon applies, and which research context
should shape the factor.

```text
A research task is the topic.
A task card is the instruction packet.
```

Public task lists normally emphasize the human-readable task name and canonical
category. Internal task handles are opaque selectors: the agent should use an
exact returned handle and never guess, edit, or derive one.

## Why Task Cards Exist

A vague request such as `find a profitable trading idea` is too broad to
evaluate responsibly. A task card narrows the job to a market mechanism,
supported data, and a declared test horizon.

For example:

```text
Investigate whether deteriorating liquidity precedes market fragility.
Use only the task's allowed headers.
Generate contract-compliant plugin.py and a readable formula.
Validate the complete source before submission.
```

## Task Information You May See

| Field | Meaning |
| --- | --- |
| name | Human-readable task name |
| category | Canonical family such as `Microstructure`, `Technical`, or `Volatility` |
| description | The market behavior to investigate |
| allowed data | Exact headers available to the factor contract |
| forward period | Evaluation horizon in bars; current public tasks use seven daily bars |
| status | Whether the task is currently open |
| core question | The precise research question |
| primary alpha source | The proposed source of predictive information |
| economic principle | Why the mechanism could exist |
| microstructure or crypto mechanism | Market-specific explanation when applicable |
| research directions and feature hints | Candidate approaches, not required formulas |
| regime considerations and risk sources | Conditions that may weaken or invalidate the idea |
| target behavior | What successful factor output should capture |

The exact returned object can contain additional structured context. Use that
object and the scoped factor contract as the authority instead of copying a
static example from this page.

## Simplified Example

```json
{
  "name": "Market Microstructure And Liquidity Fragility",
  "category": "Microstructure",
  "description": "Test whether liquidity deterioration predicts market fragility.",
  "core_question": [
    "Does weakening liquidity precede unstable price behavior?"
  ],
  "allowed_data": [
    "open",
    "high",
    "low",
    "close",
    "volume",
    "quote_volume",
    "taker_buy_volume",
    "taker_sell_volume",
    "open_interest_close",
    "funding_rate_close",
    "liquidation_long_usd",
    "liquidation_short_usd",
    "binance_premium_index_close"
  ],
  "fwd_period": 7,
  "status": "open"
}
```

This example is explanatory. The task and contract returned in the current
session decide the exact fields, data headers, and horizon.

## How The Agent Uses A Task Card

Good agent behavior:

* select one exact returned task;
* restate its objective and mechanism;
* read the scoped construction contract;
* use only exact allowed headers;
* check for materially similar existing work;
* generate and fully validate [`plugin.py`](plugin.py.md);
* explain assumptions, applicability, and risks;
* ask before submitting a mutation.

The task card is a constraint, not a suggestion.
