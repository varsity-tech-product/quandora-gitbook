---
translation_status: reviewed
description: 一条因子结果的结构化报告，包含 Health、等级、证据、风险和下一项实验。
---

# 因子卡

因子卡是一条明确因子结果在服务端留存的证据记录。它把原始回测转化为人和 AI Agent 都可以检查、质疑和比较的内容，不依赖本地文件。

## 阅读顺序

建议按以下顺序阅读：

```text
Success / Fail
-> evidence quality and Health
-> grade and continuous metrics
-> risks and caveats
-> next controlled experiment
```

## Success 与等级回答不同问题

| 结果 | 含义 |
| --- | --- |
| Success / Fail | 是否通过了全部必需的因子证据检查 |
| SSS、SS、S、A、B、C、D、F | 评估运行时返回的截面 Sharpe 等级 |

一个因子即使获得非 F 等级，也可能因为某项必需检查失败而得到 Fail。解释等级前，应先阅读记录中的 Gate 证据。当前语义请参考[Quandora 如何评估因子](how-factors-are-judged.md)。

## 常见字段

| 字段 | 含义 |
| --- | --- |
| Success / Fail | 必需检查的组合结果 |
| grade 与 grade score | 上游返回的分类和连续评分证据 |
| factor idea 与 formula | 信号希望捕捉的机制 |
| data 与 evaluation scope | 数据 Header、Bar Size、Horizon 和可见证据区间 |
| Health | Coverage、missingness、输出可用性和失败字段 |
| key metrics | Sharpe、Rank IC、autocorrelation、drawdown、turnover 等可用诊断指标 |
| assumptions 与 caveats | 可能削弱证据的条件 |
| next experiment | 受控改动建议，不会自动提交 |

缺失或 `null` 证据必须保持不可用，不能改写为零或视为通过。

## 示例

假设一个因子使用日线 Bar 和 7 天 Forward Horizon：

| 字段 | 值 | 解释 |
| --- | --- | --- |
| Success | Fail | 至少一项必需检查未通过 |
| Grade | D | 截面 Sharpe 位于 D 区间 |
| Cross-sectional Sharpe | 0.81 | 通过严格的 `> 0.8` 检查 |
| Absolute Rank IC | 0.008 | 未通过严格的 `> 0.01` 检查 |
| Autocorrelation, lag 1 | 0.62 | 通过 `>= 0.4` 检查 |
| Health | Passed | 记录中的输出质量检查通过 |
| Max drawdown | −32% | 观察到的最大峰谷回撤 |
| Turnover | 0.63 | 隐含组合的变化程度 |
| Cost viability | Failed | 诊断警告，不参与四项必需检查 |

简要结论为：Absolute Rank IC 未达到要求，所以结果是 **Fail**；Sharpe 为 0.81，所以等级是 **D**；如果 Cost viability 也失败，则实现风险较高。这些字段分别回答不同问题。

## 服务端证据与图表

因子分析 Skill 会读取一条明确运行中对产品安全的 **In-Sample（IS）** 证据。根据可用性，它可能包含因子卡、Health 与等级字段、factor profile、group NAV、daily returns、simulation NAV、simulation PnL，以及只用于解释的惰性源码文本。

不要把当前公开分析描述为 OOS 或 ALL 分析。未来的公开契约可能提供其他 Window，但当前分析范围只有 IS。

## 可选 Result Bundle

因子分析不需要本地压缩包。在可写 Host 中导出已完成结果时，本地规范结果是一个经过校验的 ZIP：

```text
Quandora result/factor/<factor_slug>.zip
```

ZIP 不会自动解压或重新构建。它的 runtime manifest 是判断已包含、等待中和省略项目的权威依据。

| Bundle 状态 | 含义 |
| --- | --- |
| Available | 校验后的压缩包已准备好 |
| Partial | 压缩包可读，manifest 会说明仍在等待或省略的可选项目 |
| Pending / materializing | 压缩包仍在准备，可以稍后再次请求同一结果 |

Bundle 准备较慢时，不要重新启动回测。
