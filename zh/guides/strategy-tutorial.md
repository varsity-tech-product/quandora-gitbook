---
translation_status: draft
content_status: handoff
content_owner: plugin-and-product-backend
---

# 构建策略

将可用因子组成一个截面策略，并检查其回测。开始前，策略可用因子池中至少需要一个因子。

## 网页操作

1. 打开 **Research → Strategies → Create strategy**。
2. 输入名称，通过 **Pick from your factors** 选择 1–20 个可用因子。
3. 设置表单中的方向、流动性阈值与头部/尾部排名，并检查可用的因子权重设置。
4. 展开 **Backtest execution parameters** 阅读产品级测试假设。展示的假设不一定都是可编辑输入。
5. 提交 **Create strategy**，跟进所创建的结果直至完成，再打开策略结果评估表现。

## 向 Agent 提问

先选择，不提交：

```text
使用 Quandora Strategy Building 列出我能使用的因子。为多空中性策略建议一个较小的组合，解释排名和权重。先展示方案，不要提交。
```

确定方案后：

```text
用选定因子、等权和头尾各 20% 排名构建并回测该策略，命名为 Momentum Study。报告准确的策略与回测结果，以及实际采用的假设。
```

这些参数仅用于演示，不代表最优配置。Agent 会检查当前资格和支持的字段，并跟进返回的运行，不会因计算或产物准备较慢而重复提交。

## 修订或重新运行

**Edit** 修改定义，在同一文件夹下创建新策略；**Rerun** 再次评估不变策略。两者都需要先选定准确版本，同名时尤其如此。归档单个策略，与整理文件夹或移除某次结果是不同操作。

## 完成标准

结果明确策略定义、因子组成、实际配置及回测状态。运行失败时应说明原因；导出尚未就绪不影响已完成的计算结果。

接着阅读[分析策略](strategy-analysis.md)。如需前向观察，先[构建组合](portfolio-building.md)，即使组合只有这一个策略。可选结果导出保留为已验证 ZIP，分析无需依赖它。
