---
translation_status: draft
description: Quandora 使用的量化与产品术语简明解释
---

# 术语表

以下定义尽量使用简单中文。遇到不熟悉的术语时，可以让 AI Agent 结合一条明确运行举例说明。

## 研究对象与 Skills

**因子（Factor）** — 可以量化并转化为分数的市场特征。Quandora 会测试该分数是否包含有用的截面证据。

**信号（Signal）** — 因子输出。每个市场、每根 Bar 对应一个值，可以在 active universe 中进行截面排序。

**任务卡（Task Card）** — 结构化研究任务，包含目标、类别、允许的数据 Header、Horizon 和研究上下文。参见[任务卡](task-card.md)。

**`plugin.py`** — 由 Quandora 验证并运行的可执行因子定义。参见[`plugin.py`](plugin.py.md)。

**因子挖掘（Factor Mining）** — 创建、验证并回测因子。它也可以浏览当前用户拥有的因子历史，并明确导出 Result Bundle。

**因子分析（Factor Analysis）** — 使用服务端留存的 IS 证据，只读诊断一条明确因子结果。它不需要本地 ZIP。

**因子卡（Factor Card）** — 包含 Success/Fail、Health、等级、指标、风险和实验建议的结构化因子结果。参见[因子卡](factor-card.md)。

**Success / Fail** — Absolute Rank IC、lag-1 autocorrelation、cross-sectional Sharpe 和 Factor Health 是否全部满足当前记录的要求。

**等级（SSS–F）** — 截面 Sharpe 区间，与 Success/Fail 分开解释。

**策略构建（Strategy Building）** — 选择符合条件的因子，并提交截面策略配置进行回测。

**策略分析（Strategy Analysis）** — 使用规范配置、留存产物和数值图表证据，只读诊断一条明确策略运行。

**Official / Mine / Shared** — 策略因子的来源。Official 是只读产品因子库；Mine 是当前用户拥有且符合策略条件的因子；Shared 是已加入当前用户策略因子池的共享因子。

**模拟盘来源（Paper source）** — 已完成、属于当前用户且符合条件，可以用于模拟盘的策略运行。

**策略组合（Strategy Portfolio）** — 一组静态、独立分配资金的策略 Sleeve，可以先回测，再进入模拟盘。

**Result Bundle** — 已完成因子或策略结果导出的校验 ZIP。它的 runtime manifest 会记录已包含、等待中和省略项目。分析不依赖该 ZIP。

**实盘交易（Live Trading）** — 使用真实资金执行交易。它不属于当前公开产品，本文档也不说明任何实盘实现或控制模型。

## 测试术语

**回测（Backtest）** — 使用历史数据评估因子或策略。它只描述已测试区间，不承诺未来表现。

**In-Sample（IS）** — 当前公开因子分析契约提供的历史证据区间。

**Out-of-sample（OOS）** — 独立留出的历史区间。当前公开因子分析 Skill 不声明 OOS 证据。

**ALL** — 包含 IS 的组合范围。在策略分析中，ALL 不能描述为纯 OOS。

**过拟合（Overfitting）** — 规则捕捉了历史噪声，没有形成能够泛化的机制。

**Forward Horizon（`fwd_period`）** — 评估因子分数时向前看的距离。当前公开任务使用 7 根日线 Bar。

**数据 Header Blindbox** — Agent 可以看到允许的 Header 名称，Quandora 在服务端绑定持续变化的市场数据。参见[我们的数据](our-data.md)。

## 因子指标

**Sharpe Ratio** — 单位波动对应的收益。当前 Factor Success 要求 cross-sectional Sharpe 严格大于 `0.8`。

**Rank IC** — 因子分数排序与 Forward Return 排序之间的相关性。当前 Factor Success 要求其绝对值严格大于 `0.01`。

**Autocorrelation** — 信号与上一根 Bar 信号的相似程度。当前 Factor Success 要求 lag-1 autocorrelation 至少为 `0.4`。

**Health** — 因子输出可用性检查，包括声明口径下的 coverage 和 missingness。未知 Health 证据不会通过。

**ICIR** — IC 除以其波动，用于观察一致性。

**IC Decay** — 预测证据在不同 Forward Horizon 下的变化。

**Turnover** — 隐含组合在两次再平衡之间的变化程度。

**Calmar** — 年化收益除以最大回撤。

**Hit Rate** — 在已声明定义下，盈利观察值或交易所占比例。

**Maximum Drawdown** — 评估路径中的最大峰谷回撤。

**Net vs Gross** — Gross 表现未扣除模拟成本；Net 表现包含适用的费用、turnover 和 funding 影响。

**Cost Viability** — 诊断一个 Edge 在模拟成本后是否仍然存在。它只提供诊断信息，不参与四项必需检查。

## 模拟盘术语

**模拟盘（Paper Trading）** — 使用符合条件的策略来源进行模拟执行，不会使用真实资金下单。

**Portfolio Snapshot** — 当前模拟盘的 balance、PnL、assets，以及 open 或 partially open positions。

**Closed Position History** — 已完成的净持仓生命周期。Open 或 partially open positions 保留在当前 portfolio snapshot 中。

**Fill** — 一条模拟成交通知。

**Funding** — 模拟盘运行中记录的资金费变动。

**Stop** — 模拟盘的终态操作。停止后不能恢复；再次启动会创建新运行。
