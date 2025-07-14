import asyncio
import websockets


async def send_message():
    try:
        async with websockets.connect(
                "ws://localhost:8765",
                ping_interval=None,  # Отключить ping от клиента
                close_timeout=10  # Время ожидания закрытия соединения
        ) as websocket:
            message = "Привет, сервер!"
            await websocket.send(message)
            print(f"Отправлено сообщение: {message}")

            for _ in range(5):
                response = await websocket.recv()
                print(response)

    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Соединение закрыто с кодом: {e.code}")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    asyncio.run(send_message())

