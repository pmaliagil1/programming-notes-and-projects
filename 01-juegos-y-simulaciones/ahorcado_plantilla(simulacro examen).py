from random import choice
MAX_INTENTOS = 6

PALABRAS_SECRETAS = (
    "pizza", "hamburguesa", "espaguetis", "sushi", "taco",
    "burrito", "ensalada", "sopa", "lasagna", "empanada",
    "croqueta", "arroz", "paella", "tortilla", "ceviche",
    "falafel", "hummus", "quesadilla", "tarta", "pastel",
    "chocolate", "fresa", "manzana", "banano", "sandía",
    "mango", "naranja", "papaya", "limon",
    "melocoton", "aguacate", "berenjena", "calabacin", "zanahoria",
    "brocoli", "pepino", "pimiento", "ajo",
    "tomate", "cebolla", "patata", "pollo", "cerdo",
    "ternera", "salchicha", "chorizo", "jamon", "queso",
    "yogur", "helado", "bizcocho", "galleta", "caramelo",
    "macarrones", "ravioli", "lasaña", "sandwich", "panqueque"
)



# Palabras iniciales
print("¡Bienvenido al juego del Ahorcado!")
print("¡Tu objetivo es adivinar la palabra secreta, ya sea letra por letra o en su totalidad.")
print("Cada vez que aciertes, la letra o la palabra completa se revelarán")
print(f"Pero ten cuidado: si te equivocas, perderás una oportunidad. Tienes un máximo de {MAX_INTENTOS} intentos.")
print("¡Mucha suerte, y que comience el desafío!")
print("----------------------------------------")


# Bucle rondas
ronda = 1
seguir = "s"
while seguir == "s":
    print(f"Ronda {ronda}")
    print("-----\n")

    p_secreta = choice(PALABRAS_SECRETAS)
    print(p_secreta)

    """cad_oculta = ""
    for _ in range(len(p_secreta)):
        cad_oculta += "-"""
    # Más fácil:
    cad_oculta = "-" * len(p_secreta)

    # Bucle intentos dentro de una ronda
    acertada = False
    intentos = 1
    while intentos <= MAX_INTENTOS and not acertada:
        entrada = input("Ingresa una letra o la palabra a adivinar: ")

        # Si la entrada es una LETRA la busca en la p_secreta y crea cad_oculta con letra revelada
        if len(entrada) == 1:
            posicion = 0
            while posicion != -1:
                posicion = p_secreta.find(entrada, posicion)
                if posicion != -1:
                    cad_oculta = cad_oculta[:posicion] + entrada + cad_oculta[posicion+1:]
                    posicion += 1

            if cad_oculta == p_secreta: # Acertada
                acertada = True     # No hace falta un continue, ya no va a entrar en los demás if
            else:
                print(f"Intento {intentos}: {cad_oculta}\n")
                intentos += 1
        
        elif entrada == p_secreta:
            acertada = True     # No hace falta un continue, ya no va a entrar en los demás if
        # Si la entrada es una PALABRA y no es acertada
        else:
            print(f"No es esa la palabra secreta. Llevas {intentos} intentos: {cad_oculta}\n")
            intentos += 1

    if acertada:
        print(f"Enhorabuena!! Adivinaste en {intentos} intentos")
    else:
        print(f"Se te han agotado los intentos. La palabra secreta era: {p_secreta}")
    
    # Hacer Bucle control de errores
    while True:
        seguir = input("¿Quieres volver a jugar s/n? ")
        if seguir == "s" or seguir == "n":
            break

    # Otra forma:
    """seguir = "*"
    while seguir not in ["s", "n"]:
        seguir = input("¿Quieres volver a jugar s/n? ")

    ronda += 1"""

# Estadisticas