numero = int (input("Introduce un entero positivo: "))
if numero >= 0:
    suma = ((numero * (numero + 1)) // 2)
    print ("El resultado de la suma de todos los numeros hasta el seleccionado es", suma)
else:
    print ("No es un entero positivo")
