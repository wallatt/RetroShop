import grpc
import billetera_pb2
import billetera_pb2_grpc

class BilleteraClient():

    def __init__(self):
        self.host = 'localhost'
        self.port = '50054'

        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.client = billetera_pb2_grpc.BilleteraStub(self.channel)

    def getSaldo(self, idUsuario):
        request = billetera_pb2.saldoRequest(idUsuario=idUsuario)
        response = self.client.getSaldo(request)
        return response.saldo


    def puedeHacerCompra(self, idUsuario, importe):
        request = billetera_pb2.puedeHacerCompraRequest(idUsuario = idUsuario, importe = importe)
        response = self.client.puedeHacerCompra(request)
        print("Puede hacer compra si o no,",response.puedeHacerCompra)
        return response.puedeHacerCompra
    
    def hacerCompra(self, idComprador, idVendedor, importe):
        print("por hacer compra")
        request = billetera_pb2.hacerCompraRequest(idComprador = idComprador, idVendedor = idVendedor, importe = importe)
        self.client.hacerCompra(request)
        
