def user_input():
    while True:
        cmd = input("Enter your command: ")
        if cmd == 'exit':
            break
        else:
            # lógica para tratar diferentes tipos de comandos.
            pass

def display_message(message):
    print(f"Server says: {message}")
