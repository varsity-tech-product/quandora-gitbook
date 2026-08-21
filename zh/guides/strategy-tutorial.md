---
translation_status: reviewed
description: 构建、回测、分析并导出一条截面策略。
content_status: handoff
content_owner: plugin-and-product-backend
---

# 策略使用教程

策略构建和策略分析已经向公众用户开放。当前公开工作流使用符合条件的因子构建截面策略。

## 1. 列出可选因子

```text
/quandora:strategy-building list available factors
```

第一页会显示三类符合条件的因子：

| 来源 | 含义 |
| --- | --- |
| Official | 只读的产品因子库 |
| Mine | 当前用户拥有且符合策略条件的因子 |
| Shared | 已加入当前用户策略因子池的共享因子 |

列表采用分页，不会自动读取所有页面。需要更多结果时再请求下一页。

## 2. 选择因子组合

一条策略可以使用 1–20 个符合条件的因子。你可以使用等权，也可以提供明确的因子权重。提交前，让 Agent 展示最终生效的配置。

当前公开配置可以包含：

| 设置 | 作用 |
| --- | --- |
| name | 面向用户的策略名称 |
| factor selection 或 weights | 符合条件的因子及其组合方式 |
| ranking | 截面排序规则 |
| strategy type | 当前截面策略模式 |
| start 和 end dates | 回测区间 |
| initial cash | 初始模拟资金 |
| maker 和 taker fee rates | 模拟费用假设 |
| rebalance bars | 再平衡间隔 |
| attribution | 是否请求受支持的归因结果 |

省略 ranking 和 strategy type 时，当前默认值是 neutral top/bottom 20%。当前 Session 返回的 contract 始终是判断支持字段和默认值的权威依据。

如果 contract 中没有 custom universe、entry/exit rules、liquidity filters、maximum drawdown limit、deployment target 等字段，不要假设公开提交支持这些设置。

## 3. 检查并提交

```text
Use Quandora Strategy Building to combine the selected factors, show the exact
effective configuration, and ask me before submitting the backtest.
```

检查名称、因子、权重、日期、资金、费用、ranking 和 rebalance 设置。提交会改变状态，必须经过明确确认。

## 4. 监控同一条运行

Agent 应继续跟踪返回的运行，避免重复提交。终态失败结果不可变；只有用户明确要求后，才创建新运行进行重试。计算完成时间和 Result Bundle 准备完成时间可能不同。

## 5. 分析结果

使用只读策略分析 Skill：

```text
/quandora:strategy-analysis analyze my latest strategy result
```

策略分析会把规范运行配置、留存产物和有界数值图表证据结合起来。它可以诊断表现、风险、turnover、exposure、attribution、因子组合和模拟盘准备状态。它不会修订、重新运行、导出或启动模拟盘。

策略分析中的 `ALL` 表示包含 IS 的组合范围，不能把它描述为纯 OOS 证据。

## 6. 导出可选 Result Bundle

让策略构建导出一条明确的已完成运行。在可写 Host 中，校验后的压缩包会保存为：

```text
Quandora result/strategy/<strategy_slug>.zip
```

ZIP 会原样保留，不会自动解压或重新构建。它的 runtime manifest 会记录已包含、等待中和省略的项目。

## 7. 决定下一步

* 把结果保留为历史证据；
* 让策略分析提出一个受控的组合或配置实验；
* 明确确认一条新的策略构建运行；
* 来源符合条件时，单独确认一条模拟盘运行。

分析结果不会自动提交新回测，也不会自动启动模拟盘。
