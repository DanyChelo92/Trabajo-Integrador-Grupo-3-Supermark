from ConexionBd import Conexion_BD
class Cliente:
    def __init__(self,nombre,apellido,domicilio,correo,dni,id=None):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__domicilio=domicilio
        self.__correo=correo
        self.__dni=dni
        self.__id = id
    #Getters
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_domicilio(self):
        return self.__domicilio
    def get_correo(self):
        return self.__correo
    def get_dni(self):
        return self.__dni
    #Setters
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_apellido(self,apellido):
        self.__apellido=apellido
    def set_domicilio(self,domicilio):
        self.__domicilio=domicilio
    def set_correo(self,correo):
        self.__correo=correo
    def set_dni(self,dni):
        self.__dni=dni

    def insert_cliente(self):
        conn = Conexion_BD("Supermark.db")
        conn.insertar(F"INSERT INTO cliente (nombre,apellido,dni,domicilio,correo) VALUES('{self.get_nombre()}','{self.get_apellido()}',{self.get_dni()},'{self.get_domicilio()}','{self.get_correo()}')")
    
    def actualizar_cliente(self):
        conn = Conexion_BD("Supermark.db")
        conn.actualizar(f"UPDATE cliente SET nombre = '{self.get_nombre()}', apellido = '{self.get_apellido()}', dni = '{self.get_dni()}', domicilio = '{self.get_domicilio()}' WHERE id = {self.get_id()};")
    
    @staticmethod
    def datos_cliente():
        conn=Conexion_BD('Supermark.db')
        registros=conn.consulta("select * from usuario inner join cliente on usuario.correo=cliente.correo")  
        return registros
    @staticmethod
    def clientes_compras():
        conn=Conexion_BD('Supermark.db')
        registros=conn.consulta("select * from (select * from usuario inner join cliente on usuario.correo=cliente.correo) as usuCliente,venta where usuCliente.id=venta.id_cliente group by usuCliente.id")
        return registros
    def __str__(self):
      return f"Nombre: {self.__nombre} \nApellido: {self.__apellido}\nD.N.I.: {self.__dni}\nDomicilio: {self.__domicilio}"
    
    
if __name__ == '__main__' :
  cl = Cliente('Crsitian','Barrios','La nacion 3379','cristian@gmail.com',34062691)
  cl2 = Cliente('Roberto','Gomez','Suiza 788','roberto@gmail.com',12345678)
  print(cl.get_dni())
  cl.insert_cliente()
  cl2.insert_cliente()