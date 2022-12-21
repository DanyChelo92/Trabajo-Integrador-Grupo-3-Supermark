from datetime import date
from datetime import datetime
from ProductoCarrito import ProductoCarrito
class Carrito:
  def __init__(self,fecha=None,productos=[],codigo=None,tipoComprobante=''):
    self.__tipoComprobante = tipoComprobante
    self.__fecha = fecha
    self.__productos = productos
    self.__codigo = codigo
    #self.__total = self.totalCarrito()

  @property
  def fecha(self):
    return self.__fecha
  
  @fecha.setter
  def fecha(self,fecha):
    self.__fecha = fecha

  @property
  def tipoComprobante(self):
    return self.__tipoComprobante

  @tipoComprobante.setter
  def tipoComprobante(self,tipoComprobante):
    self.__tipoComprobante = tipoComprobante

  @property
  def codigo(self):
    return self.__codigo

  @codigo.setter
  def codigo(self,codigo):
    self.__codigo = codigo

  @property
  def productos(self):
    return self.__productos
  
  @productos.setter
  def productos(self,productos):
    self.__productos = productos

  
  
  def totalCarrito(self):
    sum = 0.00
    for p in self.__productos:
      sum += (p.precio*p.cantidad)
    return sum
    
  def agregar_producto(self,producto):
    self.__productos.append(producto)

  def eliminar_producto(self,producto):
    codigos = list(map(lambda cod: cod.id_producto,self.productos))
    for codigo in codigos:
      if codigo == producto.id_producto :
        indice_producto=codigos.index(codigo)
        self.productos.pop(indice_producto)
        break

  def modificar_producto(self,producto):
    codigos = list(map(lambda cod: cod.id_producto,self.productos))
    for codigo in codigos:
      if codigo == producto.id_producto :
        indice_producto=codigos.index(codigo)
        self.productos[indice_producto].cantidad = producto.cantidad
        break

  #retorna la posisicion de un producto en el carrito
  def indice_producto(self,codigo):
    pos = None
    codigos = list(map(lambda cod: cod.id_producto,self.productos))
    for cod in codigos:
      if cod == codigo :
        pos = codigos.index(cod)
    return pos

  def lista_carrito(self):
    lista=''
    for producto in self.__productos:
      lista += '\n'+producto.__str__()+'\n'
    lista +='\n'+"Subtotal: "+str(self.totalCarrito())
    return lista

  #retorna la canridad de articulos del carrito
  def cantidad_articulos(self):
    cantidad = 0
    for prod in self.productos:
      cantidad += prod.cantidad
    return cantidad

  def __str__(self):
    cadena = ''
    cadena +=f"\nCodigo: {self.codigo}\n"
    cadena +=f"Fecha: {self.fecha}\n"
    cadena +=f"Tipo Comprobante: {self.tipoComprobante}\n"
    cadena +=self.lista_carrito()
    return cadena
  
  #Retorna un objeto producto por codigo
  def busca_codigo(self,codigo):
    p = None
    for p in self.__productos:
      if p.id_producto == codigo:
        return p
    return p

  #comprueba la existencia de un producto en el carrito
  def existencia(self,producto):
    codigos = list(map(lambda cod: cod.id_producto,self.productos))
    if producto.id_producto in codigos:
      return True
    else:
      return False

  @staticmethod
  def lista_disponibles():
    registros = ProductoCarrito.productos_con_stock()
    for p in registros:
      print(f"ID: {p[0]}\nNombre: {p[1]}\nMarca: {p[2]}\nPrecio: {p[3]}\nCategoria: {p[4]}\nStock: {p[5]}\nDescripcion: {p[6]}")
      print()

  


  

if __name__ == '__main__':
  #Carrito.lista_disponibles()
  miCarrito = Carrito()
  miCarrito.agregar_producto(ProductoCarrito('Pelota','Penalti',800.49,1,'Pelota n° 7 penalti',2,1))
  miCarrito.agregar_producto(ProductoCarrito('arroz','Cañuelas',150,1,'x 1kg 0000',2,2))
  miCarrito.agregar_producto(ProductoCarrito('Aciete','Cañuelas',150,1,'x 1kg 0000',2,3))
  miCarrito.agregar_producto(ProductoCarrito('Harina','Cañuelas',150,1,'x 1kg 0000',2,4))
  #print(miCarrito.lista_carrito())
  #print(miCarrito.total)
  #miCarrito.modificar_producto(0,80)
  #print(miCarrito.lista_carrito())
  print(len(miCarrito.productos))
  #print(miCarrito.busca_codigo(2))
  #miCarrito.eliminar_producto(miCarrito.busca_codigo(2))
  #print(miCarrito.lista_carrito())
  lista = list(map(lambda cod: cod.id_producto,miCarrito.productos))
  print(lista)
  '''for codigos in lista:
    if codigos == 3 :
      print(lista.index(codigos))
      print(miCarrito.productos.pop(lista.index(codigos)))
      break
  '''
  print(miCarrito.existencia(ProductoCarrito('Aciete','Cañuelas',150,1,'x 1kg 0000',2,6)))
  #miCarrito.lista_disponibles()
  #miCarrito.eliminar_producto()
  '''for p in miCarrito.productos:
    print(p)'''

  #print(miCarrito.productos.index(ProductoCarrito('Aciete','Cañuelas',150,1,'x 1kg 0000',2,2)))

  #for p in miCarrito.productos:
    #print(p.nombre)