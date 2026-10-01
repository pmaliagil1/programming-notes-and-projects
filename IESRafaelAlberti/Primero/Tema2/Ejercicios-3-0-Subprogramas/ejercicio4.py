#Ejercicio 4: Indicar si un número es par

def numeroPar(numero):
    respuesta = False
    if numero%2 == 0:
        respuesta = True
    else:
        respuesta = False
    return (respuesta)

if __name__ =="__main__":

    numero = int(input("Introduce un número: "))
    print(numeroPar(numero))