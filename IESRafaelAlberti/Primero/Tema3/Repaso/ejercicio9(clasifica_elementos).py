"""9. Clasificar elementos
Dada una lista con números repetidos, crea:
• una lista sin duplicados
• una tupla con los duplicados
• un conjunto con los elementos únicos
Pista: necesitarás recorrer la lista y usar estructuras de datos auxiliares."""

def clasificaElementos(numeros):
    vistos = set()
    lista_sin_duplicados = []
    duplicados = set()

    for n in numeros:
        if n in vistos:
            duplicados.add(n)
        else:
            lista_sin_duplicados.append(n)
            vistos.add(n)
    duplicados = tuple(duplicados)
    return duplicados, lista_sin_duplicados, vistos



if __name__ == "__main__":
    try:
        numeros = [1, 2, 2, 3, 4, 4, 4, 5]
        duplicados, lista_sin_duplicados, vistos = clasificaElementos(numeros)
        print(f"Lista sin duplicados: {lista_sin_duplicados}\nTupla con duplicados: {duplicados}\nUnicos: {vistos}")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")