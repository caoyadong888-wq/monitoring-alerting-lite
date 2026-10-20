# Grafana single-host dashboards (lite)

Free subset. The host dashboard only, plus provisioning and a Compose file that starts Prometheus, Grafana, and node_exporter. nginx and MySQL boards are in the full pack.

## English

### Deliverables

- `deliverables/dashboards/host-node-exporter.json` — CPU, memory, disk, network, load, file descriptors. Instance variable defaults to `node-exporter:9100`, job `node`.
- `deliverables/provisioning/datasources/prometheus.yml` — datasource uid `prom-single-host`
- `deliverables/provisioning/dashboards/provider.yml` — loads the dashboard folder
- `deliverables/compose/docker-compose.yml` — Prometheus, Grafana, node_exporter
- `deliverables/compose/prometheus.yml` — scrapes Prometheus and node_exporter

```bash
cd deliverables/compose
docker compose up -d
```

Open http://127.0.0.1:3000 and sign in as `admin`. The lab password is `admin`.

The full pack adds the nginx dashboard, the MySQL dashboard, stub_status, and mysqld_exporter.

Full version / 完整版: GUMROAD_URL

## 中文

免费子集。只有主机看板，加上供应文件，以及只启动 Prometheus、Grafana 和 node_exporter 的 Compose。nginx 和 MySQL 看板在完整版里。

### 交付物

- `deliverables/dashboards/host-node-exporter.json` — CPU、内存、磁盘、网络、负载、文件描述符。instance 默认 `node-exporter:9100`，job 为 `node`。
- `deliverables/provisioning/datasources/prometheus.yml` — 数据源 uid `prom-single-host`
- `deliverables/provisioning/dashboards/provider.yml` — 加载看板目录
- `deliverables/compose/docker-compose.yml` — Prometheus、Grafana、node_exporter
- `deliverables/compose/prometheus.yml` — 抓取 Prometheus 和 node_exporter

```bash
cd deliverables/compose
docker compose up -d
```

打开 http://127.0.0.1:3000 ，用 `admin` 登录。实验环境的密码是 `admin`。

完整版另外包含 nginx 看板、MySQL 看板、stub_status 和 mysqld_exporter。

Full version / 完整版: GUMROAD_URL

## Delivery time / 交付时间

- Lite (this folder): free, available now. / 精简版（本目录）：免费，立即可用。
- Full version: instant download after purchase (GUMROAD_URL). / 完整版：购买后即时下载（GUMROAD_URL）。
