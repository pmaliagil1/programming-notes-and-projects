total_ahorro = 0
for mes in range (1,13):
    ahorro_mes = float(input(f"Ingrese el ahorro del mes {mes}: "))
    total_ahorro = total_ahorro + ahorro_mes
    print(f"El total de ahorro en todo el año es de: {total_ahorro} €")