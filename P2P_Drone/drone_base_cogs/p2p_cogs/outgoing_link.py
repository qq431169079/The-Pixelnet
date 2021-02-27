import socket
import threading
import sys
from ..head_send import *
def outreach_local_peer(address):
    outreach_command = threading.Thread(target=outreach, args=(address,))
    outreach_command.name = "OUTREACH_LINK_FOR_REAL"
    outreach_command.start()
    sys.exit()

def outreach(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"STARTED OUTREACH LINK TO {address}")
    try:
        sock.connect(address)
        sock.settimeout(5)
    except:
        print("OUTREACH_FAILED")
        try:
            sock.shutdown(2)
        except:
            pass
        try:
            sock.close()
        except:
            sys.exit()
        sys.exit()
    print("connected")
    head_send(sock, "hi")
    sock.shutdown(2)
    sock.close()
    sys.exit()