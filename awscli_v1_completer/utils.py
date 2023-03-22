# -*- coding: utf-8 -*-

import socket
import os
import time
import syslog

def recv_header(sock):
    # 32bits: 0x0000ffff
    data = sock.recv(10)
    if not data:
        syslog.syslog("no data")
        return -1

    s = str(data, 'utf-8')
    l = int(data, 16)

    return l

def recv_data(sock, data_len):
    buffer = ''
    recv_bytes = 0

    while recv_bytes < data_len:
        remain = data_len-recv_bytes
        data = sock.recv(remain)
        if not data:
            break

        recv_bytes = recv_bytes + len(data)
        buffer = buffer + str(data, 'utf-8')

    return buffer

def send_data(sock, msg):
    # <data-length><data>
    buf = "0x%08x%s" % (len(msg), msg)

    # send the buf
    sock.send(buf.encode('utf-8'))

def find_prefix(data):
    data.sort()
    prefixs = []
    start = -1
    end = -1

    for i, value in enumerate(data):
        if start == -1:
            start = i
            end = i
        elif value[0] == data[start][0]:
            end = i
        else:
            prefix = os.path.commonprefix(data[start:end])
            prefixs.append(prefix)
            start = i
            end = i

    if start != -1:
        if start == end:
            prefixs.append(data[start])
        else:
            prefix = os.path.commonprefix(data[start:end])
            prefixs.append(prefix)

    return prefixs
