# main.py

"""
Este archivo ejecuta un ejemplo de cómo usar las clases Alternativa, Pregunta, 
Usuario, Encuesta y ListadoRespuestas para crear un sistema básico de encuestas.

Se crean alternativas, preguntas, usuarios y encuestas, luego se muestran las encuestas
y se asocian respuestas de un usuario a una encuesta.
"""

# Importación de las clases necesarias para el funcionamiento del sistema de encuestas
from Alternativa import Alternativa
from pregunta import Pregunta
from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion
from usuario import Usuario
from listado_respuesta import ListadoRespuestas

# Crear alternativas para una pregunta
alt1 = Alternativa("Sí", "Selecciona si estás de acuerdo")  # Alternativa 1: Sí con ayuda
alt2 = Alternativa("No", "Selecciona si no estás de acuerdo")  # Alternativa 2: No con ayuda

# Crear una pregunta utilizando las alternativas creadas
pregunta1 = Pregunta("¿Te gusta el chocolate?", True, [alt1, alt2])  
# Pregunta: "¿Te gusta el chocolate?" con dos alternativas (Sí y No), y es requerida.

# Crear un usuario que participará en la encuesta
usuario1 = Usuario("usuario@example.com", 25, 13)  
# Usuario: con correo, edad 25, y región 13.

# Crear una encuesta con la pregunta previamente creada
encuesta = Encuesta("Encuesta sobre gustos", [pregunta1])  
# Encuesta: "Encuesta sobre gustos" que incluye una lista con la pregunta anterior.

# Mostrar la encuesta y sus preguntas
print(encuesta.mostrar())  
# Muestra la encuesta con su nombre, pregunta, y alternativas.

# Crear un listado de respuestas para asociar las respuestas del usuario a la encuesta
listado_respuestas = ListadoRespuestas(usuario1, [1])  
# Listado de respuestas: El usuario selecciona la primera opción (índice 1: "Sí").

# Agregar las respuestas del usuario a la encuesta
encuesta.agregar_respuestas(listado_respuestas)  
# Se asocia el listado de respuestas a la encuesta.

# Confirmar que las respuestas fueron agregadas
print("Respuestas agregadas a la encuesta.")
