---
translation_status: reviewed
description: 使用模拟订单监控策略、检查证据，并由用户决定下一步。
---

# 模拟盘与监控

策略模拟盘已经向公众用户开放。它会复用一条符合条件且已完成的策略结果，使用模拟订单运行，不会承担真实资金风险。

它回答的问题是：

```text
How is this exact Strategy source behaving in simulation now?
```

模拟盘证据不能证明未来或真实资金表现。

## 可以检查的内容

当前公开模拟盘工作流可以提供：

* 运行生命周期和安全来源信息；
* 当前 balance、assets、PnL 和 portfolio positions；
* 已关闭的净持仓生命周期；
* 模拟 fills 和 funding；
* 固定回看区间的 equity curves；
* 有界策略代码；
* 经过明确确认的终态 stop。

Portfolio snapshot 是读取 open 和 partially open positions 的依据。Closed position history 只包含已经完成的净持仓生命周期。

固定回看区间为 `7D`、`30D`、`90D`、`180D`、`1Y` 和 `3Y`。为保持请求区间固定，运行开始前的日期可能使用明确的零值填充；这些零值不代表模拟表现。

## 监控提供证据，不执行自动化决策

通过 detail state 跟踪一条明确运行。暂时无法读取 portfolio，不代表 PnL 为零、组合为空或运行失败。应稍后检查同一条运行，避免快速轮询或重复提交。

公开 Skill 不承诺自动告警、自主识别 Regime、自动判断信号衰减，也不会由 Agent 维护交易叙事。只解释服务返回的证据。

## 由用户控制的决策点

证据保持稳定时，可以继续监控。出现亏损、回撤或非预期表现时，可以：

* 检查 fills、funding、positions、equity 和 code；
* 经过明确确认后停止模拟盘；
* 让策略分析只读诊断来源结果；
* 选择一个受控策略构建实验；
* 证据支持时返回因子分析或因子挖掘。

后续动作都不会自动发生。某个指标变化不会让模拟盘自行停止、修订策略、重启因子挖掘或提交替代运行。

具体步骤请阅读[模拟盘使用教程](../guides/paper-trading-tutorial.md)。
