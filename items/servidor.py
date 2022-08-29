import image_pb2
import image_pb2_grpc
from image_pb2 import Empty, DataChunk, DownloadProductImageRequest, UploadProductResponse
from concurrent import futures
import grpc
from pathlib import Path


class servicioImagen(image_pb2_grpc.ImageServiceServicer):

    def UploadImage(self, request, context):
        content = request.data

        file = open('bkpimg/abc1.png', 'wb')

        file.write(content)
        return Empty()
    
    def DownloadProductImage(self, request, context):
        chunk_size = 1024
        image_path = Path(__file__).resolve().parent.joinpath('img/abc1.png')
        print(image_path)

        with image_path.open('rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield DataChunk(data=chunk)
    

    def UploadProductImage(self, request_iterator, context):
        target_image_file = 'bkpimg/hola.png'
        with open(target_image_file, 'wb') as f:
            for DataChunk in request_iterator:
                f.write(DataChunk.data)

        return UploadProductResponse(result_status=UploadProductResponse.SUCCESS)



    



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_pb2_grpc.add_ImageServiceServicer_to_server(servicioImagen(), server)
    
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()



if __name__ == "__main__":

    serve()

