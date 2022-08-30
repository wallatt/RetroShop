from pathlib import Path
import grpc
from faker import Faker
import articulo_pb2_grpc
from articulo_pb2 import DownloadProductImageRequest, DataChunk, metadata

class ImageClient():

    def __init__(self):
        self.host = 'localhost'
        self.port = '50051'
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.client = articulo_pb2_grpc.ItemServiceStub(self.channel)

    def test_DownloadProductImage(self):
        faker = Faker()
        image_file = faker.file_name(category=None, extension='png')
        target_image_file = 'bkpimg/'+image_file
        data_chunks = self.client.DownloadProductImage(DownloadProductImageRequest(product_id=1))
        with open(target_image_file, 'wb') as f:
            for chunk in data_chunks:
                f.write(chunk.data)
    
    def uploadImage(self,image_path, nombre, tipo):
        chunk_size = 1024
        # image_path = Path(__file__).resolve().parent.joinpath('img/abc2.png')
        print('hola')
        #with image_path.open('rb') as f:
        chunks = []
        
        with open(image_path, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                chunks.append(DataChunk(data=chunk))
        chunks.append(DataChunk(configuration = metadata(user_id =1, item_id =1, tipo_img='png',nombre = nombre)))
        self.client.UploadProductImage(iter(chunks))

    # def uploadImages(self, image_paths, tipo):
    #     chunk_size = 1024
    #     for image_path in image_paths.keys():
    #         chunks = []
    #         with open(image_path, 'rb') as f:
    #             while True:
    #                 chunk = f.read(chunk_size)
    #                 if not chunk:
    #                     break
    #                 chunks.append(DataChunk(data=chunk, user_id =1, item_id =1, tipo_img='png', nombre = image_paths[image_path]))
    #         self.client.UploadProductImage(iter(chunks))






cliente = ImageClient()
image_paths = {'img/abc1.png':'abc1'}
cliente.uploadImage('img/abc1.png','abc1.png','png')
# cliente.uploadImage('img/abc1.png','png')


cliente.test_DownloadProductImage()




