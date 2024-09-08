# usuario.py

class Usuario:
    """
    Clase que representa un usuario.
    
    Atributos:
    - correo (str): Correo electrónico del usuario.
    - edad (int): Edad del usuario.
    - region (int): Región del usuario.
    
    Métodos:
    - modificar_correo(): Modifica el correo del usuario.
    - modificar_edad(): Modifica la edad del usuario.
    - modificar_region(): Modifica la región del usuario.
    """
    
    def __init__(self, correo, edad, region):
        """Inicializa un nuevo usuario."""
        self.correo = correo
        self.edad = edad
        self.region = region

    def __str__(self):
        """Retorna una representación en texto del usuario."""
        return f"Usuario: {self.correo}, Edad: {self.edad}, Región: {self.region}"

    def modificar_correo(self, nuevo_correo):
        """Modifica el correo electrónico del usuario."""
        self.correo = nuevo_correo

    def modificar_edad(self, nueva_edad):
        """Modifica la edad del usuario."""
        self.edad = nueva_edad

    def modificar_region(self, nueva_region):
        """Modifica la región del usuario."""
        self.region = nueva_region
