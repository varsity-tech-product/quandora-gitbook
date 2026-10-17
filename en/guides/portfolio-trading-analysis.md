# Analyze Simulation And Live

Explain an account's observed forward performance and execution. Start with an
existing Simulation run or an owned Live account you are authorized to inspect.
Live access is separate from research access; see [Live Trading Access](../understanding-quandora/deployment-and-live-trading.md).

## In The Web App

1. Open **Trading**, choose **Paper** or **Live**, then select the account and
   the intended run. Check its source Portfolio and lifecycle state.
2. Read account performance and its valuation time. Expand the net-account
   details to distinguish equity, balance, realized and unrealized PnL, fees,
   and settled funding where available.
3. Compare current holdings with the position table. Use **Closed positions**
   and **Filled Record** in Simulation, or **Position history** and **Fills** in
   Live, to inspect the corresponding evidence.
4. Use the return chart for the chosen window, and read coverage before
   interpreting risk statistics. Pending or incomplete evidence is a limitation.

## Ask Your Agent

```text
Use Quandora Portfolio Trading Analysis to review this account and exact run.
Report the source Portfolio, observation period, freshness, net performance,
exposure, and execution issues supported by the ledger. Explain plausible
reasons for divergence from its backtest and the missing evidence. Keep this
read-only; do not change the account or research.
```

For a focused question, ask for that evidence directly, such as whether funding
explains the difference between realized PnL and account return. The Agent should
use the authoritative net book rather than add member snapshots together.

## Interpret The Ledger Correctly

| Evidence | Interpretation |
| --- | --- |
| Net equity and account performance | Use the recorded capital and flow conventions; do not subtract included fees twice |
| Target or signal | Intended exposure, not proof of execution |
| Order | A submitted instruction, not necessarily a fill |
| Fill | Observed simulated or actual execution, according to account mode |
| Open or partially closed position | Current exposure; not a completed position cycle |
| Completed position cycle | Closed lifecycle evidence under that account's records |

Live order and fill reads can be bounded recent records. They are not a complete
historical export and cannot alone establish all-time fees, turnover, or a full
trade distribution. Slippage or latency claims need synchronized reference and
execution evidence, not just one of them.

## Compare With Research Carefully

A numerical comparison needs matching definitions, dates, capital/exposure
conventions, and costs. Without an available comparable control, discuss the
observed risks and expected mechanisms with qualifications; do not invent a
historical replay for the same dates.

Separate **observed evidence**, **inference**, **alternative explanations**, and
the **next investigation**. A short loss streak may be noise, an operational
fault, a cost effect, or a changing market regime. The available evidence must
support the explanation.

## Done When

The report identifies the account and run, describes freshness and coverage,
gives supported performance/risk observations, and proposes the smallest useful
next check. Missing evidence remains missing. Analysis does not pause, stop,
close positions, retune weights, or start a replacement run.

An authorized Simulation operation stays in this workflow; a research revision
goes to [Portfolio Building](portfolio-building.md), Strategy Building, or Factor
Mining as appropriate. Live setup and execution actions stay in the web app.
A request for ongoing monitoring needs a separately supported scheduling setup;
a current analysis does not promise future notifications.
