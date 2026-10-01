name = input("Introduce el nombre de la acción: ")
shares = int(input("Introduce la cantidad de acciones: "))
price = float(input("Introduce el precio de la acción (€): "))

print(f"{'Name':>10} {'Shares':>10} {'Price':>10}")
print(f"{'-'*10} {'-'*10} {'-'*10}")

print(f"{name:>10} {shares:>10} {price:10.2f}€")
