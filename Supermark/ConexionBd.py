import sqlite3 as sql
class Conexion_BD():

    def __init__(self,db):#bd es el nombre de la base de datos
        self.db = db
        self.conexion = sql.connect(db)
        self.cursor = self.conexion.cursor()

    #abre la conexion si el objeto ya esta creado
    def conectar(self):
        self.conexion = sql.connect(self.db)
        self.cursor = self.conexion.cursor()

    #Obtiene los registros de una tabla de la db recibe como paramaetro un string para hacer la consulta(SELECT)
    def consulta(self, consulta):
        self.conexion = sql.connect(self.db)
        self.cursor = self.conexion.cursor()
        self.cursor.execute(consulta)
        registros = self.cursor.fetchall()
        self.conexion.close()
        return registros
    
    #desde aca los metodos insertar eliminar y actualizar tienen identica definicion y recibin un str como paramaetro para realizar el query
    def insertar(self, query):
        self.conexion = sql.connect(self.db)
        self.cursor = self.conexion.cursor()
        self.cursor.execute(query)
        self.conexion.commit()
        self.conexion.close()

    def actualizar(self, query):
        self.conexion = sql.connect(self.db)
        self.cursor = self.conexion.cursor()
        self.cursor.execute(query)
        self.conexion.commit()
        self.conexion.close()

    def eliminar(self, query):
        self.conexion = sql.connect(self.db)
        self.cursor = self.conexion.cursor()
        self.cursor.execute(query)
        self.conexion.commit()
        self.conexion.close()
    
    
    def commit(self):
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()


if __name__ == '__main__':
    conn = Conexion_BD('Supermark.db')
    #conn.consulta('SELECT * FROM producto')
    #conn.commit()
    #registros = conn.obtnerRegistros('SELECT * FROM producto')
    #registros = conn.cursor.fetchall()
    #conn.cerrar()
    #for registro in registros:
        #print(registro)

    #cod = conn.consulta("SELECT last_insert_rowid() FROM producto;")
    cod = conn.consulta("SELECT seq from SQLITE_SEQUENCE WHERE name = 'producto';")

    print(cod[0][0])
