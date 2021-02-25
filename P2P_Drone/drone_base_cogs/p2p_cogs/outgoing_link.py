import socket
import threading
import sys
global outreach_socket
outreach_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def outreach_local_peer(address):
    print("NOTHING HERE TO SEE")
    outreach_command = threading.Thread(target=outreach, args=(address, outreach_socket))
    outreach_command.name = "OUTREACH_LINK_FOR_REAL"
    outreach_command.start()
    sys.exit()

def outreach(address, sock):
    try:
        sock.connect(address)
    except:
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
    sock.sendall(bytes("hi", "utf-8"))
    sock.shutdown(2)
    sock.close()
    sys.exit()