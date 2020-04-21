import socket
import os
from threading import *


class py_comm_client(Thread):

    def __init__(self, socket, server_addr):
        Thread.__init__(self)
        self.socket = socket
        self.server_addr = server_addr
        self.start()

    def run(self):
        while True:
            c_message = input(os.getenv('USER') + ' ')
            self.socket.send(c_message.encode())
            if c_message == 'bye':
                self.socket.close()
                break
            #print('[INFO] About to get data')
            data = self.socket.recv(1024).decode()
            #print('[INFO] Got the data data')
            # print(data)
            if data == '':
                print('[INFO] Did not get data')
                break
            print(data)
        print('[INFO] Ended session')


if __name__ == "__main__":
    obj = py_comm_client(12345, '192.168.0.8')
