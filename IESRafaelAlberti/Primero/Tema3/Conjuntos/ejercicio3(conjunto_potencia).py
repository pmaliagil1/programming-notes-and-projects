"""El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.
Por ejemplo, el conjunto potencia de {1,2,3} es:
{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto 
cualquiera s y retorne su «lista potencia» (la lista de todos sus subconjuntos):
>>> conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), 
set([1, 4]), set([6, 1, 4])]
"""


#HAY QUE TERMINARLO
from itertools import combinations

def conjunto_potencia(s):
    s = list(s) #Convertimos a lista para poder indexar
    potencia = []
    #Para cada tamaño posible de subconjunto (0 hasta len(s))
    for r in range(len(s)+1):
        #Generamos todas las combinaciones de tamaño r
        for comb in combinations(s, r):
            potencia.append(set(comb))
    #PARCHE: SE ELIMINA EL CONJUNTO VACIO
    potencia.remove(set())
    return potencia


if __name__ == "__main__":
    try:
        print(conjunto_potencia((1, 2, 3)))
    except Exception as e:
        print(f"Algo ha salido mal: {e}")


"""def conjunto_potencia(s):
    s = list(s)     #convertimos a lista para poder recorrerla
    potencia = [set()]   #Inicializamos resultado con el conjunto vacio

    #Para cada elemento del conjunto original
    for elem in s:
        numeros_subconjuntos = []
        #Recorremos los subconjuntos ya generados
        for subconjunto in potencia:
            #Creamos un nuevo subconjunto añadiendo el elemento actual
            nuevos_subconjuntos.append(subconjunto | {elem})
        #Añadimos los nuevos subconjuntos a la lista potencia
        potencia.extend(nuevos_subconjuntos)

    #PARCHE: SE ELIMINA EL CONJUNTO VACIO
    potencia.remove(set())
    return potencia
"""