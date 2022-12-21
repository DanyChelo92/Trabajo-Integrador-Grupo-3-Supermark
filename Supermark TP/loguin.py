from Usuario import Usuario
from ConexionBd import Conexion_BD
#este metodo realiza el loguin y retorna un usario
def loguear():
    usuario = None
    print("___Iniciar Sesion____")
    user = input("Ingrese su Usuario: ")
    clave = input("Ingrese su clave: ")
    conn = Conexion_BD("Supermark.db")
    u = conn.consulta(f"SELECT * FROM usuario WHERE correo = '{user}'")
    if u != [] and u[0][1] == clave :
        usuario = Usuario(u[0][0],u[0][1],u[0][2])
    else:
        print("Contraseña o usuario incorrecto")
    return usuario
