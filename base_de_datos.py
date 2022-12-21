import sqlite3
conexion = sqlite3.connect('Supermark.db')
cursor = conexion.cursor()

cursor.execute("""create table if not exists usuario(
              correo text(50) primary key not null,
              clave text(16) not null,
              tipo_usuario text(20) not null)""")

cursor.execute("""create table if not exists cliente(
              id integer primary key autoincrement,
              nombre text (50) not null,
              apellido text(50) not null,
              dni text(10) not null,
              domicilio text(200) not null,
              correo text(50) not null,
              foreign key(correo) references usuario(correo))""")

cursor.execute("""create table if not exists categoria(
              id integer primary key autoincrement,
              categoria text(20) unique not null)""")

cursor.execute("""create table if not exists producto(
              id integer primary key autoincrement,
              nombre text(50) not null,
              marca text(50) not null,
              precio real (6,2) not null,
              stock integer not null,
              id_categoria integer not null,
              descripcion text(200),
              foreign key(id_categoria) references categoria(id)
              )""")

cursor.execute(""" create table if not exists detalle_ventas(
              id integer primary key autoincrement,
              id_prod integer(4),
              id_vent interger,
              cantidad integer(4) not null,
              foreign key(id_prod) references usuario(id),
              foreign key(id_vent) references venta(id)
              )""")

cursor.execute("""create table if not exists venta(
              id integer primary key autoincrement,
              tipo_comprobante char(1) not null,
              fecha datetime not null,
              id_cliente integer not null,
              foreign key(id_cliente) references cliente(id)
              )""")

cursor.execute("""create table if not exists administrador(
              id integer primary key autoincrement,
              nombre text (50) not null,
              apellido text(50) not null,
              dni text(10) not null,
              domicilio text(200) not null,
              correo text(50) not null,
              foreign key(correo) references usuario(correo))""")
