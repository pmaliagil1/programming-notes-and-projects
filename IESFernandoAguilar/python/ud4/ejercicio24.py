producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto (€): "))
unidades = int(input("Introduce el número de unidades: "))

total = precio * unidades

resultado = f"{producto}: {unidades:5d} unidades x {precio:6.2f}€ = {total:8.2f}€"
print(resultado)
