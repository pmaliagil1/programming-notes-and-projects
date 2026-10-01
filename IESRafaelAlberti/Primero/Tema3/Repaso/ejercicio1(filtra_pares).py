"""1. Lista: Filtrar números pares
Dada una lista de números, crea una nueva lista que contenga solo los números pares.
Pista: es una estructura mutable"""

def filtraPares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares


if __name__ == "__main__":
    try:
        numeros = [1,2,3,4,5,6,7,8,9,10]
        print(filtraPares(numeros))
    except Exception as e:
        print(f"Algo ha salido mal: {e}")