import tkinter as tk
from tkinter import ttk,messagebox
from time import sleep
from Carrito import Carrito
from MiCuenta import Cuenta

class VentanaUsuario:
    def __init__(self,root,cuenta):
        self._root = root
        self.cuenta = cuenta
        #self.iconbitmap('icono.ico')
        self._crear_componentes_usuario()

    def _crear_componentes_usuario(self):
        self.frame_usuario = ttk.LabelFrame(self._root,text="DATOS USUARIO")
        self.frame_usuario.grid(row=0,column=0,pady=10)

        self.button_modificar = ttk.Button(self.frame_usuario,text="Modificar Datos",command=self.modificar_campos)
        self.button_modificar.grid(row=0,column=0,padx=10,pady=5)

        self.label_dni= ttk.Label(self.frame_usuario,text="DNI:")
        self.label_dni.grid(row=1,column=0,padx=10,pady=5)
        self.label_nombre= ttk.Label(self.frame_usuario,text="Nombre:")
        self.label_nombre.grid(row=2,column=0,padx=10,pady=5)
        self.label_apellido= ttk.Label(self.frame_usuario,text="Apellido:")
        self.label_apellido.grid(row=3,column=0,padx=10,pady=5)
        self.label_domicilio= ttk.Label(self.frame_usuario,text="Domicilio:")
        self.label_domicilio.grid(row=4,column=0,padx=10,pady=5)
        self.label_correo= ttk.Label(self.frame_usuario,text="Correo:")
        self.label_correo.grid(row=5,column=0,padx=10,pady=5)

        self.entry_dni= ttk.Entry(self.frame_usuario,text="",width=25)
        self.entry_dni.grid(row=1,column=1,padx=10,pady=5,sticky="W")
        self.entry_nombre= ttk.Entry(self.frame_usuario,text="",width=50)
        self.entry_nombre.grid(row=2,column=1,padx=10,pady=5,columnspan=2)
        self.entry_apellido= ttk.Entry(self.frame_usuario,text="",width=50)
        self.entry_apellido.grid(row=3,column=1,padx=10,pady=5,columnspan=2)
        self.entry_domicilio= ttk.Entry(self.frame_usuario,text="",width=50)
        self.entry_domicilio.grid(row=4,column=1,padx=10,pady=5,columnspan=2)
        self.entry_correo= ttk.Entry(self.frame_usuario,text="",width=50)
        self.entry_correo.grid(row=5,column=1,padx=10,pady=5,columnspan=2)

        self.button_guardar = ttk.Button(self.frame_usuario,text="Guardar Cambios",command=self.guardar_cambios)
        self.button_guardar.grid(row=6,column=1,padx=10,pady=5,sticky="EW")

        self.button_cancelar = ttk.Button(self.frame_usuario,text="Cancelar",command=self.cancelar)
        self.button_cancelar.grid(row=6,column=2,padx=10,pady=5,sticky="EW")
    
    def cargar_datos(self):
        self.activar_entrys()

        self.entry_dni.delete(0,"end")
        self.entry_dni.insert(0,self.cuenta.cliente.get_dni())
        
        self.entry_nombre.delete(0,"end")
        self.entry_nombre.insert(0,self.cuenta.cliente.get_nombre())
        
        self.entry_apellido.delete(0,"end")
        self.entry_apellido.insert(0,self.cuenta.cliente.get_apellido())
        
        self.entry_domicilio.delete(0,"end")
        self.entry_domicilio.insert(0,self.cuenta.cliente.get_domicilio())
        
        self.entry_correo.delete(0,"end")
        self.entry_correo.insert(0,self.cuenta.cliente.get_correo())
        self.desactivar_entrys()

        self.desactivar_buttons()

    def activar_entrys(self):
        self.entry_dni.config(state="normal")
        self.entry_nombre.config(state="normal")
        self.entry_apellido.config(state="normal")
        self.entry_domicilio.config(state="normal")
        self.entry_correo.config(state="normal")

    def desactivar_entrys(self):
        self.entry_dni.config(state="readonly")
        self.entry_nombre.config(state="readonly")
        self.entry_apellido.config(state="readonly")
        self.entry_domicilio.config(state="readonly")
        self.entry_correo.config(state="readonly")

    def desactivar_buttons(self):
        self.button_cancelar.config(state="disabled")
        self.button_guardar.config(state="disabled")
    
    def activar_buttons(self):
        self.button_cancelar.config(state="enabled")
        self.button_guardar.config(state="enabled")

    def modificar_campos(self):
        self.activar_entrys()
        self.activar_buttons()
        self.entry_correo.config(state="disabled")

    def cancelar(self):
        self.cargar_datos()

    def guardar_cambios(self):
        item_nombre = self.entry_nombre.get()
        item_apellido = self.entry_apellido.get()
        item_dni = self.entry_dni.get()
        item_domicilio = self.entry_domicilio.get()
        if item_nombre != "" and item_apellido != "" and item_dni != "" and item_domicilio!= "":
            self.cuenta.cliente.set_nombre(item_nombre)
            self.cuenta.cliente.set_apellido(item_apellido)
            self.cuenta.cliente.set_dni(item_dni)
            self.cuenta.cliente.set_domicilio(item_domicilio)
            self.cuenta.cliente.actualizar_cliente()
            messagebox.showinfo("Mi Cuenta","Operación Exitosa!")
            self.cargar_datos()
        else:
            messagebox.showerror("Mi Cuenta","Los campos no deben estar vacios.")

        


        
