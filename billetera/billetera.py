import grpc
import billetera_pb2
import billetera_pb2_grpc
from billeteraDao import DAO
from billetera_pb2 import saldoResponse, Empty, puedeHacerCompraResponse

class servicioBilletera(billetera_pb2_grpc.BilleteraServicer):

    def __init__(self,):
        self.billetera = DAO()

    def getSaldo(self, config, context):
        print("preguntando por saldo")
        idUsuario = config.idUsuario
        print(idUsuario)
        saldo = 0.0
        print(self.billetera.existeUsuario(idUsuario))
        if self.billetera.existeUsuario(idUsuario):
            saldo = self.billetera.getSaldo(idUsuario)
        return saldoResponse(saldo = saldo)


    def cargarSaldo(self, config, context):
        print("por cargar saldo")
        idUsuario = config.idUsuario
        importe = config.importe
        print("importe a cargar ",importe)
        print("importe a cargar ",idUsuario)
        if(importe <= 0):
            return Empty()
        if not self.billetera.existeUsuario(idUsuario):
            self.billetera.nuevoUsuario(idUsuario)
        self.billetera.cargarSaldo(idUsuario,importe)
        print("saldo cargado")
        return Empty()
        

    def puedeHacerCompra(self,config, context):
        print("evaluando si puede hacer compra")
        idUsuario = config.idUsuario
        importe = config.importe
        if(importe <= 0 or not self.billetera.existeUsuario(idUsuario)):
            return puedeHacerCompraResponse(puedeHacerCompra = False)
        saldo = self.billetera.getSaldo(idUsuario)
        if(importe>=saldo):
            return puedeHacerCompraResponse(puedeHacerCompra = False)
        return puedeHacerCompraResponse(puedeHacerCompra = True)

        
    def hacerCompra(self,config, context):
        print("por realizar transaccion")
        comprador = config.idComprador
        vendedor = config.idVendedor
        importe = config.importe
        self.billetera.hacerTransaccion(comprador, vendedor, importe)
        print("print transaccion realizada")
        return Empty()
        