total_empresa = 0
N = int(input("Ingrese el número de trabajadores: "))

for i in range(N):
    horas_diarias = [] 
    for dia in range(1, 8): 
        horas_dia = float(input(f"Ingrese las horas trabajadas el día {dia} por el trabajador {i + 1}: "))
        horas_diarias.append(horas_dia) 
    tarifa_por_hora = float(input(f"Ingrese la tarifa por hora del trabajador {i + 1}: "))
    sueldo_semanal = sum(horas_diarias) * tarifa_por_hora
    
    print(f"Sueldo semanal del trabajador {i + 1}: {sueldo_semanal:.2f} unidades monetarias")
    total_empresa += sueldo_semanal

print(f"\nTotal pagado por la empresa a los {N} trabajadores: {total_empresa:.2f} unidades monetarias")