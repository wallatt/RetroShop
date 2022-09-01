import grpc
import articulo_pb2
import articulo_pb2_grpc
from articulo_pb2 import Empty, DataChunk, DownloadProductImageRequest, UploadProductResponse, ItemId, metadata
from concurrent import futures
from pathlib import Path
from articulodao import DAO


class servicioArticulo(articulo_pb2_grpc.ItemServiceServicer):

    def __init__(self,):
        self.BDItems = DAO()

    def DownloadProductImage(self, request, context):
        """Recibe una lista de nombres de imagenes y devuelve las imagenes"""
        imagesPaths = request.nombre_imagen.replace('[', '').replace(']', '').replace("'", '').replace(' ', '').split(',')
        chunk_size = 1024
        for path in imagesPaths:
            image_path = Path(__file__).resolve().parent.joinpath('img/'+path)
            config_imagen = metadata(user_id = 1, item_id = 1, tipo_img ='png', nombre = path)
            yield DataChunk(configuration = config_imagen)

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

    def NuevoItemSaleRequest(self, request_iterator, context):
        s=[]
        for DataChunk in request_iterator:
            s.append(DataChunk.data)
            if DataChunk.configuration:
                config = DataChunk.configuration
        
        filename = self.nombreFoto(config)
        #Verificar cantidad de fotos ya guardadas
        parametros = self.getParametros(config, filename)
        item_id = self.BDItems.insertarNuevoArticulo(*parametros)
        #guardar
        with open('bkpimg/'+filename,'wb') as f:
            for chunk in s:
                f.write(chunk)
        return ItemId(item_id = item_id, user_id = parametros[0])

    def nombreFoto(self, config):
        cantPublicacionVendedor = self.BDItems.getCantPublicaciones(config.user_id)
        return str(config.user_id)+'_'+str(cantPublicacionVendedor)+'_'+'1'+'.'+config.tipo_img

    def getParametros(self,config, filename):
        parametros = []
        parametros.append(config.user_id)
        parametros.append(config.item.nombre)
        parametros.append(config.item.fecha_fabricacion)
        parametros.append(config.item.category)
        parametros.append(filename)
        parametros.append(config.item.descripcion)
        parametros.append(config.item.precio)
        parametros.append(config.item.cantidad)
        return parametros
        
        




    





