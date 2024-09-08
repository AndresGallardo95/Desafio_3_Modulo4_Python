# alternativa.py

class Alternativa:
    """
    Clase que representa una alternativa dentro de una pregunta.
    
    Atributos:
    - contenido (str): El contenido textual de la alternativa.
    - ayuda (str, opcional): Texto de ayuda asociado a la alternativa.
    
    Métodos:
    - mostrar(): Muestra la alternativa y su ayuda si está presente.
    - modificar_contenido(): Modifica el contenido de la alternativa.
    - modificar_ayuda(): Modifica el texto de ayuda de la alternativa.
    """
    
    def __init__(self, contenido, ayuda=None):
        """
        Inicializa una nueva alternativa.
        
        Args:
        - contenido (str): El contenido de la alternativa.
        - ayuda (str, opcional): Texto de ayuda (por defecto es None).
        """
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar(self):
        """Retorna el contenido y la ayuda (si existe) de la alternativa."""
        if self.ayuda:
            return f"Alternativa: {self.contenido}, Ayuda: {self.ayuda}"
        else:
            return f"Alternativa: {self.contenido}"

    def modificar_contenido(self, nuevo_contenido):
        """Modifica el contenido de la alternativa."""
        self.contenido = nuevo_contenido

    def modificar_ayuda(self, nueva_ayuda):
        """Modifica el texto de ayuda de la alternativa."""
