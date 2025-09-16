# Logica para el CRUD de usuarios

from models import Usuario
from db.connection import get_connection
from datetime import datetime


def crear_usuario(usuario: Usuario):
    # Lógica para crear un usuario en la base de datos
    conn = get_connection()

    try:
        cur = conn.cursor()

        # 1. Insertar persona
        cur.execute("""
            INSERT INTO personas (nombre, email, num_celular, direccion, ciudad, fecha_nacimiento, creado_en)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            usuario.nombre,
            usuario.email,
            usuario.num_celular,
            usuario.direccion,
            usuario.ciudad,
            usuario.fecha_nacimiento,
            datetime.now()
        ))
        persona_id = cur.lastrowid

        # 2. Insertar usuario
        cur.execute("""
            INSERT INTO usuarios (id, rol)
            VALUES (?, ?)
        """, (persona_id, usuario.rol))

        conn.commit()
        return persona_id

    except Exception as e:
        print(f" Error al crear usuario: {e}")
        conn.rollback()
        return None

    finally:
        conn.close()


def obtener_usuario(usuario_id: int):
    """Devuelve un usuario como diccionario, o None si no existe."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * 
        FROM usuarios u
        JOIN personas p ON u.id = p.id
        WHERE u.id = ?;
    """, (usuario_id,))

    row = cur.fetchone()
    conn.close()

    if row:
        return row  
    return None


