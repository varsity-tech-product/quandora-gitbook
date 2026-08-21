---
translation_status: reviewed
description: Quandora 公开工作流与真实资金执行之间的当前边界。
---

# 部署与实盘交易

{% hint style="warning" %}
实盘交易不属于当前公开产品。公众账户可以使用因子挖掘、因子分析、策略构建、策略分析和模拟盘。任何研究或模拟结果都不会授予真实资金执行权限。
{% endhint %}

## 公开产品支持的能力

公开工作流提供历史或模拟证据：

```text
Factor Mining -> Factor Analysis
-> Strategy Building -> Strategy Analysis
-> simulated Paper Trading
```

因子和策略回测描述已测试的历史条件。模拟盘使用模拟订单。这些工作流不会把公众用户连接到 Broker 或 Exchange 进行真实资金执行。

## 本文档没有声明的能力

当前公开文档不说明任何实盘交易实现、Broker Permission Model、上线流程、支持 Venue、Risk-limit Schema 或运维控制系统。不要根据因子等级、策略结果、模拟盘运行、插件工具或账户状态推断这些能力。

如果真实资金执行未来成为有正式文档的公开能力，Quandora 会在要求用户使用前，单独发布经过审核的可用性、授权、风险、监控与支持契约。

## 用户安全边界

Quandora 研究结果不构成金融建议、收益保证，也不会指示用户买入、卖出、持有、调整仓位或平仓。用户仍需对公开研究和模拟工作流之外的决定负责。

当前边界请参考[产品功能可用性](../trust/product-availability.md)和[安全、风险限制与紧急停止](safety-risk-limits-and-kill-switch.md)。
