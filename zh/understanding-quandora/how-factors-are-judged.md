---
translation_status: reviewed
description: 因子卡当前使用的 Success 检查与 SSS–F 等级，提供证据而不承诺结果。
---

# Quandora 如何评估因子

每个提交的因子都会使用服务端绑定的市场数据进行评估。两个核心结果需要分别阅读：

* **Success 或 Fail**：是否通过全部必需证据检查；
* **Grade**：因子的截面 Sharpe 所在区间。

评估运行时拥有这些语义。对于一条明确运行，因子卡记录的数值、阈值、Health 证据和失败原因是权威依据。

## 当前公开证据范围

因子分析 Skill 当前读取对产品安全的 **In-Sample（IS）** 证据，不声明 OOS 或 ALL 证据。IS 仍然是历史证据，不能预测未来或模拟表现。

## Success 或 Fail

截面因子只有在以下四项检查全部通过时才会得到 Success：

| 检查 | Success 条件 | 它回答的问题 |
| --- | --- | --- |
| Absolute Rank IC | `> 0.01` | 排序关系是否足够强？ |
| Autocorrelation, lag 1 | `>= 0.4` | 信号在相邻 Bar 之间是否足够稳定？ |
| Cross-sectional Sharpe | `> 0.8` | 截面风险调整后表现是否足够强？ |
| Factor Health | Passed | 在记录的 Health 口径下，因子输出是否足够完整并可用？ |

Rank IC 和 Sharpe 使用严格大于；autocorrelation 包含阈值本身。任何必需证据为 unknown、unavailable 或 non-finite 时都不会通过。

Cost viability、turnover、drawdown 和其他诊断信息仍然重要，但它们不会单独决定因子的 Success 或 Fail。

## Health 与 Coverage

Health 在 active universe 内检查因子值。一个 Symbol 的 active span 从第一个有效值开始，到最后一个有效值结束；span 之外的 Cell 不计入 active coverage。

因子卡可以记录 Health 指标、阈值、coverage basis 和失败字段。缺失或 `null` Health 证据应视为未知，不能视为通过。比较两条运行时，只有在 Window、active-universe 定义、缺失值处理和阈值一致时，才直接比较 Health。

## Grade

等级使用截面 Sharpe：

| Cross-sectional Sharpe | Grade |
| --- | --- |
| `< 0.8` | F |
| `0.8 – < 1.2` | D |
| `1.2 – < 1.4` | C |
| `1.4 – < 1.6` | B |
| `1.6 – < 1.8` | A |
| `1.8 – < 2.0` | S |
| `2.0 – < 2.2` | SS |
| `>= 2.2` | SSS |

Grade 是上游返回的证据，不是晋级决定。它不会覆盖失败的必需检查，也不代表该因子已经适合真实资金交易。

{% hint style="info" %}
Success 只表示因子在已测试条件下提供了相应证据。回测描述历史，不保证未来收益。
{% endhint %}
