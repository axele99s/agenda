import sqlite3

connect = sqlite3.connect('baseAgendaPy.db')


# conecto el curso a la BD
cursor = connect.cursor()

# creo la tabla si no existe
#cursor.execute('''CREATE TABLE IF NOT EXISTS USUARIOS
 #                 (id INTEGER PRIMARY KEY, 
 #                   nombre TEXT, 
 #                  edad INTEGER
  #                , email TEXT, 
  #                 num_celular TEXT
   #               , direccion TEXT, 
   #                ciudad TEXT)''')

# inserto un registro de prueba
#cursor.execute('''INSERT INTO USUARIOS(nombre,edad,email,num_celular,direccion,ciudad) 
 #               VALUES("Axel", 25, "axelemail@email.com", "random_number", "random_address", "random_city")''')
#


# selecciono todos los registros de la tabla
# (me los guardo en la variable datos TODOS los registros)
datos = cursor.execute('''SELECT * FROM USUARIOS''')

# los imprimo (fila por fila)    
for fila in datos:
    print(fila)


# guardo los cambios y cierro la conexión
connect.commit()
connect.close()
#print("Base de datos y tabla creada exitosamente.")