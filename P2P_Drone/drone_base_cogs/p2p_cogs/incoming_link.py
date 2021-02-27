import threading
import socket
import os.path
import time
import sys
from ..scanner_cogs import *
from ..scanner_cogs import neighborhood_scanner
from ..scanner_cogs import ip_range
from .. scanner_cogs import get_ip
from ..head_recv import *
local_net = []
lhost = get_ip.get_ip()
currently_connected_bots = []

def p2p_welcomer(server):
    while True:
        server.listen(10)
        print("SERVER LISTENING")
        conn, addr = server.accept()
        print(f"BOT_CONNECTED:{conn}, {addr}")
        if conn:
            if addr:
                link_drone_thread = threading.Thread(target=link, args=(conn,))
                link_drone_thread.name = "drone_link"
                link_drone_thread.start()

def link(conn):
    print("STARTED INCOMING LINK")
    conn.settimeout(5)
    disconnection_counter = 0
    waiting_for_info = True
    while waiting_for_info == True:
        net_link = head_recv(conn)
        if net_link:
            print(net_link)
        elif not net_link:
            disconnection_counter += 1
        if disconnection_counter == 5:
            try:
                conn.sendall("conn_test", "utf-8")
                disconnection_counter = 0
            except:
                print("INCOMING_LINK_DISCONNECTED")
                try:
                    conn.shutdown(2)
                except:
                    pass
            finally:
                conn.close()
                sys.exit()
def link_drone(conn, addr):
    link_thread = threading.Thread(target=link, args=(conn,addr))
    link_thread.start()
    print(f"Link with {conn}, {addr} established.")
    sys.exit()