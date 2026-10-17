# Build A Portfolio

Combine **one to five distinct Strategies** with initial capital allocations,
then evaluate the combined historical result. One member is valid; five is a
limit, not a target.

## Before You Start

Choose eligible evaluated Strategies and a goal, such as reducing the core
Strategy's drawdown or a named exposure. Start with a credible core, identify
its main weakness, then consider a complementary member. Different names or
low correlation alone do not establish independent sources of return.

For an explicit composition, preserve the user's chosen members and weights.
For delegated selection, state which candidates were actually inspected and
which remain unverified. See [Analyze a Strategy](strategy-analysis.md).

## In The Web App

1. Open **Portfolio Center → Mine → New portfolio**.
2. In **Select strategies**, choose 1–5 completed Strategy backtests from your
   library, then select **Continue**.
3. In **Allocate capital**, enter the Portfolio name and optionally choose an
   icon. Review each member's capital allocation and the resulting weights.
   Follow the minimum amounts and increments displayed in the form.
4. Review the total allocation and the **BTC** backtest benchmark, then submit
   **Create**.
5. Open the created Portfolio and follow its backtest. Check the actual member
   results and common interval used before comparing performance.

Equal initial capital is a useful baseline. It does not imply equal risk
contribution, daily rebalancing, or fixed weights throughout the run.

## Ask Your Agent

For a proposal first:

```text
Use Quandora Portfolio Building to propose a Portfolio around my Core Strategy.
Look for one complementary Strategy that could reduce its drawdown. Explain the
candidate scope, evidence, initial weights, and gaps. Do not create it yet.
```

For an exact, authorized build:

```text
Create and backtest a Portfolio named Core and Diversifier using the two exact
Strategies we selected, with 70% and 30% initial capital weights. Preserve those
weights and compare the result against the core. Do not start an additional
Simulation account.
```

Custom weights must be positive and sum to one. The Agent uses the current
Portfolio contract, not arbitrary capital, date, fee, leverage, or source-run
overrides. The service resolves the actual Strategy backtests and common window
used by the Portfolio evaluation. Confirm that returned lineage in the result.

## Read Preparation States

**Preparing sources** means member research is being prepared. **Running** means
the Portfolio evaluation is underway. Follow the same run; neither state is a
reason to submit a duplicate. A failure should identify the available cause.

The Portfolio result and its BTC benchmark can become ready separately. A
pending benchmark does not mean the completed Portfolio result is empty.

## Revisions And Automatic Observation

Changing members or weights creates a new Portfolio in the same folder. Older
research and running accounts keep their original definitions. Rerunning an
unchanged Portfolio creates another backtest, not a new composition.

After a completed backtest, inspect any automatically associated Simulation
observation and its source. That association can refer to an earlier backtest
of the same immutable Portfolio. A pending association is not authorization to
create a duplicate account. An additional named Simulation account is an
explicit next action under [Portfolio Trading Analysis](paper-trading-tutorial.md).

## Done When

You can identify the exact Portfolio, member Strategies, initial weights, actual
source runs, test interval, and result state. Use [Portfolio Analysis](portfolio-analysis.md)
to judge incremental value. Use [Community and Sharing](community-and-sharing.md)
to publish or share an existing Portfolio without rerunning it.
