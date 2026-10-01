"""4. Tupla: Máximo y mínimo
Dada una tupla de números, devuelve una tupla nueva con el mínimo y el máximo.
Pista: existen funciones primitivas en python como min() y max().
"""

def MaxMin(numeros):
    maximo = max(numeros)
    minimo = min(numeros)
    return maximo, minimo

if __name__ == "__main__":
    try:
        numeros = (20,44,34,182,3445,1,23)
        max_val, min_val = MaxMin(numeros)
        print(f"Maximo: {max_val}\nMinimo: {min_val}")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")