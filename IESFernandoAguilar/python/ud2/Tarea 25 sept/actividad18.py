resultado = int(input("Introduce el resultado del dado (del 1 al 6): "))

if resultado < 1 or resultado > 6:
    print("Dato no válido")
else:
    if resultado == 1:
        cara_contraria = "seis"
    elif resultado == 2:
        cara_contraria = "cinco"
    elif resultado == 3:
        cara_contraria = "cuatro"
    elif resultado == 4:
        cara_contraria = "tres"
    elif resultado == 5:
        cara_contraria = "dos"
    elif resultado == 6:
        cara_contraria = "uno"
    print(f"La cara opuesta a {resultado} es {cara_contraria}.")