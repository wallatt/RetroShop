from concurrent import futures
import billetera_pb2_grpc
import grpc

from billetera import servicioBilletera


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    billetera_pb2_grpc.add_BilleteraServicer_to_server(servicioBilletera(), server)
    
    server.add_insecure_port("[::]:50053")
    server.add_insecure_port("[::]:50054")
    server.start()
    server.wait_for_termination()



if __name__ == "__main__":

    serve()