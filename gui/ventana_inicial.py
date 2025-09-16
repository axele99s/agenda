# gui/ventana_inicial.py
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from gui.clientes_window import ClientesWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AgendaPy - Ventana Principal")
        self.resize(800, 600)

        label = QLabel("Bienvenido a AgendaPy 👋")
        btn_salir = QPushButton("Salir")
        btn_clientes = QPushButton("Gestionar Clientes")

        btn_salir.clicked.connect(self.close)
        btn_clientes.clicked.connect(self.abrir_clientes)

        lay = QVBoxLayout()
        lay.addWidget(label)
        lay.addWidget(btn_clientes)
        lay.addWidget(btn_salir)

        central = QWidget()
        central.setLayout(lay)
        self.setCentralWidget(central)

        self.clientes_window = None

    def abrir_clientes(self):
        if self.clientes_window is None:
            self.clientes_window = ClientesWindow()
        self.clientes_window.show()
