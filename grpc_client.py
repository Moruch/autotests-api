# Импорт основной библиотеки gRPC для Python
import grpc

# Импорт сгенерированного модуля с классами сообщений Protobuf
import user_service_pb2

# Импорт сгенерированного модуля с gRPC сервисами и классами-заглушками (stubs)
import user_service_pb2_grpc

# Создание небезопасного (без SSL/TLS) канала связи с gRPC-сервером на localhost, порт 50051
channel = grpc.insecure_channel('localhost:50051')

# Создание объекта-заглушки (stub) для удаленного вызова методов сервиса UserService
stub = user_service_pb2_grpc.UserServiceStub(channel)

# Вызов удаленного метода Getuser с передачей объекта GetUserRequest, содержащего имя "Alice"
response = stub.Getuser(user_service_pb2.GetUserRequest(username="Alice"))

# Вывод полученного от сервера ответа (объекта GetUserResponse)

