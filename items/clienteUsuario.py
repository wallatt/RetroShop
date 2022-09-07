import grpc
import usuario_pb2
import usuario_pb2_grpc
import unittest


class UsuarioClient():
    
    def __init__(self):
        self.host = 'localhost'
        self.port = '50055'

        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.client = usuario_pb2_grpc.UsuarioStub(self.channel)


    def getSessionStatus(self, id_sesion, id_persona):
        request = usuario_pb2.getSessionStatus(id_sesion = id_sesion, id_persona = id_persona)
        response = self.client.GetEstadoSesion(request)
        return response.userSesion.isActiveSesion









        













