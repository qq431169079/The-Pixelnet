import zlib
import sys
import re
def heading_wrap(message):
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
            testing = [message[i:i+2010] for i in range(0, len(message), 2010)]
            messages_concat = []
            for messages in testing:
                crc_check_format_message = bytes(messages, "utf-8")
                crc_check = zlib.crc32(crc_check_format_message)
                crc_check = str(crc_check)
                message = str(messages)
                message_length = len(messages)
                message_length = str(messages)
                headed_message = f"[!$HEADER$!] " + message_length + " " + crc_check + " " + message + " [$!FOOTER$!]"
                headed_message.encode('utf-8')
                messages_concat.append(headed_message)
                #TODO: Change code so that the heading_wrap sends message in fragments if this happens.
            return headed_message
        else:
            return headed_message
    else:
        return "null"

def head_send(conn, message):
    if conn:
        if message:
            headed_message = heading_wrap(message)
            if headed_message:
                if headed_message == type([]):
                    for message in headed_message:
                        try:
                            conn.sendall(bytes(headed_message, "utf-8"))
                        except Exception as e:
                            print(f"FATAL OUTGOING CONNECTION ERROR: {e}")
                            try:
                                conn.shutdown(2)
                            except:
                                pass
                            sys.exit()
                else:
                    try:
                        conn.sendall(bytes(headed_message, "utf-8"))
                    except Exception as e:
                        print(f"FATAL OUTGOING CONNECTION ERROR: {e}")
                        try:
                            conn.shutdown(2)
                        except:
                            pass
                        sys.exit()
            elif not headed_message:
                return "NO_MESSAGE"