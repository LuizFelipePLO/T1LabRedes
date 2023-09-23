from user_interaction_module import user_input, display_message
from communication_module import send_message, receive_message


def main():
    while True:
        user_input()  # Espera e processa a entrada do usuário
        # Envia mensagem para o servidor
        send_message("localhost", 8080, "Your Message")
        data, addr = receive_message(1024)  # Recebe a resposta do servidor
        display_message(data.decode())  # Mostra a mensagem recebida


if __name__ == "__main__":
    main()
