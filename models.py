from datetime import datetime


# persona base
class Persona:

    def __init__(self, id: int, nombre: str, email: str, num_celular: str, direccion: str, ciudad: str, fecha_nacimiento: str, creado_en: datetime):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.num_celular = num_celular
        self.direccion = direccion
        self.ciudad = ciudad
        self.fecha_nacimiento = fecha_nacimiento
        self.creado_en = creado_en 

    def setNombre(self, nombre: str):
        self.nombre = nombre
    
    def setEmail(self, email: str):
        self.email = email
    
    def setNumCelular(self, num_celular: str):
        self.num_celular = num_celular

    def setDireccion(self, direccion: str):
        self.direccion = direccion
    def setCiudad(self, ciudad: str):
        self.ciudad = ciudad
    def setFechaNacimiento(self, fecha_nacimiento: str):
        self.fecha_nacimiento = fecha_nacimiento
    
    def getNombre(self):
        return self.nombre
    def getEmail(self):
        return self.email
    def getNumCelular(self):
        return self.num_celular
    def getDireccion(self):
        return self.direccion
    def getCiudad(self):
        return self.ciudad
    def getFechaNacimiento(self):
        return self.fecha_nacimiento
    


#usuario
class Usuario(Persona):
    rol: str

    def __init__(self, id: int, nombre: str, email: str, num_celular: str, direccion: str, ciudad: str, fecha_nacimiento: str, creado_en: datetime, rol: str):
        super().__init__(id, nombre, email, num_celular, direccion, ciudad, fecha_nacimiento, creado_en)
        self.rol = rol
    
    def setRol(self, rol: str):
        self.rol = rol
    def getRol(self):
        return self.rol
    

class Cliente(Persona):
    edad: int  
    notas: str

    def __init__(self, id: int, nombre: str, email: str, num_celular: str, direccion: str, ciudad: str, fecha_nacimiento: str, creado_en: datetime, edad: int, notas: str):
        super().__init__(id, nombre, email, num_celular, direccion, ciudad, fecha_nacimiento, creado_en)
        self.edad = edad
        self.notas = notas
    
    def setEdad(self, edad: int):
        self.edad = edad
    def setNotas(self, notas: str):
        self.notas = notas

