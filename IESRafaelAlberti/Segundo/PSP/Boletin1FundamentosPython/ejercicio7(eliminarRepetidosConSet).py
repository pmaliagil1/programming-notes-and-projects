"""7. Control de Duplicados (Conjuntos / Sets): Escribe un programa que reciba una
lista con elementos repetidos (ej. ["python", "java", "c", "python", "java"]) y
devuelva una lista con los elementos únicos manteniendo el uso de set."""

def eliminaRepetidos(lista):
    elementos_unicos = set(lista)
    return list(elementos_unicos)
    

if __name__ == "__main__":
    lista = ["python", "java", "c", "python", "java"]
    print(eliminaRepetidos(lista))