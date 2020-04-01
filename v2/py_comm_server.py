import socket


class py_comm_server:

    def __init__(self):
        self.setup()

    def setup(self):
        try:
            s = socket.socket()
            print("[INFO] Socket created")
        except:
            print("[ERROR] Not successful creating socket")
        port = 12345
        s.bind(('', port))
        s.listen(5)
        print('[INFO] socket is listening')

        while True:
            c, addr = s.accept()
            print('[INFO] Got connection from', addr)
            c.close()
            break


if __name__ == "__main__":
    obj = py_comm_server()
