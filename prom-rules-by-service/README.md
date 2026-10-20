# Prometheus rules by service (lite)

Free subset. Eleven of the thirty full-pack alerts: MySQL reachability, connection fill, slow queries, and replica lag; Redis reachability and memory; nginx reachability and dropped connections; blackbox failure, slow probes, and the 3 day certificate page.

## English

### Deliverables

- `MySQLExporterDown` in `deliverables/rules/mysqld.yml` — MySQL exporter cannot reach mysqld ({{ $labels.instance }}) / MySQL 导出器连不上 mysqld（{{ $labels.instance }}）
- `MySQLConnectionsFilling` in `deliverables/rules/mysqld.yml` — MySQL connections are filling max_connections on {{ $labels.instance }} / MySQL 连接数正在接近上限（{{ $labels.instance }}）
- `MySQLSlowQueryBurst` in `deliverables/rules/mysqld.yml` — MySQL slow queries are rising on {{ $labels.instance }} / MySQL 慢查询突然增多（{{ $labels.instance }}）
- `MySQLReplicaLagHigh` in `deliverables/rules/mysqld.yml` — MySQL replica lag is high ({{ $labels.instance }}) / MySQL 复制延迟过高（{{ $labels.instance }}）
- `RedisExporterDown` in `deliverables/rules/redis.yml` — Redis exporter cannot reach Redis ({{ $labels.instance }}) / Redis 导出器连不上 Redis（{{ $labels.instance }}）
- `RedisMemoryNearMax` in `deliverables/rules/redis.yml` — Redis memory is near maxmemory ({{ $labels.instance }}) / Redis 内存接近 maxmemory（{{ $labels.instance }}）
- `NginxExporterDown` in `deliverables/rules/nginx.yml` — nginx-prometheus-exporter cannot read stub_status ({{ $labels.instance }}) / nginx-prometheus-exporter 读不到 stub_status（{{ $labels.instance }}）
- `NginxConnectionsNotHandled` in `deliverables/rules/nginx.yml` — Nginx is accepting connections it does not handle ({{ $labels.instance }}) / Nginx 接受了处理不了的连接（{{ $labels.instance }}）
- `BlackboxProbeFailed` in `deliverables/rules/blackbox.yml` — Blackbox probe is failing ({{ $labels.instance }}) / Blackbox 探测失败（{{ $labels.instance }}）
- `BlackboxProbeSlow` in `deliverables/rules/blackbox.yml` — Blackbox probe is slow but succeeding ({{ $labels.instance }}) / Blackbox 探测成功但很慢（{{ $labels.instance }}）
- `BlackboxTLSCertCritical` in `deliverables/rules/blackbox.yml` — TLS certificate expires within 3 days ({{ $labels.instance }}) / TLS 证书将在 3 天内到期（{{ $labels.instance }}）

Copy the YAML next to your Prometheus config and add `rule_files`. Annotations are Chinese and English. Runbook URLs point at `https://ops.example.com/runbooks/...`, which the full pack ships as markdown.

The full pack adds Postgres, the rest of the Redis and nginx rules, the 14 day certificate warning, HTTP 5xx, promtool unit tests, and the bilingual runbooks.

Full version / 完整版: GUMROAD_URL

## 中文

免费子集。完整版 30 条告警里的 11 条：MySQL 不可达、连接数、慢查询和复制延迟；Redis 不可达和内存；nginx 不可达和连接丢弃；blackbox 失败、慢探测，以及 3 天证书呼叫。

### 交付物

- `MySQLExporterDown` in `deliverables/rules/mysqld.yml` — MySQL exporter cannot reach mysqld ({{ $labels.instance }}) / MySQL 导出器连不上 mysqld（{{ $labels.instance }}）
- `MySQLConnectionsFilling` in `deliverables/rules/mysqld.yml` — MySQL connections are filling max_connections on {{ $labels.instance }} / MySQL 连接数正在接近上限（{{ $labels.instance }}）
- `MySQLSlowQueryBurst` in `deliverables/rules/mysqld.yml` — MySQL slow queries are rising on {{ $labels.instance }} / MySQL 慢查询突然增多（{{ $labels.instance }}）
- `MySQLReplicaLagHigh` in `deliverables/rules/mysqld.yml` — MySQL replica lag is high ({{ $labels.instance }}) / MySQL 复制延迟过高（{{ $labels.instance }}）
- `RedisExporterDown` in `deliverables/rules/redis.yml` — Redis exporter cannot reach Redis ({{ $labels.instance }}) / Redis 导出器连不上 Redis（{{ $labels.instance }}）
- `RedisMemoryNearMax` in `deliverables/rules/redis.yml` — Redis memory is near maxmemory ({{ $labels.instance }}) / Redis 内存接近 maxmemory（{{ $labels.instance }}）
- `NginxExporterDown` in `deliverables/rules/nginx.yml` — nginx-prometheus-exporter cannot read stub_status ({{ $labels.instance }}) / nginx-prometheus-exporter 读不到 stub_status（{{ $labels.instance }}）
- `NginxConnectionsNotHandled` in `deliverables/rules/nginx.yml` — Nginx is accepting connections it does not handle ({{ $labels.instance }}) / Nginx 接受了处理不了的连接（{{ $labels.instance }}）
- `BlackboxProbeFailed` in `deliverables/rules/blackbox.yml` — Blackbox probe is failing ({{ $labels.instance }}) / Blackbox 探测失败（{{ $labels.instance }}）
- `BlackboxProbeSlow` in `deliverables/rules/blackbox.yml` — Blackbox probe is slow but succeeding ({{ $labels.instance }}) / Blackbox 探测成功但很慢（{{ $labels.instance }}）
- `BlackboxTLSCertCritical` in `deliverables/rules/blackbox.yml` — TLS certificate expires within 3 days ({{ $labels.instance }}) / TLS 证书将在 3 天内到期（{{ $labels.instance }}）

把 YAML 放到 Prometheus 配置旁边并写上 `rule_files`。注解是中英双语。Runbook URL 指向 `https://ops.example.com/runbooks/...`，完整版里有对应的 markdown。

完整版另外包含 Postgres、其余 Redis 和 nginx 规则、14 天证书警告、HTTP 5xx、promtool 单测，以及中英对照 runbook。

Full version / 完整版: GUMROAD_URL

## Delivery time / 交付时间

- Lite (this folder): free, available now. / 精简版（本目录）：免费，立即可用。
- Full version: instant download after purchase (GUMROAD_URL). / 完整版：购买后即时下载（GUMROAD_URL）。
