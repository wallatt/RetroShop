from concurrent import futures
import grpc

import usuario_pb2_grpc
from  usuario_pb2 import (
    Persona, 
    Cuenta,
    UsuarioResponse,
    GetPersonaResponse,
    IniciarSesionRequest
    
)

#Reemplazar por BD
BDPersonas = [
    Persona(id=1, nombre="walter",apellido="lacoste",dni=111111,mail="wl@gmail.com"),
    Persona(id=2, nombre="pedro",apellido="perez",dni=222222,mail="pp@gmail.com"),
    Persona(id=3, nombre="jorge",apellido="smith",dni=333333,mail="js@gmail.com"),
    Persona(id=4, nombre="nacho",apellido="nike",dni=444444,mail="nn@gmail.com"),
    Persona(id=5, nombre="javier",apellido="balbin",dni=555555,mail="jb@gmail.com"),
]
BDUsuario= [
    {"id":1,"usuario":"aguila37", "hashedPassword":"abc123"},
    {"id":2,"usuario":"ringo45", "hashedPassword":"abc123"},
    {"id":3,"usuario":"blanco33", "hashedPassword":"abc123"},
    {"id":4,"usuario":"perro62",  "hashedPassword":"abc123"},
]

class ServicioUsuario(usuario_pb2_grpc.UsuarioServicer):

    def NuevoUsuario(self, request, context):
        #Validacion de datos
        self.validacionDatos(request, context)
        #Guardado de datos
        persona = request.persona
        persona.id = len(BDPersonas)+1
        BDPersonas.append(persona)

        return UsuarioResponse(id = persona.id)

    def UsuarioSesion(self, request, context):
        
        validUser = self.validacionContraseña(request, context)

        if validUser:
            self.iniciarSesion(validUser)

        return UsuarioResponse(id = validUser)

    def GetUsuario(self, request, context):
        user_id = request.id

        resultado = Persona()
        for persona in BDPersonas:
            if persona.id == user_id:
                resultado = persona

        return GetPersonaResponse(persona = resultado)



    def validacionDatos(self, request, context):
        persona = request.persona
        for p in BDPersonas:
            if persona.dni == p.dni:
                context.abort(grpc.StatusCode.ALREADY_EXISTS, "Usuario ya registrado")
    
    def validacionContraseña(self, request, context):
        cuenta = request.cuenta
        password = request.cuenta.hashedPassword + '123'
        for i in BDUsuario:
            if i['usuario'] == cuenta.usuario:
                if i['hashedPassword'] == password:
                    return i['id']
                else:
                    context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Fallo autenticacion')
                    return 0
    
    def iniciarSesion(self, user_id):
        pass
        
                

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    usuario_pb2_grpc.add_UsuarioServicer_to_server(ServicioUsuario(), server)
    
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()



if __name__ == "__main__":

    serve()

    