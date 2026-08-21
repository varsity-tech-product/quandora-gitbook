---
translation_status: reviewed
description: 启动、监控、检查并停止 Quandora 模拟盘运行。
content_status: handoff
content_owner: plugin-and-product-backend
---

# 模拟盘使用教程

模拟盘使用模拟订单，不会使用真实资金下单。它从已有且符合条件的策略结果开始；因子选择和策略回测仍由策略构建负责。

## 1. 选择符合条件的来源

```text
/quandora:paper-trading start a paper run
```

如果你没有指定明确来源，Agent 会列出当前用户的可用模拟盘来源。应选择列表返回的来源，不要猜测标识符。

来源必须属于当前用户、已经完成并成功提交、采用截面策略，并且服务能够重建它的语义。预检查可能返回：

* **eligible**：安全检查已经通过，提交时仍会进行最终校验；
* **provider validation required**：当前还无法确认是否符合条件；
* **ineligible**：返回的原因会说明该来源为何不可用。

如果没有符合条件的来源，请返回[策略构建](strategy-tutorial.md)。

## 2. 确认模拟盘运行

提交前，检查并明确确认：

* 明确的来源和安全策略标签；
* 可选的 initial balance；
* 可选的 start date；
* 可选的 leverage。

模拟盘 Skill 不接受自定义 symbols 列表或 universe policy。Quandora 会在下游选择并冻结模拟标的池。

## 3. 通过运行详情监控生命周期

提交后，通过 detail state 监控同一条运行。早期 portfolio 或 equity 结果仍在准备时，不要创建第二条运行。

可以自然提问，也可以使用：

```text
/quandora:paper-trading show my current Paper PnL
```

可读取内容包括：

* 当前 portfolio、assets、PnL 和 open positions；
* 已关闭的净持仓生命周期；
* 模拟 fills；
* funding 记录；
* 固定回看区间的 equity curves；
* 用于检查的有界策略代码。

Open 或 partially open positions 属于当前 portfolio snapshot。Position history 只包含已关闭的净持仓生命周期。

## 4. 正确理解权益曲线

当前固定回看区间为 `7D`、`30D`、`90D`、`180D`、`1Y` 和 `3Y`。在模拟盘实际运行期开始前，曲线可能包含明确的零值填充。它表示“该运行尚未开始”，不表示历史亏损为零或市场数据缺失。

## 5. 确认后再停止

停止是终态操作，需要明确确认。已经停止的模拟盘不能恢复。再次使用同一来源会创建一条拥有独立历史的新运行。

当前公开 Agent 工作流不提供模拟盘 archive、unarchive 或 resume 操作。隐藏历史不能替代停止运行。

## 策略组合模拟盘

模拟盘还支持由多个静态、独立分配资金的策略 Sleeve 组成的 Strategy Portfolio。工作流为：

```text
create or revise the Portfolio definition
-> backtest the Portfolio
-> inspect the result
-> explicitly confirm a Portfolio Paper run
-> monitor or stop that exact run
```

创建因子或单条策略回测仍由策略构建负责。

## 不执行自动修复

亏损、回撤或疑似衰减不会授权 Agent 停止运行、挖掘新因子、修订策略或启动其他工作流。Agent 可以报告证据并提出交接建议，后续动作由用户决定并确认。
