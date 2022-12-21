import tkinter as tk
from tkinter import ttk,messagebox,scrolledtext
from ProductoCarrito import ProductoCarrito
from categoria import Categoria
from VentanaProductos import ventanaProducto
from VentanaCarrito import VentanaCarrito
from VentanaMisCompras import VentanaCompras
from VentanaUsuario import VentanaUsuario
from MiCuenta import Cuenta
from Usuario import Usuario

class VentanaCuenta(tk.Tk):
    def __init__(self,cuenta):
        super().__init__()
        self.cuenta = cuenta
        self.geometry('800x400+600+300')  # +600+300 ubicamos donde queremeos que se vizualise la ventana
        self.title('Supermark')
        self.resizable(0,0)
        self.iconbitmap('icono.ico')
        self._crear_pestañas()
        self.mainloop()

    def _crear_pestañas(self):
        # crear un tab control, para ellos usamos la clase notebook
        control_tabulador = ttk.Notebook(self)
        # agregamos un marco frame para agregar dentro del tabulados
        #Creacion pestaña cuenta
        frame_cliente = ttk.Frame(control_tabulador)
        control_tabulador.add(frame_cliente,text = "Mi Cuenta")
        control_tabulador.pack(fill='both')
        #self._crear_elementos_cuenta(frame_cuenta)
        vu = VentanaUsuario(frame_cliente,self.cuenta)

        #Creacion pestaña productos
        frame_productos = ttk.Frame(control_tabulador)
        control_tabulador.add(frame_productos, text="Productos")
        control_tabulador.pack(fill='both')
        vp = ventanaProducto(frame_productos,self.cuenta.carrito)
       
        #self._crear_elementos_productos(frame_productos)

        #Creacion pestaña carrito
        self.frame_carrito = ttk.Frame(control_tabulador)
        control_tabulador.add(self.frame_carrito, text="Mi Carrito")
        control_tabulador.pack(fill='both')
        #self._crear_elementos_carrito(self.frame_carrito)
        vc = VentanaCarrito(self.frame_carrito,self.cuenta)

        #Creacion pestaña mis compras
        self.frame_compras = ttk.Frame(control_tabulador)
        control_tabulador.add(self.frame_compras, text="Mis Compras")
        control_tabulador.pack(fill='both')
        vcompras = VentanaCompras(self.frame_compras,self.cuenta)


        
        def pestaña_seleccionada(evento):
            pestaña = control_tabulador.select()
            if control_tabulador.index(pestaña) == 2:
                #print("Nueva pestaña seleccionad: Carrito")
                vc.llenar_tabla_carrito()
            elif control_tabulador.index(pestaña) == 3:
                #print("Nueva pestaña seleccionad: mis compras")
                vcompras.cargar_compras()
            elif control_tabulador.index(pestaña) == 0:
                vu.cargar_datos()
            elif control_tabulador.index(pestaña) == 1:
                vp.cargar_tabla("")
        control_tabulador.bind("<<NotebookTabChanged>>",pestaña_seleccionada)

if __name__ == '__main__':
    mi_usuario = Usuario("fernando_compras@gmail.com","147fer","C")
    mi_cuenta = Cuenta(mi_usuario)
    
    #root = tk.Tk()
    ventana_cliente = VentanaCuenta(mi_cuenta)
    #root.mainloop()