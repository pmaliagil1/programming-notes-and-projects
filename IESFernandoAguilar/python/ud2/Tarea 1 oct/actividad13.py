total_empresa = 0
N = int(input("Ingrese el número de trabajadores: "))
for i in range(N):
    horas_trabajadas = float(input(f"Ingrese el total de horas trabajadas por el trabajador {i + 1}: "))
    tarifa_por_horas = float(input(f"Ingrese la tarifa por hora del trabajador {i + 1}: "))
    sueldo_semanal = horas_trabajadas * tarifa_por_horas
    print (f"Sueldo semanal del trabajador {i + 1}: {sueldo_semanal} €")
    total_empresa = total_empresa + sueldo_semanal
print(f"Total pagado por la empresa a los {N} trabajadores: {total_empresa} €")