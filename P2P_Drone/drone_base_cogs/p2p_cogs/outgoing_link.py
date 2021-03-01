import socket
import threading
import sys
import os
from ..head_send import *
def outreach_local_peer(address):
    outreach_command = threading.Thread(target=outreach, args=(address,))
    outreach_command.name = "OUTREACH_LINK_FOR_REAL"
    outreach_command.start()
    sys.exit()

def outreach(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"STARTED OUTREACH LINK TO {addr}")
    try:
        sock.connect(addr)
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
    addr = str(addr)
    while 1:
        ip_message_file_name = addr + ".ipmessage"
        ip_message_file_location = "./permanence_files/ip_messages/outgoing_messages/"
        ip_message_file_path = os.path.join(ip_message_file_location, ip_message_file_name)
        if not os.path.isdir(ip_message_file_location):
            os.makedirs(ip_message_file_location, exist_ok=True)
        try:
            file = open(ip_message_file_path, "r")
        except:
            try:
                file = open(ip_message_file_path, "x")
            except Exception.error as e:
                    print(f"UNEXPECTED READ/WRITE ERROR FOR .IPMESSAGE FUNCTIONALITY: {e}")
                    sys.exit()
            finally:
                try:
                    file = open(ip_message_file_path, "a+")
                except:
                    sys.exit()
        if file:
            output = []
            for line in file:
                output.append(line)
                if output:
                    message_to_send = output[0]
                    message_to_send = str(message_to_send)
                    head_send(message_to_send)
                    output.pop(0)
                else:
                    break
        else:
            head_send("DRONE_IDLE")
