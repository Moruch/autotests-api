from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """
    email: str
    password: str
    firstName: str
    lastName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичным API пользователей (/api/v1/users).
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод создает нового пользователя в системе.

        :param request: Словарь с данными для создания пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)