import time
import zlib
import sys
def heading_wrap(message):
    time.sleep(0.5)
    if message:
        print(f"MESSAGE TO SEND: {message}")
        crc_check_format_message = bytes(message, "utf-8")
        crc_check = zlib.crc32(crc_check_format_message)
        crc_check = str(crc_check)
        message = str(message)
        message_length = len(message)
        message_length = str(message_length)
        headed_message = f"[!$HEADER$!] " + message_length + " " + crc_check + " " + message + " [$!FOOTER$!]"
        headed_message.encode('utf-8')
        if len(headed_message) > 2048:
            print("Message larger than 2048 bits. Sending Fragments.")
            #TODO: Change code so that the heading_wrap sends message in fragments if this happens.
        return headed_message
    else:
        return "null"

def head_send(conn, message):
    if conn:
        if message:
            headed_message = heading_wrap(message)
            if headed_message:
                try:
                    conn.sendall(bytes(headed_message, "utf-8"))
                    return
                except Exception as e:
                    print(f"FATAL OUTGOING CONNECTION ERROR: {e}")
                    try:
                        conn.shutdown(2)
                    except:
                        pass
                    sys.exit()
            elif not headed_message:
                return "NO_MESSAGE"