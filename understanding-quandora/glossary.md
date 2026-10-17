# Glossary

Use these terms to keep the research object, test, and evidence scope clear.

## Objects And Workflows

**Factor** — A measurable market feature turned into a score. Its **signal**
can be ranked across the active universe.

**Factor Mining** — Creates, validates, and backtests factors; reads owned
history and exports available results when requested.

**Factor Analysis** — Read-only diagnosis of a saved factor result using IS
evidence from owned or accessible active Official research.

**Task Card** — A research work order defining the objective, allowed data,
horizon, and context. See [Task Card](task-card.md).

**`plugin.py`** — The executable factor definition validated and run by Quandora.
See [Writing plugin.py](plugin.py.md).

**Strategy** — An immutable combination of eligible factors and trading rules.
**Strategy Building** creates or revises it and runs backtests. **Strategy
Analysis** diagnoses an existing result without changing it.

**Portfolio** — An immutable set of 1–5 distinct Strategies and their initial
capital weights. A one-member Portfolio is valid. Weights can drift with member
performance; initial weights do not imply equal risk or daily rebalancing.

**Portfolio Building** — Selects members, allocates capital, creates or revises
Portfolios, runs backtests, and handles requested Community discovery, favorites,
and sharing.

**Portfolio Analysis** — Read-only evaluation of a Portfolio backtest's
incremental value against its actual members and declared baselines.

**Portfolio Trading Analysis** — Analyzes forward Simulation or Live evidence;
when requested, also manages Simulation accounts and runs. Live reads are read-only.

**Definition / version** — What is being evaluated. Revising a Strategy or
Portfolio creates a new immutable definition in the same folder.

**Backtest run** — One historical evaluation of a definition. Rerunning leaves
the definition unchanged and creates another result.

**Account / trading run** — The account contains forward activity and run
history. A run binds a selected Portfolio to a particular observation period.

**Publication / share** — Authorized access to Portfolio research. Visibility,
ownership, reuse, and trading eligibility are distinct permissions.

**Favorite** — A saved star on a Portfolio publication; it does not transfer
ownership or start execution.

**Result Bundle** — An optional verified ZIP for a completed result. Its
manifest records included, pending, and omitted items. Analysis does not need it.

## Testing And Evidence

**Backtest** — Replaying history to evaluate a Factor, Strategy, or Portfolio.

**In-Sample (IS)** — Historical evidence used within the declared research
sample. Current Factor Analysis uses the saved IS evidence it exposes.

**Out-of-sample (OOS)** — A held-out historical window. It remains a backtest,
not a forward test. Current Factor Analysis does not claim OOS evidence.

**ALL** — A combined Strategy scope that includes IS; it is not pure OOS.

**Forward test** — Observations that occur after the selected definition is
frozen and the run begins. Revisions form separate validation segments.

**Overfitting** — Capturing historical noise rather than a mechanism that generalizes.

**Forward horizon (`fwd_period`)** — How far ahead factor scores are evaluated.
Current public tasks use seven daily bars. This label does not mean forward trading.

**Data-header blindbox** — The Agent sees allowed headers while Quandora binds
changing market data server-side. See [Our Data](our-data.md).

**Baseline** — A declared reference for comparison, such as a core Strategy or
an existing same-member equal-capital Portfolio. Naming one does not create it.

**BTC benchmark** — The Bitcoin reference for Portfolio research. Its readiness
and test interval must be checked separately from the Portfolio result. Trading
benchmark views are a different evidence surface.

## Results And Metrics

**Factor Card** — The verdict, Health, grade, metrics, and caveats for a factor.
See [Factor Card](factor-card.md).

**Success / Fail** — Whether the recorded Rank IC, autocorrelation, Sharpe, and
Health requirements passed. **Grade (SSS–F)** is a separate cross-sectional
Sharpe band. See [How Factors Are Judged](how-factors-are-judged.md).

**Health** — Recorded checks of factor-output usability, coverage, and
missingness under a declared basis. Missing Health does not pass.

**Rank IC** — Correlation between signal rankings and forward-return rankings.
**ICIR** measures IC relative to its variability; **IC decay** tracks predictive
evidence across horizons.

**Autocorrelation** — Similarity between the signal and its previous-bar value.

**Sharpe ratio** — Return relative to variability under the reported convention.
Do not mix conventions, frequencies, or evidence windows in comparisons.

**Maximum drawdown** — The worst peak-to-trough decline in the evaluated path.
**Calmar** relates annual return to maximum drawdown.

**Turnover** — How much holdings change between rebalances.

**Net vs gross** — Net includes the applicable modeled or recorded costs; gross
is before them. Do not subtract fees twice from a net result.

**Cost viability** — Diagnostic evidence about whether an edge survives costs.
It is separate from the Factor verdict rules.

**Exposure / neutrality** — Exposure describes the risks a position or portfolio
carries. Neutrality needs a stated dimension, such as net dollar or market beta;
a neutral label does not prove all risk dimensions are neutral.

## Simulation And Live

**Simulation / Paper** — Forward execution with simulated orders and accounting.
Some interface labels still say Paper.

**Live** — Real exchange activity and funds, subject to account eligibility.
The plugin inspects existing owned Live evidence but does not execute Live actions.

**Net-account snapshot** — The authoritative recorded account-level net book.
Do not reconstruct it by adding member snapshots.

**Target / order / fill** — Intended exposure, submitted instruction, and
observed execution respectively. They are not interchangeable.

**Position cycle** — A net-position lifecycle. An open or partially closed
position remains current; a completed cycle belongs in closed history.

**Funding** — Funding transfers recorded under the account and run's conventions.

**Pause / resume** — A resumable Simulation lifecycle change, subject to current eligibility.

**Stop** — Terminal for that Simulation run. Starting again creates another run.

**Archive / restore** — Account visibility or availability changes under product
rules; they do not reset, delete, or stop execution.
