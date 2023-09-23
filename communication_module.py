import socket


def send_message(server_ip, server_port, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    # Montagem manual do pacote UDP pode ser feita aqui, se necessário
    s.sendto(message, (server_ip, server_port))


def receive_message(buffer_size):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    data, addr = s.recvfrom(buffer_size)
    # Desmontagem manual do pacote UDP pode ser feita aqui, se necessário
    return data, addr
