import grpc
import course_service_pb2
import course_service_pb2_grpc

# Создание канала и клиента
channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)
# Запрос к серверу
response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="api-course"))
print(response)