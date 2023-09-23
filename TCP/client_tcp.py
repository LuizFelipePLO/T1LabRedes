import socket


class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (self.host, self.port)
        tcp.connect(dest)
        print('Para sair use CTRL+X\n')
        msg = input()
        while msg != '\x18':
            tcp.send(msg.encode('utf-8'))
            msg = input()
        tcp.close()
