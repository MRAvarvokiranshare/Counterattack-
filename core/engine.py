# core/engine.py
import time
import json
import os
from collections import defaultdict


class DetectionEngine:
    def __init__(self):
        # Counters
        self.total_requests = 0
        self.ip_scores = defaultdict(int)
        self.subnet_counter = defaultdict(int)

        # Adaptive thresholds
        self.base_rate_limit = 5
        self.base_block_limit = 10

        # States
        self.blocked_ips = set()
        self.rate_limited_ips = set()
        self.alerts = []

        # Persistence
        self.state_file = "engine_state.json"
        self._load_state()

    # ================= CORE =================
    def inspect_ip(self, ip: str):
        # ---- SANITIZE INPUT ----
        ip = ip.strip().replace("IP>", "").strip()

        self.total_requests += 1
        self.ip_scores[ip] += 1

        # ---- ADAPTIVE LOGIC ----
        rate_limit, block_limit = self._adaptive_thresholds()

        # ---- SUBNET DETECTION ----
        subnet = self._get_subnet(ip)
        if subnet:
            self.subnet_counter[subnet] += 1
            if self.subnet_counter[subnet] > rate_limit:
                self._alert(ip, f"SUBNET_ATTACK ({subnet}.x)")

        # ---- IP RULES ----
        if self.ip_scores[ip] > block_limit:
            self.blocked_ips.add(ip)
            self._alert(ip, "BLOCKED")
            self._save_state()
            return {
                "ip": ip,
                "result": "ATTACK",
                "action": "BLOCK"
            }

        if self.ip_scores[ip] > rate_limit:
            self.rate_limited_ips.add(ip)
            self._alert(ip, "RATE_LIMIT")
            self._save_state()
            return {
                "ip": ip,
                "result": "SUSPICIOUS",
                "action": "RATE_LIMIT"
            }

        self._save_state()
        return {
            "ip": ip,
            "result": "CLEAN",
            "action": "ALLOW"
        }

    # ================= ADAPTIVE =================
    def _adaptive_thresholds(self):
        """
        Thresholds grow automatically with traffic
        """
        traffic_factor = max(1, self.total_requests // 10)

        rate_limit = self.base_rate_limit + traffic_factor
        block_limit = self.base_block_limit + traffic_factor * 2

        return rate_limit, block_limit

    # ================= METRICS =================
    def get_metrics(self):
        rate_limit, block_limit = self._adaptive_thresholds()
        return {
            "total_requests": self.total_requests,
            "unique_ips": len(self.ip_scores),
            "rate_limit_threshold": rate_limit,
            "block_threshold": block_limit,
            "blocked_ips": list(self.blocked_ips),
            "rate_limited_ips": list(self.rate_limited_ips),
            "top_subnets": dict(self.subnet_counter),
            "alerts": self.alerts[-20:]
        }

    # ================= HELPERS =================
    def _get_subnet(self, ip):
        parts = ip.split(".")
        if len(parts) == 4:
            return ".".join(parts[:3])
        return None

    def _alert(self, ip, reason):
        msg = f"{time.strftime('%H:%M:%S')} - {ip} - {reason}"
        self.alerts.append(msg)
        print("[ALERT]", msg)

    # ================= PERSISTENCE =================
    def _save_state(self):
        data = {
            "total_requests": self.total_requests,
            "ip_scores": dict(self.ip_scores),
            "subnet_counter": dict(self.subnet_counter),
            "blocked_ips": list(self.blocked_ips),
            "rate_limited_ips": list(self.rate_limited_ips),
            "alerts": self.alerts
        }
        with open(self.state_file, "w") as f:
            json.dump(data, f)

    def _load_state(self):
        if not os.path.exists(self.state_file):
            return

        try:
            with open(self.state_file, "r") as f:
                data = json.load(f)

            self.total_requests = data.get("total_requests", 0)
            self.ip_scores.update(data.get("ip_scores", {}))
            self.subnet_counter.update(data.get("subnet_counter", {}))
            self.blocked_ips.update(data.get("blocked_ips", []))
            self.rate_limited_ips.update(data.get("rate_limited_ips", []))
            self.alerts.extend(data.get("alerts", []))

        except Exception as e:
            print("[WARN] Failed to load engine state:", e)
