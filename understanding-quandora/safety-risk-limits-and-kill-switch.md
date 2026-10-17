# Safety And Execution Controls

Research, Simulation, and Live have different consequences. Keep the requested
object and action explicit, and read the resulting state before reporting success.

## Authorization Follows The User's Intent

Factor, Strategy, and Portfolio analysis are read-only. Portfolio Trading
Analysis is also read-only for a diagnosis; Simulation management requires an
actual account or run instruction. A request to build and backtest authorizes
that workflow, but not sharing or an additional account unless requested.

Existing authorization carries across skill handoffs. Ask when the target,
audience, settings, or intended action is materially unclear, or when the user
has explicitly required review before submission. Do not invent a fresh approval
step merely because another skill handles the next operation.

## Execution States Matter

Accepted is not running. Stopping is not stopped. An archive is not a stop, a
reset, or history deletion. Read the exact account and run after an operation;
recover the same pending operation rather than start a duplicate.

Simulation pause/resume and terminal stop are distinct. Live execution controls
are only available through authorized web flows. This documentation does not
promise a universal kill switch, guaranteed liquidation, a broker permission
model, or a particular set of Live risk limits.

## Evidence And Credentials

Missing or incomplete data stays unavailable. Do not turn short-run losses into
automatic retuning, restarting, or position closing. Proposed experiments stay
proposals until they fall within an authorized request.

Use the host's browser sign-in flow. Never paste exchange keys, API keys, bearer
tokens, passwords, or authorization codes into an Agent prompt. Use supported
web flows for account credentials.

See [Live Trading Access](deployment-and-live-trading.md) and
[Security, Privacy and Support](../trust/security-privacy-and-support.md).
