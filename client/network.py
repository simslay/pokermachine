import socket
import pickle


class Network:
    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.11"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.name = name
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except Exception as e:
            print("network.py --> [EXCEPTION]", str(e))

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            res = pickle.loads(self.client.recv(2048*2))
            # print(str(res))
            return res
        except socket.error as e:
            print(e)
