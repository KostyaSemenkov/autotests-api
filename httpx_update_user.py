import httpx  # Импортируем библиотеку HTTPX

from tools.fakers import get_random_email  # Импортируем функцию для генерации случайного email

payload = {
    "email": get_random_email(),  # Используем функцию для генерации случайного email
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
# Создаем нового рандомного пользователя
response = httpx.post("http://localhost:8000/api/v1/users", json=payload)
print(f' Статус код создания пользователя: {response.status_code}')
print(f' Данные созданного пользователя: {response.json()}')
user_email = response.json()['user']['email']
user_id = response.json()['user']['id']

# Данные для входа в систему
login_payload = {
    "email": f"{user_email}",
    "password": "string"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print(f' Статус код создания токенов: {login_response.status_code}')
print(f' Токены пользователя: {login_response_data}')


# Получаем хедер авторизации для дальнейших запросв
user_token = login_response_data['token']['accessToken']
headers_for_user = {"Authorization": f"Bearer {user_token}"}

# Используя хедер отправляем запрос на изменение imail нашего пользователя
payload_for_patch = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
patch_user = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}", headers=headers_for_user, json=payload_for_patch)
# Выводим измененные данные пользователя
print(f' Статус код изменения данных пользователя: {patch_user.status_code}')
print(f' Измененные данные пользователя: {patch_user.json()}')