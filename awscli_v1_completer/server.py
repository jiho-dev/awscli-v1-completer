import socket
import syslog
import sys
import os
from awscli_v1_completer.utils import *
import awscli.completer

def create_socket(sock_path):
    try:
        os.unlink(sock_path)
    except:
        if os.path.exists(sock_path):
            raise

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        syslog.syslog('Setting up server socket on %s' % sock_path)
        sock.bind(sock_path)
        sock.listen(5)
        syslog.syslog('Success, listening on unix domain socket %s' % sock_path)
        s = '777'
        os.chmod(sock_path, int(s, base=8))

        return sock
    except Exception as e:
        syslog.syslog (e)
        return False

def run_server(sock_path):
    sock = create_socket(sock_path)
    if not sock:
        return False

    # reuse Completer
    comp = awscli.completer.Completer()

    while True:
        try:
            connection, client_address = sock.accept()
        except socket.error as e:
            syslog.syslog("socket err: %s" % e)
            sock.close()
            os.unlink(sock_path)
            return False
        except:
            sock.close()
            os.unlink(sock_path)
            return False

        try:
            data_len = recv_header(connection)
            if data_len == -1:
                raise Exception("unknown data length")

            buffer = recv_data(connection, data_len)
            l = len(buffer)

            choices = comp.complete(buffer, l)
            out = ' \n'.join(choices)

            send_data(connection, out)

        except socket.error as e:
            syslog.syslog ("socket err: %s" % e)
        except Exception as e:
            syslog.syslog ("error: %s" % e)
        finally:
            connection.close()

    sock.close()
