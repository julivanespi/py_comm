import socket
import os
from threading import *


class py_comm_server:

    def __init__(self):
        self.s = socket.socket()
        self.wait_cor_connection()
        self.listen()
        self.c
        self.addr

    def wait_cor_connection(self):
        print('[INFO] Server waiting for connection')
        port = 12345
        self.s.bind(('', port))
        self.s.listen(5)
        #print('[INFO] socket is listening')
        self.c, self.addr = self.s.accept()

    def listen(self):
        print('[INFO] Server started listening')
        while True:
            #print('[INFO] Got connection from', self.addr)
            data = self.c.recv(1024).decode()
            if data == '':
                break
            print(data)
            s_message = input(os.getenv('USER') + ' ')
            # self.s.send(s_message.encode())
            self.c.send(s_message.encode())
        print('[INFO] Session over')


if __name__ == "__main__":
    obj = py_comm_server()
