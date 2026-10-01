#Ejercicio 13: Crea un subprogama que indique si un número es primo o no lo es.

def esPrimo(n):
    respuesta = True
    if n <=1:
        respuesta = False
    for i in range (2,n):
        if n % i == 0:
            respuesta = False
    if respuesta == True:
        respuesta = "Es primo"
    else:
        respuesta = "No es primo"
    return (respuesta)

if __name__ == "__main__":
    n = int(input("Introduce un número para comprobar si es primo o no: "))
    print(esPrimo(n))