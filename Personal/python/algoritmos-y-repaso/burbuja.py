"""
Módulo: burbuja.py
Descripción: 
    Aquí está el  algoritmo de la burbuja. Este código nos sirve para 
    ordenar una lista de números de menor a mayor.
"""
# Algoritmo de ordenación burbuja

# Algoritmo de ordenación burbuja
def burbuja (numeros):
    """
    Función que ordena una lista de números.
    
    ¿Cómo funciona?
    Va comparando números de dos en dos y si están al revés (el grande antes que el pequeño),
    los cambia. Esto hace que los números grandes "suban" como burbujas al final de la lista.
    
    
    Parámetros:
    numeros (list): La lista que queremos que quede ordenada.
    
    Retorna:
    Nada. La lista 'numeros' se ordena directamente.
    """
    
    # Este primer bucle es para saber cuántas veces tenemos que revisar la lista.
    # Hacemos una pasada menos que la cantidad total de números.
    for i in range(0,len(numeros) - 1):
        
        # Este segundo bucle es donde se hacen las comparaciones de verdad.
        # Le restamos 'i' porque ya sabemos que los últimos números ya están bien puestos.
        for j in range(0,len(numeros) - 1 -i):
            
            # Si el número de la izquierda (j) es mayor que el de la derecha (j+1)...
            if numeros[j] > numeros[j + 1]:
                
                # Intercambio de elementos si están en orden incorrecto
                # Los cambiamos de sitio para que el pequeño quede primero.
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
    
# PROGRAMA PRINCIPAL
# Esto de aquí abajo es solo para probar que la función funciona bien cuando ejecutamos el archivo.

numeros = [34, 12, 5, 66, 1, 89, 23]
print(numeros)
burbuja(numeros)
print(numeros)