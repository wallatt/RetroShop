import mysql.connector
import time

from mysql.connector import Error

def conMysql(metodo):
    def wrapper(*args, **kwargs):
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='usuarios',
                                                    user='root',
                                                    password='root')
                if connection.is_connected():
                    cursor = connection.cursor()
                    print('segundo print')
                    metodo(*args, **kwargs)

            except Error as e:
                print("Error while connecting to MySQL", e)
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")
    return wrapper




class BDUsuario():

    


    def getUsuario(self, cursor,id):
        query = "SELECT id, nombre, apellido, dni, mail, username from usuario where id = %s"
        # cursor = self.cnx.cursor()
        cursor.execute(query, id)

        return cursor.fetchone()
    
    @conMysql
    def usuarioRepetidoDni(self, dni):
        query = "SELECT count(id) from usuario where dni = %s"
        # cursor = self.cnx.cursor()
        values = (dni,)
        cursor.execute(query, values)

        return cursor.fetchone()

    @conMysql
    def hola(self):
        print('hola')


    def createUser(self,cursor, nombre, apellido, dni, mail, username, password):

        if not self.usuarioRepetidoDni(dni):
            query = "INSERT INTO usuario (nombre, apellido, dni, mail, username, password) VALUES (%s, %s, %s,%s, %s, %s)"
            values = [nombre, apellido, dni, mail, username, password]
            # cursor = self.cnx.cursor()

            cursor.commit()

            cursor.execute(query,values)



bd = BDUsuario()

# bd.createUser('walter', 'lacoste', 111, 'wl@gmail.com','wlacoste', 'abc123')

print(bd.usuarioRepetidoDni(123))



    

