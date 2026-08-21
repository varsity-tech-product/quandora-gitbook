---
translation_status: draft
description: 在受支持的 AI Agent Host 中安装并连接 Quandora
icon: bolt
---

# 安装指南

Quandora 通过 `quandora@quandora` 插件发布。完成一次认证连接后，即可使用五项 Skill：

| Skill | 作用 |
| --- | --- |
| 因子挖掘 | 创建并回测因子，然后获取一个经过校验的 Result Bundle ZIP。 |
| 因子分析 | 根据服务端留存的证据，诊断一条明确的因子结果。 |
| 策略构建 | 选择符合条件的因子，组合策略并运行回测。 |
| 策略分析 | 诊断一条明确的策略结果及其数值图表证据。 |
| 模拟盘 | 经过确认后启动、监控、检查或停止模拟盘运行。 |

Quandora 使用浏览器 OAuth。不要在 Agent Prompt 中粘贴 API Key、Bearer Token、Authorization Code、密码或其他凭据。

## Codex

### Codex Desktop

让 Codex Desktop 按照当前 Agent 可读指南操作：

```text
Read https://github.com/varsity-tech-product/quandora-plugins/blob/main/agent-install-guide/chatgpt.md completely, then install and authenticate Quandora exactly as instructed. I will complete the required browser sign-in, MFA, or consent action when it opens.
```

也可以手动添加插件：

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

按提示完成授权。如果授权页面没有自动打开，运行：

```bash
codex mcp login quandora
```

安装或授权完成后，开始一个新任务。如果 Codex Desktop 仍未显示 Quandora Skills，请完全退出并重新打开应用。

## Claude

### Claude Desktop Code 或 Claude Code

在新的本地 Code Session 中，让 Claude 按照当前指南操作：

```text
Read https://github.com/varsity-tech-product/quandora-plugins/blob/main/agent-install-guide/claude.md completely, then install and authenticate Quandora exactly as instructed. I will complete the required browser sign-in, MFA, or consent action when it opens.
```

在交互式 Claude Code Terminal 中运行：

```bash
claude plugin marketplace add varsity-tech-product/quandora-plugins
claude plugin install quandora@quandora
claude mcp login plugin:quandora:quandora
```

完成浏览器授权，然后开始一个新对话。

### Claude Desktop Chat

普通 Chat Tab 使用 Connector，不使用本地 Claude Code 插件。在 **Settings -> Connectors** 中添加并连接：

```text
Name: quandora
URL: https://mcp.quandora.ai/quant
```

完成浏览器授权，然后开始一个新对话。Claude Desktop 可能会在其 Sandbox 中提供下载文件，而不会直接写入本地结果目录。

## Cursor Desktop

在新的 Cursor Agent Chat 中输入：

```text
/add-plugin quandora@https://github.com/varsity-tech-product/quandora-plugins
```

在浏览器中认证插件提供的 `quandora` 连接，然后开始一个新的 Agent Chat。

## CodeBuddy CLI

通过 CodeBuddy Plugin Manager 安装或更新：

```bash
codebuddy plugin marketplace add varsity-tech-product/quandora-plugins --name quandora
codebuddy plugin install quandora@quandora --scope user
codebuddy plugin list --json
```

建立插件连接时，CodeBuddy 会打开浏览器授权流程。无需本地 MCP Server 或 Quandora API Key。

## WorkBuddy 中国版

通过 WorkBuddy 的插件或自定义 MCP 界面，从兼容 CodeBuddy 的 Quandora Marketplace 安装 `quandora@quandora`。重新连接插件，完成 Host 原生的浏览器授权流程，然后开始新对话。不要创建本地 MCP Server，也不要粘贴凭据。

## Kimi Code CLI

安装并重新加载插件：

```text
/plugins install https://github.com/varsity-tech-product/quandora-plugins
/plugins info quandora
/plugins reload
```

开始一个新 Session，认证插件连接并确认状态：

```text
/mcp-config login plugin-quandora:quandora
/mcp
```

完成浏览器授权，然后再开始一个新 Session，之后再使用 Quandora Skill。

## 确认五项 Skill

让 Host 显示已经安装的 Quandora Skills。你应该能看到因子挖掘、因子分析、策略构建、策略分析和模拟盘。

Host 支持命名空间命令时，可以使用：

```text
/quandora:factor-mining show public tasks
/quandora:factor-analysis analyze my latest factor result
/quandora:strategy-building list available factors
/quandora:strategy-analysis analyze my latest strategy result
/quandora:paper-trading show my current Paper PnL
```

也可以使用自然语言，例如：`Use Quandora Factor Mining to show public tasks.`

## 结果文件

分析直接读取服务端留存的证据，不依赖本地 ZIP。当可写 Host 导出已完成结果时，会保存一个经过校验的压缩包：

```text
Quandora result/factor/<factor_slug>.zip
Quandora result/strategy/<strategy_slug>.zip
```

ZIP 是本地规范结果，不会自动解压、删除或重新构建。它的 runtime manifest 会记录已包含、等待中和省略的项目。某些可选项目仍在准备时，`partial` 状态的包也可能可以正常读取。

## 故障排查

**安装后看不到 Quandora Skills。** 开始一个新对话或新任务。如果仍然不可见，请完全退出并重新打开 Host。

**授权失败。** 使用上文对应 Host 的原生连接流程，并完成浏览器授权。不要改用 API Key 或本地 MCP Server。

**使用旧授权后看不到模拟盘工具。** 重新连接 Quandora 并完成新的浏览器授权。刷新旧 Token 不会自动获得后来新增的模拟盘权限。

**没有保存 Result Bundle。** 纯 Chat Host 可能只提供下载，不会写入本地磁盘。Bundle 也可能仍在 materializing；稍后让 Agent 再检查同一个已完成结果。不要为了生成 Bundle 而重复启动运行。
