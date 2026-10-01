positivos = []
negativos = []
while True:
    n = int(input("Introduce un numero (0 para terminar): "))
    if n >0 : 
        positivos.append(n)
    elif n <0 :
        negativos.append(n)
    else:
        print(f"Negativos: {negativos} \nPositivos: {positivos}")
        break
        