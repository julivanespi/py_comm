import argparse
import sys
import socket
from py_comm_server import py_comm_server
from py_comm_client import py_comm_client


def start_server():
    pcs = py_comm_server()


def start_client(port, ip_address):
    s = socket.socket()
    s.connect((ip_address, port))
    pcc = py_comm_client(s, ip_address)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', action='store',
                        type=int,
                        dest='port',
                        help='Store the port to connect to')

    parser.add_argument('-a', action='store',
                        dest='ip_address',
                        help='Store the ip_address to connect to')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    parser.add_argument('-i', metavar='in-file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o', metavar='out-file',
                        type=argparse.FileType('wt'))

    results = parser.parse_args()

    if not len(sys.argv) > 1:
        start_server()
    else:
        start_client(results.port, results.ip_address)
