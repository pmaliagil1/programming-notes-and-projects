"""Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
sobre una persona (por ejemplo, nombre, edad, sexo, teléfono, correo electrónico, etc.)
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
contenido del diccionario."""

import os

#Mejorar añadiendo correos y verificando que el usuario lo introduzca correctamente.
def infoPersona(persona):
    try:
        nombre = input("Introduzca su nombre: ")
        persona["nombre"] = nombre
        print(persona)
        edad = int(input("Introduzca su edad: "))
        persona["edad"] = edad
        print(persona)
        sexo = input("Introduzca su sexo (M/F): ").upper()
        if sexo != "M" and sexo != "F":
            raise ValueError("VALOR NO VALIDO")
        persona["sexo"] = sexo
        print(persona)
        correo = input("Introduce tu correo: ")
        if validaCorreo(correo):
            persona["correo"] = correo
        else:
            raise ValueError("VALOR NO VALIDO")
        print(persona)

        return persona
    except ValueError:
        print(f"Valor no válido")

def validaCorreo(correo):
    if '@' not in correo:
        return False

    partes = correo.split('@')
    if len(partes) != 2:
        return False

    nombre, dominio = partes
    if not nombre or not dominio:
        return False
    
    if '.' not in dominio:
        return False

    subdominio = dominio.split('.')
    if len(subdominio) < 2:
        return False

    extension = subdominio[-1]
    if len(extension) < 2:
        return False

    return True

if __name__ == "__main__":
    try:
        persona = dict()
        infoPersona(persona)
    except Exception as e:
        print(f"Algo ha salido mal: {e}")

"""Funcion validacion correo:
import os

def validaCorreo(correo):
    if '@' not in correo:
        return False

    partes = correo.split('@')
    if len(partes) != 2:
        return False

    nombre, dominio = partes
    if not nombre or not dominio:
        return False
    
    if '.' not in dominio:
        return False

    subdominio = dominio.split('.')
    if len(subdominio) < 2:
        return False

    extension = subdominio[-1]
    if len(extension) < 2:
        return False

    return True
"""