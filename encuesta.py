# encuesta.py
from pregunta import Pregunta
from listado_respuesta import ListadoRespuestas

class Encuesta:
    """
    Clase que representa una encuesta con preguntas y listados de respuestas.
    
    Atributos:
    - nombre (str): El nombre de la encuesta.
    - preguntas (list): Lista de objetos Pregunta.
    - listados_respuestas (list): Lista de listados de respuestas.
    
    Métodos:
    - mostrar(): Muestra la encuesta y sus preguntas.
    - agregar_respuestas(): Agrega un listado de respuestas a la encuesta.
    - modificar_nombre(): Modifica el nombre de la encuesta.
    """
    
    def __init__(self, nombre, preguntas):
        """
        Inicializa una nueva encuesta.
        
        Args:
        - nombre (str): El nombre de la encuesta.
        - preguntas (list): Lista de objetos Pregunta.
        """
        self.nombre = nombre
        self.preguntas = preguntas
        self.listados_respuestas = []

    def mostrar(self):
        """Retorna una representación de la encuesta y sus preguntas."""
        result = f"Encuesta: {self.nombre}\n"
        result += "Preguntas:\n"
        for pregunta in self.preguntas:
            result += f"- {pregunta.mostrar()}\n"
        return result

    def agregar_respuestas(self, listado_respuestas):
        """Agrega un listado de respuestas a la encuesta."""
        self.listados_respuestas.append(listado_respuestas)

    def modificar_nombre(self, nuevo_nombre):
        """Modifica el nombre de la encuesta."""
        self.nombre = nuevo_nombre


class EncuestaLimitadaEdad(Encuesta):
    """
    Subclase de Encuesta que restringe la participación por edad.
    
    Métodos:
    - agregar_respuestas(): Solo agrega las respuestas si la edad está en el rango permitido.
    """
    
    def __init__(self, nombre, preguntas, edad_minima, edad_maxima):
        """
        Inicializa una encuesta limitada por edad.
        
        Args:
        - nombre (str): El nombre de la encuesta.
        - preguntas (list): Lista de preguntas.
        - edad_minima (int): Edad mínima permitida.
        - edad_maxima (int): Edad máxima permitida.
        """
        super().__init__(nombre, preguntas)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    def agregar_respuestas(self, listado_respuestas):
        """Agrega las respuestas si el usuario cumple con el rango de edad."""
        if self.edad_minima <= listado_respuestas.usuario.edad <= self.edad_maxima:
            super().agregar_respuestas(listado_respuestas)
        else:
            raise ValueError("Edad del usuario fuera del rango permitido.")


class EncuestaLimitadaRegion(Encuesta):
    """
    Subclase de Encuesta que restringe la participación por región.
    
    Métodos:
    - agregar_respuestas(): Solo agrega las respuestas si la región está permitida.
    """
    
    def __init__(self, nombre, preguntas, regiones_permitidas):
        """
        Inicializa una encuesta limitada por región.
        
        Args:
        - nombre (str): El nombre de la encuesta.
        - preguntas (list): Lista de preguntas.
        - regiones_permitidas (list): Lista de regiones permitidas.
        """
        super().__init__(nombre, preguntas)
        self.regiones_permitidas = regiones_permitidas

    def agregar_respuestas(self, listado_respuestas):
        """Agrega las respuestas si la región del usuario está permitida."""
        if listado_respuestas.usuario.region in self.regiones_permitidas:
            super().agregar_respuestas(listado_respuestas)
        else:
            raise ValueError("Región del usuario no permitida.")
