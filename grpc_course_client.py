import grpc
import course_service_pb2
import course_service_pb2_grpc


def run():
    # Устанавливаем соединение с сервером
    channel = grpc.insecure_channel('localhost:50051')
    stub = course_service_pb2_grpc.CourseServiceStub(channel)

    # Отправляем запрос
    response = stub.GetCourse(
        course_service_pb2.GetCourseRequest(course_id="api-course")
    )

    # Выводим ответ
    print(f"course_id: \"{response.course_id}\"")
    print(f"title: \"{response.title}\"")
    print(f"description: \"{response.description}\"")


if __name__ == '__main__':
    run()