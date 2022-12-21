from ConexionBd import Conexion_BD
from Producto import Producto
class ProductoCarrito(Producto):
    def __init__(self,nombre,marca,precio,categoria,descripcion,cantidad,id_producto=None):
        super().__init__(nombre,marca,precio,categoria,descripcion,id_producto)
        self.__cantidad = cantidad
    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad

    def __str__(self):
        return f'{super().__str__()}\nCantidad: {self.cantidad}'

    @staticmethod
    #devuelve un objeto de producto carrito por id
    def get_producto_carrito(id):
        producto = None
        conn = Conexion_BD('Supermark.db')
        datos_producto = conn.consulta(f'SELECT * FROM producto WHERE id = {id}')
        if datos_producto!=[]:
            producto = ProductoCarrito()
        return producto

    @staticmethod
    #obtiene el stock de un producto
    def get_producto_stock(id):
        stock = None
        conn = Conexion_BD('Supermark.db')
        datos_stock = conn.consulta(f'SELECT stock FROM producto WHERE id = {id}')
        if datos_stock!=[]:
            stock = datos_stock[0][0]
        return stock

    def insertar_db(self):
        try:
            conn = Conexion_BD("Supermark.db")
            conn.consulta(f"INSERT INTO detalle_ventas (id_prod,cantidad) VALUES ({self.id_producto},{self.cantidad})")
        except:
            print("No se pudo realizar la inseccion")
        

if __name__ == '__main__':
    #prod1 = ProductoCarrito('Arroz','Marolio',120.99,1,'1kg 000',4)
    #print(prod1)
    #print(ProductoCarrito.registros_productos())
    #ProductoCarrito.listar_productos()
    #print(ProductoCarrito.productos_con_stock())
    #strproducto = ProductoCarrito.info_producto(3212)
    #print(strproducto)
    print(ProductoCarrito.get_producto_stock(1212))

