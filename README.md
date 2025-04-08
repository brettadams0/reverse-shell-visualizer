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
