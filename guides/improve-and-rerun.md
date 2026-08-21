---
description: Diagnose one tested factor and run a user-approved controlled experiment.
content_status: handoff
content_owner: plugin-and-product-backend
---

# Improve And Rerun A Factor

A failed or fragile factor is useful evidence. The safest improvement workflow
diagnoses one exact run, changes one mechanism at a time, and preserves the
original result.

## 1. Analyze The Exact Run

Use Factor Analysis for read-only diagnosis:

```text
/quandora:factor-analysis analyze my latest factor result
```

If more than one run could match, select the exact factor and run instead of
letting the agent guess. Factor Analysis reads server-persisted IS evidence and
should separate:

* observed metrics and Health fields;
* inferences about the mechanism;
* plausible alternative explanations;
* controlled experiments that could distinguish them.

It does not submit, resume, archive, or modify anything.

## 2. Choose One Controlled Change

Prefer a change with a clear reason and measurable expected effect. Examples:

* reduce missing output while preserving the economic idea;
* smooth a noisy signal and check the autocorrelation/turnover tradeoff;
* change normalization to improve cross-sectional ranking;
* remove one weak input instead of adding several new inputs;
* test whether a filter causes an applicability/Health mismatch.

For each proposal, record the motivating evidence, expected change, metric that
would confirm it, and main failure mode.

## 3. Confirm Before Creating A New Run

Analysis remains read-only. When you choose an experiment, explicitly ask
Factor Mining to create and submit it:

```text
Use Quandora Factor Mining to run the first proposed experiment. Keep the
original result unchanged and show me the exact change before submission.
```

The agent should show the new thesis and source-level change, validate the full
new `plugin.py`, and obtain confirmation before submission.

## 4. Compare Like With Like

Compare runs only when their task, horizon, evidence scope, active-universe
basis, and Health thresholds are compatible. Review:

* Success failure reasons;
* Health and missingness;
* Rank IC, autocorrelation, and Sharpe;
* path stability, drawdown, and turnover;
* whether the intended mechanism improved;
* whether a different risk appeared.

## History And Immutability

Factor Mining can browse caller-owned factor families, versions, and runs.
Historical source editing is not exposed in the current public agent workflow.
A terminal result stays unchanged; an approved experiment creates new evidence
instead of rewriting the old run.

Stop when repeated changes become curve fitting or when the evidence no longer
supports the original mechanism. Continue to [Strategy Construction](../understanding-quandora/strategy-construction.md)
only after you deliberately choose a factor for a strategy experiment.
