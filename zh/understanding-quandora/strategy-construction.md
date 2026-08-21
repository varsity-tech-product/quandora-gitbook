---
translation_status: draft
description: 符合条件的因子如何进入公开截面策略回测。
---

# 策略构建

因子是一种排序信号。策略会组合一个或多个符合条件的因子，加入截面组合配置，并在模拟费用和再平衡条件下评估组合结果。

## 符合条件的因子来源

策略构建可以使用：

* **Official**：只读的产品因子库；
* **Mine**：属于当前用户并进入策略因子池的因子；
* **Shared**：已经加入当前用户策略因子池的共享因子。

三类来源在提交策略时使用相同的 Selector 路径。外部 `plugin.py` 属于单独的显式导入流程，不会因为由用户提供就自动归类为 Mine。

## 当前公开配置

公开 Strategy Contract 支持 1–20 个因子，当前配置边界包括：

* 策略名称；
* 因子选择或明确的因子权重；
* ranking；
* 截面 strategy type；
* start 和 end dates；
* initial cash；
* maker 和 taker fee rates；
* rebalance interval；
* attribution request。

省略 ranking 和 strategy type 时，当前默认值是 neutral top/bottom 20%。提交前，应始终检查当前 Session 返回的 contract 和 product defaults。

Custom universe、entry/exit rules、liquidity filters、live risk limits 或 deployment target 等概念不属于当前公开提交字段，不应描述为 Agent 可选择的控制项。

## 策略评估

回测会评估完整的提交配置。根据产物可用性，证据可以包括：

* net 和 gross performance；
* NAV 与 drawdown 路径；
* turnover 与模拟成本；
* funding；
* exposure 与 neutrality；
* per-symbol PnL 与 attribution；
* position 或 trade history；
* 留存六图分析界面的有界数值数据。

规范运行快照是判断明确因子组合和参数的权威依据。缺失产物应保持不可用，不能根据文件名或本地文件进行推断。

## 构建与分析是两个独立步骤

**策略构建**负责列出因子、组合、提交、恢复、导出和归档受支持的策略结果。**策略分析**保持只读，诊断一条明确的已完成结果并提出受控实验。

分析建议不会改变策略。用户必须明确确认新的策略构建提交。

## 下一步

一条已完成的来源可能符合模拟盘条件。选择来源时还会再次检查 eligibility；等级或回测状态本身不能保证可用。下一步可阅读[策略使用教程](../guides/strategy-tutorial.md)或[模拟盘使用教程](../guides/paper-trading-tutorial.md)。
