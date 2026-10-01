limite_inferior = int(input("Introduzca el límite inferior: "))
limite_superior = int(input("Introduzca el límite superior"))
while limite_inferior >= limite_superior:
    print("El limite inferior debe ser menor al limite superior. Vuelva a introducir los valores.")
    limite_inferior = int(input("Introduzca el límite inferior: "))
    limite_superior = int(input("Introduzca el límite superior"))
suma_intervalo = 0
numeros_fuera = 0
limite_igual = 0
numero = int(input("Introduce un número (0 para terminar): "))
while numero != 0:
    if limite_inferior < numero < limite_inferior:
        suma_intervalo = suma_intervalo + numero
    else: 
        numeros_fuera = numeros_fuera + 1
    if numero == limite_inferior or numero == limite_superior:
        limite_igual = limite_igual + 1
    numero = int(input("Introduce un número (0 para terminar): "))
print("Resultados: ")
print(f"Suma de los números dentro del intervalo ({limite_inferior,limite_superior}):{suma_intervalo}")
print(f"Números fuera del intervalo: {numeros_fuera}")
if limite_igual > 0:
    print("Se ha introducido un número igual a uno de los límites del intervalo.")
else:
    print("No se han introducido ningún número igual a los límites del intervalo.")




#corrección clase



inferior = int(input("Introduce el limite inferior: "))

#Con bucle infinito y break
while True:
    superior = int(input("Introduce el limite superior: "))
    if superior > inferior:
        break
    print("El limite superior es incorrecto")

print(f"\nIntervalo: [{inferior}, {superior}]")

suma_intervalo = 0
fuera_intervalo = 0
limite_intervalo = False
numero = -1

#Sin bucle infinito. Bucle con condición de salida
while numero != 0:
        numero = int(input("Introduce cualquier número: "))
        if numero != 0:
            if inferior < numero < superior:
                suma_intervalo += numero
            elif numero == inferior or numero == superior:
                limite_intervalo = True
            else:
                fuera_intervalo += 1
          
print(f"\nLa suma de los números que están dentro del intervalo es {suma_intervalo}")
print(f"Hay {fuera_intervalo} numeros fuera del intervalo")
if limite_intervalo:
     en_limite = "Si"
else:
     en_limite = "No"
print(f"{en_limite} se han introducido numeros iguales a los limites del intervalo")