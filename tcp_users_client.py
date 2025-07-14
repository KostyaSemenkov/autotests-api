import socket

def send_message():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    message = "Привет, сервер!"
    client_socket.send(message.encode())
    print(f"Отправлено сообщение: {message}")

    # Получаем ответ от сервера
    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()

if __name__ == "__main__":
    send_message()
