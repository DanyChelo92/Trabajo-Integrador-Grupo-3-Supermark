import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

from ProductoCarrito import ProductoCarrito
from ProductoStock import ProductoStock
from categoria import Categoria
from VentanaAgregar import ventanaAgregar
from VentanaEditar import *
from VentanaCategoria import ventanaCategoria
from Cliente import *
class VentanaAdministrador(tk.Tk):
  def __init__(self):
    super().__init__()
  
    width=880
    height=400
    screenwidth = self.winfo_screenwidth()
    screenheight = self.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    self.geometry(alignstr)  # +600+300 ubicamos donde queremeos que se vizualise la ventana
    self.title('Supermark')
    self.iconbitmap('icono.ico')
    self.resizable(False,False)
    self._crea_pestanas()
    #self.after(125,self.__init__)
    self.lista=[]
    self.mainloop()
    
  def _crea_pestanas(self):
    notebook=ttk.Notebook(self)
    pest_prod=ttk.Frame(notebook)
    notebook.add(pest_prod,text='Productos')
    notebook.pack(fill='both')
    self._crear_elementos_productos(pest_prod)
    
    pest_cliente=ttk.Frame(notebook)
    notebook.add(pest_cliente,text='Clientes')
    notebook.pack(fill='both')
    self._crear_elementos_clientes(pest_cliente)
  
  def _crear_elementos_productos(self,frameproductos):
    
    def buscar_id():
      self.tabla_producto.delete(*self.tabla_producto.get_children())
      prod = entry_id.get()
      if  prod != '' :
        cod_id = int(prod)
        productos = ProductoCarrito.id_productos(cod_id)
        i=1
        for p in productos:
          self.tabla_producto.insert("",tk.END,text=str(i),values=(p[0],p[1],p[2],p[3],p[4],p[6]))
      else:
        messagebox.showwarning("ID del producto","El ID buscado no se encuentra en la base de datos")
        
    def buscar_nombre():
      self.tabla_producto.delete(*self.tabla_producto.get_children())
      prod = entry_nombre.get()
      if  prod != '' :
        nombre = str(prod[0])
        productos = ProductoCarrito.nombre_productos(nombre)
        i=1
        for p in productos:
          self.tabla_producto.insert("",tk.END,text=str(i),values=(p[0],p[1],p[2],p[3],p[4],p[6]))
          i+=1
      else:
        messagebox.showwarning("Lista Productos","No se ha encontrado el nombre")
      
        
    def cargar_productos_categorias():
      self.tabla_producto.delete(*self.tabla_producto.get_children())
      categoria = self.lista_categoria.get()
      if categoria =='':
        productos=ProductoCarrito.todos_productos()
        i=1
        for p in productos:
          self.tabla_producto.insert("",tk.END,text=str(i),values=(p[0],p[1],p[2],p[3],p[4],p[6]))
          i+=1
      elif  categoria != '' :
        cod_categoria = int(categoria[0])
        productos = ProductoCarrito.productos_por_categoria(cod_categoria)
        i=1
        for p in productos:
          self.tabla_producto.insert("",tk.END,text=str(i),values=(p[0],p[1],p[2],p[3],p[4],p[6]))
          i+=1
      else:
        messagebox.showwarning("Lista Categoria","No ha seleccionado la categoria")  
    
    label_id = ttk.Label(frameproductos, text="ID: ")
    label_id.grid(row=0, column=0, sticky='E', padx=10, pady=10)
    entry_id = ttk.Entry(frameproductos, width=10)
    entry_id.grid(row=0, column=1, sticky='W')
    boton_id = ttk.Button(frameproductos, text="Buscar ID",command=buscar_id)
    boton_id.grid(row=0, column=2, sticky='W')
    
    label_nombre = ttk.Label(frameproductos, text="Producto: ", width=10)
    label_nombre.grid(row=0, column=3, sticky="E", padx=5, pady=5)
    entry_nombre = ttk.Entry(frameproductos, width=20)
    entry_nombre.grid(row=0, column=4, sticky="w")
    boton_nombre = ttk.Button(frameproductos,text="Buscar Producto",command=buscar_nombre)
    boton_nombre.grid(row=0,column=5,sticky="W")
    
    
    
    label_categoria = ttk.Label(frameproductos, text="Categoria: ")
    label_categoria.grid(row=0, column=6, sticky='E', padx=5, pady=10)
    self.lista_categoria = ttk.Combobox(frameproductos, width=20,values=Categoria.retornar_categorias())
    self.lista_categoria.grid(row=0, column=7, sticky=tk.W)
    boton_categoria = ttk.Button(frameproductos, text="Mostrar Productos",command=cargar_productos_categorias)
    boton_categoria.grid(row=0, column=8, sticky='W')
    # tabla productos
    self.frameTabla = ttk.LabelFrame(frameproductos, text="PRODUCTOS")
    self.frameTabla.grid(row=2, column=0, padx=10, pady=10, sticky="EW", columnspan=9)
    self.tabla_producto = ttk.Treeview(self.frameTabla,columns=tuple(['id', 'nombre', 'marca', 'precio', 'stock', "descripcion"]))
    self.tabla_producto.grid(row=0, column=0, padx=40, pady=5,sticky='EW',columnspan=9)
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
    
    #coloque antes la funcion de la creacion del boton cuando pongo el lambda no se me ejecuta
    def ventana_agregar_productos():
      ventanaAgregar()
      
    def eliminar_productos():
      resultado = messagebox.askquestion("Eliminar", "¿Está seguro que desea eliminar el producto?")
      if resultado == "yes":
          items=self.tabla_producto.selection()
          item_cod = self.tabla_producto.item(self.tabla_producto.selection())['values'][0]
          ProductoStock.eliminar_producto(item_cod)  
          for item in items:
            self.tabla_producto.delete(item)
          resultado.destroy()
      else:
          resultado.destroy()   
    
    def ventana_editar_productos():
      
      #ventanaEditar(self.lista)
      ventanaEditar(self._obtener_fila())

    def categoria():
      ventanaCategoria()
    
    boton_agregar = ttk.Button(frameproductos, text="Agregar Producto",command=ventana_agregar_productos)
    boton_agregar.grid(row=3, column=1, sticky='W')
    
    boton_editar = ttk.Button(frameproductos, text="Editar Producto",command=ventana_editar_productos)
    boton_editar.grid(row=3, column=3, sticky='W')
    
    boton_eliminar = ttk.Button(frameproductos,text="Eliminar Producto",command=eliminar_productos)
    boton_eliminar.grid(row=3, column=5, sticky='W')
    
    boton_categoria=ttk.Button(frameproductos,text="Categorias",command=categoria)
    boton_categoria.grid(row=3,column=7,sticky='W')

  

    boton_refrescar=ttk.Button(frameproductos,text="refrescar",command=self.refrescar)
    boton_refrescar.grid(row=3,column=8,sticky='W')
    
    self.lista=self.tabla_producto.bind('<Button-1>',self.obtener_fila)
  def refrescar(self):
    self.lista_categoria.config(values=Categoria.retornar_categorias())

  
  def obtener_fila(self,event):
      a=self.tabla_producto.focus()
      self.lista=self.tabla_producto.item(a)['values']
      print(self.lista)
      return self.lista

  #prueba
  def _obtener_fila(self):
      item_id = self.tabla_producto.item(self.tabla_producto.selection())['values'][0]
      item_nombre = self.tabla_producto.item(self.tabla_producto.selection())['values'][1]
      item_marca = self.tabla_producto.item(self.tabla_producto.selection())['values'][2]
      item_precio = self.tabla_producto.item(self.tabla_producto.selection())['values'][3]
      item_stock = self.tabla_producto.item(self.tabla_producto.selection())['values'][4]
      item_descripcion = self.tabla_producto.item(self.tabla_producto.selection())['values'][5]
      item_categoria = self.lista_categoria.get()
      lista_datos = (item_id,item_nombre,item_marca,item_precio,item_stock,item_descripcion,item_categoria)
      return lista_datos
  
   
  
  def _crear_elementos_clientes(self,frameproductos):        
    def cargar_clientes():
      tabla_cliente.delete(*tabla_cliente.get_children())
      clientes = Cliente.datos_cliente()
      i=1
      for c in clientes:
        tabla_cliente.insert("",tk.END,text=str(i),values=(c[0],c[1],c[3],c[4],c[5],c[6],c[7]))
        i+=1
    
    def clientes_compras():
      tabla_cliente.delete(*tabla_cliente.get_children())
      clientes = Cliente.clientes_compras()
      i=1
      for c in clientes:
        tabla_cliente.insert("",tk.END,text=str(i),values=(c[0],c[1],c[3],c[4],c[5],c[6],c[7]))
        i+=1
    
    boton_clientes = ttk.Button(frameproductos, text="Lista Registros",command=cargar_clientes)
    boton_clientes.grid(row=0, column=2, sticky='W')
    
    boton_clientes_compras=ttk.Button(frameproductos,text="Mostrar Clientes",command=clientes_compras)
    boton_clientes_compras.grid(row=0,column=5,sticky='W')
    
    # tabla productos
    frameTabla = ttk.LabelFrame(frameproductos, text="CLIENTES")
    frameTabla.grid(row=2, column=0, padx=10, pady=10, sticky="W", columnspan=8)
    tabla_cliente = ttk.Treeview(frameTabla,columns=tuple(['usuario','clave','id','nombre','apellido','dni','domicilio']))
    tabla_cliente.grid(row=0, column=0, padx=10, pady=5)
    # asignamos tamño a las columnas
    tabla_cliente.column("#0", width=30, minwidth=10)
    tabla_cliente.column("usuario", width=120, minwidth=30)
    tabla_cliente.column("clave",width=100,minwidth=30)
    tabla_cliente.column("id", width=50, minwidth=30)
    tabla_cliente.column("nombre", width=120, minwidth=30)
    tabla_cliente.column("apellido", width=120, minwidth=20)
    tabla_cliente.column("dni", width=80, minwidth=20)
    tabla_cliente.column("domicilio", width=200, minwidth=20)
    # colocamos nombres a la cabecera
    tabla_cliente.heading("#0", text="N°", anchor="center")
    tabla_cliente.heading("usuario", text="Usuario", anchor="center")
    tabla_cliente.heading("clave", text="Clave", anchor="center")
    tabla_cliente.heading("id", text="ID", anchor="center")
    tabla_cliente.heading("nombre", text="Nombre", anchor="center")
    tabla_cliente.heading("apellido", text="Apellido", anchor="center")
    tabla_cliente.heading("dni", text="DNI", anchor="center") 
    tabla_cliente.heading("domicilio", text="Domicilio", anchor="center")   
  
if __name__ == '__main__':
    VentanaAdministrador()
    