---
content_status: handoff
content_owner: plugin-and-product-backend
---

# Build A Strategy

Turn eligible factors into one cross-sectional Strategy and inspect its backtest.
You need at least one factor in your eligible Strategy pool.

## In The Web App

1. Open **Research → Strategies → Create strategy**.
2. Enter a name and use **Pick from your factors** to choose 1–20 eligible factors.
3. Choose the direction, liquidity threshold, and top/bottom ranking shown in
   the form. Review factor weighting where available.
4. Expand **Backtest execution parameters** to read the product-level test
   assumptions. These displayed assumptions are not all editable inputs.
5. Submit **Create strategy**, then follow the created result to completion.
   Open the Strategy result before judging its performance.

## Ask Your Agent

For selection without submission:

```text
Use Quandora Strategy Building to list the factors I can use. Suggest a small
composition for a long-short neutral strategy and explain the ranking and
weights. Show the plan without submitting it.
```

After choosing the plan:

```text
Build and backtest that Strategy using the selected factors, equal weights,
and top/bottom 20% ranking. Call it Momentum Study. Report the exact Strategy
and backtest result, including the effective assumptions.
```

These are illustrative settings, not a claim that this configuration is best.
The Agent checks current eligibility and supported fields. It follows the
returned run instead of resubmitting when calculation or artifacts take time.

## Revise Or Rerun

**Edit** changes the definition and creates a new Strategy in the same folder.
**Rerun** evaluates an unchanged Strategy again. Select the exact version before
either action, especially if names repeat. Archiving an individual Strategy is
separate from organizing a folder and from removing a particular result.

## Done When

The result identifies the Strategy definition, factor composition, effective
configuration, and backtest state. A terminal failure should show its reason;
a pending export does not invalidate a completed calculation.

Continue with [Analyze a Strategy](strategy-analysis.md). If you want forward
observation, first [build a Portfolio](portfolio-building.md), even when it has
only this one Strategy. An optional result export remains a verified ZIP and is
not required for analysis.
