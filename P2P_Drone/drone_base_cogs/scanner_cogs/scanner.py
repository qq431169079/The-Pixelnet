import socket
def local_peer_scan():
    possible_peers = []
    try:
        for port in range(49152,50000):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((peer_ip, port))
            if result == 0:
                sock.sendall("[REQUEST_PEER_RESPONSE]")
                
            sock.close()

    except socket.gaierror:
        pass

    except socket.error:
        pass