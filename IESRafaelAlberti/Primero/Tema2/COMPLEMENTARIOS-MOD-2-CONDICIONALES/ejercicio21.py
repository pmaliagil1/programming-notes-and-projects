"""Escribe un programa que dada una hora determinada (horas y minutos), calcule los
segundos que faltan para llegar a la medianoche."""

def calculaHora():
    try:
        hora = int(input("Introduce una hora (0-23): "))
        if hora <0 or hora >23:
            raise ValueError ("HORA NO VÁLIDA")
        minutos = int(input("Introduce los minutos (0-59): "))
        if minutos <0 or minutos > 59:
            raise ValueError ("MINUTOS NO VÁLIDOS")
        
        SEGUNDOS_DIA = 24*60*80
        segundos_transcurridos = (hora*3600)+(minutos*60)
        segundos_restantes = SEGUNDOS_DIA - segundos_transcurridos

        return f"La hora actual es {hora}:{minutos}\nSegundos transcurridos:{segundos_transcurridos}\nSegundos que faltan hasta medianoche: {segundos_restantes}"
    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")

if __name__ == "__main__":
    print(calculaHora())