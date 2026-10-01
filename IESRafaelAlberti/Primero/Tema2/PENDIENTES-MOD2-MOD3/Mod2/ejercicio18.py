"""Dibuja un ordinograma que calcula el salario neto semanal de un trabajador en función del
número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
• Las primeras 35 horas se pagan a tarifa normal.
• Las horas que pasen de 35 se pagan a 1,5 veces la tarifa normal.
• Las tasas de impuestos son:
• Los primeros 500 euros son libres de impuestos.
• Los siguientes 400 tienen un 25% de impuestos.
• Los restantes un 45% de impuestos.
 Escribir nombre, salario bruto, tasas y salario neto."""

#CREO QUE ESTA MAL MIRA DEBAJO LA CORRECION
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


#CORRECCION 

def calculaSalario():
    try:
        nombre = input("Introduzca el nombre del trabajador: ")
        
        horas = int(input("Introduzca el número de horas trabajadas: "))
        if horas < 0:
            raise ValueError("Las horas trabajadas no pueden ser negativas.")
            
        tarifa = float(input("Introduzca la tarifa por hora: "))
        if tarifa < 0:
            raise ValueError("La tarifa por hora no puede ser negativa.")
            
    except ValueError as e:
        print(f"Error de entrada: {e}")
        return None

    if horas <= 35:
        salario_bruto = tarifa * horas
    
    else:
        horas_normales = 35
        horas_extra = horas - horas_normales
        
        bruto_normal = tarifa * horas_normales
        bruto_extra = (tarifa * 1.5) * horas_extra
        
        salario_bruto = bruto_normal + bruto_extra
        
    salario_neto = salario_bruto
    impuesto_total = 0
        
    monto_imponible = salario_bruto
    
    if monto_imponible > 500:
        monto_sujeto_a_tramos2y3 = monto_imponible - 500
        
        TRAMO2_LIMITE = 400
        TASA_TRAMO2 = 0.25
        
        if monto_sujeto_a_tramos2y3 > TRAMO2_LIMITE:
            impuesto_tramo2 = TRAMO2_LIMITE * TASA_TRAMO2
            impuesto_total += impuesto_tramo2
            
            monto_restante = monto_sujeto_a_tramos2y3 - TRAMO2_LIMITE
            TASA_TRAMO3 = 0.45
            
            impuesto_tramo3 = monto_restante * TASA_TRAMO3
            impuesto_total += impuesto_tramo3
            
        else:
            impuesto_tramo2 = monto_sujeto_a_tramos2y3 * TASA_TRAMO2
            impuesto_total += impuesto_tramo2
            
    salario_neto = salario_bruto - impuesto_total
    
    return (
        f"--- Recibo Semanal ---\n"
        f"Nombre: {nombre}\n"
        f"Salario Bruto: {salario_bruto:.2f} €\n"
        f"Tasas de Impuestos (Retención): {impuesto_total:.2f} €\n"
        f"Salario Neto: {salario_neto:.2f} €"
    )

if __name__ == "__main__":
    resultado = calculaSalario()
    if resultado:
        print(resultado)