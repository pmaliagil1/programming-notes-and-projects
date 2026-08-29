def criba_eratostenes(n):
    """
    Genera una lista de números primos en el rango [0..N] utilizando
    el algoritmo de la Criba de Eratóstenes.
    
    Args:
        n (int): El límite superior del rango.
    
    Returns:
        list: Lista de números primos en el rango [0..N].
    """
    if n < 2:
        return []  # No hay primos menores que 2.

    # Paso 1: Crear una lista para marcar números probablemente primos
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos

    # Paso 2: Iterar desde 2 hasta √n
    for i in range(2, int(n**0.5) + 1):
        if es_primo[i]:  # Si el número actual es primo
            # Marcar todos los múltiplos de i como no primos
            for j in range(i * i, n + 1, i):
                es_primo[j] = False

    # Paso 3: Los índices que aún son True son números primos
    return [i for i in range(n + 1) if es_primo[i]]


# Ejemplo de uso:
if __name__ == "__main__":
    N = int(input("Introduce un número N: "))
    primos = criba_eratostenes(N)
    print(f"Números primos en el rango [0..{N}]: {primos}")
