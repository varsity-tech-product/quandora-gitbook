---
description: Install our plugin in your Claude Code/Codex/OpenClaw
icon: bolt
---

# Installation Guide

## **Codex**

### Codex Desktop:

Ask Codex Desktop to install and connect Quandora for you:

```
Install Quandora from varsity-tech-product/quandora-plugins, then connect Quandora Factor Mining.
```

Codex may ask before running the Codex CLI setup commands. These commands install the Quandora plugin into Codex, write Codex plugin/MCP configuration, and open Quandora OAuth. They do not grant Quandora access to your local files.

You can also add the plugin manually in Codex Desktop:

```
Source: varsity-tech-product/quandora-plugins
Git ref: leave blank
Plugin: quandora@quandora
```

### Codex CLI:

```
codex plugin marketplace add varsity-tech-product/quandora-plugins
codex plugin add quandora@quandora
```

Authorize when prompted. If Codex does not open the authorization flow automatically, use:

```
codex mcp login quandora
```

After installation or authorization, open a new chat. If Codex Desktop still does not expose Quandora tools, fully quit and reopen Codex Desktop.

## **Claude**

### Claude Code (CLI):

```
claude plugin marketplace add varsity-tech-product/quandora-plugins
claude plugin install quandora@quandora
```

In Claude Code, open `/mcp` and authenticate `quandora`, then start a new chat.

### Claude Desktop:

Claude Desktop requires both the Quandora plugin and the Quandora connector. After installing the plugin, manually add and connect the Connector in Claude Desktop:

```
Name: quandora
URL: https://mcp.quandora.ai/factor-mining
```

Use Settings -> Connectors, add the Connector above, click Connect, authorize Quandora in the browser, then start a new chat.

Claude Desktop can use the connected Quandora tools in chat, but local result-folder archiving is only guaranteed in local agent environments such as Claude Code, Codex, and OpenClaw. Claude Desktop's built-in file creation uses Claude's sandbox and may provide downloadable files rather than writing directly to a chosen local folder.

Factor Mining chart downloads use returned server `source_name` values for API calls and save local PNGs to returned `standard_local_path` values. When available, the raw signal artifact is saved as `signal_raw.parquet` in the factor result folder.

## **OpenClaw**

Clone the plugins repo and run the OpenClaw installer script:

```
git clone https://github.com/varsity-tech-product/quandora-plugins.git
cd quandora-plugins
./install-openclaw.sh
```

Authorize Quandora:

```
openclaw mcp login quandora
```

Open the printed URL, approve access, then run the code command printed by OpenClaw:

```
openclaw mcp login quandora --code <code>
```

Start a new OpenClaw chat after installation or authorization.

## Use Factor Mining

Use the skill command when available:

```
/factor-mining show public tasks
```

You can also ask naturally:

```
Use Quandora Factor Mining to show public tasks.
Use Quandora Factor Mining with my custom factor idea.
Use Quandora Factor Mining to resume a run and summarize results.
```

When the host supports local files, each run is saved under a stable folder named after the factor slug:

```
Quandora result/factor-mining/aggressive_flow_exhaustion_reversal/
```

The run folder contains the submitted `plugin.py`, a redacted `run_summary.json`, `factor_card_is.json` and `factor_card_all.json` when available, `artifact_manifest.json`, and PNG charts under `artifacts/is/` and `artifacts/all/`. The agent prints the result, artifact, and chart folder paths at the end of each run.

## Troubleshooting

**Quandora tools are not visible after install.** Start a new chat first — tools are discovered per chat. If they still do not appear, fully quit and reopen the app.

**Authorization did not open or failed.**

* Claude Code: open `/mcp`, authenticate `quandora`, then start a new chat.
* Codex: run `codex mcp login quandora`, complete the browser flow, then start a new chat. In Codex Desktop, fully quit and reopen if tools stay hidden.
* Claude Desktop: the plugin alone is not enough — add the `quandora` Connector (Settings -> Connectors), click Connect, and authorize in the browser.
* OpenClaw: run `openclaw mcp login quandora` and complete the printed flow, including the `--code` step.

**Asked for an API key?** You never need one. Quandora authenticates through the browser OAuth flow only — no API keys, bearer tokens, or credential pasting. If any tool or prompt asks you to paste a key, stop and reconnect through the official flow above.

**No result files on disk.** Local result-folder archiving works in local agent environments (Claude Code, Codex, OpenClaw). Chat-only hosts such as Claude Desktop may return downloadable files instead.
