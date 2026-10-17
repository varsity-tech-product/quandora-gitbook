# Strategy Construction

A Factor produces a score. A Strategy combines **1–20 eligible factors** with
ranking, direction, and weighting rules. Its backtest evaluates the complete
trading rule, including the applicable modeled execution costs.

## Eligible Factors

Select from the Strategy factor picker or the Agent's eligible-factor list.
Ownership, visibility, a Factor grade, and eligibility are different properties.
An Official or shared result that you can read is not automatically selectable.
Use the eligibility returned for your account.

A new factor source goes through Factor Mining, validation, and evaluation
before it can be selected when eligible. Do not bypass that process by passing
an arbitrary `plugin.py` directly into Strategy creation.

## Configuration Boundaries

| Choice | How to handle it |
| --- | --- |
| Factors | Select exact eligible entries; 1–20 factors |
| Weighting | Equal weights or supported positive custom weights summing to one |
| Direction | Long-short neutral, long only, or short only |
| Ranking | State the top/bottom percentage or count |
| Liquidity threshold | Select the option exposed in the web form; do not assume the Agent exposes the same control |
| Backtest assumptions | Read the displayed execution parameters and the saved run configuration |

The web form shows uniform product-level execution parameters for comparison.
The Agent may expose a date range for a backtest; it must use only fields in its
current contract. Initial cash, maker/taker fees, attribution, and custom
universe overrides are not caller-configurable Agent backtest inputs.

## Definitions And Results

A Strategy definition is immutable. Changing factors or configuration creates a
new Strategy in the same folder. An additional backtest of an unchanged
Strategy creates a new run. Older definitions and results remain distinct.
See [Versions, Runs, and Accounts](versions-and-runs.md).

[Strategy Building](../guides/strategy-tutorial.md) creates or revises research.
[Strategy Analysis](../guides/strategy-analysis.md) reads an existing result and
proposes experiments. Analysis does not silently submit a revision.

For forward testing, place the evaluated Strategy in a one-member or multi-member
[Portfolio](../guides/portfolio-building.md). A successful Strategy backtest by
itself does not start an account.
