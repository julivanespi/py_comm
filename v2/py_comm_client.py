import socket


class py_comm_client:

    port = 0
    server_addr = ''

    def __init__(self, port, server_addr):
        self.port = port
        self.server_addr = server_addr
        self.setup()

    def setup(self):
        try:
            s = socket.socket()
            print('[INFO] Created socket')
        except:
            print('[ERROR] Could not create socket')

        try:
            print(self.port)
            print(self.server_addr)
            s.connect((self.server_addr, self.port))
            print('[INFO] Connected to server')
        except:
            print('[ERROR] Had trouble connecting to server')

        s.close()


if __name__ == "__main__":
    obj = py_comm_client(12345, '127.0.0.1')
