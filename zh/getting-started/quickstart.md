---
translation_status: reviewed
description: 大约 15 分钟，从零获得并分析第一份有证据支持的因子结果。
icon: forward
---

# 快速开始

目标：把 Quandora 连接到你的 AI Agent，运行一个研究任务，并分析一份有证据支持的因子结果。

## 适合谁

已经使用 Codex、Claude、Cursor、CodeBuddy、WorkBuddy 中国版或 Kimi Code，并希望 Agent 根据市场证据开展研究的系统化交易者、AI 工具用户和市场研究者。

## 开始前准备

* 一个受支持的 Agent Host；
* 一个 [Quandora 账户](https://app.quandora.ai/auth/signin)；
* 10–15 分钟；
* 不需要交易所 API Key，这套研究流程不会下单。

## 1. 安装并连接

根据你的 Host 阅读[安装指南](installation-guide.md)。完成浏览器 OAuth 后，开始一个新对话或新任务，让 Host 发现全部五项 Quandora Skill。

## 2. 运行第一个因子任务

列出公开研究任务：

```text
/quandora:factor-mining show public tasks
```

选择一个任务，或者让 Agent 选择：

```text
Use Quandora Factor Mining to pick a public research task, generate a factor,
run the backtest, and give me a short result summary.
```

Agent 会读取[任务卡](../understanding-quandora/task-card.md)、检查是否存在核心机制高度相似的研究、编写 [`plugin.py`](../understanding-quandora/plugin.py.md)、验证完整源码并提交。Quandora 会在服务端绑定市场数据并运行评估。

## 3. 分析这一次明确的结果

运行进入终态后，发起只读分析：

```text
/quandora:factor-analysis analyze my latest factor result
```

因子分析会解析一条明确运行，并读取当前用户范围内、由服务端留存的 IS 证据。它不依赖本地 ZIP、Python 运行时、Notebook 或解压后的图表目录。

阅读[因子卡](../understanding-quandora/factor-card.md)中的结论、Health 证据、等级、指标、风险和受控实验建议。参考[Quandora 如何评估因子](../understanding-quandora/how-factors-are-judged.md)了解当前 Success 与等级语义。

## 4. 查找可选导出文件

当 Host 可以写入本地文件，并且已完成运行的 Result Bundle 已准备好时，因子挖掘会保存一个经过校验的 ZIP：

```text
Quandora result/factor/<factor_slug>.zip
```

该压缩包不会自动解压。它的 manifest 是判断已包含、等待中和省略项目的权威依据。`partial` 状态的包仍可能可读；处于 materializing 状态时，可以稍后请求同一结果。

## 完成标准

你的 Agent 已完成一次任务，并根据服务端证据解释了一条明确结果。失败因子同样有价值：负面证据可以帮助你确定下一项值得测试的实验。

{% hint style="info" %}
因子挖掘和因子分析不会下单。策略模拟盘使用模拟订单。实盘交易不属于当前公开产品。回测只说明已测试条件下的证据，不承诺未来表现。
{% endhint %}

## 下一步

* 浏览[研究任务类别](../understanding-quandora/research-tasks.md)；
* 学习如何经过明确确认后[改进并重新运行](../guides/improve-and-rerun.md)；
* 使用[策略使用教程](../guides/strategy-tutorial.md)构建截面策略；
* 遇到陌生术语时查看[术语表](../understanding-quandora/glossary.md)。
