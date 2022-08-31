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
                db = 'items'
            )
        except Error as ex:
            print("Error al intentar conectar conectar: {0}".format(ex))

    def getItemsdentroDeParametros(self, category=None, nombre = None, preciomin=None, preciomax = None, fdesde = None, fhasta = None, venta_activa= None):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "select id from itemsventa where 1=1 "
                if category:
                    id_cate=self.getCategoriaId(category)
                    sql += " and categoria_idcategoria = '{0}'"
                    sql = sql.format(id_cate)
                if nombre:
                    nombre = '%'+nombre+'%'
                    sql += " and nombre like '{0}'"
                    sql = sql.format(nombre)
                if preciomin:
                    sql += " and precio >= '{0}'"
                    sql = sql.format(preciomin)
                if preciomax:
                    sql += " and precio <= '{0}'"
                    sql = sql.format(preciomax)
                if fdesde:
                    sql += " and fecha_fabricacion >= '{0}'"
                    sql = sql.format(fdesde)
                if fhasta:
                    sql += " and fecha_fabricacion <= '{0}'"
                    sql = sql.format(fhasta)
                if type(venta_activa)==None or venta_activa == 1:
                    sql += " and venta_activa = 1 "
                cursor.execute(sql)
                articulos = cursor.fetchall()
                resultado=[]
                for id in articulos:
                    resultado.append(id[0])
                return resultado
            except Error as ex:
                print("Error al intentar conectar conectar: {0}".format(ex))

    def getPublicacionesDelVendedor(self, id_vendedor):
        id_seller = self.getIdvendedor(id_vendedor)
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("select itemsventa.id, itemsventa.nombre, descripcion, precio, cantidad, fecha_fabricacion, c.nombre as categoria, v.vendedor_id as vendedor_id, venta_activa, cantidad_vendida "
                "from itemsventa inner join seller v on v.id = itemsventa.seller_id inner join categoria c on itemsventa.categoria_idcategoria = c.idcategoria where seller_id = '{0}'")
                cursor.execute(sql.format(id_seller))
                articulos = cursor.fetchall()
                resultado =[]
                for articulo in articulos:
                    fotos = self.getFotos(articulo[0])
                    publicacion=(*articulo, fotos,)
                    resultado.append(publicacion)
                return resultado
            except Error as ex:
                    print("No se pudo obtener articulo: {0}".format(ex))

    def comprarItem(self,item_id, id_comprador, cantidad):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                if self.esPrimeraCompra(item_id, id_comprador):
                    
                    sql = "INSERT into buyer (id_comprador, cantidad, itemsventa_id) VALUES ('{0}', '{1}', '{2}')"
                    sql = sql.format(id_comprador,cantidad, item_id)
                else:
                    sql = "UPDATE buyer set cantidad = cantidad + '{0}' where itemsventa_id = '{1}'"
                    sql = sql.format(cantidad, item_id)
                cursor.execute(sql)
                sql = "UPDATE itemsventa set cantidad = cantidad - '{0}', cantidad_vendida = cantidad_vendida + '{0}' where id = '{1}'"
                cursor.execute(sql.format(cantidad, item_id))
                self.conexion.commit()


            except Error as ex:
                    print("No se pudo obtener articulo: {0}".format(ex))

    def esPrimeraCompra(self, item_id, id_comprador):
         if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "select COUNT(id) FROM buyer where  itemsventa_id = %s and id_comprador = %s"
                nombre = (item_id ,id_comprador,)
                cursor.execute(query, nombre)
                resultado = cursor.fetchone()
                print(resultado[0]==0)
                return resultado[0] == 0
            except Error as ex:
                print("Error obteniendo id categoria: {0}".format(ex))


    def getArticulosComprado(self, id_comprador):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("select itemsventa.id from itemsventa inner join buyer b on b.itemsventa_id = itemsventa.id where b.id_comprador = '{0}'")
                cursor.execute(sql.format(id_comprador))
                articulos = cursor.fetchall()
                resultado =[]
                for a in articulos:
                    publicacion = self.getArticuloComprado(a[0])
                    resultado.append(publicacion)
                return resultado
            except Error as ex:
                    print("No se pudo obtener articulo: {0}".format(ex))

    
    def insertarNuevoArticulo(self, vendedor_id, nombre, fecha, categoria, foto, desc = "", precio =0.0, cant = 1):
        if self.conexion.is_connected():   
            idseller = self.getIdvendedor(vendedor_id)
            assert not self.itemRepetido(nombre, idseller)
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO itemsventa(nombre, descripcion, precio, cantidad, fecha_fabricacion, categoria_idcategoria, seller_id, venta_activa) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}','{6}','{7}' )"

                cursor.execute(sql.format(nombre, desc, precio, cant, fecha, categoria, idseller, 1))
                self.conexion.commit()
                id_item = cursor.lastrowid
                self.insertarFoto(id_item, foto)
                return id_item 
            except Error as ex:
                print("No se pudo registrar articulo: {0}".format(ex))
    
    def getListaItems(self, category=None, nombre = None, preciomin=None, preciomax = None, fdesde = None, fhasta = None):
        lista_items = self.getItemsdentroDeParametros(category, nombre, preciomin, preciomax, fdesde, fhasta)
        resultado =[]
        for item in lista_items:
            resultado.append(self.getArticulo(item))
        return resultado

    def getArticulo(self, id_item):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("select itemsventa.id, itemsventa.nombre, descripcion, precio, cantidad, fecha_fabricacion, c.nombre as categoria, v.vendedor_id as vendedor_id, venta_activa "
                "from itemsventa inner join seller v on v.id = itemsventa.seller_id inner join categoria c on itemsventa.categoria_idcategoria = c.idcategoria where itemsventa.id = '{0}'")
                cursor.execute(sql.format(id_item))
                articulo = cursor.fetchone()
                fotos = self.getFotos(id_item)
                resultado = (*articulo, fotos,)
                return resultado
            except Error as ex:
                    print("No se pudo obtener articulo: {0}".format(ex))

    def getArticuloComprado(self, id_item):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("select itemsventa.id, itemsventa.nombre, descripcion, precio, b.cantidad, fecha_fabricacion, c.nombre as categoria, v.vendedor_id as vendedor_id, venta_activa "
                "from itemsventa inner join seller v on v.id = itemsventa.seller_id inner join buyer b on b.itemsventa_id = itemsventa.id inner join categoria c on itemsventa.categoria_idcategoria = c.idcategoria where itemsventa.id = '{0}'")
                cursor.execute(sql.format(id_item))
                articulo = cursor.fetchone()
                fotos = self.getFotos(id_item)
                resultado = (*articulo, fotos,)
                return resultado
            except Error as ex:
                    print("No se pudo obtener articulo: {0}".format(ex))


    def eliminarArticulo(self, id_item):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE from itemsventa where itemsventa_id = '{0}'"
                cursor.execute(sql.format(id_item))
                self.conexion.commit()
            except Error as ex:
                print("No se pudo eliminar el articulo: {0}".format(ex))


    def darDeBajaPublicacion(self, id_item):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE itemsventa SET venta_activa = 0 WHERE id = '{1}' "

                cursor.execute(sql.format(id_item))
                self.conexion.commit()
                id_item = cursor.lastrowid
                return id_item 
            except Error as ex:
                print("No se pudo hacer update de articulo: {0}".format(ex)) 


    def getIdvendedor(self, usuario_id):
        """Este metodo debe buscar el id del vendedor del usuario,de no encontrarlo lo ingresa en la bd y lo devuelve,"""
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "SELECT id FROM seller where vendedor_id = %s"
                user = (usuario_id,)
                cursor.execute(query, user)
                resultado = cursor.fetchone()
                resultado = resultado[0] if resultado else None
                if not resultado:
                    query = "INSERT into seller (vendedor_id) VALUES ('{0}')"
                    cursor.execute(query.format(usuario_id))
                    self.conexion.commit()
                    resultado = cursor.lastrowid
                return resultado
            except Error as ex:
                print("Error obteniendo Id vendedor: {0}".format(ex))
        

    def insertarFoto(self, id_articulo, ruta_foto):
        if self.conexion.is_connected():   
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO fotos(ruta, itemsventa_id) VALUES ('{0}', '{1}')"

                cursor.execute(sql.format(ruta_foto, id_articulo))
                self.conexion.commit()
            except Error as ex:
                print("No se pudo guardar foto: {0}".format(ex))
    

    def getFotos(self, id_articulo):
        if self.conexion.is_connected():   
            try:
                cursor = self.conexion.cursor()
                sql = "select id, ruta from fotos where itemsventa_id = '{0}'"
                cursor.execute(sql.format(id_articulo))
                return cursor.fetchall()
            except Error as ex:
                print("No se pudieron obtener fotos del articulo: {0}".format(ex))


    def eliminarFotosItem(self, id_articulo):
        if self.conexion.is_connected():   
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE from fotos where itemsventa_id = '{0}'"
                cursor.execute(sql.format(id_articulo))
                self.conexion.commit()
            except Error as ex:
                print("No se eliminar fotos del articulo: {0}".format(ex))

        
    def eliminarFoto(self, id_foto):
        if self.conexion.is_connected():   
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE from fotos where id = '{0}'"
                cursor.execute(sql.format(id_foto))
                self.conexion.commit()
            except Error as ex:
                print("No se eliminar foto del articulo: {0}".format(ex))


    def getCategorias(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT idcategoria, nombre FROM categoria")
                resultado = cursor.fetchall()
                return resultado
            except Error as ex:
                print("Error obteniendo categorias: {0}".format(ex))        
        

    def getCategoria(self, id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT nombre FROM categoria where idcategoria = {0}".format(id))
                resultado = cursor.fetchone()
                return resultado[0] if resultado else resultado
            except Error as ex:
                print("Error obteninendo categoria: {0}".format(ex))


    def getCategoriaId(self, categoria):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "SELECT idcategoria FROM categoria where nombre = %s"
                nombre = (categoria,)
                cursor.execute(query, nombre)
                resultado = cursor.fetchone()
                return resultado[0] if resultado else resultado
            except Error as ex:
                print("Error obteniendo id categoria: {0}".format(ex))

    def itemRepetido(self, nombre, vendedor_id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "select COUNT(nombre) FROM itemsventa where venta_activa = 1 and nombre = %s and seller_id = %s"
                nombre = (nombre ,vendedor_id,)
                cursor.execute(query, nombre)
                resultado = cursor.fetchone()
                return resultado[0] if resultado else resultado
            except Error as ex:
                print("Error obteniendo id categoria: {0}".format(ex))
        

        
    def getVendedorItem(self, id_item):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT seller_id FROM itemsventa where id = {0}".format(id_item))
                resultado = cursor.fetchone() 
                return resultado[0] if resultado else resultado
            except Error as ex:
                print("Error al obteniendo al vendedor del item: {0}".format(ex))


    def updateArticulo(self, item_id, vendedor_id, nombre, fecha, categoria, desc = "", precio =0.0, cant = 1):
        if self.conexion.is_connected():
            try:
                assert self.getVendedorItem(item_id) == self.getIdvendedor(vendedor_id)
                idseller = self.getIdvendedor(vendedor_id)
                cursor = self.conexion.cursor()
                sql = "UPDATE itemsventa SET nombre = '{0}', descripcion = '{1}', precio = '{2}', cantidad = '{3}', fecha_fabricacion = '{4}' , categoria_idcategoria = '{5}', seller_id = '{6}' , venta_activa = '{7}' WHERE id = '{8}' "

                cursor.execute(sql.format(nombre, desc, precio, cant, fecha, categoria, idseller, 1, item_id))
                self.conexion.commit()
                return item_id 
            except Error as ex:
                print("No se pudo hacer update de articulo: {0}".format(ex))

if __name__ == "__main__":
    dao = DAO()
    hoy = datetime.now()
    # dao.insertarNuevoArticulo(2,'Computadora', hoy, 1, 'fotopc.png','cafetera en buen estado', 1500, 2)
    # dao.updateArticulo(item_id =3, vendedor_id= 2,nombre = 'Computadora', fecha=hoy, categoria = 1,desc='computadora en buen estado',precio= 1500,cant= 2)
    # dao.updateArticulo(1, 2,'Termo', hoy, 6, 'fototermo1.png','termo en buen estado', 560.0, 10)
    # print(dao.getCategorias())
    # print(dao.getCategoria(2))
    # print(dao.getCategoriaId('HOGAR'))
    # print(dao.getVendedorItem(1))
    # print(dao.getIdvendedor(2))
    # categoria = 'HOGAR'
    # print("SELECT idcategoria FROM categoria where nombre = {0}".format(categoria))

    # a = ('1',2,'Termo',)
    # b = list(('6',8,'Azucar',))
    # c = (*a,b,)
    # print(dao.getFotos(1))
    # print(type(dao.getFotos(3)))
    # print(dao.getFotos(3))
    # print(dao.getItemsdentroDeParametros(category='TECNOLOGIA', nombre='', preciomin=10, preciomax =100))
    # dao.insertarFoto(1,'termo2.png')
    # print(dao.getListaItems(category='HOGAR', nombre='', preciomin=10, preciomax =1600))
    # print(dao.getPublicacionesDelVendedor(2))
    # print(dao.comprarItem(1, 3, 2))
    print(dao.getArticulosComprado(3))

 
    

    
