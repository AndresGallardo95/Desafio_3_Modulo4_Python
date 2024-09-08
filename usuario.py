# usuario.py

class Usuario:
    def __init__(self, correo, edad, region):
        self.correo = correo
        self.edad = edad
        self.region = region

    def __str__(self):
        return f"Usuario: {self.correo}, Edad: {self.edad}, Región: {self.region}"

    def modificar_correo(self, nuevo_correo):
        self.correo = nuevo_correo

    def modificar_edad(self, nueva_edad):
        self.edad = nueva_edad

    def modificar_region(self, nueva_region):
        self.region = nueva_region
