import socket

class UDPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest = (self.host, self.port)
        username = input('Choose a username: ')
        udp.sendto(username.encode('utf-8'), dest)  # Send username as the first message
        print(f'Username set as {username}. To exit, use CTRL+X\n')
        while True:
            msg = input(f'{username}: ')
            if msg == '\x18':
                break
            udp.sendto(msg.encode('utf-8'), dest)
