from concurrent import futures
import usuario_pb2_grpc
import grpc

from usuario import ServicioUsuario

         

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    usuario_pb2_grpc.add_UsuarioServicer_to_server(ServicioUsuario(), server)
    
    server.add_insecure_port("[::]:50051")
    server.add_insecure_port("[::]:50055")
    server.add_insecure_port("[::]:50056")
    server.start()
    server.wait_for_termination()



if __name__ == "__main__":

    serve()

    