"""Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de 
una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que 
introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.
 Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin 
repeticiones.
 Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
 Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
 Mostrar si todos los nombres de primaria están incluidos en secundaria."""

def nombres_alumnos():
    nombresPrimaria = set()
    nombresSecundaria = set()
    preguntaP = ""
    preguntaS = ""
    while preguntaS.lower() != "x":
        while preguntaP.lower() != "x":
            preguntaP = input("Introduce un nombre de pila de un alumno de PRIMARIA: ")
            if preguntaP.lower() != "x":
                nombresPrimaria.add(preguntaP)
        preguntaS = input("Introduce un nombre de pila de un alumno de SECUNDARIA: ")
        nombresSecundaria.add(preguntaS)
        if preguntaS.lower() != "x":
            nombresSecundaria.add(preguntaS)
    return nombresPrimaria, nombresSecundaria

def comparaNombres(primaria, secundaria):
    union = primaria.union(secundaria)
    interseccion = primaria.intersection(secundaria)
    diferencia = primaria.difference(secundaria)
    subconjunto = primaria.issubset(secundaria)
    return f"Union: {union}\nInterseccion: {interseccion}\nDiferencia: {diferencia}\nSubconjunto: {subconjunto}"


if __name__ == "__main__":
    try:
        primaria, secundaria = nombres_alumnos()
        print(comparaNombres(primaria,secundaria))
    except Exception as e:
        print(f"Algo ha salido mal: {e}")



        
