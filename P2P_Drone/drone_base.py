import socket
import threading
import time
import drone_base_cogs.hierarchy_check as hc
HOST = ''
PORT = 5555
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(HOST, PORT)
squadron_dict = {}
squadron_checked = 0
def initialize_process():
    pass
def modules(connection, address):
    pass
def recv(connection):
    if connection:
        pass
def send(connection):
    if connection:
        pass
def squadron_check(squadron_dict):
    if 
while True:
    time.sleep(1)