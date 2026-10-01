import random

def genera_lista_ordenada(n, inf, sup):
    lista = [random.randint(inf, sup) for _ in range(n)]
    lista.sort()
    return lista

n = int(input("¿Cuántos números deseas generar? "))
inf = int(input("Introduce el límite inferior: "))
sup = int(input("Introduce el límite superior: "))

lista_ordenada = genera_lista_ordenada(n, inf, sup)
print("\nLista ordenada:", lista_ordenada)
