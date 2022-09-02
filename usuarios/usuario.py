import hashlib
import grpc
import usuario_pb2_grpc
from  usuario_pb2 import (
    Persona, 
    Cuenta,
    UsuarioResponse,
    GetPersonaResponse,
    UserSesion, UserSesionResponse
)
from dao import DAO

import logging



class ServicioUsuario(usuario_pb2_grpc.UsuarioServicer):


    def __init__(self,):
        self.BDUsuarios = DAO()


    def NuevoUsuario(self, request, context):
        persona = request.persona
        cuenta = request.cuenta
        hashedPassword = self.hashear(cuenta.hashedPassword)
        id_usuario = 0
        try:
            id_usuario = self.BDUsuarios.ingresarUsuario(persona.nombre,persona.apellido,persona.dni, persona.mail, cuenta.usuario, hashedPassword)
        except:
            print("No se pudo registrar usuario")    
        return UsuarioResponse(id = id_usuario)


    def hashear(self, string):
        hash = hashlib.sha256()
        hash.update(bytes(string, 'utf-8'))
        hashedpassword = hash.hexdigest()
        return str(hashedpassword)


    def UsuarioSesion(self, request, context):
        cuenta = request.cuenta
        validUser = self.validacionContraseña(request, context)

        sesionUser = UserSesion()
        if validUser:
            id_sesion = self.iniciarSesion(cuenta.usuario)
            user_id = self.BDUsuarios.getUsuarioId(cuenta.usuario)[0]
            sesionUser = UserSesion(id_sesion= id_sesion, id_persona = user_id, isActiveSesion = True)
        
        return UserSesionResponse(userSesion = sesionUser)


    def validacionContraseña(self, request, context):
        cuenta = request.cuenta
        password = self.hashear(cuenta.hashedPassword)
        bdpassword = ''
        try:
            bdpassword = self.BDUsuarios.getCredenciales(cuenta.usuario)[0]
        except:
            print("No se pudo obetener usuario")
        if password == bdpassword:
            return True
        return False


    def iniciarSesion(self, usuario):
        id_sesion = 0
        try:
            id_sesion = self.BDUsuarios.iniciarSesion(usuario)
        except:
            print('No se pudo iniciar sesion')
        return id_sesion


    def GetUsuario(self, request, context):
        user_id = request.id
        persona = Persona()
        cuenta = Cuenta()
        # print('hola')
        # persona = Persona(id =1, nombre = 'walter', apellido = 'lacoste', dni = 111 ,mail = 'yo@gmail.co')
        # cuenta = Cuenta(usuario = 'wlacoste', hashedPassword = '')
        
        try:
            res = self.BDUsuarios.getUsuario(user_id)
            persona = Persona(id =res[0], nombre = res[1], apellido = res[2], dni = res[3] ,mail = res[4])
            cuenta = Cuenta(usuario = res[5], hashedPassword = '')
        except:
            print('no se pudo obetener usuario')

        return GetPersonaResponse(persona = persona, cuenta = cuenta)


    def GetEstadoSesion(self, request, context):
        id_sesion = request.id_sesion
        id_persona = request.id_persona
        estadoSesion = UserSesion(id_sesion=id_sesion, id_persona=id_persona, isActiveSesion=False)
        try:
            estadoSesion.isActiveSesion = self.BDUsuarios.isActiveSesion(id_persona, id_sesion)
        except:
            print('No se pudo obtener estado sesion')

        return UserSesionResponse(userSesion = estadoSesion)


    def CloseSession(self, request, context):
        try:
            self.BDUsuarios.cerrarSesion(request.id_persona, request.id_sesion)
        except:
            print('Error cerrando sesion')
        return UserSesionResponse()