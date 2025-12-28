#!/bin/bash
# Firewall Adapter برای AntiDDoS
# Usage: ./firewall.sh <IP>

IP="$1"

if [ -z "$IP" ]; then
    echo "[!] Usage: ./firewall.sh <IP>"
    exit 1
fi

echo "[Firewall] Blocking IP: $IP"

if command -v iptables >/dev/null 2>&1; then
    iptables -A INPUT -s "$IP" -j DROP
    echo "[+] IP $IP blocked successfully"
else
    echo "[!] iptables not available on this system"
    echo "[!] This script is intended to be run on a Linux server"
fi
