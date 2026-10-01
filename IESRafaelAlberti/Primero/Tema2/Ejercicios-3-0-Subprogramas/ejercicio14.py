#Ejercicio 14: Utilizando el ejercicio anterior, indica los divisores del número. 
import ejercicio13
def tieneDivisores():
    divisores = []
    if ejercicio13.esPrimo(n) == "Es primo":
        respuesta = "No tiene divisores"
    elif ejercicio13.esPrimo(n) == "No es primo":
        respuesta = "Los divisores son: "
    if respuesta == "Los divisores son: ":
        for i in range(2, n):
            if n % i == 0:
                divisores.append(i)
    if divisores == []:
        divisores = "No hay divisores, es primo"
    return divisores


if __name__ == "__main__":
    
    n = int(input("Introduce un número para comprobar si es primo o no: "))
    print(tieneDivisores())