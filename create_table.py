import sqlite3

connect = sqlite3.connect('baseAgendaPy.db')


# conecto el curso a la BD
cursor = connect.cursor()

# creo la tabla  de CLIENTES
# cursor.execute('''CREATE TABLE IF NOT EXISTS CLIENTES
#                  (id INTEGER PRIMARY KEY, 
#                    nombre TEXT, 
#                   edad INTEGER
#                 , email TEXT, 
#                  num_celular TEXT
#                , direccion TEXT, 
#                 ciudad TEXT)''')
cursor.execute("""
CREATE TABLE IF NOT EXISTS turnos (
    id INTEGER PRIMARY KEY,
    usuario_id INTEGER NOT NULL,
    cliente_id INTEGER NOT NULL,
    inicio TEXT NOT NULL,   -- formato: 'YYYY-MM-DD HH:MM:SS'
    fin TEXT NOT NULL,
    estado TEXT NOT NULL DEFAULT 'pendiente',
    notas TEXT,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE RESTRICT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE RESTRICT,
    CHECK (julianday(fin) > julianday(inicio)),
    CHECK (estado IN ('pendiente','confirmado','cancelado','completado','ausente'))
);
""")
# uniques, turnos no repetidos
# CREATE UNIQUE INDEX IF NOT EXISTS uq_turno_exacto
# ON turnos (usuario_id, cliente_id, inicio, fin);

# indices para busquedas
# CREATE INDEX idx_turnos_usuario_inicio ON turnos (usuario_id, inicio);
# CREATE INDEX idx_turnos_cliente_inicio ON turnos (cliente_id, inicio);


connect.commit()
connect.close()

# inserto un registro de prueba
#cursor.execute('''INSERT INTO USUARIOS(nombre,edad,email,num_celular,direccion,ciudad) 
 #               VALUES("Axel", 25, "axelemail@email.com", "random_number", "random_address", "random_city")''')
#