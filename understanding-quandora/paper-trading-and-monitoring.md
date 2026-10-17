# Forward Testing

A backtest replays historical data. A forward test records what happens after
a selected definition is frozen and a run starts. Historical OOS remains a
backtest; it does not become forward evidence because it was not used in fitting.

**Simulation** uses modeled execution. **Live** uses actual exchange activity
and real funds. Portfolio Trading Analysis reads both, while its account and
run management tools apply to Simulation only.

## What To Observe

Start with the exact account, run, Portfolio, start time, and evidence cutoff.
Read the authoritative net-account view, available net equity, positions,
completed position cycles, fills, fees, and funding. Preserve the distinction
between a target, an order, a fill, an open position, and a settled cycle.

An incomplete snapshot or delayed valuation is not evidence of zero positions
or zero PnL. Report freshness and coverage before interpreting performance.

## Curves And Risk Metrics

Available return lookbacks include **7D, 30D, 90D, 180D, 1Y, and 3Y**. The return
curve shows percentage performance; it is not the account-balance ledger.
Use actual observation times and the history that exists. Dates before the run
are not measured zero-return days.

Whole-run risk statistics can use completed UTC daily observations, while a
selected chart shows a different lookback and sampling. Do not recompute a
whole-run drawdown or Sharpe from a partial display curve. Too little history
can leave a statistic unavailable; it is not a zero-risk result.

## Forward Evidence Has Its Own Limits

Recent gains do not prove long-term validity, and recent losses alone do not
prove signal failure. Distinguish changing market conditions, implementation
costs, stale data, and execution problems before proposing a response.

A revised Portfolio or Strategy starts a separate validation segment. Do not
join selected winning periods from different versions into one track record.

For operations, use [Simulation Accounts and Runs](../guides/paper-trading-tutorial.md).
For diagnosis, use [Analyze Simulation and Live](../guides/portfolio-trading-analysis.md).
A one-time read does not establish continuous monitoring or future alerts.
