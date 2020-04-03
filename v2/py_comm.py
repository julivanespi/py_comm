import argparse
import sys
from py_comm_server import py_comm_server
from py_comm_client import py_comm_client


def start_server():
    print('This is a server brehhh')
    pcs = py_comm_server()


def start_client(port, ip_address):
    #print('The port is: ' + port)
    #print('The server address is: ' + ip_address)
    pcc = py_comm_client(port, ip_address)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', action='store',
                        dest='port',
                        help='Store the port to connect to')

    parser.add_argument('-a', action='store',
                        dest='ip_address',
                        help='Store the ip_address to connect to')

    parser.add_argument('-t', action='store_const',
                        dest='constant_value',
                        const='value-to-store',
                        help='Store a constant value')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    parser.add_argument('-i', metavar='in-file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o', metavar='out-file',
                        type=argparse.FileType('wt'))

    results = parser.parse_args()

    if not len(sys.argv) > 1:
        print('oh shit')
        start_server()
    else:
        start_client(results.port, results.ip_address)
