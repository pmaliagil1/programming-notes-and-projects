"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las 
letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante"""

def eliminaAbedecario():     #MEJOR FORMA DEBAJO
    abecedario = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    abecedario_nuevo = []
    contador = 0
    for letra in abecedario:
        contador +=1
        if contador % 3 != 0:
            abecedario_nuevo.append(letra)
    return abecedario_nuevo

if __name__ == "__main__":
    try:
        print(eliminaAbedecario())
    except Exception as e:
        print(f"Algo ha salido mal: {e}")

"""OTRA FORMA DE HACERLO:
def elimina_inplace():
    letras = list("abcdefghijklmnopqrstuvwxyz")  AL HACER ESTO NO HACE FALTA IR LETRA POR LETRA y queda como char, por lo que puedes usar pop()
    # Empezamos desde el final hasta el principio para evitar el acortamiento de la lista
    for i in range(len(letras), 0, -1):
        if i % 3 == 0:
            letras.pop(i - 1) # i-1 porque el índice es posición - 1
    return letras"""