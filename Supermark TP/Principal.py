from ConexionBd import Conexion_BD
from Usuario import Usuario
from loguin import loguear
from RegistroCliente import realizarRegistro
from formularioCliente import *


def opcion():
    op = -1
    while op > 3 or op < 1 :
        print(f"1-Iniciar Sesion.\n2-Registrarse.\n3-Salir")
        op=int(input("Seleccione una Opcion: "))
        if op>3 or op<1:
            print('Opcion incorrecta.') 
    return op

def menu():  
    op = opcion()
    if op == 1 :
        usuario = loguear()
        if usuario != None :
            print("Bienvenido")
            print(f"Usuario: {usuario.get_username()}")
            if usuario.get_tipo() == "C":
                mi_cliente = retorna_cliente(usuario.get_username())
                mi_carrito = Carrito()
                menu_cliente(mi_carrito,mi_cliente)
            elif usuario.get_tipo() == "A" :
                print("Agregar el menu del Administrador")
        else:
            print("Contraseña o usuario incorrecto")

    elif op == 2:
        realizarRegistro()
    elif op == 3 :
        print("Hasta Pronto")


print(":::::::::::::::::::::::BIENVENIDO A SUPERMARK:::::::::::::::::::::::")
menu()
