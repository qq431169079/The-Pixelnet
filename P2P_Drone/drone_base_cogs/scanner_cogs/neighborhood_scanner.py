import socket
import threading
import sys
import time
import os.path
from . import ip_range
from . import get_ip
possible_peers = []
max_ip = ip_range.ip_range()
global lhost
lhost = get_ip.get_ip()
targets = []

def peer_scan():
    target_number = 0
    for i in range(0, max_ip):
        target_number = int(target_number)
        target_number += 1
        target_number = str(target_number)
        targets.append(lhost[:lhost.rfind(".")] + "." + target_number)
        if i >= max_ip - 1:
            for workers in targets:
                worker_threads = threading.Thread(target=worker_scan, args=(workers))
                time.sleep(0.01)
                worker_threads.start()

def peer_recording(ip, port):
    ip = str(ip)
    port = str(port)
    import os.path
    directory = './permanence_files'
    filename = "port_report.txt"
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    ip_to_write = ip + ":" + port
    file = open(file_path, "a")
    if ip_to_write in file:
        file.close()
    else:
        file.write(ip_to_write)
        file.write("\n")
        file.close()

def port_scan(ip):
    try:
        for port in range(49975,50000):
            ip = str(ip)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            result = sock.connect_ex((ip, port))
            if port >= 50000:
                print("Completed Scan.")
                sys.exit()
            if result == 0:
                print(f"GOT POSSIBLE PEER FROM {ip}:{port}")
                peer_record_thread = threading.Thread(target=peer_recording, args=(ip, port))
                peer_record_thread.name = "Peer_Recording_Thread_Manager"
                peer_record_thread.start()
                break
            sock.close()
    except socket.gaierror:
        pass

    except socket.error:
        pass

def worker_scan(*ip):
    str = ''.join(ip)
    port_scan(str)

