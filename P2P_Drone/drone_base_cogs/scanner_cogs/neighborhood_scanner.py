import socket
import ip_range
import get_ip
import threading
import sys
import time
possible_peers = []
max_ip = ip_range.ip_range()
global lhost
lhost = get_ip.get_ip()
targets = []

def target_list():
    target_number = 0
    for i in range(0, max_ip):
        target_number = int(target_number)
        print(f"TARGET {targets}")
        target_number += 1
        target_number = str(target_number)
        targets.append(lhost[:lhost.rfind(".")] + "." + target_number)
        print(lhost)
        if i >= max_ip - 1:
            for workers in targets:
                worker_threads = threading.Thread(target=worker_scan, args=(workers))
                time.sleep(0.1)
                worker_threads.start()

def port_scan(ip):
    try:
        for port in range(49975,50000):
            ip = str(ip)
            print(f"Scanning {ip}, {port}")  
            connection_attempts = 0
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            result = sock.connect_ex((ip, port))
            print(f"RESULT: {result}")
            if port >= 50000:
                sys.exit()
            if result == 0:
                break
            sock.close()
    except socket.gaierror:
        pass

    except socket.error:
        pass

def worker_scan(*ip):
    str = ''.join(ip)
    port_scan(str)

target_list()