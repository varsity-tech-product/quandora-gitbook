---
translation_status: draft
description: 根据你的背景和目标，选择进入 Quandora 的最短路径。
icon: route
---

# 选择你的使用路径

你不需要先学完 Quandora 的所有概念。选择最符合你当前目标的路径即可。

## 我没有量化研究经验

先阅读 [Quandora 101](quandora-101-for-non-quants.md)，然后完成[快速开始](quickstart.md)。你会通过运行一个有明确约束的研究任务，理解什么是因子以及如何阅读它的证据。

## 我有一个市场想法想测试

直接进入[快速开始](quickstart.md)。你可以选择一个公开研究任务，也可以向 Agent 描述自己的想法。运行结束后，阅读 [Quandora 如何评估因子](../understanding-quandora/how-factors-are-judged.md)。

## 我已经有因子代码

按照[安装指南](installation-guide.md)连接 Quandora，然后让 Agent 在回测前验证你的 `plugin.py`。验证只检查代码是否满足所选任务和因子规范，不会自动运行或保存因子。

## 我使用 AI Agent 或开发集成

按照[安装指南](installation-guide.md)连接 Codex、Claude 或 OpenClaw。[plugin.py 参考](../understanding-quandora/plugin.py.md)说明因子挖掘工作流使用的可执行因子格式。

## 我想构建策略

先阅读[策略构建](../understanding-quandora/strategy-construction.md)，理解如何把评估过的因子组合成策略，然后进入[策略使用教程](../guides/strategy-tutorial.md)。

## 我想观察策略未来的表现

从一份已完成的策略回测开始，然后进入[模拟盘使用教程](../guides/paper-trading-tutorial.md)。模拟盘会复用那份已经评估过的策略，并使用模拟订单运行；启动时不需要重新拼装因子。

