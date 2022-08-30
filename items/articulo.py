import articulo_pb2
import articulo_pb2_grpc
from articulo_pb2 import Empty, DataChunk, DownloadProductImageRequest, UploadProductResponse
from concurrent import futures
import grpc
from pathlib import Path


class servicioArticulo(articulo_pb2_grpc.ItemServiceServicer):

    def DownloadProductImage(self, request, context):
        product_id = request.product_id
        # imagesPaths = BDItems.getPaths(product_id)
        imagesPaths = 'hola.png'
        chunk_size = 1024
        for path in imagesPaths:
            image_path = Path(__file__).resolve().parent.joinpath('img/'+path)

            with image_path.open('rb') as f:
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    yield DataChunk(data=chunk)
    

    def UploadProductImage(self, request_iterator, context):
        s=[]
        for DataChunk in request_iterator:
            s.append(DataChunk.data)
            if DataChunk.configuration:
                config = DataChunk.configuration
        filename = str(config.user_id)+'_'+str(config.item_id)+'_'+config.nombre
        #Verificar cantidad de fotos ya guardadas
        #Obtener id foto
        #guardar
        with open('bkpimg/'+filename,'wb') as f:
            for chunk in s:
                f.write(chunk)

        return UploadProductResponse(result_status=UploadProductResponse.SUCCESS)



    





