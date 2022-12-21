import tkinter as tk
from tkinter import ttk,messagebox
from time import sleep
from Carrito import Carrito
from ProductoCarrito import ProductoCarrito

class VentanaCarrito:
    def __init__(self,root,cuenta):
        self._root = root
        self.cuenta = cuenta
        #self.iconbitmap('icono.ico')
        self._crear_componentes_carrito()

    def _crear_componentes_carrito(self):
        #Botones y cajas de texto
        self.boton_seleccionar = ttk.Button(self._root,text="Seleccionar Producto",command=self.seleccionar_producto)
        self.boton_seleccionar.grid(row=0,column=0,padx=10,pady=2,sticky="EW")
        self.boton_modificar = ttk.Button(self._root,text="Modificar Producto",state="disabled",command= self.modificar_producto)
        self.boton_modificar.grid(row=1,column=0,padx=10,pady=2,sticky="EW")
        self.boton_eliminar = ttk.Button(self._root,text="Eliminar Producto",state="disabled",command=self.eliminar_producto)
        self.boton_eliminar.grid(row=2,column=0,padx=10,pady=2,sticky="EW")
        self.label_codigo = ttk.Label(self._root,text="Coidgo: ")
        self.label_codigo.grid(row=0,column=1,sticky="W")
        self.entry_codigo = ttk.Entry(self._root,text="",state="readonly")
        self.entry_codigo.grid(row=0,column=2,sticky="W")
        self.label_producto = ttk.Label(self._root,text="Producto: ")
        self.label_producto.grid(row=1,column=1,sticky="W")
        self.entry_producto = ttk.Entry(self._root,text = "", width=50,state="readonly")
        self.entry_producto.grid(row=1,column=2,columnspan=2,sticky="W")
        self.label_cant = ttk.Label(self._root,text="Cantidad: ")
        self.label_cant.grid(row=2,column=1,sticky="W")
        self.entry_cant = ttk.Entry(self._root,text = "", width=10,state="readonly")
        self.entry_cant.grid(row=2,column=2,sticky="W")
        self.boton_confirmar = ttk.Button(self._root,text="Confirmar",command=self.confirmar_modificacion,state="disabled")
        self.boton_confirmar.grid(row=2,column=3,padx=10,sticky="W")

        self.boton_cancelar = ttk.Button(self._root,text="Cancelar",command=self.llenar_tabla_carrito,state="disabled")
        self.boton_cancelar.grid(row=2,column=4,padx=10,sticky="W")

        self.label_total = ttk.Label(self._root,text="Total a pagar: ")
        self.label_total.grid(row=4,column=0,sticky="E")
        self.entry_total = ttk.Entry(self._root,text = "", width=10,state="readonly")
        self.entry_total.grid(row=4,column=1,sticky="W")
        self.label_comprobante = ttk.Label(self._root,text="Seleccione tipo de comprobante: ")
        self.label_comprobante.grid(row=4,column=2,sticky="E")
        self.lista_comprobante = ttk.Combobox(self._root, width=10,values=("A","B","C"),state="readonly")
        self.lista_comprobante.grid(row=4,column=3,sticky="W")
        self.boton_comprar = ttk.Button(self._root,text="Confirmar Compra",command=self.confirmar_compra,state="disabled")
        self.boton_comprar.grid(row=4,column=4,padx=10,sticky="W")
        self.label_estado = ttk.Label(self._root,text="")
        self.label_estado.grid(row=1,column=4)
        
        # tabla carrito
        self.frameCarrito = ttk.Frame(self._root)
        self.frameCarrito.grid(row=3, column=0, padx=10,pady=5,sticky="W",columnspan=8)

        self.tabla_carrito = ttk.Treeview(self.frameCarrito, columns=tuple(['id', 'nombre', 'marca', 'descripcion', 'precio', 'cantidad', 'total']))
        self.tabla_carrito.grid(row=1, column=0, padx=10, pady=5)

        # asignamos tamño a las columnas
        self.tabla_carrito.column("#0", width=50, minwidth=10)
        self.tabla_carrito.column("id", width=50, minwidth=10)
        self.tabla_carrito.column("nombre", width=200, minwidth=10)
        self.tabla_carrito.column("marca", width=125, minwidth=10)
        self.tabla_carrito.column("descripcion", width=170, minwidth=10)
        self.tabla_carrito.column("precio", width=50, minwidth=10)
        self.tabla_carrito.column("cantidad", width=50, minwidth=10)
        self.tabla_carrito.column("total", width=50, minwidth=10)

        # colocamos nombres a la cabecera
        self.tabla_carrito.heading("#0", text="N°", anchor="center")
        self.tabla_carrito.heading("id", text="Id", anchor="center")
        self.tabla_carrito.heading("nombre", text="Nombre", anchor="center")
        self.tabla_carrito.heading("marca", text="Marca", anchor="center")
        self.tabla_carrito.heading("descripcion", text="Descripcion", anchor="center")
        self.tabla_carrito.heading("precio", text="Precio", anchor="center")
        self.tabla_carrito.heading("cantidad", text="Cant", anchor="center")
        self.tabla_carrito.heading("total", text="Total", anchor="center")

    def llenar_tabla_carrito(self):
        self.tabla_carrito.delete(*self.tabla_carrito.get_children())
        self.estado_inicial_mod_elim()
        num=0
        if self.cuenta.carrito.productos != []:
            self.label_estado['text']=""
            for producto in self.cuenta.carrito.productos:
                num += 1
                self.tabla_carrito.insert("", tk.END, text=str(num), values=(
                    producto.id_producto, producto.nombre, producto.marca, producto.descripcion, producto.precio, producto.cantidad, (producto.precio*producto.cantidad)))
            self.entry_total.config(state="normal")
            self.entry_total.delete(0,"end")
            self.entry_total.insert(0,self.cuenta.carrito.totalCarrito())
            self.entry_total.config(state="readonly")
            self.boton_comprar.config(state="enabled")
        else:
            self.entry_total.config(state="normal")
            self.entry_total.delete(0,"end")
            self.entry_total.insert(0,self.cuenta.carrito.totalCarrito())
            self.entry_total.config(state="readonly")

            self.label_estado['text']="EL CARRITO ESTA VACIO :("
            self.label_estado['foreground']="#68376f"


    def seleccionar_producto(self):

        try:
            item_codigo = self.tabla_carrito.item(self.tabla_carrito.selection())['values'][0]
            item_nombre = self.tabla_carrito.item(self.tabla_carrito.selection())['values'][1]
            item_marca = self.tabla_carrito.item(self.tabla_carrito.selection())['values'][2]
            item_descripcion = self.tabla_carrito.item(self.tabla_carrito.selection())['values'][3]
            item_cantidad = self.tabla_carrito.item(self.tabla_carrito.selection())['values'][5]
            str_cadena = item_nombre+" "+item_marca+" "+item_descripcion
            self.entry_producto.config(state="normal")
            self.entry_cant.config(state="normal")
            self.entry_codigo.config(state="normal")
            self.entry_producto.delete(0,"end")
            self.entry_codigo.delete(0,"end")
            self.entry_codigo.insert(0,item_codigo)
            self.entry_producto.insert(0,str_cadena)
            self.entry_cant.delete(0,"end")
            self.entry_cant.insert(0,str(item_cantidad))
            self.entry_codigo.config(state="readonly")
            self.entry_producto.config(state="readonly")
            self.entry_cant.config(state="readonly")
            self.activar_botones_mod_elim()
            
        except:
            messagebox.showinfo("Carrito","No ah seleccionado un producto")

    def activar_botones_mod_elim(self):
        self.boton_modificar.config(state="enabled")
        self.boton_eliminar.config(state="enabled")
    
    def limpiar_cajas_modificar(self):
        self.entry_cant.config(state="normal")
        self.entry_producto.config(state="normal")
        self.entry_codigo.config(state="normal")
        self.entry_cant.delete(0,"end")
        self.entry_producto.delete(0,"end")
        self.entry_codigo.delete(0,"end")
        self.entry_cant.config(state="readonly")
        self.entry_producto.config(state="readonly")
        self.entry_codigo.config(state="readonly")

    def modificar_producto(self):
        self.entry_cant.config(state="normal")
        self.boton_confirmar.config(state="enabled")
        self.boton_cancelar.config(state="enabled")
    
    def confirmar_modificacion(self):
        self.entry_codigo.config(state="normal")
        codigo = int(self.entry_codigo.get())
        self.entry_codigo.config(state="readonly")
        #producto = self.cuenta.carrito.busca_codigo(codigo)
        self.entry_cant.config(state="normal")
        nueva_cantidad = int(self.entry_cant.get())
        for p in self.cuenta.carrito.productos:
            if p.id_producto == codigo:
                if nueva_cantidad <= ProductoCarrito.get_producto_stock(codigo):
                    p.cantidad =  nueva_cantidad
                    self.llenar_tabla_carrito()
                else:
                    messagebox.showerror("Carrito","La cantidad solicitada supera el Stock")
                break
    
    def eliminar_producto(self):
        self.entry_codigo.config(state="normal")
        codigo = int(self.entry_codigo.get())
        self.entry_codigo.config(state="readonly")
        eliminado = self.cuenta.carrito.busca_codigo(codigo)
        self.cuenta.carrito.eliminar_producto(eliminado)
        self.limpiar_cajas_modificar()
        self.llenar_tabla_carrito()

    def confirmar_compra(self):
        comprobante = self.lista_comprobante.get()
        if comprobante != "":
            if self.cuenta.carrito.cantidad_articulos() <= 30:
                self.cuenta.ejecutar_compra(comprobante)
                messagebox.showinfo("Carrito","Compra exitosa, Gracias por elegirnos!!!")
                self.llenar_tabla_carrito()
                self.lista_comprobante.set("")
            else:
                messagebox.showwarning("Carrito","El limite del carrito es de 30 articulos.")
        else:
            messagebox.showwarning("Carrito","Selecciona el tipo de comprobante")

    def estado_inicial_mod_elim(self):
        self.boton_confirmar.config(state="disabled")
        self.boton_eliminar.config(state="disabled")
        self.boton_modificar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")

        self.entry_codigo.config(state="normal")
        self.entry_codigo.delete(0,"end")
        self.entry_codigo.config(state="readonly")

        self.entry_producto.config(state="normal")
        self.entry_producto.delete(0,"end")
        self.entry_producto.config(state="readonly")

        self.entry_cant.config(state="normal")
        self.entry_cant.delete(0,"end")
        self.entry_cant.config(state="readonly")
