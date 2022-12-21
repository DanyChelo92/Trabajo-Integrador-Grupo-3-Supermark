import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from categoria import Categoria
from ConexionBd import Conexion_BD
conexion=Conexion_BD('Supermark.db')

class ventanaCategoria(tk.Tk):
  def __init__(self):
        super().__init__()
        self.width=300
        self.height=250
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.geometry(self.alignstr)  # +600+300 ubicamos donde queremeos que se vizualise la ventana
        self.title('Supermark')
        self.iconbitmap('icono.ico')
        self.resizable(False,False)
        self.miFrame=tk.LabelFrame(self,text='Agregar Categoria')
        self._crear_componentes()
        self.miFrame.pack(fill='both',expand='yes')
        self.miFrame2=tk.LabelFrame(self,text='Eliminar Categoria')
        self._crear_componentes2()
        self.miFrame2.pack(fill='both',expand='yes')
        self.mainloop()

  def _crear_componentes(self):
      label_categoria = ttk.Label(self.miFrame,text='Nueva Categoria:')
      label_categoria.grid(row=0, column=0, sticky='E', padx=10, pady=10)
      self.entry_categoria = ttk.Entry(self.miFrame)
      self.entry_categoria.grid(row=0, column=1, pady=10, padx=10, sticky=tk.EW,columnspan=1)

      boton_login = tk.Button(self.miFrame, text='Guardar',command=self.guardar)
      boton_login.grid(row=1, column=1,pady=10,padx=10,sticky=tk.E)

  def guardar(self):
    try:  
      conexion.insertar(f"insert into categoria(categoria) values('{self.entry_categoria.get()}')")
      messagebox.showinfo("Aviso", "Categoria Agregada!!!")
      super().destroy()  
    except:
      messagebox.showerror("Aviso","Error al agregar...")
  def _crear_componentes2(self):    
      self.label_categoria = ttk.Label(self.miFrame2,text='Eliminar Categoria:')
      self.label_categoria.grid(row=0, column=0, sticky='E', padx=10, pady=10)
      self.lista_categoria = ttk.Combobox(self.miFrame2, width=20, values=Categoria.retornar_categorias())
      self.lista_categoria.grid(row=0, column=1, sticky=tk.W)

      boton_login = tk.Button(self.miFrame2, text='Eliminar',command=self.eliminar)
      boton_login.grid(row=1, column=1,pady=10,padx=10,sticky=tk.E)
  
  def eliminar(self):
    try:
      conexion.eliminar(f"delete from categoria where id='{self.lista_categoria.get()[0]}'")
      messagebox.showinfo("Aviso", "Categoria Eliminada!!!")
      super().destroy()  
    except:
      messagebox.showerror("Aviso","No se pudo eliminar la categoria")
          
      
        
    