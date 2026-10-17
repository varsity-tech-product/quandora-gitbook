---
content_status: handoff
content_owner: plugin-and-product-backend
---

# Simulation Accounts And Runs

Use Portfolio Trading Analysis to manage Simulation accounts and observe
Portfolio behavior after a run starts. Some web controls use **Paper** for
Simulation. These runs use simulated execution, not real funds.

## Before You Start

Select an eligible owned Portfolio or an authorized Community publication/share.
For one Strategy, first create and backtest a one-member Portfolio. Check for
an existing automatic Simulation association before creating another account.

An account and its run are different objects. Decide whether you want to inspect
an existing run, start a run in an existing account, or create an additional
named account. Account quotas and starting settings are enforced by the product.

## In The Web App

1. Open **Trading** and select **Paper**. Use the account list to open an existing
   account and inspect its active run or run history.
2. To create an additional account, select **Create Paper account**, enter a
   name, and submit **Create account**. Creating the account alone does not
   choose a Portfolio or prove that a run is executing.
3. Choose an eligible Portfolio through the account's selection flow. Review
   the displayed settings and submit the start action when ready.
4. Check the resulting run state. Read **Current Position**, **Closed positions**,
   **Filled Record**, and the net-account details as applicable.
5. Use **Pause**, **Resume**, or **Stop** only for the specific run you intend to
   change. Account management and run execution are separate actions.

## Ask Your Agent

Inspect first without starting anything:

```text
Use Quandora Portfolio Trading Analysis to find the Simulation already associated
with this Portfolio. Show its account, exact run, source, and current state.
Do not create or start another account.
```

For an additional account when that is what you want:

```text
Create a Simulation account named Core Observation and start the exact Portfolio
we selected. Use the starting leverage we agreed. Follow the same operation to
its final state and report the account and run. Do not create a replacement if
the initial response is delayed.
```

If required settings are missing, the Agent asks for them. It must recover the
same operation after a timeout or uncertain response. **Accepted** means the
request was accepted, not that execution is already running. A failed start can
leave an account that still needs to be reported and managed.

## Lifecycle And Account Actions

| Action | Meaning |
| --- | --- |
| Rename account | Changes the account label; preserves its history |
| Archive / restore account | Changes account visibility or availability under eligibility and quota rules; does not stop, reset, or delete history |
| Start | Starts a new eligible Portfolio run in the chosen account |
| Pause | Requests a pause of the current run; read the returned state |
| Resume | Continues an eligible paused run after current plan and sharing checks |
| Stop | Ends that run; a stopped run cannot be resumed |

Starting again after a stop creates a new run. Account reset, history deletion,
and editing active capital are not plugin capabilities. An archived account is
not a substitute for a stopped run. During settlement or another transition,
wait for the same operation's outcome instead of forcing a new start.

## Done When

The account and exact run are identified, the final returned state is clear,
and the source Portfolio matches your intent. A request to analyze performance
alone never authorizes pause, stop, a new version, or a new account.

Continue with [Analyze Simulation and Live](portfolio-trading-analysis.md).
Real Live execution controls belong to the web app for eligible accounts;
Simulation authorization never authorizes a Live action.
