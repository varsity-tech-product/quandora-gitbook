---
description: Improve a tested factor and compare the next run with the original evidence.
content_status: handoff
content_owner: plugin-and-product-backend
---

# Improve And Rerun A Factor

An unsuccessful factor is not a dead end. Its Factor Card shows which part of
the evidence was weak and gives you a starting point for the next experiment.

The complete step-by-step rerun and comparison tutorial is being prepared. It
will cover:

* reviewing the factor's existing versions and backtest history;
* choosing one evidence-backed change and naming the research direction;
* saving the change as a new checkpoint without rewriting the original factor;
* rerunning an unchanged checkpoint when only the test configuration changes;
* comparing Success checks, grade, charts, and caveats;
* applying useful run parameters to a new checkpoint instead of mutating the
  completed run;
* stopping when repeated changes become curve fitting.

Until that tutorial is complete, ask your agent to explain the failed checks and
propose one small change at a time. Keep every earlier Factor Card as part of
the research record.

## The Choices To Keep Separate

| Your intent | What should happen |
| --- | --- |
| Explore a different idea for the same factor | Create a named research direction with a new checkpoint |
| Change the factor definition | Save a new immutable version |
| Test the exact same definition again | Create a new backtest run for the same version |
| Keep useful parameters discovered by a run | Save them into a new version; do not rewrite the completed run |

If another update reached the same research direction before yours, reload the
latest checkpoint and decide whether your change still applies. Quandora should
not silently overwrite either result.

Next, review [How Factors Are Judged](../understanding-quandora/how-factors-are-judged.md)
or continue to [Strategy Construction](../understanding-quandora/strategy-construction.md)
when you have a factor you want to combine into a strategy.
