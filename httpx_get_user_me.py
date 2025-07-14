import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "dotvh03917@atminmail.com",
    "password": "123"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

# Получаем хедер авторизации для дальнейших запросв
user_token = login_response_data['token']['accessToken']
headers_for_user = {"Authorization": f"Bearer {user_token}"}

# Используя хедер отправляем гет-запрос на нашего пользователя
get_user_info = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers_for_user)

# Получаем статус код ответа и джсон с данными пользователя
print(f'Статус код ответа: {get_user_info.status_code}')
print(f'JSON с данными пользователя: {get_user_info.json()}')
