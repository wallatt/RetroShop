from logging import Logger
import mysql.connector
from mysql.connector import Error
from datetime import time, datetime

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost', 
                port = 3306,
                user = 'root',
                password = 'root',
                db = 'billetera'
            )
        except Error as ex:
            print("Error al intentar conectar conectar: {0}".format(ex))




    def nuevoUsuario(self, id_usuario):
        if self.conexion.is_connected():   
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO billetera(usuario) VALUES ('{0}')"
                cursor.execute(sql.format(id_usuario))
                self.conexion.commit()
                return cursor.lastrowid
            except Error as ex:
                print("No se pudo generar usuario: {0}".format(ex))

    def getUsuario(self, id_usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("select id, dinero from billetera where usuario = '{0}'")
                cursor.execute(sql.format(id_usuario))
                usuario = cursor.fetchone()
                return usuario
            except Error as ex:
                    print("No se pudo obtener usuario: {0}".format(ex))    

    def existeUsuario(self, id_usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("select COUNT(id) from billetera where usuario = '{0}'")
                cursor.execute(sql.format(id_usuario))
                usuario = cursor.fetchone()[0]
                return bool(usuario)
            except Error as ex:
                    print("No se pudo obtener usuario: {0}".format(ex))

    def getSaldo(self, id_usuario):
        return self.getUsuario(id_usuario)[1]

    def cargarSaldo(self, id_usuario, importe):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE billetera set dinero = dinero + '{0}' where usuario = '{1}'"
                sql = sql.format(importe, id_usuario)
                cursor.execute(sql)
                self.conexion.commit()
            except Error as ex:
                print("No se pudo cargar saldo: {0}".format(ex))

    def hacerTransaccion(self, id_comprador, id_vendedor, importe):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE billetera set dinero = dinero + '{0}' where usuario = '{1}'"
                sql = sql.format(importe, id_vendedor)
                sql2 = "UPDATE billetera set dinero = dinero - '{0}' where usuario = '{1}'"
                sql2 = sql2.format(importe, id_comprador)
                cursor.execute(sql)
                cursor.execute(sql2)
                self.conexion.commit()
            except Error as ex:
                print("No se pudo hacer transaccion: {0}".format(ex))


if __name__ == "__main__":
    dao = DAO()
