import socket
import threading
import sys
import time
import os.path
import random
from . import ip_range
from . import get_ip
from . import broadcast_get
possible_peers = []
max_ip = ip_range.ip_range()
global lhost
lhost = get_ip.get_ip()
targets = []
actual_workers = []
lock_dir = "./permanence_files"
lock_file_name = "peer_scan.lock"
lock_file_path = os.path.join(lock_dir, lock_file_name)
if not os.path.isdir(lock_dir):
    os.mkdir(lock_dir)

def peer_scan():
    while os.path.exists(lock_file_path):
        print("scanner_locked")
        time.sleep(1)
    time.sleep(random.randint(1,10))
    peer_lock = open(lock_file_path, "x")
    target_number = 0
    broadcast = broadcast_get.get()
    for i in range(0, max_ip):
        target_number = int(target_number)
        target_number += 1
        target_number = str(target_number)
        targets.append(lhost[:lhost.rfind(".")] + "." + target_number)
        if i >= max_ip - 1:
            targets.remove(lhost)
            targets.remove(broadcast)
            for workers in targets:
                worker_threads = threading.Thread(target=worker_scan, args=(workers))
                worker_threads.name = f"Port Scan Worker {workers}"
                time.sleep(0.01)
                worker_threads.start()
                if workers == targets[-1]:
                    print("WORKERS END")
                    time.sleep(5)
                    while True:
                        if not actual_workers:
                            print("Targets is equal to finished_workers")
                            try:
                                os.remove(lock_file_path)
                            except:
                                pass
                            finally:
                                sys.exit()

def peer_recording(ip, port):
    ip = str(ip)
    port = str(port)
    filename = "port_report.txt"
    file_path = os.path.join(lock_dir, filename)
    if not os.path.isdir(lock_dir):
        os.mkdir(lock_dir)
    ip_to_write = ip + ":" + port
    try:
        file = open(file_path, "r")
    except:
        try:
            file = open(file_path, "x")
        except:
            print("UNEXPECTED PEER RECORDING FILE ERROR")
            sys.exit()
    finally:
        try:
            file = open(file_path, "a+")
        except:
            print("UNEXPECTED PEER RECORDING FILE ERROR")
            sys.exit()
    if ip_to_write in file.read():
        file.close()
        print("FILE ALREADY WRITTEN!")
        sys.exit()
    else:
        file.close()
        file = open(file_path, "a")
        file.write(ip_to_write)
        file.write("\n")
        file.close()
        sys.exit()

def port_scan(ip):
    actual_workers.append(ip)
    try:
        for port in range(49975,50001):
            ip = str(ip)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            sock.settimeout(20)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"GOT POSSIBLE PEER FROM {ip}:{port}")
                peer_record_thread = threading.Thread(target=peer_recording, args=(ip, port))
                peer_record_thread.name = "Peer_Recording_Thread_Manager"
                peer_record_thread.start()
                if port == 50000:
                    actual_workers.remove(ip)
                    print("Completed Scan.")
                    print(actual_workers)
                    try:
                        sock.close()
                    except:
                        pass
                    sys.exit()
                else:
                    break
            if port == 50000:
                actual_workers.remove(ip)
                print("Completed Scan.")
                print(actual_workers)
                try:
                    sock.close()
                except:
                    pass
                sys.exit()
            else:
                print(f"Nothing on {ip}:{port}")
            sock.close()
    except socket.gaierror:
        actual_workers.remove(ip)
        sys.exit()

    except socket.error:
        print(f"SOCKET ERROR:{socket.error}")

def worker_scan(*ip):
    str = ''.join(ip)
    port_scan(str)