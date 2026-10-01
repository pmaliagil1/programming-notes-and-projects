num = int(input("Ingrese un número: "))
if num % 2 == 0 and num % 5 == 0:
    print ("El número seleccionado es múltiplo de 2 y de 5")
elif num % 2 == 0:
    print ("El número seleccionado es múltiplo de 2.")
elif num % 5 == 0:
    print ("El número seleccionado es múltiplo de 5.")
else:
    print ("Operación no válida")