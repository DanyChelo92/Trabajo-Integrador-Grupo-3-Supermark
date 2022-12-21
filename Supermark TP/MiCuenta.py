from Usuario import Usuario
from Cliente import Cliente
from ConexionBd import Conexion_BD
from Carrito import Carrito
from ProductoCarrito import ProductoCarrito
from datetime import datetime
class Cuenta:
    def __init__(self,usuario):
        self.__usuario = usuario
        self.__cliente = self.get_cliente()
        self.__carrito = Carrito()
        self.__compras = self.get_compras_carrito()

    @property
    def carrito(self):
        return self.__carrito

    @carrito.setter
    def carrito(self,carrito):
        self.__carrito = carrito

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self,usuario):
        self.__usuario = usuario

    @property
    def compras(self):
        return self.__compras

    @compras.setter
    def compras(self,compras):
        self.__compras = compras

    @property
    def cliente(self):
        return self.__cliente
    
    
    def get_correo_usuario(self):
        return self.__usuario.get_correo()

    def set_correo_usuario(self,correo):
        self.__usuario.set_correo(correo) 

    #retorna un objeto cliente
    def get_cliente(self):
        cliente = None
        conn = Conexion_BD("Supermark.db")
        datos = conn.consulta(f"SELECT * FROM cliente WHERE correo='{self.get_correo_usuario()}';")
        if datos != [] :
            cliente = Cliente(datos[0][1],datos[0][2],datos[0][4],datos[0][5],datos[0][3],datos[0][0])
        return cliente
    
    #retorna informacion de las compras del cliente array
    def get_cliente_compras(self):
        compras = []
        cliente = self.get_cliente()
        conn = Conexion_BD("Supermark.db")
        consulta_compras=conn.consulta(f"SELECT * FROM venta WHERE id_cliente='{cliente.get_id()}';")
        if consulta_compras!=[]:
            compras = consulta_compras
        return compras

    #retorna una lista de carritos las compras que hizo el usuario
    def get_compras_carrito(self):
        ventas = self.get_cliente_compras()
        lista_compras = []
        if ventas != [] :  
            for venta in ventas :
                carrito = Carrito()
                carrito.productos=[]
                carrito.codigo=venta[0]
                carrito.fecha=venta[2]
                carrito.tipoComprobante=venta[1]
                conn = Conexion_BD("Supermark.db")
                compras_detalle =conn.consulta(f"""SELECT venta.id,venta.fecha,venta.tipo_comprobante,detalle_ventas.id_prod,
                                                detalle_ventas.cantidad,producto.nombre,producto.marca,producto.precio,producto.id_categoria,
                                                producto.descripcion
                                                FROM venta
                                                INNER JOIN detalle_ventas on detalle_ventas.id_vent = venta.id
                                                INNER JOIN producto ON producto.id = detalle_ventas.id_prod
                                                WHERE venta.id_cliente = {self.__cliente.get_id()} AND venta.id = {venta[0]};
                                                """)
                #print(compras_detalle)
                for p in compras_detalle :
                    carrito.agregar_producto(ProductoCarrito(p[5],p[6],p[7],p[8],p[9],p[4],p[3]))
                lista_compras.append(carrito)
                
        return lista_compras

    def ejecutar_compra(self,tipo_factura):
        if len(self.carrito.productos) > 0 :  
            self.carrito.comprobante = tipo_factura
            conn = Conexion_BD('Supermark.db')
            conn.insertar(f"INSERT INTO venta (tipo_comprobante,fecha,id_cliente) VALUES ('{self.carrito.comprobante}','{datetime.now()}',{self.__cliente.get_id()})")
            id_venta = conn.consulta("SELECT seq from SQLITE_SEQUENCE WHERE name = 'venta';")
            for p in self.carrito.productos:
                conn.insertar(f"INSERT INTO detalle_ventas (id_prod,id_vent,cantidad) VALUES ({p.id_producto},{id_venta[0][0]},{p.cantidad})")
                conn.actualizar(f"UPDATE producto SET stock = (stock-{p.cantidad}) WHERE id = {p.id_producto}")
            self.compras = self.get_compras_carrito()
            self.carrito.productos = []

  

if __name__ == '__main__' :
    mi_usuario = Usuario("fernando_compras@gmail.com","147fer","C")
    mi_cuenta = Cuenta(mi_usuario)
    print(mi_cuenta.get_cliente())
    print(mi_cuenta.get_cliente_compras())
    compras = mi_cuenta.compras
    for compra in compras:
       print(compra)
       input()