---
translation_status: reviewed
description: 诊断一个已测试因子，并运行经过用户确认的受控实验。
content_status: handoff
content_owner: plugin-and-product-backend
---

# 改进并重新运行因子

失败或表现脆弱的因子仍然是有价值的证据。稳妥的改进流程会先诊断一条明确运行，每次只改变一个机制，并保留原始结果。

## 1. 分析明确运行

使用因子分析进行只读诊断：

```text
/quandora:factor-analysis analyze my latest factor result
```

如果有多条运行都可能匹配，应选择明确的因子和运行，不要让 Agent 猜测。因子分析读取服务端留存的 IS 证据，并区分：

* 指标和 Health 字段中的直接观察；
* 对机制的推断；
* 其他合理解释；
* 能够区分这些解释的受控实验。

因子分析不会提交、恢复、归档或修改任何内容。

## 2. 选择一个受控改动

优先选择依据明确、预期效果可测量的改动。例如：

* 在保留经济逻辑的同时减少缺失输出；
* 平滑噪声较大的信号，并检查 autocorrelation 与 turnover 的取舍；
* 调整归一化方法，提高截面排序能力；
* 删除一个表现较弱的输入，避免一次增加多个新输入；
* 检查某个过滤条件是否造成适用范围与 Health 的错配。

每一项提议都应记录触发它的证据、预期变化、用于确认的指标，以及主要失败风险。

## 3. 创建新运行前进行确认

分析始终保持只读。选择实验后，明确要求因子挖掘创建并提交：

```text
Use Quandora Factor Mining to run the first proposed experiment. Keep the
original result unchanged and show me the exact change before submission.
```

Agent 应展示新的研究假设和源码改动，验证完整的新 `plugin.py`，并在提交前取得确认。

## 4. 使用可比证据进行比较

只有在任务、horizon、证据范围、active-universe 口径和 Health 阈值兼容时，才直接比较两条运行。重点查看：

* Success 失败原因；
* Health 与 missingness；
* Rank IC、autocorrelation 和 Sharpe；
* 路径稳定性、drawdown 和 turnover；
* 预期机制是否改善；
* 是否出现新的风险。

## 历史与不可变性

因子挖掘可以浏览当前用户拥有的因子家族、版本和运行。当前公开 Agent 工作流不提供历史源码编辑。终态结果保持不变；经过确认的实验会产生新证据，不会重写旧运行。

当连续改动开始接近曲线拟合，或证据已不再支持原始机制时，应停止修改。只有在你明确选择一个因子用于策略实验后，再继续阅读[策略构建](../understanding-quandora/strategy-construction.md)。
