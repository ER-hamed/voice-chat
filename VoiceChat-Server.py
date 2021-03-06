import socket
from _thread import start_new_thread


class Server:
    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 9999
        self.buffer = 512
        self.clients = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.start()

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print('Start on ' + self.host + ':' + str(self.port))
        while True:
            try:
                client, (ip, port) = self.socket.accept()
                print('join ' + str(ip))
                self.clients.append(client)
                start_new_thread(self.handle, (client, ip))
            except KeyboardInterrupt:
                exit()

    def broadcast(self, sock, data):
        for client in self.clients:
            if client == sock:
                continue
            else:
                client.send(data)

    def handle(self, client, ip):
        while True:
            try:
                data = client.recv(self.buffer)
                if data == ''.encode():
                    self.close(client, ip)
                else:
                    self.broadcast(client, data)
            except socket.error:
                self.close(client, ip)

    def close(self, client, ip):
        client.close()
        if client in self.clients:
            self.clients.remove(client)
            print('leave ' + str(ip))
        exit()


server = Server()
