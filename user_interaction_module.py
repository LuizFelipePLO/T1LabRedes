from application_manager import ApplicationManager
from TCP.client_tcp import TCPClient
from UDP.client_udp import UDPClient


def display_menu():
    print("1. Iniciar Cliente TCP")
    print("2. Iniciar Cliente UDP")
    print("3. Iniciar Servidor TCP")
    print("4. Iniciar Servidor UDP")
    print("5. Sair")


def user_input():
    app_manager = ApplicationManager()

    while True:
        display_menu()
        choice = input("Escolha uma opção: ")

        if choice == '1':
            host = input("Insira o endereço IP do servidor: ")
            port = int(input("Insira a porta do servidor: "))
            client = TCPClient(host, port)
            client.run()

        elif choice == '2':
            host = input("Insira o endereço IP do servidor: ")
            port = int(input("Insira a porta do servidor: "))
            client = UDPClient(host, port)
            client.run()

        elif choice == '3':
            host = input(
                "Insira o endereço IP do servidor (deixe em branco para localhost): ")
            port = int(input("Insira a porta do servidor: "))
            app_manager.handle_tcp(host, port)

        elif choice == '4':
            host = input(
                "Insira o endereço IP do servidor (deixe em branco para localhost): ")
            port = int(input("Insira a porta do servidor: "))
            app_manager.handle_udp(host, port)

        elif choice == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    user_input()
