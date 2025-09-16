# gui/clientes_window.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton,
    QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QListWidget
)


class ClientesWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de Clientes")
        self.resize(600, 400)

        # Widgets
        self.lista_clientes = QListWidget()
        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nombre del cliente")
        self.btn_agregar = QPushButton("Agregar Cliente")

        # Eventos
        self.btn_agregar.clicked.connect(self.agregar_cliente)

        # Layout superior
        form_layout = QHBoxLayout()
        form_layout.addWidget(self.input_nombre)
        form_layout.addWidget(self.btn_agregar)

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Clientes:"))
        layout.addWidget(self.lista_clientes)
        layout.addLayout(form_layout)

        # Central widget
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    def agregar_cliente(self):
        nombre = self.input_nombre.text().strip()
        if nombre:
            self.lista_clientes.addItem(nombre)
            self.input_nombre.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ClientesWindow()
    ventana.show()
    sys.exit(app.exec())
