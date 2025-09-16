-- Crear la base de datos (en SQLite es opcional, solo sirve en CLI con .open)
-- CREATE DATABASE IF NOT EXISTS baseAgendaPy;

-- Tabla personas (base para usuarios y clientes)
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT,
    num_celular TEXT,
    direccion TEXT,
    ciudad TEXT,
    fecha_nacimiento TEXT,   -- formato 'YYYY-MM-DD'
    creado_en TEXT DEFAULT (datetime('now'))
);

-- Usuarios "hereda" de personas
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    rol TEXT,
    FOREIGN KEY (id) REFERENCES personas(id)
);

-- Clientes "hereda" de personas
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    edad INTEGER,
    FOREIGN KEY (id) REFERENCES personas(id)
);

-- Turnos
CREATE TABLE IF NOT EXISTS turnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    cliente_id INTEGER NOT NULL,
    inicio TEXT NOT NULL,   -- formato 'YYYY-MM-DD HH:MM:SS'
    fin TEXT NOT NULL,
    estado TEXT NOT NULL DEFAULT 'pendiente',
    notas TEXT,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE RESTRICT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE RESTRICT,
    CHECK (julianday(fin) > julianday(inicio)),
    CHECK (estado IN ('pendiente','confirmado','cancelado','completado','ausente'))
);

-- Uniques: turnos no repetidos
CREATE UNIQUE INDEX IF NOT EXISTS uq_turno_exacto
ON turnos (usuario_id, cliente_id, inicio, fin);

-- Índices para búsquedas
CREATE INDEX IF NOT EXISTS idx_turnos_usuario_inicio ON turnos (usuario_id, inicio);
CREATE INDEX IF NOT EXISTS idx_turnos_cliente_inicio ON turnos (cliente_id, inicio);
