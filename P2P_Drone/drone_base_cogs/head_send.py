import time
def heading_wrap(message):
    time.sleep(0.5)
    if message:
        print(f"MESSAGE TO SEND: {message}")
        message = str(message)
        message_length = len(message)
        message_length = str(message_length)
        headed_message = f"[!$HEADER$!] " + message_length + " " + message + " [$!FOOTER$!]"
        headed_message.encode('utf-8')
        print(headed_message)
        if len(headed_message) > 2048:
            print("Message larger than 2048 bits. Sending Fragments.")
            #TODO: Change code so that the heading_wrap sends message in fragments if this happens.
        if message_length != len(message):
            # This is just extra, to make sure there really ARE no screw ups, in the event that there are multiple requests to send things at the same time.
            message = str(message)
            message_length = len(message)
            message_length = str(message_length)
            headed_message = f"[!$HEADER$!] " + message_length + " " + message + " [$!FOOTER$!]"
            headed_message.encode('utf-8')
            return headed_message
        return headed_message
    else:
        return "null"

def head_send(conn, message):
    if conn:
        if message:
            headed_message = heading_wrap(message)
            if headed_message:
                conn.sendall(bytes(headed_message, "utf-8"))
            elif not headed_message:
                return "NO_MESSAGE"