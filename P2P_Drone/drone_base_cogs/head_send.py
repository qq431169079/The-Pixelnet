import threading
import socket
def heading_wrap(message):
    if message:
        message = str(message)
        headed_message = f"[!$HEADER$!] " + message + " [$!FOOTER$!]"
        headed_message.encode('utf-8')
        return headed_message
    else:
        return "null"

def head_send(connection, message):
    if connection:
        if message:
            headed_message = heading_wrap(message)
            