from pathlib import Path
import grpc
from faker import Faker
import image_pb2_grpc
from image_pb2 import DownloadProductImageRequest, DataChunk

class ImageClient():

    def __init__(self):
        self.host = 'localhost'
        self.port = '50051'
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.client = image_pb2_grpc.ImageServiceStub(self.channel)

    def test_DownloadProductImage(self):
        faker = Faker()
        image_file = faker.file_name(category=None, extension='png')
        target_image_file = 'bkpimg/'+image_file
        data_chunks = self.client.DownloadProductImage(DownloadProductImageRequest(product_id=1))
        with open(target_image_file, 'wb') as f:
            for chunk in data_chunks:
                f.write(chunk.data)
    
    def uploadImage(self,image_path, tipo):
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
                chunks.append(DataChunk(data=chunk, user_id =1, item_id =1, tipo_img='png'))
                # self.client.UploadProductImage(DataChunk(data=chunk, user_id =1, item_id =1, tipo_img = tipo))
        # print(len(chunks))
        # with open('img/img45.png', 'wb') as f:
        #     for chunk in chunks:
        #         f.write(chunk.data)
            

        self.client.UploadProductImage(iter(chunks))





cliente = ImageClient()
cliente.uploadImage('img/abc1.png','png')


# cliente.test_DownloadProductImage()




