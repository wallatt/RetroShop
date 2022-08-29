import grpc
import usuario_pb2
import usuario_pb2_grpc

from usuario_pb2 import Persona, Cuenta


class UsuarioClient():
    
    def __init__(self):
        self.host = 'localhost'
        self.port = '50051'

        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.client = usuario_pb2_grpc.UsuarioStub(self.channel)

    def crearUsuario(self, persona, cuenta):
        request = usuario_pb2.CrearUsuarioRequest(persona = persona, cuenta = cuenta)
        return self.client.NuevoUsuario(request)

    def iniciarSesion(self, usuario, password):
        hashedPassword = password + '123' #implementar hash de contraseña
        cuenta = Cuenta(usuario = usuario, hashedPassword=hashedPassword)
        request = usuario_pb2.IniciarSesionRequest(cuenta = cuenta)
        return self.client.UsuarioSesion(request)

    def getUsuario(self, id_persona):
        request = usuario_pb2.GetUsuarioRequest(id = id_persona)
        return self.client.GetUsuario(request)

    def getSessionStatus(self, id_sesion, id_persona):
        request = usuario_pb2.getSessionStatus(id_sesion = id_sesion, id_persona = id_persona)
        return self.client.GetEstadoSesion(request)

    def CloseSession(self, id_sesion, id_persona):
        request = usuario_pb2.closeSessionRequest(id_sesion = id_sesion, id_persona = id_persona)
        return self.client.CloseSession(request)


cliente = UsuarioClient()


nuevoUsuario = {"id": 3, 
                "nombre":'roman',
                "apellido":'palacio',
                "dni":888888,
                "mail" : 'asds@gmail.com'}
nuevaCuenta = {"hashedPassword":'abc123', "usuario": "bebitofiumfium"}

print(cliente.crearUsuario(nuevoUsuario, nuevaCuenta))

print(cliente.iniciarSesion('blanco33', 'abc'))














