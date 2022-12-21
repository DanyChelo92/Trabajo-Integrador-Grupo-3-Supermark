import tkinter
import tkinter as tk
from tkinter import ttk,messagebox,scrolledtext
from ProductoCarrito import ProductoCarrito
from categoria import Categoria
from time import sleep
class ventanaProducto:
    def __init__(self,root,carrito):
        self.root = root
        self.carrito = carrito
        
        self._crear_elementos_productos()

    def _crear_elementos_productos(self):  
        self.label_categoria = ttk.Label(self.root, text="Categoria: ")
        self.label_categoria.grid(row=0, column=0, sticky='E', padx=10, pady=10)
        self.lista_categoria = ttk.Combobox(self.root, width=20, values=Categoria.retornar_categorias(),state="readonly")
        self.lista_categoria.grid(row=0, column=1, sticky=tk.W)
        self.boton_categoria = ttk.Button(self.root, text="Mostrar Productos",command = self.cargar_productos)
        self.boton_categoria.grid(row=0, column=2, sticky='W')
        self.label_cant = ttk.Label(self.root, text="Cantidad: ", width=10)
        self.label_cant.grid(row=0, column=3, sticky="E", padx=5, pady=5)
        self.lista_cant = ttk.Entry(self.root, width=10)
        self.lista_cant.grid(row=0, column=4, sticky="w")
        self.boton_agregar = ttk.Button(self.root, text="Agregar al Carrito", command=self._agregar_producto_carrito)
        self.boton_agregar.grid(row=0, column=5, sticky="W")
        # tabla productos
        self.frameTabla = ttk.LabelFrame(self.root, text="STOCK")
        self.frameTabla.grid(row=2, column=0, padx=10, pady=10, sticky="W", columnspan=8)
        self.tabla_producto = ttk.Treeview(self.frameTabla,columns=tuple(['id', 'nombre', 'marca', 'precio', 'stock', "descripcion"]))
        self.tabla_producto.grid(row=0, column=0, padx=10, pady=5)
        # asignamos tamño a las columnas
        self.tabla_producto.column("#0", width=50, minwidth=10)
        self.tabla_producto.column("id", width=50, minwidth=10)
        self.tabla_producto.column("nombre", width=200, minwidth=30)
        self.tabla_producto.column("marca", width=150, minwidth=30)
        self.tabla_producto.column("precio", width=50, minwidth=20)
        self.tabla_producto.column("stock", width=50, minwidth=20)
        self.tabla_producto.column("descripcion", width=200, minwidth=20)

        # colocamos nombres a la cabecera
        self.tabla_producto.heading("#0", text="N°", anchor="center")
        self.tabla_producto.heading("id", text="Id", anchor="center")
        self.tabla_producto.heading("nombre", text="Nombre", anchor="center")
        self.tabla_producto.heading("marca", text="Marca", anchor="center")
        self.tabla_producto.heading("precio", text="Precio", anchor="center")
        self.tabla_producto.heading("stock", text="Stock", anchor="center")
        self.tabla_producto.heading("descripcion", text="Descripcion", anchor="center")

        #def _cargar_tabla
    def cargar_productos(self):
        self.tabla_producto.delete(*self.tabla_producto.get_children())
        categoria = self.lista_categoria.get()
        if  categoria != '' :
            cod_categoria = int(categoria[0])
            self.cargar_tabla(cod_categoria)
            
        else:
            messagebox.showwarning("Lista Categoria","No ha seleccionado la categoria")
    
    def cargar_tabla(self,categoria):
        try:
            if categoria != "":
                productos = ProductoCarrito.productos_por_categoria(categoria)
                i=1
                for p in productos:
                    self.tabla_producto.insert("",tk.END,text=str(i),values=(p[0],p[1],p[2],p[3],p[4],p[6]))
                    i+=1
        except:
            messagebox.showwarning("Productos","Categoria Inválida")

        
    def _agregar_producto_carrito(self):
            #recupera un el valor de los campos del item seleccionado
            try:
                if self.lista_cant.get() != '' and int(self.lista_cant.get())>0: 
                    item_cod = self.tabla_producto.item(self.tabla_producto.selection())['values'][0]
                    item_cant = int(self.lista_cant.get())
                    categoria = self.lista_categoria.get()
                    item_categoria = int(categoria[0])    
                    item_nombre = self.tabla_producto.item(self.tabla_producto.selection())['values'][1]
                    item_marca = self.tabla_producto.item(self.tabla_producto.selection())['values'][2]
                    item_descripcion = self.tabla_producto.item(self.tabla_producto.selection())['values'][5]
                    item_precio = float(self.tabla_producto.item(self.tabla_producto.selection())['values'][3])
                    #item_total = item_cant * item_precio
                    
                    #self.carrito.agregar_producto(producto_carrito)
                    if (self.carrito.cantidad_articulos()+item_cant) <= 30:
                        posicion = self.carrito.indice_producto(item_cod)
                        if posicion!=None:
                            if (self.carrito.productos[posicion].cantidad + item_cant) <= ProductoCarrito.get_producto_stock(item_cod):
                                self.carrito.productos[posicion].cantidad += item_cant
                                self.lista_cant.delete(0,"end")
                            else:
                                messagebox.showwarning("Productos","El producto ya existe en el carrito, la cantidad asignada supera al stock")
                        else:
                            if item_cant <= ProductoCarrito.get_producto_stock(item_cod):
                                producto_carrito = ProductoCarrito(item_nombre,item_marca,item_precio,item_categoria,item_descripcion,item_cant,item_cod)
                                self.carrito.agregar_producto(producto_carrito)
                                self.lista_cant.delete(0,"end")
                            else:
                                messagebox.showwarning("Productos","Stock insuficiente")
                    else:
                        messagebox.showwarning("Productos","El limite del carrito es de 30 articulos. ")
                else:
                    if self.lista_cant.get() == '' :
                        messagebox.showinfo("Productos","El campo cantidad no debe estar vacio")
                    elif int(self.lista_cant.get())<1:
                        messagebox.showinfo("Productos","La cantidad minima es 1")
                    
            except:
                messagebox.showerror("Productos","Ha ingresado un valor inválido")
                
            
            #print(item_cod)