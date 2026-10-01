nombre = input("Introduce el nombre del trabajador: ")
horas = int(input("Introduce las horas trabajadas: "))
tarifa_hora = int(input("Introduce la tarifa por hora trabajada: "))

bruto = horas * tarifa_hora
print(f"El salario bruto es {bruto}")

if horas > 35:
    horas_trabajadas = horas  # guardas el valor, está bien
    horas = horas - 35
    primeras_horas = 35 * tarifa_hora
    siguientes_horas = horas * (tarifa_hora * 1.5)

    total = primeras_horas + siguientes_horas

    if total > 500:
        primeros_500 = 500
        excedente = total - 500

        if excedente > 400:
            segundos_400 = 400 * 0.75
            resto = (excedente - 400) * 0.55
            total_neto = primeros_500 + segundos_400 + resto
        else:
            total_neto = primeros_500 + (excedente * 0.75)
    else:
        total_neto = total

else:
    total_neto = horas * tarifa_hora

tasas = bruto - total_neto
print(f"Nombre: {nombre}\nSalario neto: {total_neto:.2f}\nTasas: {tasas:.2f}")
