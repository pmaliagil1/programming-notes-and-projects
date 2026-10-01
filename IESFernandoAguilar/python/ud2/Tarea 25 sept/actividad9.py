base = float(input("Introduzca un número como base: "))
exponente = float (input("Introduzca un número como exponente: "))
if exponente > 0:
    print(f"El resultado es: {base**exponente}")
elif exponente == 0:
    print(f"El resultado es: {base**0}")
elif exponente < 0:
    print(f"El resultado es: {1/(base**-exponente)}")
