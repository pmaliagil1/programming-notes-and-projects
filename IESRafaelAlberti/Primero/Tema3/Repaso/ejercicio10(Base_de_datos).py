"""10. Base de datos simple
Crea un programa que gestione un diccionario donde:
• la clave sea el nombre de un alumno 
• el valor sea una lista con tres notas 
El programa debe:
1. Añadir alumnos 
2. Mostrar la media de cada uno usando funciones 
3. Mostrar el conjunto de todas las notas distintas que han sacado todos los alumnos 
Pista: combina diccionarios, listas y conjuntos"""

#USA ESTO
"""
def agregar_alumno(alumnos):
    nombre = input("Nombre del alumno: ")
    notas=[]

    for i in range(1, 4):
        nota = float(input(f"Nota {i}: "))
        notas.append(nota)

    alumnos[nombre] = notas
    print(f"Alumno: '{nombre}' añadido\n")"""

def calculaMedia(notas):
    return sum(notas) / len(notas)

def gestionaAcademia():
    academia = {}

    #Añadir alumnos
    academia["Pepe"] = [5, 7, 8]
    academia["Maria"] = [9, 10, 9]
    academia["Juan"] = [5, 4, 5]

    #Mostrar medias
    for nombre, notas in academia.items():
        media = calculaMedia(notas)
        print(f"Alumno: {nombre} - Media: {media:.2f}")

    #Mostrar notas distintas
    notas_totales = set()
    for nota in academia.values():
        notas_totales.update(nota)
    
    print(f"Todas las notas distintas conseguidas: {notas_totales}")


if __name__ == "__main__":
    try:
        gestionaAcademia()
    except Exception as e:
        print(f"Algo ha salido mal: {e}")