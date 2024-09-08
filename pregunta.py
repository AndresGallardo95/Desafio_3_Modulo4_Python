# pregunta.py
from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado, es_requerida, alternativas, ayuda=None):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.es_requerida = es_requerida
        self.alternativas = alternativas  # Lista de objetos de tipo Alternativa

    def mostrar(self):
        result = f"Pregunta: {self.enunciado}\n"
        if self.ayuda:
            result += f"Ayuda: {self.ayuda}\n"
        result += "Alternativas:\n"
        for alternativa in self.alternativas:
            result += f"- {alternativa.mostrar()}\n"
        return result

    def modificar_enunciado(self, nuevo_enunciado):
        self.enunciado = nuevo_enunciado

    def modificar_ayuda(self, nueva_ayuda):
        self.ayuda = nueva_ayuda
