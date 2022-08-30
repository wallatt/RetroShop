import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost', 
                port = 3306,
                user = 'root',
                password = 'root',
                db = 'usuarios'
            )
        except Error as ex:
            print("Error al intentar conectar conectar: {0}".format(ex))
        
        self.duracionSesion = timedelta(minutes=10)
        
    def listarUsuarios(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT id, nombre, apellido, dni, mail, username FROM usuario")
                resultado = cursor.fetchall()
                return resultado
            except Error as ex:
                print("Error al intentar conectar conectar: {0}".format(ex))
    
    def getUsuario(self, id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT id, nombre, apellido, dni, mail, username FROM usuario where id = {0}".format(id))
                resultado = cursor.fetchone()
                return resultado
            except Error as ex:
                print("Error al intentar conectar conectar: {0}".format(ex))
    
    def getUsuarioDNI(self, dni):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT id, nombre, apellido, dni, mail, username FROM usuario where dni = {0}".format(dni))
                resultado = cursor.fetchone()
                return resultado
            except Error as ex:
                print("Error al intentar conectar conectar: {0}".format(ex))

    def getUsuarioUser(self, username):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "SELECT id, nombre, apellido, dni, mail, username FROM usuario where username = %s"
                user = (username,)
                cursor.execute(query, user)
                resultado = cursor.fetchone()
                return resultado
            except Error as ex:
                print("Error al intentar conectar conectar: {0}".format(ex))

    
    def ingresarUsuario(self,nombre, apellido, dni, mail, username, password ):
        if self.conexion.is_connected():
            if not self.getUsuarioDNI(dni) and not self.getUsuarioUser(username):
                try:
                    cursor = self.conexion.cursor()
                    sql = "INSERT INTO usuario (nombre, apellido, dni, mail, username, password) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')"

                    cursor.execute(sql.format(nombre, apellido, dni, mail, username, password))
                    self.conexion.commit()
                    return cursor.lastrowid
                except Error as ex:
                    print("No se pudo registrar usuario: {0}".format(ex))
    
    def getCredenciales(self, username):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "SELECT password FROM usuario where username = %s"
                user = (username,)
                cursor.execute(query, user)
                resultado = cursor.fetchone()
                return resultado
            except Error as ex:
                print("Error al intentar conectar conectar: {0}".format(ex))

    def iniciarSesion(self,username):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                self.closeOpenSesions(username)
                sql = "INSERT INTO sesion (inicioSesion, usuario_id) VALUES ('{0}', '{1}')"
                id_persona = self.getUsuarioUser(username)[0]
                inicio = datetime.now()
                cursor.execute(sql.format(inicio, id_persona))
                self.conexion.commit()
                return cursor.lastrowid

            except Error as ex:
                print("Error al intentar conectar conectar: {0}".format(ex))

    def closeOpenSesions(self,username):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "SELECT idsesion FROM sesion where usuario_id = %s and closedSesion <=> NULL"
                id_persona = self.getUsuarioUser(username)[0]
                sesion = (id_persona,)
                cursor.execute(query, sesion)
                sesiones = cursor.fetchall()
                for sesion in sesiones:
                    self.cerrarSesion(id_persona, sesion[0])
            except Error as ex:
                print("Error al intentar conectar conectar: {0}".format(ex))


    def isActiveSesion(self,user_id, sesion_id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "SELECT inicioSesion FROM sesion where usuario_id = %s and idsesion = %s and closedSesion <=> NULL"
                sesion = (user_id, sesion_id,)
                cursor.execute(query, sesion)

                resultado = cursor.fetchone()
                if resultado:
                    resultado = resultado[0]
                    inicio = datetime.now()
                    c = (inicio - resultado)
                    return c < self.duracionSesion
                return False
            except Error as ex:
                print("Error al intentar conectar conectar: {0}".format(ex))
    
    def cerrarSesion(self, user_id, sesion_id):
        if self.isActiveSesion(user_id, sesion_id):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    query = "UPDATE sesion set closedSesion = 1 where idsesion = %s"
                    sesion = (sesion_id,)
                    cursor.execute(query, sesion)
                    self.conexion.commit()
                    return True

                except Error as ex:
                    print("Error al intentar conectar conectar: {0}".format(ex))
        


    
    
         
if __name__ == "__main__":
    dao = DAO()

    # print(dao.ingresarUsuario('ferruccio', 'Lambo',333, 'fl@gmail.com','Myura', 'fgh123'))
    # print(dao.listarUsuarios())
    # print(dao.getUsuario(2))
    # print(dao.getUsuarioDNI(232))
    # print(dao.getUsuarioUser('Myura'))
    # print(dao.listarUsuarios())
    print(dao.iniciarSesion('MCP1'))
    # print(dao.isActiveSesion(2,8))
    # dao.cerrarSesion(2,8)
    # print(dao.isActiveSesion(2,8))

