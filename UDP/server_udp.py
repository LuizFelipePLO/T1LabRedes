import socket

class UDPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_db = {}  # To store usernames for each client IP address and port

    def run(self):
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        orig = (self.host, self.port)
        udp.bind(orig)
        print("UDP server started...")
        while True:
            msg, cliente = udp.recvfrom(1024)
            decoded_msg = msg.decode("utf-8")

            if cliente not in self.client_db:
                self.client_db[cliente] = decoded_msg  # Assume the first message is the username
                print(f"Username {decoded_msg} has been registered from {cliente}")
            else:
                username = self.client_db[cliente]
                print(f"{username} ({cliente}) said: {decoded_msg}")
