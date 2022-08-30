import mysql.connector
from mysql.connector import Error

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
        
    def listarUsuarios(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM usuario")
                resultado = cursor.fetchall()
                return resultado
            except Error as ex:
                print("Error al intentar conectar conectar: {0}".format(ex))
         

dao = DAO()

print(dao.listarUsuarios())