import socket
import threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = socket.gethostname()
port = 2500
server.bind((address, port))
server.listen(200)
def threaded_welcomer():
    pass
def threaded_read():
    pass
def threaded_write():
    pass
def thread_parsers():
    pass
def threaded_data_requests():
    pass
def threaded_lts():
    pass
while True:
    conn, addr = server.accept()
    