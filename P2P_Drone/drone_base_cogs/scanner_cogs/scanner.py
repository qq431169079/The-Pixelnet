import socket
from ipaddress import ip_network, ip_address
import ipaddress
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    net = ip_network(f"{IP}/255")
    ip_address(("192.168.1.255") in net)
    [str(ip) for ip in ipaddress.IPv4Network('192.0.2.0/28')]
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