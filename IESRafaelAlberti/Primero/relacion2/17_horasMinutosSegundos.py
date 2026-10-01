horas = int(input("Introduce las horas: "))
minutos = int(input("Introduce los minutos: "))
segundos = int(input("Introduce los segundos: "))

segundos = segundos + 1

if segundos ==  60:
    minutos = minutos + 1
    segundos =0
elif minutos == 60:
    horas = horas + 1
    minutos = 0
elif horas == 24:
    horas =0
    minutos=0
    segundos=0
print(f"Horas:{horas} \nMinutos:{minutos} \nSegundos:{segundos}")