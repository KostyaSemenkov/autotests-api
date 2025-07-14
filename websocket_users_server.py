import asyncio
import websockets

async def echo(websocket, path):
    try:
        async for message in websocket:
            print(f"Получено сообщение от пользователя: {message}")
            for i in range(1, 6):
                response = f"{i} Сообщение пользователя: {message}"
                await websocket.send(response)
    except websockets.exceptions.ConnectionClosedError:
        print("Клиент отключился")
    except Exception as e:
        print(f"Ошибка: {e}")

async def start_server():
    server = await websockets.serve(
        echo,
        "localhost",
        8765,
        ping_interval=20,  # Отправлять ping каждые 20 секунд
        ping_timeout=60    # Закрывать соединение после 60 секунд без ответа
    )
    print("Сервер запущен на ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(start_server())



