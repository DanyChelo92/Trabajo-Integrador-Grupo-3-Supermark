import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ProductoStock import ProductoStock
from categoria import Categoria


class ventanaEditar(tk.Tk):
    def __init__(self,lista):
        super().__init__()
        self.lista=lista
        self.width=300
        self.height=400
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.geometry(self.alignstr)  # +600+300 ubicamos donde queremeos que se vizualise la ventana
        self.title('Supermark')
        self.iconbitmap('icono.ico')
        self.resizable(False,False)
        self.miFrame=tk.LabelFrame(self,text='Editar Producto')
        self._editar_producto()
        self.miFrame.pack(fill='both',expand='yes')
        self.mainloop()
        
    def _editar_producto(self):
        self.label_nombre = tk.Label(self.miFrame,text="Nombre: ", width=10)
        self.label_nombre.grid(row=0, column=1, sticky="E", padx=10, pady=10)
        self.entry_nombre = tk.Entry(self.miFrame, width=25)
        self.entry_nombre.grid(row=0, column=2, sticky="W")
        
        self.label_marca = tk.Label(self.miFrame,text="Marca: ", width=10)
        self.label_marca.grid(row=1, column=1, sticky="E", padx=10, pady=10)
        self.entry_marca = tk.Entry(self.miFrame, width=25)
        self.entry_marca.grid(row=1, column=2, sticky="W")
        
        
        self.label_precio = tk.Label(self.miFrame,text="Precio: ", width=10)
        self.label_precio.grid(row=2, column=1, sticky="E", padx=10, pady=10)
        self.entry_precio = tk.Entry(self.miFrame, width=25)
        self.entry_precio.grid(row=2, column=2, sticky="W")
        
        self.label_categoria = tk.Label(self.miFrame, text="Categoria: ")
        self.label_categoria.grid(row=3, column=1, sticky='E', padx=10, pady=10)
        self.lista_categoria = ttk.Combobox(self.miFrame, width=22, values=Categoria.retornar_categorias())
        self.lista_categoria.grid(row=3, column=2, sticky=tk.W)
        
        self.label_cantidad = tk.Label(self.miFrame,text="Cantidad: ", width=10)
        self.label_cantidad.grid(row=4, column=1, sticky="E", padx=10, pady=10)
        self.entry_cantidad = tk.Entry(self.miFrame, width=25)
        self.entry_cantidad.grid(row=4, column=2, sticky="W")
        
        self.label_descripcion = tk.Label(self.miFrame,text="Descripción: ", width=10)
        self.label_descripcion.grid(row=5, column=1, sticky="E", padx=10, pady=10)
        self.text_descripcion = tk.Text(self.miFrame, width=19, height=5)
        self.text_descripcion.grid(row=5, column=2, sticky="W")
            
        
        self.boton_guardar = tk.Button(self.miFrame, text="Editar",command=self.editar)
        self.boton_guardar.grid(row=6, column=2, sticky='W',pady=20)
        
        if self.lista !=[]:
            self.id=self.lista[0]
            self.entry_nombre.insert(0,self.lista[1])
            self.entry_marca.insert(0,self.lista[2])
            self.entry_precio.insert(0,self.lista[3])
            self.entry_cantidad.insert(0,self.lista[4])
            self.text_descripcion.insert(1.0,self.lista[5])
            self.lista_categoria.set(self.lista[6])
            
        
    def editar(self):
        try:
            ProductoStock.editar_producto(self.id,self.entry_nombre.get(),self.entry_marca.get(),float(self.entry_precio.get()),int(self.lista_categoria.get()[0]),str(self.text_descripcion.get('0.0',"end")),int(self.entry_cantidad.get()))
            messagebox.showinfo("Supermark","Producto editado con éxito!!!")
            super().destroy()
        except:
            messagebox.showwarning("Alerta","Error al editar, algun campo invalido!!!")     
            
 