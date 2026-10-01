"""3. Tupla: Intercambiar valores
Dada una tupla de dos elementos, realiza una función que devuelva una nueva tupla con los valores
intercambiados. Se supone de longitud 2 siempre
Ejemplo: (10, 20) → (20, 10)
Pista: desempaquetado de estructuras (mirar ejercicios resueltos de clase)."""

def intercambiaValores(tupla):
    a, b = tupla
    nuevaTupla = b, a
    return nuevaTupla
    

if __name__ == "__main__":
    try:
        tupla = (10, 20)
        intercambiaValores(tupla)
        print(f"Tupla: {tupla}\nNueva tupla: {intercambiaValores(tupla)}")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")


"""ESTA BIEN PERO NO ES DESEMPAQUETADO

def intercambiaValores(tupla):
    nuevaTupla = []
    for elemento in tupla[::-1]:
        nuevaTupla.append(elemento)
    nuevaTupla = tuple(nuevaTupla)
    return f"Tupla: {tupla}\nNueva tupla: {nuevaTupla}"""