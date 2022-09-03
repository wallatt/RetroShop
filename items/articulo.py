import grpc
import articulo_pb2
import articulo_pb2_grpc
from articulo_pb2 import Empty, DataChunk
from articulo_pb2 import DownloadProductImageRequest, UploadProductResponse, ItemId, metadata
from articulo_pb2 import ItemSale, Item, ItemCategory
from concurrent import futures
from pathlib import Path
from articulodao import DAO
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import logging


class servicioArticulo(articulo_pb2_grpc.ItemServiceServicer):

    def __init__(self,):
        self.BDItems = DAO()

    def DownloadProductImage(self, request, context):
        """Recibe una lista de nombres de imagenes y devuelve las imagenes"""
        f = list(request.nombre_imagen)
        f = str(f)
        imagesPaths = f.replace('[', '').replace(']', '').replace("'", '').replace(' ', '').split(',')
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
            if str(DataChunk.configuration):
                config = DataChunk.configuration
                print(config)

        cantFotos = self.BDItems.getCantidadFotos(config.item_id)
        if cantFotos >= 5:
            return UploadProductResponse(result_status=UploadProductResponse.FAILED)

        idFoto = self.BDItems.insertarFoto(config.item_id, "")

        punto = '.' if config.tipo_img[0] !='.' else ''
        filename = str(config.user_id)+'_'+str(config.item_id)+'_'+str(idFoto)+punto+config.tipo_img

        self.BDItems.updateRutaFoto(config.item_id, filename, idFoto)

        #Verificar cantidad de fotos ya guardadas
        #Obtener id foto
        #guardar
        with open('bkpimg/'+filename,'wb') as f:
            for chunk in s:
                f.write(chunk)

        return UploadProductResponse(result_status=UploadProductResponse.SUCCESS)


    def NuevoItemSaleRequest(self, request_iterator, context):
        s=[]
        for NewItemSaleRequest in request_iterator:
            s.append(NewItemSaleRequest.data)
            if str(NewItemSaleRequest.configuration):
                config = NewItemSaleRequest.configuration
        
        # filename = self.nombreFoto(config)
        
        parametros = self.getParametros(config)
        item_id = self.BDItems.insertarNuevoArticulo(*parametros)

        idFoto = self.BDItems.insertarFoto(item_id, "abc")
        
        punto = '.' if config.tipo_img[0] !='.' else ''
        filename = str(config.user_id)+'_'+str(item_id)+'_'+str(idFoto)+punto+config.tipo_img

        print(item_id)
        print(filename)
        print(idFoto)
        self.BDItems.updateRutaFoto(item_id, filename, idFoto)

        with open('bkpimg/'+filename,'wb') as f:
            for chunk in s:
                f.write(chunk)
        return ItemId(item_id = item_id, user_id = parametros[0])


    def GetItem(self,request, context):
        id_usuario = request.user_id
        print(id_usuario,' usuario pidio item')
        id_item = request.item_id
        articulo = self.BDItems.getArticulo(id_item)
        seller, item, imagen = self.parsearArticulo(articulo)
        return ItemSale(seller_id=seller, item=item, imagen=imagen)

    def parsearArticulo(self, articulo):
        logging.info('paerse')
        fotos =[]
        for ruta in articulo[9]:
            fotos.append(ruta[0])
        timestamp = Timestamp()
        fecha = articulo[5]
        timestamp.FromDatetime(fecha)

        item = Item(item_id = articulo[0],
        nombre = articulo[1],
        descripcion = articulo[2],
        precio = articulo[3],
        cantidad = articulo[4],
        fecha_fabricacion = timestamp,
        category = articulo[6],
        )
        vendedor = articulo[7]

        return vendedor, item, fotos


        

    def nombreFoto(self, config):
        cantPublicacionVendedor = self.BDItems.getCantPublicaciones(config.user_id)
        return str(config.user_id)+'_'+str(cantPublicacionVendedor)+'_'+'1'+'.'+config.tipo_img

    def getParametros(self,config):

        print(type(config.item.fecha_fabricacion))
        fech = config.item.fecha_fabricacion
        num = str(fech).split(':')
        
        fecha = datetime.fromtimestamp(int(num[1]))
        categoria = int(str(config.item.category))+1
        parametros = []
        parametros.append(config.user_id)
        parametros.append(config.item.nombre)
        parametros.append(fecha)
        parametros.append(categoria)
        # parametros.append('')
        parametros.append(config.item.descripcion)
        parametros.append(config.item.precio)
        parametros.append(config.item.cantidad)
        print(parametros)
        return parametros
        
        




    





