from ConexionBd import Conexion_BD
from ProductoCarrito import ProductoCarrito as producto
from Carrito import Carrito
from datetime import datetime
from Cliente import Cliente

def opcion():
    op = -1
    while op>5 or op<1:
        print("______Menu Carrito______")
        print("""
                1-Añadir producto al carrito.
                2-Eliminar producto.
                3-Mostrar Carrito.
                4-Confirmar Compra
                5-Salir.
            """)
        op = int(input("Seleccione una opcion: "))
        if op>5 or op<1:
            print('Opcion incorrecta.')

    return op

def retorna_cliente(mail):
    conn = Conexion_BD("Supermark.db")
    datos = conn.consulta(f"SELECT * FROM cliente WHERE correo = '{mail}'")
    cliente = None
    if datos != [] :
        cliente = Cliente(datos[0][1],datos[0][2],datos[0][4],datos[0][5],datos[0][3],datos[0][0])
    return cliente

def menu_cliente(carrito,cliente):
    op = -1
    while op != 5:
        op = opcion()
        if(op == 1):
            rta = -1
            print(Carrito.lista_disponibles())
            while rta != 0:
                id = int(input('Ingrese el id del producto seleccionado: '))
                if producto.info_producto(id) != []:
                    cant = int(input('Ingrese la cantidad deseada: '))
                    p = producto.info_producto(id)
                    nombre = p[0][1]
                    marca = p[0][2]
                    precio = p[0][3]
                    categoria = p[0][4]
                    descripcion = p[0][6]
                    cantidad = cant
                    id_producto = id
                    pc = producto(nombre,marca,precio,categoria,descripcion,cant,id)
                    carrito.agregar_producto(pc)
                    rta = int(input('Ingrese 0 para terminar de ingresar o 1 para seguir: '))
                else:
                    print("El id proporcionado no existe, ingrese un id valido.")
        elif op == 2 :
            cod = input("Ingrese el codigo del producto a eliminar: ")
            eliminado = carrito.busca_codigo(cod)
            if eliminado != None :
                print("Esta seguro de eliminar el siguiente producto: \n",eliminado)
                rta = str(input("Ingrese si para confirmar de lo contrario no."))
                carrito.eliminar_producto(eliminado)
            else:
                print("El producto no se encuentra en carrito")
        elif op == 3 :
            print("___Mi Carrito___")
            print(carrito.lista_carrito())

        elif op == 4:
            if len(carrito.productos) > 0 :  
                comprobante=input("Ingrese tipo de comprobante(A,B,C): ")
                carrito.comprobante = comprobante
                conn = Conexion_BD('Supermark.db')
                conn.insertar(f"INSERT INTO venta (tipo_comprobante,fecha,id_cliente) VALUES ('{carrito.comprobante}','{datetime.now()}',{cliente.get_id()})")
                id_venta = conn.consulta("SELECT seq from SQLITE_SEQUENCE WHERE name = 'venta';")
                for p in carrito.productos:
                    conn.insertar(f"INSERT INTO detalle_ventas (id_prod,id_vent,cantidad) VALUES ({p.id_producto},{id_venta[0][0]},{p.cantidad})")
                print("Gracias por comprar en Supermark....:)")
                carrito.productos = []
        elif op == 5:
            print("Saliendo del carrito---")
        
        input()
