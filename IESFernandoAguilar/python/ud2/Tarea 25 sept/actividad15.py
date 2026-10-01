tipo = (input("Ingrese el tipo de uva (A o B): "))
tamaño = int(input("Ingrese el tamaño de uva (1 o 2): "))
precio = int(input("Ingrese el precio inicial por kg de uva: "))
peso = float (input("Ingrese el peso de las uvas en kg: "))
carga_precio = 0
if tipo == "A":
    if tamaño == 1:
        carga_precio = 0.20
    elif tamaño == 2:
        carga_precio = 0.30
elif tipo == "B":
    if tamaño == 1:
        carga_precio = -0.30
    elif tamaño == 2:
        carga_precio = -0.50
precio_final = precio + carga_precio
ganancia_total = precio_final * peso
print(f"El precio final por kg es de: {precio_final} euros.")
print(f"La ganancia total por {peso} kg de uva es de: {ganancia_total}")
             
