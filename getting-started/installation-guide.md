---
description: Install and connect Quandora in supported AI agent hosts
icon: bolt
---

# Installation Guide

The web app can be used without installing an Agent plugin. To work through an
Agent, install `quandora@quandora` and connect your Quandora account. The seven
workflow skills are:

| Skill | What it does |
| --- | --- |
| Factor Mining | Creates, validates, and backtests factors. |
| Factor Analysis | Reads saved factor IS evidence. |
| Strategy Building | Builds and backtests a Strategy from eligible factors. |
| Strategy Analysis | Diagnoses one exact Strategy backtest. |
| Portfolio Building | Selects Strategies, allocates capital, backtests Portfolios, and handles requested discovery, favorites, and sharing. |
| Portfolio Analysis | Evaluates a Portfolio's historical incremental value. |
| Portfolio Trading Analysis | Analyzes forward Simulation/Live evidence and manages Simulation accounts and runs when requested. |

The first six workflows concern backtests. The seventh concerns forward tests.
Live inspection is read-only in the plugin; execution controls remain in the
web app for eligible accounts.

Quandora uses browser OAuth. Never paste an API key, bearer token, authorization
code, password, or other credential into an agent prompt.

## Codex

### Codex Desktop

Ask Codex Desktop to follow the current agent-readable guide:

```text
Read https://github.com/varsity-tech-product/quandora-plugins/blob/main/agent-install-guide/chatgpt.md completely, then install and authenticate Quandora exactly as instructed. I will complete the required browser sign-in, MFA, or consent action when it opens.
```

You can also add the plugin manually:

```text
Source: varsity-tech-product/quandora-plugins
Git ref: leave blank
Plugin: quandora@quandora
```

### Codex CLI

```bash
codex plugin marketplace add varsity-tech-product/quandora-plugins
codex plugin add quandora@quandora
```

Authorize when prompted. If authorization does not open automatically, run:

```bash
codex mcp login quandora
```

After installation or authorization, start a new task. If the skills remain
hidden in Codex Desktop, fully quit and reopen the application.

## Claude

### Claude Desktop Code Or Claude Code

In a new local Code session, ask Claude to follow the current guide:

```text
Read https://github.com/varsity-tech-product/quandora-plugins/blob/main/agent-install-guide/claude.md completely, then install and authenticate Quandora exactly as instructed. I will complete the required browser sign-in, MFA, or consent action when it opens.
```

For an interactive Claude Code terminal:

```bash
claude plugin marketplace add varsity-tech-product/quandora-plugins
claude plugin install quandora@quandora
claude mcp login plugin:quandora:quandora
```

Complete browser authorization, then start a new chat.

### Claude Desktop Chat

The normal Chat tab uses a Connector rather than the local Claude Code plugin.
In **Settings -> Connectors**, add and connect:

```text
Name: quandora
URL: https://mcp.quandora.ai/quant
```

Complete browser authorization, then start a new chat. Claude Desktop may
provide downloadable files in its sandbox instead of saving them directly to a
local result folder.

## Cursor Desktop

In a new Cursor Agent chat, enter:

```text
/add-plugin quandora@https://github.com/varsity-tech-product/quandora-plugins
```

Authenticate the plugin-provided `quandora` connection in the browser, then
start a new Agent chat.

## CodeBuddy CLI

Install or update the plugin through the CodeBuddy plugin manager:

```bash
codebuddy plugin marketplace add varsity-tech-product/quandora-plugins --name quandora
codebuddy plugin install quandora@quandora --scope user
codebuddy plugin list --json
```

CodeBuddy opens its browser authorization flow when the plugin connection is
established. No local MCP server or Quandora API key is required.

## WorkBuddy China Edition

Install `quandora@quandora` from the CodeBuddy-compatible Quandora marketplace
through WorkBuddy's plugin or custom-MCP interface. Reconnect the plugin,
complete the host-native browser authorization flow, and start a new chat. Do
not create a local MCP server or paste credentials.

## Kimi Code CLI

Install the plugin and reload it:

```text
/plugins install https://github.com/varsity-tech-product/quandora-plugins
/plugins info quandora
/plugins reload
```

Start a new session, authorize the plugin connection, and verify it:

```text
/mcp-config login plugin-quandora:quandora
/mcp
```

Complete browser authorization, then start another new session before using a
Quandora skill.

## Verify The Seven Skills

Ask your host to show the installed Quandora skills and check all seven names
above. If it shows the older five-skill layout, update the plugin using the
host's plugin manager, reconnect if needed, and start a fresh session. A tool
connection alone does not necessarily install skill instructions; follow the
host-specific installation guide.

Natural-language examples are portable across hosts:

```text
Use Quandora Factor Mining to show available research tasks.
Use Quandora Factor Analysis to explain this factor result without rerunning it.
Use Quandora Strategy Building to list eligible factors.
Use Quandora Strategy Analysis to analyze this exact Strategy backtest.
Use Quandora Portfolio Building to propose a Portfolio without creating it.
Use Quandora Portfolio Analysis to compare this result with its actual members.
Use Quandora Portfolio Trading Analysis to inspect my selected Simulation run.
```

When a host supports explicit skill commands, use the names it actually lists.
Do not substitute an old Paper Trading command for the new Portfolio Trading
Analysis workflow. The [workflow map](../understanding-quandora/quandora-workflow.md)
explains the boundaries between the skills.

## Result Files

Analysis reads server-persisted evidence and does not require a local ZIP. When
a writable host exports a completed result, it saves one verified archive:

```text
Quandora result/factor/<factor_slug>.zip
Quandora result/strategy/<strategy_slug>.zip
```

The ZIP is the canonical local output. It is not automatically extracted,
deleted, or rebuilt. Its runtime manifest records which items are included,
pending, or omitted. A readable bundle can be partial while an optional item is
still preparing.

## Troubleshooting

**Quandora skills are not visible after installation.** Start a new chat or
task. If they remain hidden, fully quit and reopen the host.

**Authorization failed.** Use the host-native connection flow above and
complete browser consent. Do not substitute an API key or local MCP server.

**New tools are missing after an update.** Confirm the installed plugin version,
then reconnect through the host and review any requested permissions. Start a
fresh session so tools and skills are rediscovered. Repeatedly refreshing an
older connection does not by itself grant new permissions.

**No Result Bundle was saved.** Chat-only hosts may return a download instead
of writing to disk. A bundle can also still be materializing; ask the agent to
check the same completed result later. Do not start a duplicate run merely to
make a bundle appear.
