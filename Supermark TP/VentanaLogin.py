import tkinter as tk
from tkinter import ttk,messagebox
import tkinter.font as tkFont
from Usuario import Usuario
from MiCuenta import Cuenta
from ConexionBd import Conexion_BD
from VentanaCuenta import VentanaCuenta
from VentanaRegistro import VentanaRegistro
from VentanaAdministrador import VentanaAdministrador
class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.width=400
        self.height=150
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.geometry(self.alignstr)
        #self.geometry('400x150')  
        self.title('Loguin')
        #self.iconbitmap('login.ico')
        self.resizable(0, 0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.__crear_componentes()

    def __crear_componentes(self):

        ftTitulo = tkFont.Font(family='Times',size=15)
        ft = tkFont.Font(family='Times',size=10)

        label_titulo = tk.Label(self,text="Ingresar",font=ftTitulo,fg="#333333",justify="center")
        label_titulo.grid(row=0,columnspan=2,pady=5)

        label_usuario = tk.Label(self, text='Usuario:',font=ft,fg="#333333",justify="center")
        label_usuario.grid(row=1, column=0, sticky='E', padx=5, pady=5)
        self.input_usuario = tk.Entry(self,bg="#ffffff",borderwidth="1px",font=ft,fg="#333333",justify="center")
        self.input_usuario.grid(row=1, column=1, pady=5, padx=5, sticky=tk.EW,columnspan=1)

        label_pass = tk.Label(self, text='Password:',font=ft,fg="#333333",justify="center")
        label_pass.grid(row=2, column=0, sticky='E', padx=5, pady=5)
        self.input_pass = tk.Entry(self, show='*',bg="#ffffff",borderwidth="1px",font=ft,fg="#333333",justify="center")
        self.input_pass.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

        boton_registrar = tk.Button(self, text='Registrase', command=self.__evento_registrar,font=ft)
        boton_registrar.grid(row=3, column=0,pady=10)

        boton_login = tk.Button(self, text='Login', command=self.__evento_login,font=ft)
        boton_login.grid(row=3, column=1,pady=10,padx=10,sticky=tk.EW)

    def __evento_login(self):
        #messagebox.showinfo("Datos Login", "Usuario: " + self.input_usuario.get() + ", Password: " + self.input_pass.get())
        usuario = Usuario.get_usuario(self.input_usuario.get())
        if usuario!=None and usuario.get_clave() == self.input_pass.get() :
            if usuario.get_tipo() == 'C':
                messagebox.showinfo("Login",f"Binvenido Usuario {usuario.get_correo()}")
                self.destroy()
                mi_cuenta = Cuenta(usuario)
                ventana_cliente = VentanaCuenta(mi_cuenta)
            elif usuario.get_tipo() == 'A':
                messagebox.showinfo("Login",f"Binvenido Administrador {usuario.get_correo()}")
                self.destroy()
                ventana_admin = VentanaAdministrador()
        else:
            messagebox.showwarning("Login","Contraseña o usuario incorrecto")
        return usuario

    def __evento_registrar(self):
        VentanaRegistro()



if __name__ == '__main__':

    login_ventana = Login()
    login_ventana.mainloop()