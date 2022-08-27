import grpc
import usuario_pb2
import usuario_pb2_grpc

from usuario_pb2 import Persona, Cuenta

channel = grpc.insecure_channel("localhost:50051")
client = usuario_pb2_grpc.UsuarioStub(channel)

nuevoUsuario = {"id": 3, 
                "nombre":'roman',
                "apellido":'palacio',
                "dni":888888,
                "mail" : 'asds@gmail.com'}
nuevaCuenta = {"hashedPassword":'abc123', "usuario": "bebitofiumfium"}

request = usuario_pb2.CrearUsuarioRequest(persona=nuevoUsuario, cuenta=nuevaCuenta)

print(client.NuevoUsuario(request))


cuenta = {'usuario':'blanco33', 'hashedPassword':'abc'}

request = usuario_pb2.IniciarSesionRequest(cuenta = cuenta)

print(client.UsuarioSesion(request))





