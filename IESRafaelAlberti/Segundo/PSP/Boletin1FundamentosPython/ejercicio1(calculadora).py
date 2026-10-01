"""1. Calculadora Básica con Entradas: Crea un programa que pida dos números al
usuario e imprima su suma, resta, mulAplicación y división de forma formateada."""

def calculadora(operacion,n1,n2):
    if operacion == 1:
        return n1+n2
    elif operacion == 2:
        return n1-n2
    elif operacion == 3:
        return n1*n2
    elif operacion == 4:
        return n1//n2
    else:
        print("Numero no valido")

if __name__ == "__main__":
    operacion = 0
    while operacion != 1 and operacion!=2 and operacion !=3 and operacion!=4:
        operacion = int(input("Introduce la operacion deseada:\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n"))
    n1 = int(input("Introduzca el primer numero: "))
    n2 = int(input("Introduzca el segundo numero: "))
    print(calculadora(operacion,n1,n2))