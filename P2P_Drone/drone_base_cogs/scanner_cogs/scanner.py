import socket
import ip_range
import get_ip
import time
def local_peer_scan():
    possible_peers = []
    max_ip = ip_range.ip_range()
    global lhost
    lhost = get_ip.get_ip()
    targets = []
    target_number = 0
    for i in range(0, max_ip):
        target_number = int(target_number)
        print(f"TARGET {targets}")
        target_number += 1
        target_number = str(target_number)
        targets.append(lhost[:lhost.rfind(".")] + target_number)
        print(lhost)
    try:
        for port in range(49152,50000):  
            connection_attempts = 0
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for i in targets: 
                result = sock.connect_ex((peer_ip, port))
                if result == 0:
                    try:
                        sock.sendall("[REQUEST_PEER_RESPONSE]")
                    except:
                        result = sock.connect_ex((peer_ip, port))
                        if result == 0:
                            if connection_attempts <= 3:
                                sock.sendall("[REQUEST_PEER_RESPONSE]")
                                continue
                            else:
                                break
                        else:
                            connection_attempts += 1
                    try:
                        possible_peers[peer_ip] = port
                    except:
                        pass
                sock.close()
    except socket.gaierror:
        pass

    except socket.error:
        pass
local_peer_scan()