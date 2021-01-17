import socket
import threading
import time
import random
import sys
import scanner
HOST = ''
binding = True
bind_attempts = 0
squadron_dict = {}
squadron_checked = 0
start_address = ""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while binding == True:
    PORT = random.randrange(49152, 50000)
    if bind_attempts <= 5:
        sys.exit()
    try:
        client.bind((HOST, PORT))
        binding == False
    except:
        bind_attempts += 1
        pass
def initialize_process():
    pass
def modules(connection, address):
    pass
def recv(connection):

def send(connection):
    if connection:
        pass
def squadron_check(squadron_dict):
    pass
while True:
    time.sleep(1)