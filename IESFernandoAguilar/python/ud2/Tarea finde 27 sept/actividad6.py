num = int(input("Introduzca un número para ver su tabla de multiplicar: "))
multiplicacion = 1
print(f"Tabla de multiplicar de {num}: ")
while multiplicacion <=10:
    print(f"{num} x {multiplicacion} = {num * multiplicacion}")
    multiplicacion = multiplicacion + 1