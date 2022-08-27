from concurrent import futures
import grpc

import usuario_pb2_grpc
from  usuario_pb2 import (
    Persona, 
    Cuenta,
    UsuarioResponse
    
)

#Reemplazar por BD
BDUsuarios = [
    Persona(id=1, nombre="walter",apellido="lacoste",dni=111111,mail="wl@gmail.com"),
    Persona(id=2, nombre="pedro",apellido="perez",dni=222222,mail="pp@gmail.com"),
    Persona(id=3, nombre="jorge",apellido="smith",dni=333333,mail="js@gmail.com"),
    Persona(id=4, nombre="nacho",apellido="nike",dni=444444,mail="nn@gmail.com"),
    Persona(id=5, nombre="javier",apellido="balbin",dni=555555,mail="jb@gmail.com"),
]

class ServicioUsuario(usuario_pb2_grpc.UsuarioServicer):

    def NuevoUsuario(self, request, context):
        #Validacion de datos
        self.validacionDatos(request, context)
        #Guardado de datos
        persona = request.persona
        persona.id = len(BDUsuarios)+1
        BDUsuarios.append(persona)

        return UsuarioResponse(id = persona.id)
            
        





    def validacionDatos(self, request, context):
        persona = request.persona
        for p in BDUsuarios:
            if persona.dni == p.dni:
                context.abort(grpc.StatusCode.ALREADY_EXISTS, "Usuario ya registrado")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    usuario_pb2_grpc.add_UsuarioServicer_to_server(ServicioUsuario(), server)
    
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()



if __name__ == "__main__":

    serve()

    