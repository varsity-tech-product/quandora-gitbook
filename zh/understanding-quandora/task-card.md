---
translation_status: reviewed
description: 任务卡是因子挖掘使用的结构化研究任务。
---

# 任务卡

任务卡会告诉 Agent 需要研究什么市场行为、可以使用哪些数据 Header、适用什么 Forward Horizon，以及哪些研究上下文应当约束因子设计。

```text
A research task is the topic.
A task card is the instruction packet.
```

公开任务列表通常重点展示人类可读的任务名称和规范类别。内部 Task Handle 是不透明 Selector：Agent 应使用返回的明确 Handle，不得猜测、编辑或推导。

## 为什么需要任务卡

`find a profitable trading idea` 这样的请求范围太大，很难可靠评估。任务卡会把研究范围收窄到具体市场机制、受支持的数据和明确测试 Horizon。

例如：

```text
Investigate whether deteriorating liquidity precedes market fragility.
Use only the task's allowed headers.
Generate contract-compliant plugin.py and a readable formula.
Validate the complete source before submission.
```

## 任务信息

| 字段 | 含义 |
| --- | --- |
| name | 人类可读的任务名称 |
| category | 规范类别，例如 `Microstructure`、`Technical` 或 `Volatility` |
| description | 需要研究的市场行为 |
| allowed data | Factor Contract 允许的明确 Header |
| forward period | 以 Bar 为单位的评估 Horizon；当前公开任务使用 7 根日线 Bar |
| status | 任务当前是否开放 |
| core question | 明确研究问题 |
| primary alpha source | 可能产生预测信息的主要来源 |
| economic principle | 该机制可能存在的原因 |
| microstructure 或 crypto mechanism | 适用时提供市场特定解释 |
| research directions 与 feature hints | 可选研究方向，不是强制 Formula |
| regime considerations 与 risk sources | 可能削弱或推翻想法的条件 |
| target behavior | 理想因子输出希望捕捉的行为 |

返回对象可能包含更多结构化上下文。应使用当前 Session 返回的对象和 Scoped Factor Contract，不要照搬本页静态示例。

## 简化示例

```json
{
  "name": "Market Microstructure And Liquidity Fragility",
  "category": "Microstructure",
  "description": "Test whether liquidity deterioration predicts market fragility.",
  "core_question": [
    "Does weakening liquidity precede unstable price behavior?"
  ],
  "allowed_data": [
    "open",
    "high",
    "low",
    "close",
    "volume",
    "quote_volume",
    "taker_buy_volume",
    "taker_sell_volume",
    "open_interest_close",
    "funding_rate_close",
    "liquidation_long_usd",
    "liquidation_short_usd",
    "binance_premium_index_close"
  ],
  "fwd_period": 7,
  "status": "open"
}
```

该示例只用于说明。当前 Session 返回的任务和 Contract 决定明确字段、数据 Header 和 Horizon。

## Agent 如何使用任务卡

合理流程包括：

* 选择一个明确返回的任务；
* 重述它的目标和机制；
* 读取 Scoped Construction Contract；
* 只使用准确的 Allowed Headers；
* 检查是否存在核心机制高度相似的研究；
* 生成并完整验证 [`plugin.py`](plugin.py.md)；
* 说明假设、适用范围和风险；
* 提交前取得确认。

任务卡是约束条件，Agent 必须遵守。
