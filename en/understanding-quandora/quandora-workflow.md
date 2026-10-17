# Workflow Map

The seven workflows follow the same research objects in the web app and the
Agent plugin. Building creates evidence; analysis explains the evidence already
available. You can stop, revisit an earlier stage, or start from an existing
object.

| Workflow | Input | Outcome | Evidence type |
| --- | --- | --- | --- |
| [Factor Mining](../getting-started/quickstart.md) | Hypothesis, task, or factor source | Validated factor and evaluated run | Backtest |
| [Factor Analysis](../guides/factor-analysis.md) | Exact factor result | IS diagnosis and proposed experiments | Backtest |
| [Strategy Building](../guides/strategy-tutorial.md) | 1–20 eligible factors | Immutable Strategy and backtest | Backtest |
| [Strategy Analysis](../guides/strategy-analysis.md) | Exact Strategy run | Diagnosis of the combined trading rule | Backtest |
| [Portfolio Building](../guides/portfolio-building.md) | 1–5 distinct Strategies | Immutable Portfolio, weights, and backtest; sharing when requested | Backtest |
| [Portfolio Analysis](../guides/portfolio-analysis.md) | Exact Portfolio backtest | Evidence of incremental value against declared baselines | Backtest |
| [Portfolio Trading Analysis](../guides/portfolio-trading-analysis.md) | Simulation or Live account and run | Ledger-based forward diagnosis; Simulation management when requested | Forward test |

## Web And Agent Entry Points

**Research** contains Factors and Strategies. **Portfolio Center** contains
Markets, Mine, and Favorite. **Trading** contains Simulation and Live accounts.
Some Trading controls still use the label **Paper** for Simulation.

The Agent routes a natural-language request to the matching skill. A request to
analyze remains read-only. A request to build and backtest authorizes those
steps; changing skills does not erase that authorization. Ask a follow-up only
when an important choice or required authorization is missing.

## Keep The Object And Run Clear

A Strategy defines a combination of factors. A Portfolio defines a combination
of Strategies and their initial capital weights. Editing either creates a new
definition in the same folder. Rerunning an unchanged definition produces a new
backtest. Account observations belong to a particular forward run.

Names help you find objects, but two objects can share a name. Comparisons,
revisions, and simulations must use the exact selected definition and run. See
[Versions, Runs, and Accounts](versions-and-runs.md).

## Moving Into Forward Testing

A completed Portfolio backtest can have an automatically associated Simulation
observation. Check that association and its source before creating another
account or run. A single Strategy follows the same path through a one-member
Portfolio. Creating an additional named Simulation account is a separate choice.

Analysis may recommend an experiment, but does not automatically change a
Portfolio or stop a running account. Live account setup and execution actions
are handled in the web app for eligible users; the Agent reads existing Live
evidence only. See [Simulation Accounts and Runs](../guides/paper-trading-tutorial.md)
and [Live Trading Access](deployment-and-live-trading.md).
