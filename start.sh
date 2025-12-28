#!/data/data/com.termux/files/usr/bin/bash

echo "[*] AntiDDoS Enterprise Launcher"

# رفتن به ریشه پروژه
BASE_DIR="$HOME/antiddos-enterprise"
cd "$BASE_DIR" || exit 1

HOST="127.0.0.1"
PORT=8000

echo "[*] Checking port $PORT..."

# اگر پورت 8000 اشغال بود، kill کن
PID=$(lsof -ti tcp:$PORT)
if [ -n "$PID" ]; then
    echo "[!] Port $PORT is in use by PID $PID"
    echo "[*] Killing process..."
    kill -9 $PID
    sleep 1
fi

# اگر باز هم اشغال بود، پورت جایگزین بگیر
if lsof -i tcp:$PORT >/dev/null 2>&1; then
    PORT=8001
    echo "[!] Using alternative port $PORT"
fi

echo "[+] Starting API on http://$HOST:$PORT"

python -m uvicorn api.server:app --host $HOST --port $PORT
