"""5. Conversión y Parseo de JSON: Crea un script que convierta un diccionario de
Python con información de alumnos (nombre, curso, notas) a un archivo .json.
Luego, lee ese archivo JSON de vuelta y muestra los datos formateados."""

import json

alumno = {
    "nombre": "Pablo",
    "curso": 2,
    "notas": [8]
}

with open("alumno.json", "w") as archivo:
    json.dump(alumno, archivo)

with open("alumno.json", "r") as archivo:
    datos = json.load(archivo)

print(f"Nombre: {datos['nombre']}")
print(f"Curso: {datos['curso']}")
print(f"Notas: {datos['notas']}")