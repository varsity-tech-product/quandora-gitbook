---
translation_status: draft
description: Quandora 用户可验证的安全、授权与支持信息。
content_status: handoff
content_owner: researcher
---

# 安全、隐私与支持

Quandora 通过 Host 管理的 Agent 连接使用浏览器 OAuth。不要在 Agent Prompt 中粘贴交易所 Key、API Key、Bearer Token、Authorization Code、Access Token、Refresh Token、密码或其他凭据。

## 已验证的连接事实

* Host 负责保存和刷新 Quandora 连接；Agent 不应检查或复制凭据。
* Access Token 的有效期为 7 天，Rotating Refresh Token 的有效期为 30 天，具体仍受账户和授权状态影响。
* 旧授权不会通过 Token Refresh 自动获得后来新增的模拟盘权限。安全连接响应要求时，应重新完成浏览器授权。
* Result Bundle 下载使用短时、单次有效的传输 URL。Agent 会立即使用，并且不得打印、保存或自行构造该 URL。
* 因子分析和策略分析使用当前用户范围内的服务端证据，不需要本地压缩包或凭据。

数据保留、研究数据处理、账户删除、服务支持和事件报告政策仍需要对应 Owner 单独批准。本页不会补充未经确认的承诺。

有关安装授权和工具索要 API Key 时的处理方式，请阅读[安装指南](../getting-started/installation-guide.md)。
