import socket
from collections import defaultdict

clients = defaultdict(str)  # registro de clientes


def handle_client(data, addr):
    # Lógica para tratar os dados recebidos de um cliente
    pass


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    s.bind(("", 8080))

    while True:
        data, addr = s.recvfrom(1024)
        handle_client(data, addr)
