"""2. Lista: Eliminar duplicados manteniendo el orden
Escribe una función que reciba una lista y devuelva otra sin elementos repetidos, respetando el
orden original.
Pista: usa una lista auxiliar y comprueba si un elemento ya está incluido."""

def eliminaDuplicados(lista):
    auxiliar = []
    for elemento in lista:
        if elemento not in auxiliar:
            auxiliar.append(elemento)
    return auxiliar

if __name__ == "__main__":
    try:
        lista = ["platano", "manzana", "platano" ,"pera", "piña", "platano", "pera"]
        eliminaDuplicados(lista)
        print(f"Lista original: {lista}\nLista sin repetidos: {eliminaDuplicados(lista)}")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")
