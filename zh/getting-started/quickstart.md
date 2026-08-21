---
translation_status: draft
description: 大约 15 分钟，从零获得第一份有证据支持的因子报告。
icon: forward
---

# 快速开始

目标：把 Quandora 连接到你的 AI Agent，运行一个研究任务，并读懂返回的因子卡。

### 适合谁

已经使用 Claude Code、Codex 或 OpenClaw，并希望 Agent 根据市场证据开展研究的系统化交易者、AI 工具用户和市场研究者。

### 开始前准备

* 一个 Agent Host：Claude Code、Codex 或 OpenClaw；
* 一个 [Quandora 账户](https://app.quandora.ai/auth/signin)；
* 10–15 分钟；
* 不需要交易所 API Key。第一次研究流程不会进行交易，授权通过浏览器 OAuth 完成。

### 1. 安装并连接

根据你的 Host 阅读[安装指南](installation-guide.md)。Claude Code 示例：

```
claude plugin marketplace add varsity-tech-product/quandora-plugins
claude plugin install quandora@quandora
```

然后打开 `/mcp`，认证 `quandora`，并开始一个新对话。

### 2. 运行第一个任务

列出公开研究任务：

```
/factor-mining show public tasks
```

选择一个任务，或者让 Agent 选择：

```
Use Quandora Factor Mining to pick a public research task, generate a factor,
run the backtest, and give me a plain-English verdict with key metrics and risks.
```

Agent 会读取[任务卡](../understanding-quandora/task-card.md)、检查是否有重复研究、编写 [`plugin.py`](../understanding-quandora/plugin.py.md) 并提交。Quandora 会在服务端绑定市场数据并运行回测，通常需要几分钟。

### 3. 阅读结果

运行会返回一份[因子卡](../understanding-quandora/factor-card.md)，先给出成功或失败，再说明证据、风险和下一步实验。当 Host 支持本地文件时，图表和结果会保存在：

```
Quandora result/factor-mining/<factor_slug>/
```

阅读 [Quandora 如何评估因子](../understanding-quandora/how-factors-are-judged.md)，了解结果为什么成功或失败。

### 完成标准

你的 Agent 已完成一次研究任务，并返回一份你能解释的报告。

失败结果同样有价值：它会成为研究记录，避免 Agent 重复同一个无效方向。

{% hint style="info" %}
因子挖掘只测试想法，不会下单。策略模拟盘使用模拟订单。实盘交易是独立的内部邀请制能力。因子卡呈现历史数据证据，不构成未来收益承诺。
{% endhint %}

### 下一步

* 浏览[研究任务](../understanding-quandora/research-tasks.md)；
* 查看 Agent 可以使用的[数据](../understanding-quandora/our-data.md)；
* 学习如何[改进并重新运行](../guides/improve-and-rerun.md)因子；
* 遇到陌生术语时查看[术语表](../understanding-quandora/glossary.md)。
