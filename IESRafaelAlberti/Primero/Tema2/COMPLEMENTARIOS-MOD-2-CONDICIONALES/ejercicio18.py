"""Escribe un programa que calcule el salario neto semanal de un trabajador en función del
número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
• Las primeras 35 horas se pagan a tarifa normal.
• Las horas que pasen de 35 se pagan a 1,5 veces la tarifa normal.
• Las tasas de impuestos son:
• Los primeros 500 euros son libres de impuestos.
• Los siguientes 400 tienen un 25% de impuestos.
• Los restantes un 45% de impuestos.
Escribir nombre, salario bruto, tasas y salario neto."""

def calculaSalario():
    nombre = input("Introduzca el nombre del trabajador: ")
    horas = int(input("Introduzca el número de horas trabajadas: "))
    if horas <0:
        raise NameError ("NO PUEDE SER NEGATIVO")
    tarifa = float(input("Introduzca la tarifa por hora: "))
    if tarifa <0:
        raise NameError("NO PUEDE SER NEGATIVO")

    cartera = 0
    if horas < 35:
        cartera = tarifa*horas
        bruto = tarifa*horas
        return f"Nombre: {nombre}\nSalario neto: {cartera}\nBruto: {bruto}\nTarifa:{bruto-cartera}"
    if horas > 35:
        horas = horas -35
        primeras35 = tarifa*35
        cartera = (tarifa*1.5)*horas
        cartera = cartera +primeras35
        bruto = cartera
        if cartera < 500:
            return f"Nombre: {nombre}\nSalario neto: {cartera}\nBruto: {bruto}\nTarifa:{bruto-cartera}"
        if cartera >500:
            primeros500 = 500
            cartera = cartera-500 #cartera -500
            if cartera < 400:
                bruto = cartera+primeros500
                carteraImpuestos = cartera*0.75
                cartera = carteraImpuestos+primeros500
                return f"Nombre: {nombre}\nSalario neto: {cartera}\nBruto: {bruto}\nTarifa:{bruto-cartera}"
            if cartera > 400:
                siguientes400 = 400
                cartera = cartera-400
                bruto = cartera+primeros500+siguientes400
                carteraImpuestos = cartera*0.55
                cartera = carteraImpuestos+primeros500+siguientes400
                return f"Nombre: {nombre}\nSalario neto: {cartera}\nBruto: {bruto}\nTarifa:{bruto-cartera}"

        

if __name__ == "__main__":
    try:
        print(calculaSalario())
    except NameError:
        print("No pueden ser valores negativos")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")
