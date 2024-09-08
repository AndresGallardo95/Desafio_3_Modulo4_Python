# pregunta.py
from Alternativa import Alternativa

class Pregunta:
    """
    Clase que representa una pregunta dentro de una encuesta.
    
    Atributos:
    - enunciado (str): El enunciado de la pregunta.
    - es_requerida (bool): Si la pregunta es obligatoria o no.
    - ayuda (str, opcional): Texto de ayuda para la pregunta.
    - alternativas (list): Lista de objetos Alternativa.
    
    Métodos:
    - mostrar(): Muestra el enunciado, ayuda y alternativas de la pregunta.
    - modificar_enunciado(): Modifica el enunciado de la pregunta.
    - modificar_ayuda(): Modifica la ayuda de la pregunta.
    """
    
    def __init__(self, enunciado, es_requerida, alternativas, ayuda=None):
        """
        Inicializa una nueva pregunta.
        
        Args:
        - enunciado (str): El texto de la pregunta.
        - es_requerida (bool): Si la pregunta es obligatoria.
        - alternativas (list): Lista de alternativas (objetos Alternativa).
        - ayuda (str, opcional): Texto de ayuda (por defecto es None).
        """
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.es_requerida = es_requerida
        self.alternativas = alternativas

    def mostrar(self):
        """Retorna una representación de la pregunta con sus alternativas."""
        result = f"Pregunta: {self.enunciado}\n"
        if self.ayuda:
            result += f"Ayuda: {self.ayuda}\n"
        result += "Alternativas:\n"
        
        # Aquí corregimos la indentación
        for alternativa in self.alternativas:
            result += f"- {alternativa.mostrar()}\n"
        
        return result

    def modificar_enunciado(self, nuevo_enunciado):
        """Modifica el enunciado de la pregunta."""
        self.enunciado = nuevo_enunciado

    def modificar_ayuda(self, nueva_ayuda):
        """Modifica la ayuda de la pregunta."""
        self.ayuda = nueva_ayuda
