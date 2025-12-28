


<div align="center">

<img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="650"/>



# Counterattack – Anti-DDoS Framework

Counterattack is a modular Anti-DDoS detection framework designed to run on
Termux and Linux servers. The project focuses on behavioral traffic analysis,
subnet-based attack detection, and real-time metrics.

---

## Features
- Behavioral IP inspection
- Subnet attack detection
- Real-time metrics & alerts
- Modular detection engine
- Firewall integration (server-side ready)
- Fully testable on Termux (mobile)

---

## Project Structure




# 🛡️ Counterattack
## Advanced Anti‑DDoS Detection Framework

</div>

---

## ⚠️ LEGAL WARNING
### 🚫 Defensive Use Only

**Counterattack is a defensive security framework.**  
It is designed strictly for **educational, research, and defensive security purposes**.

> Any offensive usage, illegal activity, or misuse is **strictly prohibited**.  
> The author takes **no responsibility** for improper use.

<sub>⚠️ هشدار: این ابزار صرفاً برای استفاده دفاعی و آموزشی طراحی شده است و هرگونه استفاده غیرقانونی ممنوع می‌باشد.</sub>

---

## 🧠 How Counterattack Works

### 🔍 Behavioral Traffic Analysis
Counterattack continuously analyzes incoming IP behavior instead of relying on static rules.

It monitors:
- Request frequency
- IP uniqueness
- Subnet patterns
- Abnormal request bursts

<sub>🔍 این ابزار به‌جای قوانین ثابت، رفتار IPها را به‌صورت پویا تحلیل می‌کند.</sub>

---

### 🌐 Subnet‑Based Attack Detection
When multiple IPs from the same subnet generate traffic in a short period,  
the engine detects it as a **potential distributed attack pattern**.

This approach allows detection of:
- Botnet‑style floods
- Distributed scanning
- Low‑rate DDoS attacks

<sub>🌐 شناسایی حملات مبتنی بر Subnet برای تشخیص بات‌نت و حملات توزیع‌شده استفاده می‌شود.</sub>

---

### 📊 Real‑Time Metrics & Alerts
The engine maintains live metrics including:
- Total request count
- Unique IPs
- Active subnets
- Alert history

Alerts are generated automatically when thresholds are exceeded.

<sub>📊 متریک‌ها و هشدارها به‌صورت لحظه‌ای ثبت و تحلیل می‌شوند.</sub>

---

### 🛡️ Firewall Integration Ready
Detected malicious IPs can be forwarded to firewall modules  
(iptables on Linux servers) for real blocking.

On Termux, firewall actions are safely simulated.

<sub>🛡️ قابلیت اتصال مستقیم به فایروال در سرورهای لینوکسی وجود دارد.</sub>

---

## 🚀 Key Features

- ✅ Behavioral IP Analysis  
- ✅ Subnet Attack Detection  
- ✅ Real‑Time Metrics Collection  
- ✅ Automatic Alert System  
- ✅ Modular Detection Engine  
- ✅ Firewall‑Ready Architecture  
- ✅ Multi‑Terminal Execution  
- ✅ Mobile & Server Compatible  

<sub>🚀 مجموعه‌ای از قابلیت‌های دفاعی پیشرفته در یک معماری ماژولار.</sub>

---

## 🧠 Technologies & Platforms

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Termux-black?logo=android&logoColor=white">
  <img src="https://img.shields.io/badge/OS-Linux-blue?logo=linux">
  <img src="https://img.shields.io/badge/Language-Python-yellow?logo=python">
  <img src="https://img.shields.io/badge/Scripting-Bash-green?logo=gnu-bash">
  <img src="https://img.shields.io/badge/API-FastAPI-teal?logo=fastapi">
  <img src="https://img.shields.io/badge/Server-Uvicorn-purple">
  <img src="https://img.shields.io/badge/Security-Defensive-red">
</p>

<sub>🧠 این ابزار با Python و Bash نوشته شده و روی Termux و Linux اجرا می‌شود.</sub>

---

## 🖥️ Supported Operating Systems

- ✔️ Android (via **Termux**)
- ✔️ Linux (Ubuntu / Debian / Arch)
- ❌ Windows (Not Recommended)

<sub>🖥️ تمرکز اصلی روی اندروید (ترموکس) و لینوکس است.</sub>

---
---

## 🧰 Technologies Used

<p align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="60" title="Python"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" width="60" title="Linux"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bash/bash-original.svg" width="60" title="Bash"/>
</p>

<small>
Python is used for core logic and detection engine.  
Linux & Bash are used for CLI interaction and system-level control.
</small>

---

## 💻 Supported Operating Systems

### ✔ Linux
<small>Ubuntu • Debian • Arch • Kali • etc.</small>

### ✔ Android (Termux)
<small>Fully optimized for low-resource mobile environments</small>

### ✔ macOS
<small>Intel & Apple Silicon supported</small>

### ✔ Windows
<small>Recommended via WSL (Windows Subsystem for Linux)</small>

---


<div align="center">

<img src="![1000408649](https://github.com/user-attachments/assets/7c050b0a-e785-4f00-88bf-60cf2501c3cf)
"/>


## 📦 Installation

### 🔹 Linux / macOS
```bash
git clone https://github.com/MRAvarvokiranshare/Counterattack-.git
cd Counterattack-
pip install -r requirements.txt


🔹 Android (Termux)
Copy code
Bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/MRAvarvokiranshare/Counterattack-.git
cd Counterattack-
pip install -r requirements.txt


🔹 Windows (WSL)
Copy code
Bash
git clone https://github.com/MRAvarvokiranshare/Counterattack-.git
cd Counterattack-
pip install -r requirements.txt


▶️ Run the Service
Copy code
Bash
python -m uvicorn api.server:app --host 127.0.0.1 --port 8000
�
The engine will start listening on port 8000 Make sure the port is not already in use. 


🧪 Test IP Inspection
Copy code
Bash
curl -X POST http://127.0.0.1:8000/inspect \
-H "Content-Type: application/json" \
-d '{"ip":"5.5.5.5"}'


📊 View Live Metrics
Copy code
Bash
curl http://127.0.0.1:8000/metrics
�
Returns real-time traffic statistics and detected anomalies. 






## با تشکر از سیسی ها گلم برا ساخت پروژه🌕🪽
