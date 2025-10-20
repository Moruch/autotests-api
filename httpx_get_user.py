import httpx  # Импортируем библиотеку для отправки HTTP-запросов

from tools.fakers import get_random_email  # Импортируем функцию генерации случайного email

# Создаем пользователя
create_user_payload = {  # Создаем словарь с данными для регистрации пользователя
    "email": get_random_email(),  # Генерируем уникальный email для каждого теста
    "password": "string",  # Пароль (в данном случае простой строкой)
    "lastName": "string",  # Фамилия пользователя
    "firstName": "string",  # Имя пользователя
    "middleName": "string"  # Отчество пользователя
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)  # Отправляем POST-запрос на создание пользователя
create_user_response_data = create_user_response.json()  # Преобразуем ответ сервера из JSON в словарь Python
print('Create user data:', create_user_response_data)  # Выводим данные созданного пользователя

# Проходим аутентификацию
login_payload = {  # Создаем словарь с данными для входа
    "email": create_user_payload['email'],  # Берем email из данных регистрации
    "password": create_user_payload['password']  # Берем пароль из данных регистрации
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)  # Отправляем POST-запрос на авторизацию
login_response_data = login_response.json()  # Преобразуем ответ сервера из JSON в словарь Python
print('Login data:', login_response_data)  # Выводим данные авторизации (включая токен)

# Получаем данные пользователя
get_user_headers = {  # Создаем заголовки для авторизованного запроса
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"  # Формируем заголовок Authorization с JWT-токеном
}
get_user_response = httpx.get(  # Отправляем GET-запрос для получения данных пользователя
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",  # Формируем URL с ID пользователя
    headers=get_user_headers  # Передаем заголовки с токеном авторизации
)
get_user_response_data = get_user_response.json()  # Преобразуем ответ сервера из JSON в словарь Python
print('Get user data:', get_user_response_data)  # Выводим полученные данные пользователя
