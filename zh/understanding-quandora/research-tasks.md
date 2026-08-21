---
translation_status: draft
description: 研究任务告诉 Agent 需要测试哪一类市场规律。
---

# 研究任务

研究任务是 Quandora 因子挖掘的起点。

它会给 AI Agent 一个明确的市场行为作为研究目标，避免从空白 Prompt 开始“寻找 Alpha”。任务会把宽泛的交易问题转化成包含目标、允许数据、研究提示和评估 Horizon 的结构化工作。

***

## 为什么研究任务很重要

AI Agent 擅长提出想法，但金融研究还需要明确问题、可用数据、可测试逻辑和判断结果的方法。

研究任务会为 Agent 提供这些边界。

宽泛请求：

```text
Find me a good trading strategy.
```

Quandora 使用更具体的问题：

```text
Find a testable factor that detects liquidity fragility before volatility expands.
```

范围收窄后，Agent 才能产生 Quandora 可以评估的因子源码、Formula 和结果证据。

***

## 当前研究任务类别

当前规范类别为 `Technical`、`Microstructure`、`Volatility`、`Imbalance`、`Order Flow`、`Auction`、`Momentum`、`Volume` 和 `Liquidity`。自定义想法无法匹配这些类别时，可以使用 `Other`。当前 Session 返回的任务响应始终是权威依据。

### Technical Price Action & Pattern Structure

研究重复出现的价格行为或多 Bar 结构是否包含可测试的截面信号。

它可以分析收益、区间、收盘、突破、反转和波动结构，同时避免依赖纯视觉或主观图表判断。

```text
Does this price pattern repeat consistently enough to test?
```

### Market Microstructure And Liquidity Fragility

研究市场是否正在变得脆弱。

它关注流动性减弱、价格更容易被推动，以及清算连锁反应可能造成的不稳定状态。Agent 可以使用 volume、taker flow、open interest、funding、liquidations 和 premium 数据构建因子。

```text
Is the market becoming easier to push around?
```

### Volatility Regime And Risk Compensation

研究市场是否正在进入不同的波动状态。

它关注恐慌、Squeeze、波动扩张和风险条件变化，判断市场正在变得平静、剧烈还是不稳定。

```text
Is the market environment changing?
```

### Order Imbalance And Persistent Pressure

研究是否存在持续的买入或卖出压力。

它关注积累、派发、趋势延续和单边压力，判断买方或卖方是否在一段时间内持续占据主导。

```text
Is one side of the market quietly taking control?
```

### Aggressive Order Flow And Informed Trading

研究主动交易者是否正在推动市场向某个方向发展。

它关注 taker flow、aggressive volume、短期漂移和可能的信息资金足迹。

```text
Are aggressive traders telling us something before price fully reacts?
```

### Funding, Premium And Positioning Crowding

研究杠杆是否过度拥挤或正在变得不稳定。

它关注 funding reversal、premium deviation、拥挤持仓和趋势衰竭，判断是否有太多交易者站在同一方向。

```text
Is the trade becoming too crowded?
```

### Price Momentum And Trend Quality

研究趋势是否足够清晰和稳定。

它会用平滑度、volume confirmation 和 flow support 等条件判断价格运动是持续趋势还是随机噪声。

```text
Is this a real trend or just random movement?
```

### Volume Shock And Trend Confirmation

研究异常成交量是否确认价格运动。

它关注异常 Volume、信息到达，以及市场参与度是否支持或否定某次价格变化。

```text
Did volume confirm the move?
```

### Liquidity Premium And Trading Cost

研究信号在交易成本后是否仍然有效。

它关注 slippage risk、liquidity collapse、trading cost 和 impact-adjusted liquidity，判断想法是否能承受真实交易摩擦。

```text
Does the idea survive real trading friction?
```
