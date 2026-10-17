# Your First Factor

Test one market idea and understand one exact result. This workflow creates
historical evidence and does not place trades.

## Before You Start

Create or sign in to your [Quandora account](https://app.quandora.ai/auth/signin)
and [connect the plugin](installation-guide.md) in your Agent host. You can use
a public research task, describe your own hypothesis, or provide factor code.
No exchange credentials are needed for this research workflow.

## Ask Your Agent

Start with discovery if you want to choose a task:

```text
Use Quandora Factor Mining to show available research tasks. Explain what each
would test before we choose one.
```

Or authorize a complete first experiment:

```text
Use Quandora Factor Mining to choose one public research task, explain the
hypothesis, validate the factor, and run its backtest. Summarize the exact
result and any missing evidence.
```

The Agent reads the current [task contract](../understanding-quandora/task-card.md),
checks related work, writes and validates the complete factor source, then
submits and follows the same run. Validation checks the code contract; it is
not itself a saved backtest result. You do not need to write `plugin.py` yourself.

## In The Web App

1. Open **Research → Factors**.
2. Find the factor in your library and open its result. The sidebar **New**
   control creates a folder; factor authoring uses the Agent workflow above.
3. Match the factor and run to the Agent's result before reading its metrics.
4. Inspect the verdict, grade, Health, charts, and available research context.

Official factors can be a starting point for analysis without mining a new one.
Their visibility does not grant permission to inspect private source code.

## Analyze The Result

```text
Use Quandora Factor Analysis to explain this factor run. Separate observed IS
metrics from hypotheses, and suggest one controlled experiment. Do not submit
another run.
```

A completed calculation, its charts, and its optional export may become ready
at different times. Recheck the same result when evidence is preparing. Missing
evidence is not zero and does not justify a duplicate submission.

## Done When

You have one identified factor result and understand what its recorded evidence
supports. A failed factor is still a useful result. Read
[Analyze a Factor](../guides/factor-analysis.md) and
[How Factors Are Judged](../understanding-quandora/how-factors-are-judged.md)
before choosing the next experiment or eligible Strategy factors.

Analysis uses saved server evidence. If you need a local result, ask for the
optional verified Result Bundle ZIP; see [Result Files](installation-guide.md#result-files).
