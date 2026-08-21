---
translation_status: draft
description: Quandora 五项公开 Skill、各自的证据边界和阶段之间的明确确认。
---

# Quandora 工作流

Quandora 将创建与分析分开，也将历史测试与模拟执行分开。公开工作流由五项 Skill 组成：

```text
Factor Mining -> Factor Analysis -> Strategy Building
      ^                |                   |
      +-- user-approved factor experiment-+

Strategy Building -> Strategy Analysis -> Paper Trading
        ^                    |
        +-- user-approved strategy experiment
```

分析保持只读。因子实验建议返回因子挖掘；组合或配置实验建议返回策略构建。模拟盘只有经过另一项独立确认后才会开始。

{% hint style="info" %}
五项 Skill 都对公众用户开放。模拟盘使用模拟订单。实盘交易不属于当前公开产品。参见[产品功能可用性](../trust/product-availability.md)。
{% endhint %}

## 1. 因子挖掘

因子挖掘从公开[研究任务](research-tasks.md)或自定义想法开始。Agent 会读取服务端 Contract，创建并验证符合契约的 [`plugin.py`](plugin.py.md)，检查是否存在核心机制高度相似的研究，提交通过验证的明确源码，并跟踪返回的运行。

输出：一条因子结果；明确请求且文件可用时，还可以得到一个经过校验的 Result Bundle ZIP。

## 2. 因子分析

因子分析选择一条明确运行，读取当前用户范围内、由服务端留存的 IS 证据。它会诊断[因子卡](factor-card.md)、Health、等级字段、图表数据，并在需要时读取惰性源码文本。

输出：直接观察、推断、其他解释、风险和受控实验。它不会提交或修改内容。

## 3. 策略构建

策略构建会列出符合条件的 Official、Mine 和 Shared 因子，组合一条公开截面策略，展示最终配置，取得确认，提交回测，跟踪同一条运行，并可以明确导出经过校验的 Result Bundle。

输出：一条规范策略运行，包含明确的因子和参数。

## 4. 策略分析

策略分析选择一条明确运行，读取它的规范配置和留存产物，并使用有界数值图表证据进行诊断。

输出：performance、risk、turnover、exposure、attribution、因子组合和模拟盘准备状态分析。它不会提交新策略或模拟盘运行。

## 5. 模拟盘

模拟盘选择一条符合条件的已完成策略来源，并在启动模拟执行前取得单独确认。它可以检查当前 portfolio、closed positions、fills、funding、equity 和有界代码，也可以在明确确认后停止运行。

输出：模拟执行证据。已停止运行进入终态，不能恢复。

## 明确交接

| 起点 | 下一步 | 用户需要作出的决定 |
| --- | --- | --- |
| 因子分析 | 因子挖掘 | 选择一个因子实验建议，并确认新运行 |
| 因子或策略证据 | 策略构建 | 选择符合条件的因子，并确认明确配置 |
| 策略分析 | 策略构建 | 选择一个组合或配置实验建议 |
| 符合条件的策略来源 | 模拟盘 | 确认明确来源和模拟设置 |
| 模拟盘证据 | 任意研究 Skill | 选择下一步；不会自动重启或修复 |

## 本地输出

分析不依赖本地文件。在可写 Host 中，明确导出的已完成结果使用：

```text
Quandora result/factor/<factor_slug>.zip
Quandora result/strategy/<strategy_slug>.zip
```

每个校验后的 ZIP 会保持原样，不会自动解压或重新构建。它的 runtime manifest 是判断已包含、等待中和省略项目的权威依据。

## 安全边界

回测和模拟盘只提供声明条件下的证据。它们不保证未来收益，不构成金融建议，也不授权真实资金执行。缺失证据会保持缺失，分析保持只读，任何修改状态的操作都需要明确确认。
