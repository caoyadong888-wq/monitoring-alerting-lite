# TLS certificate expiry checker (lite)

Free subset: one warning threshold and a text table. The full script adds a critical threshold, CSV, JSON, and the Nagios `CERTCHECK` line.

## English

### Deliverables

- `deliverables/check_certs.py` — dial a host, print days left, exit 0 or 1
- `examples/hosts.txt` — sample names (`app.example.com`, `192.0.2.15`)

```bash
python3 deliverables/check_certs.py --hosts examples/hosts.txt --warn-days 30
python3 deliverables/check_certs.py --host 127.0.0.1:443 --sni app.example.com --insecure --warn-days 30
```

Exit `0` when every certificate is above the warning threshold. Exit `1` when one is at or below it, or the handshake fails. Chain verification is on unless you pass `--insecure`.

Full version: GUMROAD_URL

## 中文

免费子集：只有一个警告阈值和文本表格。完整版增加严重阈值、CSV、JSON，以及 Nagios 的 `CERTCHECK` 行。

### 交付物

- `deliverables/check_certs.py`：连接主机，打印剩余天数，退出码 0 或 1
- `examples/hosts.txt`：示例名字（`app.example.com`、`192.0.2.15`）

```bash
python3 deliverables/check_certs.py --hosts examples/hosts.txt --warn-days 30
```

全部高于警告阈值时退出 `0`。有证书落到阈值上或握手失败时退出 `1`。默认校验证书链，私有证书加 `--insecure`。

Full version: GUMROAD_URL
