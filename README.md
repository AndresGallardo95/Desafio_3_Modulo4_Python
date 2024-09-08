# Desafío - Diagrama de Clases y Programación en Python

## Descripción

Este proyecto es una implementación de un sistema de encuestas, que permite crear y contestar encuestas a través de usuarios, preguntas, alternativas, y respuestas. El desafío se divide en varias partes que incluyen la creación de diagramas de clases y el desarrollo de un conjunto de clases en Python basadas en esos diagramas.

El objetivo del proyecto es:
1. Crear un diagrama de clases que represente las relaciones entre encuestas, preguntas, alternativas, usuarios, y listados de respuestas.
2. Implementar las clases necesarias en Python para manejar estas entidades.

## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos de Python:

- `alternativa.py`: Contiene la clase `Alternativa`, que representa una alternativa dentro de una pregunta.
- `pregunta.py`: Contiene la clase `Pregunta`, que incluye un enunciado, si es requerida, y una lista de alternativas.
- `encuesta.py`: Contiene la clase `Encuesta` y sus subclases `EncuestaLimitadaEdad` y `EncuestaLimitadaRegion`.
- `usuario.py`: Contiene la clase `Usuario`, que gestiona la información del usuario.
- `listado_respuestas.py`: Contiene la clase `ListadoRespuestas`, que asocia a un usuario con sus respuestas a una encuesta.
- `main.py`: Un archivo que muestra cómo se utilizan las clases en un flujo simple.


## Instalación y Configuración

### Requisitos:

- Python 3.x
- IDE o editor de texto (como Visual Studio Code o PyCharm)

### Instalación:

1. **Clona el repositorio o descarga el código fuente:**

   ```bash
   git clone https://github.com/AndresGallardo95/Desafio_3_Modulo4_Python.git
