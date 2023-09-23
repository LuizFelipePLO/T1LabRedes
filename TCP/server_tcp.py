import socket


class TCPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        orig = (self.host, self.port)
        tcp.bind(orig)
        tcp.listen(1)
        while True:
            con, cliente = tcp.accept()
            print('Conectado por', cliente)
            while True:
                msg = con.recv(1024)
                if not msg:
                    break
                print(cliente, msg)
            print('Finalizando conexao do cliente', cliente)
            con.close()
