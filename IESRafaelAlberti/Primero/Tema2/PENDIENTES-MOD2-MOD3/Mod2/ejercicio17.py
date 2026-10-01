"""Dibuja un ordinograma que recibe como datos de entrada una hora expresada en horas,
minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán,
transcurrido un segundo."""

def calculaHoras():
    hora,minuto,segundo = input("Introduce la hora, minutos y segundos separados por : (h:m:s): ").split(":")
    hora = int(hora)
    minuto = int(minuto)
    segundo = int(segundo)

    if hora >23 or hora <0:
        raise ValueError ("DATO NO VÁLIDO")
    elif minuto > 59 or minuto <0:
        raise ValueError ("DATO NO VÁLIDO")
    elif segundo >59 or segundo<0:
        raise ValueError ("DATO NO VÁLIDO")

    segundo = segundo+1
    if segundo==60:
        segundo = 0
        minuto = minuto+1
    if minuto == 60:
        minuto = 0
        hora = hora+1
    if hora == 24:
        hora = 0
        minuto=0
        segundo=0
    return f"La hora tras un segundo es {hora}:{minuto}:{segundo}"

if __name__ == "__main__":
    try:
        print(calculaHoras())
    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")