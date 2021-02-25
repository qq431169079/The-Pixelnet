import socket
import threading

outreach_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def outreach_local_peer(address, socket):
    socket.connect(address)
    print("Connected")
