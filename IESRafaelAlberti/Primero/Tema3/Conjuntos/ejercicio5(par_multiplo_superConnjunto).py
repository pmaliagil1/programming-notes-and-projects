"""Dado el conjunto de números enteros:
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
1. Crea un conjunto pares que contenga los números pares del conjunto numeros.
2. Crea un conjunto multiplos_de_tres que contenga los números que son 
múltiplos de tres del conjunto numeros.
3. Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y 
guárdala en un conjunto llamado pares_y_multiplos_de_tres.
4. Indica si el conjunto números es un superconjunto de pares."""

def pares(numeros):
    pares = set()
    for numero in numeros:
        if numero % 2 == 0:
            pares.add(numero)
    return pares

def multiploTres(numeros):
    multiplo_de_tres = set()
    for numero in numeros:
        if numero % 3 == 0:
            multiplo_de_tres.add(numero)
    return multiplo_de_tres
    
def conjunto(par, multiplo_tres, numeros):
    pares_y_multiplo_tres = par.intersection(multiplo_tres)
    es_super = numeros.issuperset(par)
    return f"Pares: {par}\nMultiplo de tres:{multiplo_tres}\nInterseccion:{pares_y_multiplo_tres}\nSuper:{es_super}"


if __name__ == "__main__":
    try:
        numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        par = pares(numeros)
        multiplo_tres = multiploTres(numeros)
        print(conjunto(par, multiplo_tres, numeros))
    except Exception as e:
        print(f"Algo ha salido mal: {e}")