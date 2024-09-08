# encuesta.py
from pregunta import Pregunta
from listado_respuesta import ListadoRespuestas

class Encuesta:
    def __init__(self, nombre, preguntas):
        self.nombre = nombre
        self.preguntas = preguntas  # Lista de objetos de tipo Pregunta
        self.listados_respuestas = []  # Lista de listados de respuestas

    def mostrar(self):
        result = f"Encuesta: {self.nombre}\n"
        result += "Preguntas:\n"
        for pregunta in self.preguntas:
            result += f"- {pregunta.mostrar()}\n"
        return result

    def agregar_respuestas(self, listado_respuestas):
        self.listados_respuestas.append(listado_respuestas)

    def modificar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre


class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, preguntas, edad_minima, edad_maxima):
        super().__init__(nombre, preguntas)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    def agregar_respuestas(self, listado_respuestas):
        if self.edad_minima <= listado_respuestas.usuario.edad <= self.edad_maxima:
            super().agregar_respuestas(listado_respuestas)
        else:
            raise ValueError("Edad del usuario fuera del rango permitido.")


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, preguntas, regiones_permitidas):
        super().__init__(nombre, preguntas)
        self.regiones_permitidas = regiones_permitidas

    def agregar_respuestas(self, listado_respuestas):
        if listado_respuestas.usuario.region in self.regiones_permitidas:
            super().agregar_respuestas(listado_respuestas)
        else:
            raise ValueError("Región del usuario no permitida.")
