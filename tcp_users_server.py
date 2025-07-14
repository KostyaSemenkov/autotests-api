import socket
import threading

# Список для хранения сообщений
messages = []


def handle_client(client_socket, client_address):
    print(f"Пользователь с адресом: {client_address} подключился к серверу")

    while True:
        try:
            # Получаем сообщение от клиента
            message = client_socket.recv(1024).decode()
            if not message:
                break  # Если сообщение пустое, клиент отключился

            print(f"Пользователь с адресом: {client_address} отправил сообщение: {message}")
            messages.append(message)  # Добавляем сообщение в список

            # Отправляем всю историю сообщений клиенту
            client_socket.send('\n'.join(messages).encode())
        except Exception as e:
            print(f"Ошибка: {e}")
            break

    print(f"Пользователь с адресом: {client_address} отключился")
    client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(10)  # Максимум 10 подключений
    print("Сервер запущен на порту 12345")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()


if __name__ == "__main__":
    start_server()
