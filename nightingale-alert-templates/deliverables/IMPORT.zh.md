# 精简版导入

1. 业务组里能查到 `cpu_usage_active{cpu="cpu-total"}` 再继续。
2. 告警规则 → 导入 → 选择数据源 → 粘贴 `rules/host.json`。
3. 需要 HTTP 存活时再粘贴 `rules/http-probe.json`。完整的证书和 5xx 规则在完整版。
4. 勾选新规则，批量绑定通知规则。本文件不包含媒介配置。

完整步骤、Redis 对照表和消息模板见完整版。

Full version / 完整版: GUMROAD_URL
