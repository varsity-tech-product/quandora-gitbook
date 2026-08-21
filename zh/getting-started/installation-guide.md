---
translation_status: pending
description: Install and connect Quandora in supported AI agent hosts
icon: bolt
---

{% hint style="warning" %}
本页中文内容正在审核中，以下暂时显示英文原文。
{% endhint %}


# Installation Guide

Quandora is distributed as the `quandora@quandora` plugin. One authenticated
connection provides five skills:

| Skill | What it does |
| --- | --- |
| Factor Mining | Creates and backtests a factor, then retrieves one verified Result Bundle ZIP. |
| Factor Analysis | Diagnoses one exact factor result from server-persisted evidence. |
| Strategy Building | Selects eligible factors, composes a strategy, and runs its backtest. |
| Strategy Analysis | Diagnoses one exact strategy result and its numerical chart evidence. |
| Paper Trading | Starts, monitors, inspects, or stops simulated Paper runs after confirmation. |

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

## Verify The Five Skills

Ask your host to show the installed Quandora skills. You should see Factor
Mining, Factor Analysis, Strategy Building, Strategy Analysis, and Paper
Trading.

Use a namespaced skill command when the host supports it:

```text
/quandora:factor-mining show public tasks
/quandora:factor-analysis analyze my latest factor result
/quandora:strategy-building list available factors
/quandora:strategy-analysis analyze my latest strategy result
/quandora:paper-trading show my current Paper PnL
```

Natural-language requests work too, for example: `Use Quandora Factor Mining
to show public tasks.`

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

**Paper tools are missing after an older authorization.** Reconnect Quandora
and complete fresh browser consent. Refreshing an older token does not add newly
granted Paper permissions.

**No Result Bundle was saved.** Chat-only hosts may return a download instead
of writing to disk. A bundle can also still be materializing; ask the agent to
check the same completed result later. Do not start a duplicate run merely to
make a bundle appear.
