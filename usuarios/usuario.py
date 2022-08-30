import grpc
import usuario_pb2_grpc
from  usuario_pb2 import (
    Persona, 
    Cuenta,
    UsuarioResponse,
    GetPersonaResponse,
    UserSesion, UserSesionResponse
)
# from dao import DAO as BDPersonas


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

BDSession={
    1: UserSesion(id_sesion=1, id_persona=1, isActiveSesion=False),
}

class ServicioUsuario(usuario_pb2_grpc.UsuarioServicer):

    def NuevoUsuario(self, request, context):
        #Validacion de datos
        self.validacionDatos(request, context)
        #Guardado de datos
        persona = request.persona
        persona.id = len(BDPersonas)+1
        BDPersonas.append(persona)

        return UsuarioResponse(id = persona.id)

    def validacionDatos(self, request, context):
        persona = request.persona
        for p in BDPersonas:
            if persona.dni == p.dni:
                context.abort(grpc.StatusCode.ALREADY_EXISTS, "Usuario ya registrado")

    def UsuarioSesion(self, request, context):
        
        validUser = self.validacionContraseña(request, context)

        sesionUser = UserSesion()
        if validUser:
            self.iniciarSesion(validUser)
            sesionUser = BDSession[validUser]
        
        return UserSesionResponse(userSesion = sesionUser)

    def validacionContraseña(self, request, context):
        cuenta = request.cuenta
        password = request.cuenta.hashedPassword
        for i in BDUsuario:
            if i['usuario'] == cuenta.usuario:
                if i['hashedPassword'] == password:
                    return i['id']
                else:
                    context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Fallo autenticacion')
                    return 0

    def iniciarSesion(self, user_id):
        if user_id not in BDSession:
            BDSession[user_id] = UserSesion(id_sesion=len(BDSession)+1, id_persona=user_id, isActiveSesion=True)
        else:
            #en lugar de cambiar solo el estado de session se deberia asignar un nuevo id de session
            BDSession[user_id].isActiveSesion = True

    def GetUsuario(self, request, context):
        user_id = request.id

        resultado = Persona()
        for persona in BDPersonas:
            if persona.id == user_id:
                resultado = persona

        return GetPersonaResponse(persona = resultado)

    def GetEstadoSesion(self, request, context):
        estadoSesion = UserSesion(id_sesion=request.id_sesion, id_persona=request.id_persona, isActiveSesion=False)
        if request.id_persona in BDSession:
            estadoSesion.isActiveSesion = BDSession[request.id_persona].isActiveSesion

        return UserSesionResponse(userSesion = estadoSesion)

    def CloseSession(self, request, context):
        if request.id_persona in BDSession:
            BDSession[request.id_persona].isActiveSesion = False

        userSession = BDSession[request.id_persona]
        return UserSesionResponse(userSesion = userSession)