import socket
import subprocess
import threading
import os
import time
import re
from datetime import datetime
from collections import deque

# Settings
PORT_THRESHOLD = 1024  # Anything outbound below this port is suspect
CHECK_INTERVAL = 2     # Seconds
MAX_HISTORY = 100

# Storage for logging connections
connection_log = deque(maxlen=MAX_HISTORY)
blocked_ips = set()

def detect_suspicious_connections():
    """
    Continuously check for suspicious outbound connections using netstat.
    Looks for signs of reverse shells or unexpected activity.
    """
    while True:
        try:
            result = subprocess.check_output(['netstat', '-ntp'], stderr=subprocess.DEVNULL)
            lines = result.decode().splitlines()[2:]

            for line in lines:
                parts = re.split(r'\s+', line)
                if len(parts) < 7:
                    continue

                proto, recv_q, send_q, local, remote, state, pid_prog = parts[:7]
                if state != "ESTABLISHED":
                    continue

                remote_ip, remote_port = remote.rsplit(':', 1)
                local_ip, local_port = local.rsplit(':', 1)

                if int(remote_port) < PORT_THRESHOLD and remote_ip not in blocked_ips:
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    log_entry = f"[{timestamp}] Suspicious connection: {local_ip}:{local_port} → {remote_ip}:{remote_port}"
                    connection_log.append(log_entry)
                    block_ip(remote_ip)

        except Exception as e:
            connection_log.append(f"[!] Error: {str(e)}")
        
        time.sleep(CHECK_INTERVAL)

def block_ip(ip):
    """
    Blocks the given IP using iptables.
    """
    if os.geteuid() != 0:
        connection_log.append(f"[!] Must run as root to block IPs. Detected: {ip}")
        return
    try:
        subprocess.call(['iptables', '-A', 'OUTPUT', '-d', ip, '-j', 'DROP'])
        blocked_ips.add(ip)
        connection_log.append(f"[+] Blocked IP: {ip}")
    except Exception as e:
        connection_log.append(f"[!] Failed to block IP {ip}: {str(e)}")

def draw_ui():
    """
    Draws the live terminal UI for monitoring.
    """
    try:
        while True:
            os.system('clear')
            print("=" * 60)
            print("🔒 Reverse Shell Firewall Visualizer")
            print("=" * 60)
            print(f"Blocked IPs: {len(blocked_ips)}")
            print("-" * 60)

            for line in list(connection_log)[-20:]:
                print(line)

            print("-" * 60)
            print("Monitoring for suspicious connections...")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting gracefully...")
        exit(0)

def main():
    print("Starting Reverse Shell Firewall Visualizer...")
    detector_thread = threading.Thread(target=detect_suspicious_connections, daemon=True)
    ui_thread = threading.Thread(target=draw_ui, daemon=True)

    detector_thread.start()
    ui_thread.start()

    detector_thread.join()
    ui_thread.join()

if __name__ == "__main__":
    main()
