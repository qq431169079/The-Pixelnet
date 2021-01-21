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
finished_workers = []
def peer_scan():
    if os.path.exists("peer_scan.lock"):
        while os.path.exists("peer_scan.lock"):
            if os.path.exists("peer_scan.lock"):
                time.sleep(1)
            else:
                break
    else:
        peer_lock = open("peer_scan.lock", "x")
        target_number = 0
        for i in range(0, max_ip):
            target_number = int(target_number)
            target_number += 1
            target_number = str(target_number)
            targets.append(lhost[:lhost.rfind(".")] + "." + target_number)
            if i >= max_ip - 1:
                targets.remove(lhost)
                for workers in targets:
                    worker_threads = threading.Thread(target=worker_scan, args=(workers))
                    worker_threads.name = f"Port Scan Worker {workers}"
                    time.sleep(0.01)
                    worker_threads.start()
                    if workers == targets[-1]:
                        scanner_lock = True
                        while scanner_lock == True:
                            if targets == finished_workers:
                                os.remove("peer_scan.lock")
                            else:
                                time.sleep(1)

def peer_recording(ip, port):
    ip = str(ip)
    port = str(port)
    directory = './permanence_files'
    filename = "port_report.txt"
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
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
    try:
        for port in range(49975,50000):
            ip = str(ip)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            result = sock.connect_ex((ip, port))
            if port >= 50000:
                print("Completed Scan.")
                finished_workers.append(ip)
                try:
                    sock.close()
                except:
                    pass
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