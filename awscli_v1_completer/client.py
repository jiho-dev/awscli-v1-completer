import socket
import os
import time
from datetime import datetime
import syslog
from awscli_v1_completer.utils import *

def run_client(socket_path, cmdline, point):
    # st = datetime.now()

    if not os.path.exists(socket_path):
        syslog.syslog("awscli-v1-completer server is not ready at %s" % socket_path)
        return ""

    try:
        client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        client.connect(socket_path)
    except socket.error as e:
        syslog.syslog("socket err: %s" % e)
        return ""
    except:
        syslog.syslog("failed to connect to %s" %socket_path)
        return ""

    # send data
    send_data(client, cmdline)

    data_len = recv_header(client)
    if data_len == -1:
        syslog.syslog("unknown data length")
        return ""

    # receive the response
    buffer = recv_data(client, data_len)
    l = len(buffer)

    #et = datetime.now()
    #syslog.syslog('Complete Duration: {}'.format(et - st))

    client.close()
    return buffer

