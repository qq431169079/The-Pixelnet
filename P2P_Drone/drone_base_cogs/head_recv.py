import socket 

def head_recv(conn):
    while 1:
        message_raw = conn.recv(2048)
        if message_raw:
            message = message_raw.decode('utf-8')
            message = str(message)
            message_split = message.split()
            if message_split:
                if "[!$HEADER$!]" in message_split:
                    if "[$!FOOTER$!]" in message_split:
                        if len(message_split[2]) == int(message_split[1]):
                            return "complete"
                        else:
                            print("Message length does not to match length expected.")
                            return "MESSAGE_LEN_ERROR"
                    else:
                        print("Footer missing or compromised.")
                        return "FOOTER_ERROR"
                else:
                    print("Header missing or compromised")
                    return "HEADER_ERROR"
        else:
            return message_raw
