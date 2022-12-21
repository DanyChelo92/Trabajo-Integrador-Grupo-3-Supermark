from ConexionBd import Conexion_BD
class Usuario:
    def __init__(self,correo,clave,tipo):
        self.__correo=correo
        self.__clave=clave
        self.__tipo=tipo

    #Getters
    def get_correo(self):
      return self.__correo
    def get_clave(self):
      return self.__clave
    def get_tipo(self):
      return self.__tipo

    #Setters
    def set_correo(self,correo):
      self.__correo=correo
    def set_clave(self,clave):
      self.__clave=clave
    def set_tipo(self,tipo):
      self.__tipo=tipo

    def __str__(self):
      return f"Username: {self.__correo} \nclave: {self.__clave}\ntipo: {self.__tipo}"
  
    def insertar(self):
      conn = Conexion_BD("Supermark.db")
      conn.insertar(f"insert into usuario (correo,clave,tipo_usuario) values ('{self.__correo}','{self.__clave}','{self.__tipo}')")
    
    @staticmethod
    def existe_usuario(correo):
        conn = Conexion_BD("Supermark.db")
        u = conn.consulta(f"SELECT * FROM usuario WHERE correo = '{correo}'")
        if u != [] :
            return True
        else:
            return False

    @staticmethod
    def get_usuario(correo):
        usuario = None
        conn = Conexion_BD("Supermark.db")
        u = conn.consulta(f"SELECT * FROM usuario WHERE correo = '{correo}'")
        if u != [] :
            usuario = Usuario(u[0][0],u[0][1],u[0][2])
        return usuario
    
  
if __name__ == '__main__' :
    miUsuario = Usuario('Admin1@gmail.com','1234a','A')
    print(miUsuario)
    #miUsuario.insertar()

  