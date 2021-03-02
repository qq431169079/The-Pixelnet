import socket
import threading
import sys
import os
import time
from .head_send import *
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
    ip_message_file_name = addr + ".ipmessage"
    ip_message_file_location = "./permanence_files/ip_messages/outgoing_messages/"
    ip_message_file_path = os.path.join(ip_message_file_location, ip_message_file_name)
    if not os.path.isdir(ip_message_file_location):
        os.makedirs(ip_message_file_location, exist_ok=True)
    while 1:
        try:
            file = open(ip_message_file_path, "r")
        except:
            try:
                file = open(ip_message_file_path, "x")
                file.close()
            except Exception as e:
                    print(f"UNEXPECTED FATAL READ/WRITE ERROR FOR .IPMESSAGE FUNCTIONALITY: {e}")
                    sys.exit()
            finally:
                try:
                    file = open(ip_message_file_path, "a+")
                except Exception as e:
                    print(f"UNEXPECTED FATAL READ/WRITE ERROR FOR .IPMESSAGE FUNCTIONALITY: {e}")
                    sys.exit()
        output = []
        for line in file:
            output.append(line)
            if output[0]:
                message_to_send = output[0]
                message_to_send = str(message_to_send)
                print(f"MESSAGE TO SEND: {message_to_send}")
                check_for_error = head_send(sock, message_to_send)
                if check_for_error:
                    if check_for_error == "FATAL_CONNECTION_ERROR":
                        print()
                        try:
                            file.close()
                        except:
                            pass
                        try:
                            sock.shutdown(2)
                        except:
                            pass
                        sock.close()
                        sys.exit()
                lst = []
                for line in file:
                    for word in output[0]:
                        if word in line:
                            line = line.replace(word,'')
                    lst.append(line)
                file = open(ip_message_file_path,'w')
                for line in lst:
                    file.write(line)
        time.sleep(1)
        head_send(sock, "DRONE_IDLE")
        file.close()