from concurrent import futures
import grpc
import course_service_pb2
import course_service_pb2_grpc


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация методов gRPC-сервиса CourseService"""

    def GetCourse(self, request, context):
        """Метод GetCourse обрабатывает входящий запрос"""
        print(f'Получен запрос к методу GetCourse для курса: {request.course_id}')

        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов"
        )


def serve():
    """Функция создает и запускает gRPC-сервер"""

    # Создаем сервер с пулом потоков (до 10 потоков)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Регистрируем сервис CourseService на сервере
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(
        CourseServiceServicer(), server)

    # Настраиваем сервер для прослушивания порта 50051
    server.add_insecure_port('[::]:50051')

    # Запускаем сервер
    server.start()
    print("gRPC сервер курсов запущен на порту 50051...")

    # Ожидаем завершения работы сервера
    server.wait_for_termination()


if __name__ == '__main__':
    serve()










