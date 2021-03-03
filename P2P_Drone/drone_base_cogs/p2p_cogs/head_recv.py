def head_recv(conn, addr):
    while 1:
        try:
            message_raw = conn.recv(2048)
        except Exception as e:
            print(f"FATAL CONNECTION ERROR WITH {addr}")
            print(f"ENCOUNTERED ERROR {e}")
            return ["FATAL_CONNECTION_ERROR", "LOCAL_ERROR"]
        if message_raw:
            message = message_raw.decode('utf-8')
            message = str(message)
            message_split = message.split()
            message = message_split[2]
            if message_split:
                if "[!$HEADER$!]" in message_split:
                    if "[$!FOOTER$!]" in message_split:
                        if len(message) == int(message_split[1]):
                            if "LOCAL_ERROR" not in message_split:
                                return message
                            else:
                                return ["ATTEMPTED_ERROR_HIJACK", "SECURITY_ALERT"]
                        else:
                            print("Message length does not to match length expected.")
                            return ["MESSAGE_LEN_ERROR", "LOCAL_ERROR"]
                    else:
                        print("Footer missing or compromised.")
                        return ["FOOTER_ERROR", "LOCAL_ERROR"]
                else:
                    print("Header missing or compromised")
                    return ["HEADER_ERROR", "LOCAL_ERROR"]
        else:
            return message_raw
