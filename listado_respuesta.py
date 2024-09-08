# listado_respuestas.py
from usuario import Usuario

class ListadoRespuestas:
    def __init__(self, usuario, respuestas):
        self.usuario = usuario
        self.respuestas = respuestas  # Lista de respuestas (números enteros)

    def mostrar_respuestas(self):
        return f"Respuestas del usuario {self.usuario.correo}: {self.respuestas}"
