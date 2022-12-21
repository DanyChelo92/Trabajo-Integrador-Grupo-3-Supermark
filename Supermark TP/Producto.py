from categoria import Categoria
from ConexionBd import Conexion_BD as conexion
class Producto:
    def __init__(self,nombre,marca,precio,categoria,descripcion,id_producto=None):
        self.__id_producto=id_producto
        self.__nombre = nombre
        self.__marca = marca
        self.__precio = precio
        self.__categoria= categoria
        self.__descripcion = descripcion

    
    @property
    def id_producto(self):
        return self.__id_producto
  
    @id_producto.setter
    def id_producto(self,id_producto):
        self.__id_producto=id_producto
    
    @property
    def nombre(self):
        return self.__nombre
  
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def marca(self):
        return self.__marca
  
    @marca.setter
    def marca(self,marca):
        self.__marca = marca

    @property
    def precio(self):
        return self.__precio
  
    @precio.setter
    def precio(self,precio):
        self.__precio = precio
    
    @property
    def categoria(self):
        return self.__categoria
  
    @categoria.setter
    def categoria(self,categoria):
        self.__categoria=categoria
    
    @property
    def descripcion(self):
        return self.__descripcion
  
    @descripcion.setter
    def descripcion(self,descripcion):
        self.__descripcion = descripcion
    
    def strCategoria(self,id):
        return Categoria.str_nombre(id)

    def __str__(self):
        return f"""Id Producto: {self.__id_producto} \nNombre: {self.__nombre} \nMarca: {self.__marca} 
Precio: {self.__precio} \nCategoria: {self.strCategoria(self.categoria)} \nDescripcion: {self.__descripcion}"""

    @staticmethod
    def registros_productos():  
        conn = conexion('Supermark.db')
        registros = conn.consulta('SELECT * FROM producto')
        return registros
    
    @staticmethod
    def productos_con_stock():
        conn = conexion('Supermark.db')
        registros = conn.consulta('SELECT * FROM producto WHERE stock > 0')
        return registros

    @staticmethod
    def todos_productos():
        conn = conexion('Supermark.db')
        registros = conn.consulta(f"SELECT * FROM producto order by id")
        return registros
    
    @staticmethod
    def id_productos(id):
        conn = conexion('Supermark.db')
        registros = conn.consulta(f"SELECT * FROM producto where id='{id}'")
        return registros
    
    @staticmethod
    def nombre_productos(nombre):
        conn = conexion('Supermark.db')
        registros = conn.consulta(f"SELECT * FROM producto where nombre like '{nombre}%'")
        return registros
    
    @staticmethod
    def productos_por_categoria(cod_categoria):
        conn = conexion('Supermark.db')
        registros = conn.consulta(f"SELECT * FROM producto WHERE stock > 0 and id_categoria = {cod_categoria} order by nombre")
        return registros

if __name__ == '__main__':
  '''prod = Producto('Yogurt','Momy',130.00,2,'1 lt. bebible')
  print(prod)
  print(Producto.productos_con_stock())'''
  print(Producto.productos_por_categoria(5))

