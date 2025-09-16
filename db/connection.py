# db/connection.py
import sqlite3
import os

# Calcula la ruta de agenda.db relativa al proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # carpeta /db
DB_PATH = os.path.join(BASE_DIR, "agenda.db")          # db/agenda.db

def get_connection():
    return sqlite3.connect(DB_PATH)
    