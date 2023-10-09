import socket
import threading

class TCPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def handle_client(self, con, addr):
        username = con.recv(1024).decode('utf-8')
        print(f'Username {username} has been registered from {addr}')
        while True:
            msg = con.recv(1024)
            if not msg:
                break
            print(f'{username} ({addr}) said: {msg.decode("utf-8")}')
        print(f'Finalizing connection from {username} ({addr})')
        con.close()

    def run(self):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        orig = (self.host, self.port)
        tcp.bind(orig)
        tcp.listen(5)
        print("TCP server started...")
        while True:
            con, cliente = tcp.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(con, cliente))
            client_thread.start()
