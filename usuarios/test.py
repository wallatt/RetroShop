from pydoc import cli
import unittest
from usuario_pb2 import empty, GetPersonaResponse, Cuenta
from clienteUsuario import UsuarioClient

class testClienteUsuario(unittest.TestCase):


    def testiniciarSesionCorrectamente(self):
        cliente = UsuarioClient()
        res = cliente.iniciarSesion('bebitofiumfium','abc')
        self.assertTrue(res.userSesion.isActiveSesion)
    

    def testiniciarSesionMalasCredenciales(self):
        cliente = UsuarioClient()
        res = cliente.iniciarSesion('bebitofiumfium','abc1')
        self.assertFalse(res.userSesion.isActiveSesion)


    def testCerrarSesion(self):
        cliente = UsuarioClient()
        res = cliente.iniciarSesion('Type35','abc')
        sesionAbierta = res.userSesion.isActiveSesion
        id_sesion = res.userSesion.id_sesion
        id_persona = res.userSesion.id_persona
        res = cliente.CloseSession(id_sesion, id_persona)
        self.assertTrue(sesionAbierta)
        self.assertTrue(type(res)==type(empty()))
    

    def testGetEstadoSesion(self):
        cliente = UsuarioClient()
        res = cliente.iniciarSesion('Type35','abc')
        sesionAbierta = res.userSesion.isActiveSesion
        id_sesion = res.userSesion.id_sesion
        id_persona = res.userSesion.id_persona
        estado = cliente.getSessionStatus(id_sesion, id_persona)
        self.assertTrue(estado.userSesion.isActiveSesion)
        res = cliente.CloseSession(id_sesion, id_persona)
        estado = cliente.getSessionStatus(id_sesion, id_persona)
        self.assertFalse(estado.userSesion.isActiveSesion)
    

    def testGetUsuario(self):
        cliente = UsuarioClient()
        res = cliente.getUsuario(2)
        self.assertTrue(type(res) == type(GetPersonaResponse()))
        self.assertTrue(res.persona.apellido == 'McClaren')



if __name__ == '__main__':
    # unittest.main()

    cliente = UsuarioClient()
    a = cliente.getUsuario(1)
    print(a)





