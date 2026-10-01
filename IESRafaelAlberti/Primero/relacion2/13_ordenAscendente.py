print("Escriba dos numeros para ser comparados")
n1 = int(input("Introduce un primer numero: "))
n2 = int(input("Introduce un segundo numero: "))
if n1 > n2:
    print(f"El orden de los numeros es {n1}, {n2}")
elif n2 > n1:
    print(f"El orden de los numeros es {n2}, {n1}")
else:
    print(f"Has introducido el mismo numero: {n1}, {n2}")