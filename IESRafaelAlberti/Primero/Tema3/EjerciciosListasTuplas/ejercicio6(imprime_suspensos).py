"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la 
nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al 
final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que 
repetir. Usa subprogramas cuando consideres de forma justificada. Intenta controlar los 
posibles errores"""

#Esta mejor capturar las notas en una lista y hacerlo mas modular

def eliminaAprobadas():
    suspensos = []
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    for asignatura in asignaturas:
        nota = int(input(f"Introduzca la nota que ha sacado en {asignatura}: "))
        if nota >10 or nota <0:
            raise ValueError ("VALOR NO VALIDO")
        elif nota <5:
            suspensos.append(asignatura)
    return suspensos

def creaResultado(lista_suspensos):
    resultado = ""
    if not lista_suspensos:
        return "Felicidades. Has aprobado todo"
    else:
        for suspenso in lista_suspensos:
            resultado += suspenso+", "
    return f"Te han quedado las siguientes asignaturas: {resultado[:-2]}"




if __name__ == "__main__":
    try:
        lista_suspensos = eliminaAprobadas()
        print(creaResultado(lista_suspensos))

    except ValueError:
        print("Debe ser una nota entre 0 y 10")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")