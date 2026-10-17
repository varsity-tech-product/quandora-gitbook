---
translation_status: draft
---

# 你的第一个因子

测试一个市场想法，并理解一份准确的结果。此流程产生历史证据，不会下单交易。

## 开始之前

[创建或登录 Quandora 账户](https://app.quandora.ai/auth/signin)，并在 Agent 宿主中[连接插件](installation-guide.md)。你可以选择公开研究任务、描述自己的假设，或提供因子代码。此研究流程不需要交易所凭据。

## 向 Agent 提问

如果想先选择任务：

```text
使用 Quandora Factor Mining 列出可用研究任务，解释各自测试什么，先让我选择。
```

也可以直接授权完成一次实验：

```text
使用 Quandora Factor Mining 选择一个公开研究任务，解释假设，验证因子并运行回测。总结准确的结果和缺失证据。
```

Agent 会读取当前[任务要求](../understanding-quandora/task-card.md)、检查相关研究、编写并验证完整因子源码，再提交并跟进同一次运行。验证检查代码契约，本身不等于已保存的回测结果。你无需亲自编写 `plugin.py`。

## 网页操作

1. 打开 **Research → Factors**。
2. 在自己的库中找到因子并打开结果。侧栏的 **New** 用于创建文件夹；因子编写使用上面的 Agent 流程。
3. 确认因子和运行与 Agent 返回的结果一致，再阅读指标。
4. 查看判定、等级、Health、图表以及可用的研究背景。

也可以直接分析官方因子，无需先挖掘新因子。可见性不会授予读取私有源码的权限。

## 分析结果

```text
使用 Quandora Factor Analysis 解释这次因子运行。区分已观察到的样本内指标与假设，提出一项受控实验，不要提交新运行。
```

计算结果、图表和可选导出可能在不同时间就绪。证据准备中时，继续查看同一结果。缺失证据不等于零，也不构成重复提交的理由。

## 完成标准

你已经定位一份因子结果，并理解已有证据支持哪些判断。失败的因子也能提供有用信息。选择下一项实验或策略因子之前，先阅读[分析因子](../guides/factor-analysis.md)和[因子如何评定](../understanding-quandora/how-factors-are-judged.md)。

分析读取服务端保存的证据。需要本地结果时，可以请求导出已验证的结果包 ZIP；参见[安装指南](installation-guide.md)。
