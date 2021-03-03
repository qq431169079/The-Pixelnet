import socket
import time
import random
import sys
import threading
import os
import shutil
from drone_base_cogs.scanner_cogs import *
from drone_base_cogs.scanner_cogs import get_ip
from drone_base_cogs.scanner_cogs import neighborhood_scanner
from drone_base_cogs.p2p_cogs import *
from drone_base_cogs.p2p_cogs import incoming_link
binding = True
squadron_dict = {}
squadron_checked = 0
start_address = ""
global server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bind_attempts = 0
def initialization_process():
    try:
        self_name = os.path.basename(__file__)
    except:
        pass
    if ".pyw" in self_name:
        sys.stdout = open(os.devnull, 'w')
    p2p_server_thread = threading.Thread(target=incoming_link.p2p_welcomer, args=(server,))
    p2p_server_thread.name = "p2p_welcomer"
    p2p_server_thread.start()
    try:
        # Should be noted that after finishing development on VSCode, this needs to be taken out to mean in the context of the stand-alone drone
        os.remove("./permanence_files/peer_scan.lock")
    except:
        pass
    try:
        shutil.rmtree("./permanence_files/ip_messages")
    except:
        pass
    neighborhood_scanner_init_thread = threading.Thread(target=neighborhood_scanner.peer_scan, args=())
    neighborhood_scanner_init_thread.name = "init_scanner_thread"
    neighborhood_scanner_init_thread.start()
tried_binds = []
while binding == True:
    HOST = get_ip.get_ip()
    PORT = random.randrange(49995, 50000)
    if bind_attempts >= 5:
        sys.exit()
    if PORT not in tried_binds:
        try:
            server.bind((HOST, PORT))
            print(f"BOUND TO: {HOST}:{PORT}")
            init_thread = threading.Thread(target=initialization_process, args=())
            init_thread.name = "init_thread"
            init_thread.start()
            binding = False
        except:
            tried_binds.append(PORT)
            bind_attempts += 1
    else:
        continue

while True:
    time.sleep(1)