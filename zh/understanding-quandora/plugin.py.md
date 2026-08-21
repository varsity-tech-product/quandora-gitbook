---
translation_status: reviewed
description: `plugin.py` 是 AI Agent 交给 Quandora 验证并回测的契约化因子源码。
---

# 编写 `plugin.py`

因子挖掘会把任务或自定义想法转化为一份完整的 `plugin.py` 源码：

```text
task or custom idea
-> scoped server contract
-> agent writes plugin.py and a readable formula
-> agent validates the exact complete source
-> user confirms submission
-> Quandora runs the backtest
```

## 从当前 Contract 开始

服务端返回的 Construction Contract 是以下内容的权威依据：

* 明确的 `build_signal` 输入；
* 支持的数据 Column；
* Forward Horizon；
* 必需 Metadata 和 Runtime Sections；
* 支持的 Python 与 Runtime Expressions；
* 验证规则。

不要从旧运行复制过时的 Signature 或不受支持的 Header。Agent 可以看到允许的 Header 名称，Quandora 会在服务端绑定持续变化的市场数据。

## Formula 与源码

人类可读的 Formula 用于解释机制。例如：

```text
signal = normalized_change(open_interest_close, 4, 20)
         * direction(one_day_return(close))
```

它表达的含义是：

```text
Measure unusual open-interest change,
scale it by its recent behavior,
and align it with the latest price direction.
```

`plugin.py` 会让这一想法按照返回的 Contract 执行。提交源码必须使用明确支持的形式，包含必需 Metadata、`build_signal` 和所有声明的 Runtime Sections。

## 验证规则

Agent 应当：

* 编写一份完整源码；
* 让 `build_signal` 参数与返回的 Data Columns 一致；
* 返回对齐的浮点 DataFrame；
* 把无限值替换为 `NaN` 或契约允许的有限值；
* 检查是否存在核心机制高度相似的因子；
* 每次修改后重新验证完整源码；
* 只根据安全的结构化验证诊断进行修复；
* 提交刚刚通过验证的同一份源码。

生成的因子源码不得在本地 import、execute 或 eval。Quandora 负责远程验证和评估。

## `plugin.py` 不包含的能力

`plugin.py` 不属于以下内容：

* 买入或卖出指令；
* 完整策略；
* 实盘交易系统；
* 收益保证；
* 让服务端读取的文件系统路径。

它是一份可测试的因子定义，在通过验证和明确确认后以内联源码形式提交。

## 已接受源码的导出位置

对于已完成运行，因子挖掘拥有的已接受源码可以包含在经过校验的 Result Bundle 中：

```text
Quandora result/factor/<factor_slug>.zip
```

该 ZIP 是已完成结果的规范本地导出。Agent 不会创建第二套解压目录，也不会自动执行压缩包中的源码。
