# Live Trading Access

Live uses real exchange activity and funds. Access remains invite-only and
subject to the eligibility shown for your account. A research result, Simulation
account, or installed plugin does not grant Live execution access.

## Web And Agent Responsibilities

| Task | Where it belongs |
| --- | --- |
| Inspect an authorized owned Live account, its runs, positions, orders, fills, and performance | Web app or read-only Portfolio Trading Analysis |
| Connect an exchange account or provide credentials | The supported web flow; never an Agent prompt |
| Prepare or start Live execution, stop a Live run, or close Live positions | Authorized web controls |
| Manage Simulation accounts and run lifecycle | Web app or Portfolio Trading Analysis, within the requested scope |

The plugin does not perform Live account creation, credential submission, Live
start/stop, or position closing. A request to start Simulation cannot be reused
as authorization for any Live action.

## In The Web App

Open **Trading → Live** to inspect accounts available to you. Before using any
execution control, check the account, selected Portfolio, run, and the details
shown in the interface. If access or an action is unavailable, follow the
product's eligibility information; the Agent cannot bypass it.

This guide does not promise access for every account, a specific venue, or a
universal set of risk limits. Use the controls and requirements actually shown
for your authorized account.

For evidence-based review, use [Analyze Simulation and Live](../guides/portfolio-trading-analysis.md).
For product scope, see [Product Availability](../trust/product-availability.md).
