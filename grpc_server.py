# Импорт основных библиотек
import grpc  # Основная библиотека gRPC для Python
from concurrent import futures  # Для работы с потоками/асинхронностью
import user_service_pb2  # Сгенерированный Protobuf-модуль с типами сообщений
import user_service_pb2_grpc  # Сгенерированный модуль с gRPC сервисами


# Реализация gRPC сервиса
class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    """
    Класс-обработчик gRPC сервиса, наследуется от сгенерированного базового класса
    """

    def Getuser(self, request, context):
        """
        Реализация RPC-метода Getuser, объявленного в .proto-файле
        :param request: Объект GetUserRequest (с полем username)
        :param context: Контекст вызова (метаданные, таймауты и т.д.)
        :return: Объект GetUserResponse
        """
        print(f"Получен запрос к методу Getuser от пользователя: {request.username}")
        return user_service_pb2.GetUserResponse(message=f"Привет, {request.username}")


# Функция запуска сервера
def serve():
    """
    Настраивает и запускает gRPC сервер
    """
    # 1. Создаем сервер с пулом из 10 потоков
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # 2. Регистрируем наш обработчик сервиса
    user_service_pb2_grpc.add_UserServiceServicer_to_server(
        UserServiceServicer(), server)

    # 3. Открываем порт 50051 без шифрования (для тестов)
    server.add_insecure_port('[::]:50051')  # [::] - слушаем все IPv6-адреса

    # 4. Запускаем сервер
    server.start()
    print("gRPC сервер запущен на порту 50051...")

    # 5. Блокируем поток, пока сервер не будет остановлен
    server.wait_for_termination()


# Точка входа
if __name__ == "__main__":
    serve()  # Запускаем сервер при выполнении файла
