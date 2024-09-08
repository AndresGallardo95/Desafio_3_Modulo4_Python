# main.py
from Alternativa import Alternativa
from pregunta import Pregunta
from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion
from usuario import Usuario
from listado_respuesta import ListadoRespuestas

# Crear alternativas
alt1 = Alternativa("Sí", "Selecciona si estás de acuerdo")
alt2 = Alternativa("No", "Selecciona si no estás de acuerdo")

# Crear una pregunta
pregunta1 = Pregunta("¿Te gusta el chocolate?", True, [alt1, alt2])

# Crear un usuario
usuario1 = Usuario("usuario@example.com", 25, 13)

# Crear una encuesta
encuesta = Encuesta("Encuesta sobre gustos", [pregunta1])

# Mostrar encuesta
print(encuesta.mostrar())

# Crear un listado de respuestas
listado_respuestas = ListadoRespuestas(usuario1, [1])

# Agregar las respuestas a la encuesta
encuesta.agregar_respuestas(listado_respuestas)
print("Respuestas agregadas a la encuesta.")
