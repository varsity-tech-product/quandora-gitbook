# Versions, Runs, And Accounts

Use names to find research; use the exact selected object and run to operate on
it. Two items can have the same display name and still be different objects.

| Object | What it represents | What changes it |
| --- | --- | --- |
| Factor result | One evaluated factor and its recorded evidence | A new experiment produces new evidence |
| Strategy | An immutable factor composition and configuration | Editing creates a new Strategy in the same folder |
| Strategy backtest | One historical evaluation of a Strategy | Rerunning creates another run |
| Portfolio | An immutable set of Strategies and initial weights | Changing members or weights creates a new Portfolio in the same folder |
| Portfolio backtest | One evaluation using resolved member runs and interval | Rerunning creates another result |
| Account | The container for Simulation or Live activity | Account management does not rewrite research |
| Trading run | One forward observation/execution period tied to its source | Starting another run creates separate history |
| Publication or share | Authorized access to an owned Portfolio's research | Sharing changes access, not the research definition |

## Revision, Rerun, And Archive

A revision changes a definition. A rerun changes the evaluation while preserving
the definition. Archiving changes availability or organization under the
product's rules; it does not mean “stop execution” or erase a historical ledger.
A folder groups research and is not itself a Strategy or Portfolio definition.

When an action targets an individual Strategy, it should not be interpreted as
archiving every Strategy in its folder. Likewise, selecting a new Portfolio
version does not migrate a running account to that version.

## Accounts And Runs

An account may have run history. Always select the intended run before reading
performance or requesting pause, resume, or stop. Pausing and stopping have
different lifecycle meanings; see [Simulation Accounts and Runs](../guides/paper-trading-tutorial.md).

Automatic Simulation observations can be associated with an existing immutable
Portfolio. Inspect the association's actual source, rather than assuming it
belongs to the most recent backtest displayed.

## Keep Comparisons Traceable

Record the definition, run, interval, and evidence cutoff for each comparison.
After a revision, begin a separate validation segment. Do not concatenate the
best periods from different tuned versions into one forward track record.
