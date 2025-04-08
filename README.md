# 🔒 Reverse Shell Firewall Visualizer

A blazing-fast, terminal-based real-time visualizer that detects and blocks suspicious reverse shell connections on your system.

---

## 🚀 Features

- 🧠 **Intelligent Detection**  
  Scans active outbound TCP connections for unusual behavior (e.g., suspicious low-port activity).

- 🔥 **Real-Time Terminal UI**  
  A beautiful live-updating console with logs and status.

- 🛡️ **Firewall Integration**  
  Instantly blocks IPs via `iptables` (Linux) upon detection.

- 🧱 **Zero Dependencies**  
  Written in 100% pure Python — no external packages required.

- 🧩 **Modular & Hackable**  
  Designed to be easily extended — alerting, logging, remote control, and more.

---

## 🛠️ Installation

```bash
git clone https://github.com/brettadams0/reverse-shell-visualizer.git
cd reverse-shell-visualizer
sudo python3 main.py

Note: You must run as root to allow firewall rules to be applied.
```
---

## 📂 Structure
```
reverse-shell-visualizer/
├── app.py            # Entry point
└── README.md
```
---

## 🧠 How It Works
- Uses netstat -ntp to inspect active TCP connections.

- Flags connections where a local process initiates an outbound connection to a low-numbered port (common with reverse shells).

- Visualizes connection logs in a terminal dashboard.

- Automatically blocks IPs using iptables.
- 
---

## ⚠️ Disclaimer
This tool is designed for educational and defensive security purposes only. Use responsibly and only on systems you own or have permission to monitor.
