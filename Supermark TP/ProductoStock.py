from Producto import Producto
from ConexionBd import Conexion_BD
conexion=Conexion_BD('Supermark.db')

class ProductoStock(Producto):
  def __init__(self,nombre,marca,precio,categoria,descripcion,stock,id_producto=None):
    super().__init__(nombre,marca,precio,categoria,descripcion,id_producto)
    self.__stock = stock

  #Getter
  def get_stock(self):
    return self.__stock

  #Setter
  def set_stock(self, stock):
    self.__stock = stock
    
  #def registrar_producto():
    #nombre=input("producto: ")
    #marca=input("marca: ")
    #precio=float(input("precio: $"))
    #stock=int(input("Stock: "))
    #categoria=int(input("nro de categoria: "))
    #descripcion=input("descripción: ")
    #return nombre,marca,precio,stock,categoria,descripcion

  def insertar_producto(self):
    conexion.insertar(f"""insert into producto (nombre,marca,precio,stock,id_categoria,descripcion) 
    values('{self.nombre}','{self.marca}','{self.precio}','{self.get_stock()}','{self.categoria}','{self.descripcion}')""")   

  def cargar_producto(nombre,marca,precio,categoria,descripcion,stock):
    #datos_producto= ProductoStock.registrar_producto()
    nuevo_producto=ProductoStock(nombre,marca,precio,categoria,descripcion,stock,None)
    nuevo_producto.insertar_producto()
    
  def editar_producto(id_prod,nombre,marca,precio,categoria,descripcion,stock):
    #id_prod=0
    #while conexion.consulta(f"select * from producto where id='{id_prod}'") ==[]:
    #  try:
    #    id_prod=int(input("ingrese id del producto: "))
    #    conexion.consulta(f"select * from producto where id='{id_prod}'")
    #    if conexion.consulta(f"select * from producto where id='{id_prod}'") !=[]:
    #      break
    #    print(f"""El id ingreado no se encuentra en la base de datos. 
    #        Por favor intente de nuevo""")
    #  except:  
    #    print(f"""El tipo de dato es incorrecto. 
    #        Por favor intente de nuevo""")
    #print(conexion.consulta(f"select * from producto where id='{id_prod}'"))
    #datos_producto= ProductoStock.cargar_producto()
    conexion.actualizar(f"""update producto set nombre='{nombre}',marca='{marca}',
                        precio='{precio}',stock='{stock}', id_categoria='{categoria}',
                        descripcion='{descripcion}' where id='{id_prod}'""")
    #print(conexion.consulta(f"select * from producto where id='{id_prod}'"))
    
  def eliminar_producto(id_prod):
    try:
      #id_prod=int(input("ingrese id del producto: "))
      #print(f"""***Producto a eliminar*** 
      #{conexion.consulta(f"select * from producto where id='{id_prod}'")}""")
      conexion.eliminar(f"delete from producto where id={id_prod}")
      #print("***Producto Eliminado***")
    except:  
      print(f"""el id no se encuentra en la base de datos o tipo de dato incorrecto. 
            Por favor intente de nuevo""")
      #ProductoStock.eliminar_producto()          

  def __str__(self):
    return f'Producto:\n {super().__str__()} \nStock: {self.stock}'

  def __str__(self):
    return f'Producto:\n {super().__str__()} \nStock: {self.stock}'

  def str_insert(self):
    return f"INSERT INTO producto (nombre,marca,precio,id_categoria,descripcion,stock) VALUES ('{self.nombre}','{self.marca}',{self.precio},{self.categoria},'{self.descripcion}',{self.stock})"

  def str_update(self):
    return f""

#if __name__ == '__main__':
    #prod = ProductoStock('Galletas Surtidas','Bagley',256.99,1,'galletas dulces surtidas x 250gs',50)
    #print(prod)
    #conn = conexion('Supermark.db')
    #conexion.insertar(prod.cargar_producto())
    #print(ProductoStock.registros_productos())
    #prod.stock = 100
    #print(prod)
    #conn.actualizar('UPDATE producto SET stock = 100 WHERE id = 3213')



