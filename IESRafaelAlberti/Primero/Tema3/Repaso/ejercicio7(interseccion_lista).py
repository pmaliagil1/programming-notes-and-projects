"""7. Conjuntos: Intersección de listas
Dadas dos listas, obtén un conjunto con los elementos que aparecen en ambas.
Pista: convierte las listas en conjuntos y usa &."""

def interseccionLista(lista1, lista2):
    set_a = set(lista1)
    set_b = set(lista2)
    #conjunto = set_a.intersection(set_b)
    conjunto = set_a&set_b
    return conjunto

if __name__ == "__main__":
    try:
        L1 = [1, 2, 3, 4, 5, 5] # Nota que hay un 5 repetido
        L2 = [4, 5, 6, 7, 8]
        print(f"{L1}\n{L2}\n{interseccionLista(L1,L2)}")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")