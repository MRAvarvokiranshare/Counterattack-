#!/usr/bin/env python3
"""
CLI کامل AntiDDoS برای Termux
- اجرای همزمان Engine + API + Metrics
- تست API با curl
- مدیریت سرویس‌ها (status/stop/start)
"""

import subprocess
import time
import os
import argparse

# مسیرهای ماژول‌ها
SERVICES = {
    "api": ["python", "-m", "uvicorn", "api.server:app", "--host", "127.0.0.1", "--port", "8000"],
    "engine": ["python", "core/engine.py"],
    "metrics": ["python", "metrics/metrics.py"],
}

# نگه‌داری پروسه‌ها
processes = {}

def start():
    print("[+] Starting all AntiDDoS services...\n")
    for name, cmd in SERVICES.items():
        print(f"[*] Starting {name}...")
        proc = subprocess.Popen(cmd)
        processes[name] = proc
        time.sleep(0.3)
    print("\n[+] All services started successfully!")

def status():
    for name, proc in processes.items():
        ret = proc.poll()
        state = "running" if ret is None else "stopped"
        print(f"{name}: {state}")

def stop():
    print("[!] Stopping all services...")
    for name, proc in processes.items():
        proc.terminate()
    print("[+] All services stopped!")

def test_api():
    print("[*] Testing API with curl...")
    os.system("curl http://127.0.0.1:8000/status")

# argparse
parser = argparse.ArgumentParser(description="Full AntiDDoS CLI")
parser.add_argument("command", choices=["start", "status", "stop", "test"], help="Command to manage services")
args = parser.parse_args()

if args.command == "start":
    start()
elif args.command == "status":
    status()
elif args.command == "stop":
    stop()
elif args.command == "test":
    test_api()
