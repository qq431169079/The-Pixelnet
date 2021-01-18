import socket
import ip_range
import get_ip
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
        targets.append(lhost[:lhost.rfind(".")] + "." + target_number)
        print(lhost)
    
    try:
        for ip in targets:
            for port in range(49975,50000):
                print(f"Scanning {ip}, {port}")  
                connection_attempts = 0
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                result = sock.connect_ex((ip, port))
                print(f"RESULT: {result}")
                if result == 0:
                    possible_peers.append(ip)
                    break
                sock.close()
    except socket.gaierror:
        pass

    except socket.error:
        pass
local_peer_scan()