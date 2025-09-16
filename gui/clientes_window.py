from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QListWidget, QLineEdit, QPushButton, QWidget
from db.connection import get_connection   # <- NUNCA importes ventana_inicial ni main aquí

class ClientesWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Gestión de Clientes")
        self.resize(600, 400)

        self.lista = QListWidget()
        self.input_nombre = QLineEdit(placeholderText="Nombre del cliente")
        self.btn_agregar = QPushButton("Agregar Cliente")
        self.btn_agregar.clicked.connect(self.agregar_cliente)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Clientes"))
        layout.addWidget(self.lista)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.btn_agregar)

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

        self.cargar_clientes()

    def cargar_clientes(self):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                SELECT c.id, p.nombre
                FROM clientes c
                JOIN personas p ON c.id = p.id
                ORDER BY p.nombre
            """)
            rows = cur.fetchall()
        finally:
            conn.close()

        self.lista.clear()
        for rid, nombre in rows:
            self.lista.addItem(f"{rid} - {nombre}")


            
    def agregar_cliente(self):
        pass
