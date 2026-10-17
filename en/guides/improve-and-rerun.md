---
content_status: handoff
content_owner: plugin-and-product-backend
---

# Improve And Rerun A Factor

Use the diagnosis of one exact factor run to test one controlled change. Preserve
the original evidence so you can tell whether the change helped.

## In The Web App

Open the original result under **Research → Factors** and record its run, task,
horizon, and evidence scope. After the new experiment completes, return to the
new result and compare compatible metrics. Factor source revisions are handled
through the Agent workflow.

## Ask Your Agent

First request a proposal:

```text
Use Quandora Factor Analysis to propose one change to this result. State the
evidence motivating it, the expected effect, and what would disprove it.
```

Then authorize the selected experiment when ready:

```text
Use Quandora Factor Mining to implement and backtest that smoothing experiment.
Keep the original result unchanged. Validate the full revised source and compare
the resulting run with the original on compatible evidence.
```

A clear implementation-and-backtest request authorizes both steps. An Agent
should not ask again solely because it hands off from analysis to mining. If
you ask to review the change before submission, it must stop at that review.

## Compare Like With Like

Check task, horizon, data/evidence scope, and Health basis before comparing
Success reasons, coverage, Rank IC, autocorrelation, Sharpe, drawdown, turnover,
and costs. A different test window or applicability basis can explain a change
without validating the new mechanism.

Useful experiments include smoothing a noisy score, fixing missing outputs,
changing normalization, or removing one weak input. Avoid changing many
mechanisms at once or selecting only the best result from repeated trials.

## Done When

The new run is identified, the original remains available, and the comparison
states whether the intended effect occurred and what tradeoff appeared.
A failed or inconclusive experiment should be reported as such. Continue to
[Strategy Building](strategy-tutorial.md) only when you choose to test eligible
factors together.
