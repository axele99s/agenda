# main.py
from models import Usuario
from servicios.usuarios_service import crear_usuario, obtener_usuario
from datetime import datetime

from PyQt6.QtWidgets import QApplication
from gui.ventana_inicial import MainWindow
import sys
if __name__ == "__main__":
#    Crear un nuevo usuario (se crea persona + usuario)
    # nuevo_usuario = Usuario(
    #     id=-1,  # lo genera SQLite, asi que no lo tiene en cuenta
    #     nombre="Axel",
    #     email="axel2@email.com",
    #     num_celular="1111111111",
    #     direccion="Calle Falsa 123",
    #     ciudad="Santa Fe",
    #     fecha_nacimiento="2000-01-01",  # formato YYYY-MM-DD
    #     creado_en=datetime.now(),
    #     rol="empleado"
    # )

    # usuario_id = crear_usuario(nuevo_usuario)
    # if usuario_id:
    #     print( Usuario creado con ID {usuario_id}")
    #     # Consultar el mismo usuario
    #     usuario = obtener_usuario(usuario_id)
    #     print("Datos del usuario desde la BD:")
    #     print(usuario)
    # else:
    #     print("" No se pudo crear el usuario")

    # Consultar un usuario existente
    # usuario = obtener_usuario(1)
    # if usuario:
    #     print("Datos del usuario desde la BD:")
    #     print(usuario)
    # else:
    #     print("No existe el usuario con ese ID")

    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())