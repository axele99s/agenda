from datetime import datetime

class Persona:
    id: int
    nombre: str
    email: str
    num_celular: str
    direccion: str
    ciudad: str
    fecha_nacimiento: str
    creado_en: datetime
    

class Usuario(Persona):
    rol: str   

class Cliente(Persona):
    edad: int  

    notas: str
