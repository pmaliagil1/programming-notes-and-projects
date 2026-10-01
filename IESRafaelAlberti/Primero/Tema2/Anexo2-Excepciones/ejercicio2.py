#Escribir un programa que pida al usuario un número entero positivo y
# muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

try:
    numero = int(input("Introduce un entero positivo: "))
except ValueError:
    print("Valor no válido")
except TypeError:
    print("El tipo de dato no es correcto")
else:
    cadena = ""
    for i in range(1,numero+1):
        if (i%2!=0):
            cadena = cadena+str(i)+","
    print(cadena[:-1])