#!/usr/bin/env python3
"""Lite TLS expiry check: one warning threshold, text only.

Exit 0 when every certificate is above --warn-days.
Exit 1 when a certificate is due, expired, or the handshake fails.
The full pack adds a critical threshold, CSV, JSON, and Nagios output.
"""

from __future__ import annotations

import argparse
import socket
import ssl
import sys
from datetime import datetime, timezone

_CN_OID = bytes((0x55, 0x04, 0x03))


def _tlv_at(data: bytes, index: int) -> tuple[int, int, int]:
    tag = data[index]
    index += 1
    first = data[index]
    index += 1
    if first < 0x80:
        length = first
    else:
        nbytes = first & 0x7F
        length = 0
        for _ in range(nbytes):
            length = (length << 8) | data[index]
            index += 1
    return tag, index, index + length


def _children(data: bytes, start: int, end: int) -> list[tuple[int, int, int]]:
    items = []
    index = start
    while index < end:
        tag, content, content_end = _tlv_at(data, index)
        items.append((tag, content, content_end))
        index = content_end
    return items


def _parse_time(tag: int, raw: bytes) -> datetime:
    text = raw.decode("ascii").rstrip("Z")
    if tag == 0x17:
        year = int(text[0:2])
        year += 2000 if year < 50 else 1900
        body = text[2:]
        return datetime(
            year, int(body[0:2]), int(body[2:4]), int(body[4:6]), int(body[6:8]), int(body[8:10]),
            tzinfo=timezone.utc,
        )
    return datetime(
        int(text[0:4]), int(text[4:6]), int(text[6:8]), int(text[8:10]), int(text[10:12]), int(text[12:14]),
        tzinfo=timezone.utc,
    )


def _common_name(data: bytes, start: int, end: int) -> str:
    for _set_tag, set_start, set_end in _children(data, start, end):
        for _seq_tag, seq_start, seq_end in _children(data, set_start, set_end):
            parts = _children(data, seq_start, seq_end)
            if len(parts) < 2 or data[parts[0][1] : parts[0][2]] != _CN_OID:
                continue
            value_tag, value_start, value_end = parts[1]
            raw = data[value_start:value_end]
            if value_tag == 0x1E:
                return raw.decode("utf-16-be", errors="replace")
            return raw.decode("utf-8", errors="replace")
    return ""


def parse_certificate_der(der: bytes) -> tuple[str, datetime]:
    _tag, start, end = _tlv_at(der, 0)
    top = _children(der, start, end)
    tbs = _children(der, top[0][1], top[0][2])
    index = 1 if tbs and tbs[0][0] == 0xA0 else 0
    _valid_tag, valid_start, valid_end = tbs[index + 3]
    _subject_tag, subject_start, subject_end = tbs[index + 4]
    times = _children(der, valid_start, valid_end)
    not_after = _parse_time(times[1][0], der[times[1][1] : times[1][2]])
    return _common_name(der, subject_start, subject_end), not_after


def days_left(not_after: datetime, now: datetime) -> int:
    return int((not_after - now).total_seconds() // 86400)


def parse_host_token(token: str, default_port: int) -> tuple[str, int]:
    if ":" in token:
        host, port_text = token.rsplit(":", 1)
        if port_text.isdigit() and host:
            return host, int(port_text)
    return token, default_port


def load_targets(hosts: list[str], hosts_file: str | None, default_port: int) -> list[tuple[str, int]]:
    targets = [parse_host_token(item, default_port) for item in hosts]
    if hosts_file:
        for raw in open(hosts_file, encoding="utf-8"):
            line = raw.split("#", 1)[0].strip()
            if line:
                targets.append(parse_host_token(line, default_port))
    if not targets:
        raise SystemExit("provide --host or --hosts")
    return targets


def fetch_der(host: str, port: int, timeout: float, sni: str | None, insecure: bool) -> bytes:
    if insecure:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
    else:
        context = ssl.create_default_context()
    server_name = sni
    if server_name is None and host.count(".") != 3:
        server_name = host
    with socket.create_connection((host, port), timeout=timeout) as raw:
        with context.wrap_socket(raw, server_hostname=server_name) as tls:
            der = tls.getpeercert(binary_form=True)
    if not der:
        raise ssl.SSLError("peer did not present a certificate")
    return der


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="check_certs.py")
    parser.add_argument("--host", action="append", default=[])
    parser.add_argument("--hosts")
    parser.add_argument("--port", type=int, default=443)
    parser.add_argument("--sni")
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--warn-days", type=int, default=30)
    parser.add_argument("--insecure", action="store_true")
    args = parser.parse_args(argv)
    targets = load_targets(args.host, args.hosts, args.port)
    now = datetime.now(timezone.utc)
    failed = False
    print(f"{'HOST':<28} {'PORT':>5} {'DAYS':>6} {'CN'}")
    for host, port in targets:
        try:
            der = fetch_der(host, port, args.timeout, args.sni, args.insecure)
            common_name, not_after = parse_certificate_der(der)
            remaining = days_left(not_after, now)
        except Exception as exc:
            failed = True
            print(f"{host:<28} {port:>5} {'':>6} error: {exc}")
            continue
        if remaining <= args.warn_days:
            failed = True
        print(f"{host:<28} {port:>5} {remaining:>6} {common_name}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
