# Nightingale alert templates (lite)

Free subset. The eight host rules, plus the HTTP probe-failed rule. MySQL, Redis, certificate windows, and the Feishu template are in the full pack.

## English

### Deliverables

- `deliverables/rules/host.json` — CPU, IO wait, memory, disk, inodes, load per CPU, NIC errors, TIME_WAIT
- `deliverables/rules/http-probe.json` — `probe_success == 0` only
- `deliverables/IMPORT.zh.md` — short import steps

Paste `host.json` into 告警规则 → 导入, choose the Prometheus datasource, then attach your own notification rule. Host metrics are Categraf (`ident` label).

Full version / 完整版: GUMROAD_URL

## 中文

免费子集。八条主机规则，外加 HTTP 探测失败。MySQL、Redis、证书窗口和飞书模板在完整版里。

### 交付物

- `deliverables/rules/host.json` — CPU、IO wait、内存、磁盘、inode、每核负载、网卡错误、TIME_WAIT
- `deliverables/rules/http-probe.json` — 只有 `probe_success == 0`
- `deliverables/IMPORT.zh.md` — 简短导入步骤

把 `host.json` 粘贴到告警规则 → 导入，选 Prometheus 数据源，再挂上你自己的通知规则。主机指标来自 Categraf（`ident` 标签）。

Full version / 完整版: GUMROAD_URL

## Delivery time / 交付时间

- Lite (this folder): free, available now. / 精简版（本目录）：免费，立即可用。
- Full version: instant download after purchase (GUMROAD_URL). / 完整版：购买后即时下载（GUMROAD_URL）。
