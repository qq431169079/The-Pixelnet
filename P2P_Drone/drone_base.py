import socket
import time
import random
import sys
import threading
from drone_base_cogs.scanner_cogs import *
from drone_base_cogs.scanner_cogs import get_ip
from drone_base_cogs.scanner_cogs import neighborhood_scanner
from drone_base_cogs.p2p_cogs import *
from drone_base_cogs.p2p_cogs import link
binding = True
squadron_dict = {}
squadron_checked = 0
start_address = ""
global server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bind_attempts = 0
def initialization_process():
    p2p_server_thread = threading.Thread(target=p2p_welcomer, args=())
    p2p_server_thread.name = "p2p_welcomer"
    p2p_server_thread.start()
    neighborhood_scanner.peer_scan()
while binding == True:
    HOST = get_ip.get_ip()
    PORT = random.randrange(49975, 50000)
    if bind_attempts >= 5:
        sys.exit()
    try:
        server.bind((HOST, PORT))
        print(f"BOUND TO: {HOST}:{PORT}")
        binding = False
        time.sleep(1)
        init_thread = threading.Thread(target=initialization_process, args=())
        init_thread.name = "init_thread"
        init_thread.start()
    except:
        bind_attempts += 1
def modules(connection, address):
    pass
def p2p_welcomer():
    while True:
        server.listen(2)
        conn, addr = server.accept()
        if conn:
            if addr:
                link_drone_thread = threading.Thread(target=link.link_drone, args=(conn, addr,))
                link_drone_thread.name = "drone_link"
                link_drone_thread.start()
def squadron_check(squadron_dict):
    pass

while True:
    time.sleep(1)