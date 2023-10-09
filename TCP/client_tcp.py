import socket

class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (self.host, self.port)
        tcp.connect(dest)
        username = input('Choose a username: ')
        tcp.send(username.encode('utf-8'))
        print(f'Username set as {username}. To exit, use CTRL+X\n')
        while True:
            msg = input(f'{username}: ')
            if msg == '\x18':
                break
            tcp.send(msg.encode('utf-8'))
        tcp.close()
