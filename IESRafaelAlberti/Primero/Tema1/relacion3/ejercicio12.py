valorA = int(input("Introduce un valor por pantalla: "))
valorB = int(input("Introdue un segundo valor por pantalla: "))

resultado = 1

if valorB == 0:
    resultado = 1
elif valorB > 0:
    for i in range (valorB):
        resultado = resultado *valorA
else:
    for i in range (valorB):
        resultado = resultado * valorA
        resultado = 1 / resultado
print(f"El resultado es: {resultado}")