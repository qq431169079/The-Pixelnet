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

def p2p_welcomer(server):
    while True:
        server.listen(2)
        print("SERVER LISTENING")
        conn, addr = server.accept()
        print(f"BOT_CONNECTED:{conn}, {addr}")
        if conn:
            if addr:
                link_drone_thread = threading.Thread(target=link, args=(conn, addr, server))
                link_drone_thread.name = "drone_link"
                link_drone_thread.start()

def link(conn):
    waiting_for_information = True
    conn.settimeout(10)
    print("NET_LINK_KINDA_ESTABLISHED")
    print(f"CONNECTED TO {conn} IN LINK")
    #attempting Link establishment
    while waiting_for_information == True:
        try:
            raw_net_link = conn.recv(2048)
            print(f"RAW NET LINK: {raw_net_link}")
        except:
            print("Likely Port Scan")
            try:
                conn.close()
            except:
                pass
            finally:
                sys.exit()
        if raw_net_link:
            print("RECEIVED INFORMATION FROM RAW_NET_LINK")
            net_link = raw_net_link.decode('utf-8')
            if net_link == "PIXELNET_CONNECT_P2P_REQUEST":
                print("P2P REQUEST ACK")
                #print("LINK BROKEN")
                #conn.close()
                #sys.exit()
                conn.send(bytes("NET_LINK_ESTABLISHED", "utf-8"))
                #print("LIKELY_PORT_SCAN")
                #conn.close()
                #sys.exit()
    try:
        net_link_confirm_raw = conn.recv(2048)
        net_link_confirm = net_link_confirm_raw.decode('utf-8')
        print(f"Net_link_confirm_debug {net_link_confirm}")
    except:
        print("CANNOT CONFIRM NET LINK")
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