from ConexionBd import Conexion_BD
class Categoria:
    def __init__(self,categoria,id = None):
        self.__id = id
        self.__categoria = categoria

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self,categoria):
        self.__categoria = categoria

    @staticmethod
    def mostrar_categorias():
        conn = Conexion_BD('Supermark.db')
        categorias = conn.consulta('SELECT * FROM categoria')
        for id,categoria in categorias:
            print(f'Id:{id} Categoria:{categoria}')

    def str_insert(self):
        return f"INSERT INTO categoria (categoria) VALUES('{self.categoria}')"

    @staticmethod
    def str_nombre(id):
        conn = Conexion_BD('Supermark.db')
        categoria = conn.consulta(f'SELECT categorias FROM categoria WHERE id={id}')
        return categoria[0][0]
    
    @staticmethod
    def retornar_categorias():
        conn = Conexion_BD('Supermark.db')
        categorias = conn.consulta('SELECT * FROM categoria')
        return categorias

if __name__ == '__main__':
    #Categoria.mostrar_categorias()
    #print(Categoria.str_nombre(2))
    print(Categoria.retornar_categorias())