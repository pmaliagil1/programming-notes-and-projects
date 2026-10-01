"""Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre
del mes."""

def cambiaMes(meses):
    try:
        dia,mes,año = input("Introduce una fecha (dd/mm/aaaa): ").split("/")
        if int(dia) <1 or int(dia)>31:
            raise ValueError ("VALOR NO VÁLIDO")
        if int(mes)<1 or int(mes)>12:
            raise ValueError ("VALOR NO VÁLIDO")
        print(f"{dia} de {meses[mes]} de {año}")

    except ValueError:
        print("Valor no válido")
    

if __name__ == "__main__":
    try:
        meses = {
            '01': 'Enero',
            '02': 'Febrero',
            '03': 'Marzo',
            '04': 'Abril',
            '05': 'Mayo',
            '06': 'Junio',
            '07': 'Julio',
            '08': 'Agosto',
            '09': 'Septiembre',
            '10': 'Octubre',
            '11': 'Noviembre',
            '12': 'Diciembre'
        }

        cambiaMes(meses)
    
    except Exception as e:
        print(f"Algo ha salido mal: {e}")