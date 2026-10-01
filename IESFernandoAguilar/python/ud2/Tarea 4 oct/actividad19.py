numero = int(input("Introduce un número entero: "))
if numero < 0:
    print ("El número introducido es negativo, por lo que se usará el valor positivo.")
    numero = abs(numero)
if numero == 0:
    print("El número tiene 1 dígito.")
else:
    contador = 0
    while numero > 0:
        numero = numero // 10
        contador = contador + 1
    print(f"El número introducido tiene {contador} dígitos.")
