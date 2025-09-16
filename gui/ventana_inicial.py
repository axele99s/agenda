# ventana_inicial.py
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

# Importa la otra ventana
from clientes_window import ClientesWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AgendaPy - Ventana Principal")
        self.resize(800, 600)

        # Widgets
        label = QLabel("Bienvenido a AgendaPy 👋")
        boton_salir = QPushButton("Salir")
        boton_clientes = QPushButton("Gestionar Clientes")

        # Eventos
        boton_salir.clicked.connect(self.close)
        boton_clientes.clicked.connect(self.abrir_clientes)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(boton_clientes)
        layout.addWidget(boton_salir)

        # Central
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

        # Mantener referencia a la ventana de clientes
        self.clientes_window = None

    def abrir_clientes(self):
        if self.clientes_window is None:
            self.clientes_window = ClientesWindow()
        self.clientes_window.show()
        self.clientes_window.raise_()  # la trae al frente


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
