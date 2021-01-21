import threading
import socket
import os.path
import sys
from scanner_cogs.neighborhood_scanner import *
from scanner_cogs.neighborhood_scanner import neighborhood_scanner
from scanner_cogs.ip_range import ip_range

local_net = []
lhost = get_ip.get_ip()

def check_linked_drone(addr):
    target_number = ip_range.ip_range()
    for i in range(0, max_ip):
        target_number = int(target_number)
        target_number += 1
        target_number = str(target_number)
        local_net.append(lhost[:lhost.rfind(".")] + "." + target_number)
        if i >= max_ip - 1:
            if addr in local_net:
                pass
            elif addr not in local_net:
                return "not_local"
    count = 0
    directory = './permanence_files'
    filename = "port_report.txt"
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        return "port_scan_required"
    else:
        try:
            file = open(file_path, "r")
            reading_for_suspects = True
            while reading_for_suspects == True:
                count += 1
                line = file.readline()
                if addr in line:
                    return "suspected_bot"
                if not line:
                    return "not_suspected"
        except:
            try:
                file = open(file_path, "x")
            except:
                return "port_scan_required"

def link(conn, addr):
    conn.settimeout(5)
    try:
        conn.sendall(bytes("NET_LINK_ESTABLISHED", "utf-8"))
    except:
        conn.close()
        sys.exit()
    try:
        net_link_confirm = conn.recv(2048)
    except:
        conn.close()
        sys.exit()
    if net_link_confirm == "NET_LINK_ESTABLISHED":
        conn.settimeout(20)
        while True:
            conn.sendall(bytes("WHEEEE", "utf-8"))
            link_check = conn.recv(2048)
def link_drone(conn, addr):
    confirm_drone = check_linked_drone(addr)
    if confirm_drone == "port_scan_required":
        neighborhood_scanner.peer_scan()
        conn.close()
        sys.exit()
    elif confirm_drone == "suspected_bot":
        link_thread = threading.Thread(target=link, args=(conn,addr,))
        link_thread.name = "DRONE_LINK_THREAD"
        link_thread.start()
    elif confirm_drone == "not_suspected":
        conn.close()
        sys.exit()
    elif check_linked_drone == "not_local":
        link_thread = threading.Thread(target=link, args=(conn,addr,))
        link_thread.name = "DRONE_LINK_THREAD"
        link_thread.start()