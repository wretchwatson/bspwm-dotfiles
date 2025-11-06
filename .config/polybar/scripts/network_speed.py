#!/usr/bin/env python3
import time
import sys
import socket
import requests

def get_network_stats():
    try:
        with open('/proc/net/dev', 'r') as f:
            lines = f.readlines()
        
        for line in lines[2:]:
            parts = line.split()
            interface = parts[0].rstrip(':')
            if interface != 'lo' and int(parts[1]) > 0:
                rx_bytes = int(parts[1])
                tx_bytes = int(parts[9])
                return interface, rx_bytes, tx_bytes
        return None, 0, 0
    except:
        return None, 0, 0

def bytes_to_mbits(bytes_val):
    return (bytes_val * 8) / (1024 * 1024)

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "N/A"

def get_public_ip_info():
    try:
        response = requests.get("http://ip-api.com/json/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get('query', 'N/A'), data.get('city', 'N/A'), data.get('country', 'N/A')
        return "N/A", "N/A", "N/A"
    except:
        return "N/A", "N/A", "N/A"

def main():
    interface, rx1, tx1 = get_network_stats()
    
    if not interface:
        print("󰞉 N/A")
        return
    
    time.sleep(1)
    interface, rx2, tx2 = get_network_stats()
    
    if not interface:
        print("󰞉 N/A")
        return
    
    rx_speed = bytes_to_mbits(rx2 - rx1)
    tx_speed = bytes_to_mbits(tx2 - tx1)
    
    if len(sys.argv) > 1 and sys.argv[1] == "--tooltip":
        local_ip = get_local_ip()
        public_ip, city, country = get_public_ip_info()
        print(f"Yerel IP: {local_ip} | Dış IP: {public_ip} | Konum: {city}, {country}")
    else:
        output = f"%{{F#2eb398}}󰞉%{{F-}}  ↓{rx_speed:.1f} ↑{tx_speed:.1f}"
        print(output.ljust(29))

if __name__ == "__main__":
    main()
