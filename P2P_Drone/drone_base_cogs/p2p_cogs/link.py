import threading
import socket
import os.path
import sys
from ..scanner_cogs import *
from ..scanner_cogs import neighborhood_scanner
from ..scanner_cogs import ip_range
from .. scanner_cogs import get_ip
local_net = []
lhost = get_ip.get_ip()
    

def link(conn, addr):
    print("NET_LINK_KINDA_ESTABLISHED")
    conn.settimeout(5)
    conn.listen(1)
    conn.connect(addr)
    #attemptng Link establishment
    conn.sendall(bytes("attempting_send", "utf-8"))
    try:
        net_link = conn.recv(2048)
    except:
        conn.close()
        sys.exit()
    try:
        conn.sendall(bytes("NET_LINK_ESTABLISHED", "utf-8"))
    except:
        print("LIKELY_PORT_SCAN")
        conn.close()
        sys.exit()
    try:
        net_link_confirm = conn.recv(2048)
    except:
        conn.close()
        sys.exit()
    if net_link_confirm == "NET_LINK_ESTABLISHED":
        print("NET_LINK_ESTABLISHED")
        conn.settimeout(20)
        while True:
            conn.sendall(bytes("WHEEEE", "utf-8"))
            raw_link_check = conn.recv(2048)
            link_check = raw_link_check.decode('utf-8')
            
def link_drone(conn, addr):
    link_thread = threading.Thread(target=link, args=(conn,addr))
    link_thread.start()
    print(f"Link with {conn}, {addr} established.")
    sys.exit()