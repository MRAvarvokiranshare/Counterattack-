#!/usr/bin/env python3

import argparse
import subprocess

# تعریف سرویس‌ها (هر سرویس یک ماژول پروژه است)
SERVICES = {
    "api": ["uvicorn", "api.server:app", "--port", "8000"],
    "engine": ["python", "core/engine.py"],
    "metrics": ["python", "metrics/metrics.py"],
}

def start():
    print("[+] Starting AntiDDoS services...")
    for name, cmd in SERVICES.items():
        subprocess.Popen(cmd)
        print(f"  └─ {name} started")

def status():
    print("[*] Services should be running (check with ps)")

def stop():
    print("[!] Stop services manually (for safety)")

# تعریف CLI با argparse
parser = argparse.ArgumentParser(
    description="AntiDDoS Enterprise CLI"
)

parser.add_argument(
    "command",
    choices=["start", "status", "stop"],
    help="Command to manage AntiDDoS services"
)

args = parser.parse_args()

# اجرا بر اساس دستور کاربر
if args.command == "start":
    start()
elif args.command == "status":
    status()
elif args.command == "stop":
    stop()
