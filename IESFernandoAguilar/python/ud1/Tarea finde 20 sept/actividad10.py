numero = float (input ("Ingrese un numero decimal: "))
numero_entero = int(numero)
decimal = numero - numero_entero
redondeo = round (decimal,2)
print ("La parte entera del número proporcionado es ",numero_entero, "y la parte decimal es ",redondeo)