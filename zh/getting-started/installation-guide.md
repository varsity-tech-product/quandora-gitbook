---
translation_status: draft
description: 在受支持的 AI Agent 宿主中安装并连接 Quandora。
icon: bolt
---

# 安装指南

使用网页不需要安装 Agent 插件。通过 Agent 工作时，请安装 `quandora@quandora` 并连接 Quandora 账户。七个工作流 Skill 如下：

| Skill | 作用 |
| --- | --- |
| Factor Mining（因子挖掘） | 创建、验证并回测因子。 |
| Factor Analysis（因子分析） | 读取已保存的因子样本内证据。 |
| Strategy Building（策略构建） | 使用可用因子构建并回测策略。 |
| Strategy Analysis（策略分析） | 诊断一次准确的策略回测。 |
| Portfolio Building（组合构建） | 选择策略、分配资金、回测组合，并按要求发现、收藏和分享。 |
| Portfolio Analysis（组合分析） | 评估组合的历史增量价值。 |
| Portfolio Trading Analysis（组合交易分析） | 分析模拟/实盘前向证据，并按要求管理模拟账户与运行。 |

前六个工作流针对回测，第七个针对前向验证。插件只读检查实盘，执行控件保留在符合条件账户的网页中。

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

## 确认七项 Skill

让宿主显示已安装的 Quandora Skills，核对上述七个名称。如果仍是旧的五项布局，通过宿主插件管理器更新，按需重新连接，并开始新会话。仅连接工具不一定安装了 Skill 指令，请遵循对应宿主安装指南。

自然语言示例可以跨宿主使用：

```text
使用 Quandora Factor Mining 展示可用研究任务。
使用 Quandora Factor Analysis 解释这份因子结果，不重新运行。
使用 Quandora Strategy Building 列出可用因子。
使用 Quandora Strategy Analysis 分析这次准确的策略回测。
使用 Quandora Portfolio Building 提出组合方案，暂不创建。
使用 Quandora Portfolio Analysis 比较这份结果与实际成员。
使用 Quandora Portfolio Trading Analysis 检查我选定的模拟运行。
```

宿主支持显式 Skill 命令时，使用它实际列出的名称。不要用旧 Paper Trading 命令替代新的 Portfolio Trading Analysis 流程。[工作流总览](../understanding-quandora/quandora-workflow.md)说明各 Skill 的边界。

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

**更新后看不到新增工具。** 先确认插件版本，再通过宿主重新连接并检查请求的权限，随后开启新会话，让工具和 Skill 重新发现。反复刷新旧连接本身不会授予新权限。

**没有保存 Result Bundle。** 纯 Chat Host 可能只提供下载，不会写入本地磁盘。Bundle 也可能仍在 materializing；稍后让 Agent 再检查同一个已完成结果。不要为了生成 Bundle 而重复启动运行。
