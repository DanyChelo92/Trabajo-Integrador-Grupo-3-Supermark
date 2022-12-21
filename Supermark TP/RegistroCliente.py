from Usuario import Usuario
from Cliente import Cliente

def registrar_cliente():
    print("___Registrar Datos del Cliente____")
    nombre=input("Nombre/s: ")
    apellido=input("Apellido/s: ")
    dni=input("D.N.I.: ")
    domicilio=input("Domicilio: ")
    return nombre,apellido,dni,domicilio

def realizarRegistro():
    print("___Registrar Usuario____")
    user = input("Ingrese cuenta de correo: ")
    clave = input("Ingrese su clave: ")
    nuevo_usuario = Usuario(user,clave,'C')
    if Usuario.existe_usuario(nuevo_usuario) == False :
        datos_cliente = registrar_cliente()
        nuevo_usuario.insertar()
        nuevo_cliente = Cliente(datos_cliente[0],datos_cliente[1],datos_cliente[3],nuevo_usuario.get_username(),int(datos_cliente[2]))
        nuevo_cliente.insert_cliente()
        print("Registro exitoso")
    else:
        print("La cuenta ya existe en el sistema.")
