import math

N = int(input("Introduce la cantidad de números primos que quieres que se muestre por pantalla: "))

contador = 0
numero = 2

while contador < N:
    es_primo = True

    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo :
        print (numero, end= " ")
        contador = contador + 1
    numero = numero + 1
    