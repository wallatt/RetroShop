from concurrent import futures
import articulo_pb2_grpc
import grpc

from articulo import servicioArticulo


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    articulo_pb2_grpc.add_ItemServiceServicer_to_server(servicioArticulo(), server)
    
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()



if __name__ == "__main__":

    serve()