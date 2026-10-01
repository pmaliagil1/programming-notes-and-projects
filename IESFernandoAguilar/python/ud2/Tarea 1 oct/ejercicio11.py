total_horas = 0
for dia in range (0,7):
    horas_dia = float(input(f"Igrese las horas trabajadas el dia {dia}: "))
    total_horas = total_horas + horas_dia

tarifa_por_hora = float(input("Ingrese la tarifa por hora del empleado: "))
sueldo = total_horas * tarifa_por_hora
print(f"Total de horas trabajadas en la semana: {total_horas} horas.")
print(f"Sueldo total: {sueldo}€")