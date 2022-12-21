import tkinter as tk
from tkinter import ttk,messagebox
from time import sleep
from Carrito import Carrito

class VentanaCompras:
    def __init__(self,root,cuenta):
        self._root = root
        self.cuenta = cuenta
        #self.iconbitmap('icono.ico')
        self._crear_componentes_compras()

    def _crear_componentes_compras(self):
        #botones y labels
        self.label_compras = ttk.Label(self._root,text="Seleccione una compra")
        self.label_compras.grid(row=0,column=0)

        self.button_mostrar = ttk.Button(self._root,text="Mostrar detalles",command=self.cargar_detalles)
        self.button_mostrar.grid(row=0,column=1,padx=5,pady=5)

        self.label_cod = ttk.Label(self._root,text="Codigo:")
        self.label_cod.grid(row=0,column=7,sticky="E",padx=5,pady=5)
        self.entry_cod=ttk.Entry(self._root,text="",width=10)
        self.entry_cod.grid(row=0,column=8,sticky="E",padx=5,pady=5)
        
        self.label_fecha = ttk.Label(self._root,text="Fecha")
        self.label_fecha.grid(row=0,column=9,sticky="E",padx=5,pady=5)
        self.entry_fecha=ttk.Entry(self._root,text="",width=20)
        self.entry_fecha.grid(row=0,column=10,columnspan=3,sticky="E",padx=5,pady=5)

        self.label_comprobante = ttk.Label(self._root,text="Tipo Factura:")
        self.label_comprobante.grid(row=2,column=7,sticky="E",padx=5,pady=5)
        self.entry_comprobante=ttk.Entry(self._root,text="",width=10)
        self.entry_comprobante.grid(row=2,column=8,sticky="E",padx=5,pady=5)
        
        self.label_total = ttk.Label(self._root,text="Total")
        self.label_total.grid(row=2,column=9,sticky="E",padx=5,pady=5)
        self.entry_total=ttk.Entry(self._root,text="",width=20)
        self.entry_total.grid(row=2,column=10,columnspan=3,sticky="E",padx=5,pady=5)


        # tabla compras
        self.frameCompras = ttk.LabelFrame(self._root,text="Compras",borderwidth=2)
        self.frameCompras.grid(row=1, column=0, padx=10,pady=5,sticky="W",columnspan=8)

        self.tabla_compras = ttk.Treeview(self.frameCompras, columns=tuple(['id', 'fecha', 'comprobante']))
        self.tabla_compras.grid(row=1, column=0, padx=10, pady=5)

        # asignamos tamño a las columnas
        self.tabla_compras.column("#0", width=30, minwidth=10)
        self.tabla_compras.column("id", width=50, minwidth=10)
        self.tabla_compras.column("fecha", width=150, minwidth=10)
        self.tabla_compras.column("comprobante", width=80, minwidth=10)
        
        # colocamos nombres a la cabecera
        self.tabla_compras.heading("#0", text="N°", anchor="center")
        self.tabla_compras.heading("id", text="Id", anchor="center")
        self.tabla_compras.heading("fecha", text="Fecha", anchor="center")
        self.tabla_compras.heading("comprobante", text="Comprobante", anchor="center")

        # tabla detalle compras
        self.frameDetalle = ttk.LabelFrame(self._root,text="Detalle compras",borderwidth=2)
        self.frameDetalle.grid(row=1, column=8, padx=10,pady=5,sticky="W",columnspan=8)

        self.tabla_detalle = ttk.Treeview(self.frameDetalle, columns=tuple(['producto', 'precio', 'cantidad','total']))
        self.tabla_detalle.grid(row=1, column=0, padx=10, pady=5)

        # asignamos tamño a las columnas
        self.tabla_detalle.column("#0", width=30, minwidth=10)
        self.tabla_detalle.column("producto", width=200, minwidth=10)
        self.tabla_detalle.column("precio", width=50, minwidth=10)
        self.tabla_detalle.column("cantidad", width=70, minwidth=10)
        self.tabla_detalle.column("total", width=50, minwidth=10)
        
        # colocamos nombres a la cabecera
        self.tabla_detalle.heading("#0", text="N°", anchor="center")
        self.tabla_detalle.heading("producto", text="Producto", anchor="center")
        self.tabla_detalle.heading("precio", text="Precio", anchor="center")
        self.tabla_detalle.heading("cantidad", text="Cantidad", anchor="center")
        self.tabla_detalle.heading("total", text="Total", anchor="center")

    #se ejecuta al cargar la pestaña compras
    def cargar_compras(self):
        self.estado_inicial()
        lista_compras = self.cuenta.get_cliente_compras()
        self.tabla_compras.delete(*self.tabla_compras.get_children())
        num=0
        if lista_compras != []:
            for compra in lista_compras:
                num += 1
                self.tabla_compras.insert("", tk.END, text=str(num), values=(compra[0], compra[2], compra[1]))
            
    def cargar_detalles(self):
        item_codigo = int(self.tabla_compras.item(self.tabla_compras.selection())['values'][0])
        item_fecha = self.tabla_compras.item(self.tabla_compras.selection())['values'][1]
        item_comprobante = self.tabla_compras.item(self.tabla_compras.selection())['values'][2]
        
        self.entry_cod.config(state="normal")
        self.entry_cod.delete(0,"end")
        self.entry_cod.insert(0,item_codigo)
        self.entry_cod.config(state="readonly")
        
        self.entry_fecha.config(state="normal")
        self.entry_fecha.delete(0,"end")
        self.entry_fecha.insert(0,item_fecha)
        self.entry_fecha.config(state="readonly")

        self.entry_comprobante.config(state="normal")
        self.entry_comprobante.delete(0,"end")
        self.entry_comprobante.insert(0,item_comprobante)
        self.entry_comprobante.config(state="readonly")

        #lista de carrito de compras echas
        lista_compras = self.cuenta.get_compras_carrito()
        self.tabla_detalle.delete(*self.tabla_detalle.get_children())
        num=0
        for compra in lista_compras:   
            if item_codigo == compra.codigo:
                for prod in compra.productos:
                    num += 1
                    self.tabla_detalle.insert("", tk.END, text=str(num), values=(f"{prod.nombre} {prod.marca} {prod.descripcion}",prod.precio,prod.cantidad,(prod.precio*prod.cantidad)))
                self.entry_total.config(state="normal")
                self.entry_total.delete(0,"end")
                self.entry_total.insert(0,compra.totalCarrito())
                self.entry_total.config(state="readonly")
                break
    #da un estado inicial a los elementos
    def estado_inicial(self):
        self.tabla_detalle.delete(*self.tabla_detalle.get_children())
        self.entry_cod.config(state="normal")
        self.entry_cod.delete(0,"end")
        self.entry_cod.config(state="readonly")

        self.entry_fecha.config(state="normal")
        self.entry_fecha.delete(0,"end")
        self.entry_fecha.config(state="readonly")

        self.entry_comprobante.config(state="normal")
        self.entry_comprobante.delete(0,"end")
        self.entry_comprobante.config(state="readonly")

        self.entry_total.config(state="normal")
        self.entry_total.delete(0,"end")
        self.entry_total.config(state="readonly")
        self.tabla_detalle.delete(*self.tabla_detalle.get_children())


        
