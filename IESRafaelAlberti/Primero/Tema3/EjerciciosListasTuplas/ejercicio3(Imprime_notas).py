"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de
las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas
por el usuario. Usa funciones siempre que se pueda."""

def escribeAsignaturas():
    contador = 0
    cont = 0
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    notas = []
    for asignatura in asignaturas:
        
        nota = float(input(f"Introduce la nota de {asignaturas[contador]}: "))
        notas.append(nota)
        contador+=1
        
    for asignatura in asignaturas:
        print(f"En {asignaturas[cont]} has sacado {notas[cont]}")
        cont+=1


if __name__ == "__main__":
    try:
        escribeAsignaturas()

    except Exception as e:
        print(f"Algo has salido mal: {e}")