from random import randint
seguir = False
maximo = 100
minimo = 1
while not seguir:
    numero = randint(minimo,maximo)
    print(f"Creo que el número es: {numero}")
    print("¿He acertado?")
    acertado = input("Escribe la respuesta (si/no): ")
    if acertado == "no":
        pregunta = input("¿Es mayor o menor?: ")
        if pregunta == "mayor":
            minimo = numero
        if pregunta == "menor":
            maximo = numero
        print("Seguire intentando")

    elif acertado == "si":
        print("¡Lo logre!")
        seguir = True
