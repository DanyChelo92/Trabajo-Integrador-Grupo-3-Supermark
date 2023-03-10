import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from Usuario import Usuario
from Cliente import Cliente

from ConexionBd import Conexion_BD

class VentanaRegistro(tk.Tk):
    def __init__(self):
        super().__init__()
        #setting title
        self.title("Registro")
        #setting window size


        self.width=415
        self.height=349
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.geometry(self.alignstr)
        self.resizable(width=False, height=False)

        
        self.crear_componentes()
        self.mainloop()
        
    def crear_componentes(self):

        ft = tkFont.Font(family='Times',size=10)

        self.label_nombre=tk.Label(self,font=ft,fg="#333333",justify="center",relief="flat",text="Nombre: ")
        self.label_nombre.place(x=20,y=20,width=70,height=25)

        self.label_apellido=tk.Label(self,font=ft,fg="#333333",justify="center",text="Apellido: ")
        self.label_apellido.place(x=20,y=70,width=70,height=25)

        self.label_dni=tk.Label(self,font=ft,fg="#333333",justify="center",text="DNI: ")
        self.label_dni.place(x=20,y=120,width=70,height=25)

        self.label_domicilio=tk.Label(self,font=ft,fg="#333333",justify="center",text="Domicilio: ")
        self.label_domicilio.place(x=20,y=170,width=70,height=25)

        self.label_correo=tk.Label(self,font=ft,fg="#333333",justify="center",text="Correo: ")
        self.label_correo.place(x=20,y=220,width=70,height=25)

        self.label_clave=tk.Label(self,font=ft,fg="#333333",justify="center",text="Clave: ")
        self.label_clave.place(x=20,y=270,width=70,height=25)

        self.entry_nombre=tk.Entry(self, text = "",bg="#ffffff",borderwidth="1px",font=ft,fg="#333333",justify="center")
        self.entry_nombre.place(x=110,y=20,width=251,height=30)

        self.entry_apellido=tk.Entry(self, text="",bg="#ffffff",borderwidth="1px",font=ft,fg="#333333",justify="center")
        self.entry_apellido.place(x=110,y=70,width=251,height=30)

        self.entry_dni=tk.Entry(self, text="",bg="#ffffff",borderwidth="1px",font=ft,fg="#333333",justify="center")
        self.entry_dni.place(x=110,y=120,width=251,height=30)

        self.entry_domicilio=tk.Entry(self, text="",bg="#ffffff",borderwidth="1px",font=ft,fg="#333333",justify="center")
        self.entry_domicilio.place(x=110,y=170,width=251,height=30)

        self.entry_correo=tk.Entry(self, text="",bg="#ffffff",borderwidth="1px",font=ft,fg="#333333",justify="center")
        self.entry_correo.place(x=110,y=220,width=251,height=30)

        self.entry_clave=tk.Entry(self, text="",show="*",bg="#ffffff",borderwidth="1px",font=ft,fg="#333333",justify="center")
        self.entry_clave.place(x=110,y=270,width=251,height=30)
    
        self.button_registrase=tk.Button(self,bg="#f0f0f0",font=ft,fg="#000000",justify="center",text="Registrarse",command=self._registrar_usuario)
        self.button_registrase.place(x=110,y=310,width=251,height=25)
   

    def _registrar_usuario(self):
        if self.validar_entrys():
            nombre=self.entry_nombre.get()
            apellido=self.entry_apellido.get()
            domicilio=self.entry_domicilio.get()
            dni=self.entry_dni.get()
            correo=self.entry_correo.get()
            clave=self.entry_clave.get()
            if Usuario.existe_usuario(correo)!=True:   
                nuevo_usuario = Usuario(correo,clave,"C")
                nuevo_cliente = Cliente(nombre,apellido,domicilio,correo,dni)
                nuevo_usuario.insertar()
                nuevo_cliente.insert_cliente()
                messagebox.showinfo("Registro de Usuario","Registro Exitoso! Inicie Sesion.")
                self.destroy()
                
                #messagebox.showerror("Registro de Usuario","Ha ocurrido un error no se pudo regitrar al usuario")
                #print()
            else:
                messagebox.showerror("Registro de Usuario",f"El usuario {correo} ya existe")
        else:
            messagebox.showwarning("Registro de Usuario","Los campos no deben estar vacios")
    
    def validar_entrys(self):
        nombre=self.entry_nombre.get()
        apellido=self.entry_apellido.get()
        domicilio=self.entry_domicilio.get()
        dni=self.entry_dni.get()
        correo=self.entry_correo.get()
        clave=self.entry_clave.get()
        if nombre!="" and apellido!="" and domicilio!="" and correo!="" and dni!="" and clave!="":
            return True
        else:
            return False


       
  
if __name__ == "__main__":
   VentanaRegistro()