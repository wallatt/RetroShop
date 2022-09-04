import grpc
import articulo_pb2
import articulo_pb2_grpc
from articulo_pb2 import Empty, DataChunk
from articulo_pb2 import DownloadProductImageRequest, UploadProductResponse, ItemId, metadata
from articulo_pb2 import ItemSale, Item, ItemCategory, Items
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

        with open('img/'+filename,'wb') as f:
            for chunk in s:
                f.write(chunk)

        return UploadProductResponse(result_status=UploadProductResponse.SUCCESS)


    def NuevoItemSaleRequest(self, request_iterator, context):
        s=[]
        for NewItemSaleRequest in request_iterator:
            s.append(NewItemSaleRequest.data)
            if str(NewItemSaleRequest.configuration):
                config = NewItemSaleRequest.configuration
                
        parametros = self.getParametros(config)
        item_id = self.BDItems.insertarNuevoArticulo(*parametros)

        idFoto = self.BDItems.insertarFoto(item_id, "abc")
        
        punto = '.' if config.tipo_img[0] !='.' else ''
        filename = str(config.user_id)+'_'+str(item_id)+'_'+str(idFoto)+punto+config.tipo_img

        self.BDItems.updateRutaFoto(item_id, filename, idFoto)

        with open('img/'+filename,'wb') as f:
            for chunk in s:
                f.write(chunk)
        return ItemId(item_id = item_id, user_id = parametros[0])


    def getParametros(self,config):
        fech = config.item.fecha_fabricacion
        num = str(fech).split(':')
        
        fecha = datetime.fromtimestamp(int(num[1]))
        categoria = int(str(config.item.category))+1
        parametros = []
        parametros.append(config.user_id)
        parametros.append(config.item.nombre)
        parametros.append(fecha)
        parametros.append(categoria)
        parametros.append(config.item.descripcion)
        parametros.append(config.item.precio)
        parametros.append(config.item.cantidad)
        return parametros


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
            isActiva = articulo[8],)
        vendedor = articulo[7]

        return vendedor, item, fotos

    def parsearArticuloVendedor(self, articulo):
        logging.info('paerse')
        fotos =[]
        for ruta in articulo[10]:
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
        cantVendida = articulo[9],
        isActiva = articulo[8])
        vendedor = articulo[7]


        return vendedor, item, fotos


    def nombreFoto(self, config):
        cantPublicacionVendedor = self.BDItems.getCantPublicaciones(config.user_id)
        return str(config.user_id)+'_'+str(cantPublicacionVendedor)+'_'+'1'+'.'+config.tipo_img


    def GetItems(self, config, context):
        id_usuario = config.user_id
        id_articulos = self.BDItems.getItemsdentroDeParametros()
        articulos =[]
        for id in id_articulos:
            articulo = self.BDItems.getArticulo(id)
            seller, item, imagen = self.parsearArticulo(articulo)
            articulos.append(ItemSale(seller_id=seller, item=item, imagen=imagen))
        return Items(items = articulos)
            
        
    def ItemsEnVenta(self, config, context):
        id_usuario = config.user_id
        articulos = self.BDItems.getPublicacionesDelVendedor(id_usuario)
        resultado =[]
        for articulo in articulos:
            seller, item, imagen = self.parsearArticuloVendedor(articulo)
            resultado.append(ItemSale(seller_id=seller, item=item, imagen=imagen))
        return Items(items = resultado)

    def ComprarItem(self,config,context):
        user_id = config.user_id
        item_id = config.item_id

        cantidad = config.cantidad
        self.BDItems.comprarItem(item_id,user_id, cantidad)
        articulo = self.BDItems.getArticulo(item_id)
        if articulo[4]<=0:
            self.BDItems.darDeBajaPublicacion(item_id)

        return Empty()


        




    





