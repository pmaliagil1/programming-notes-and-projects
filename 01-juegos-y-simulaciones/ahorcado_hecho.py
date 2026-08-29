from random import choice

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


p_secreta = choice(PALABRAS_SECRETAS)
letras_adivinadas = ["_"] * len(p_secreta)  
intentos_restantes = 6  # Número de intentos permitidos
letras_usadas = []  # Letras que el jugador ya ha intentado

print("¡Bienvenido al juego del Ahorcado!")
print("Adivina la palabra letra por letra o intenta adivinar la palabra completa. Tienes 6 intentos.")

# Bucle principal del juego
while intentos_restantes > 0 and "_" in letras_adivinadas:
    print("\nPalabra:", " ".join(letras_adivinadas))
    print("Intentos restantes:", intentos_restantes)
    print("Letras usadas:", " ".join(sorted(letras_usadas)))

    intento = input("Ingresa una letra o intenta adivinar la palabra completa: ").lower()

    # Verificar si el jugador intenta adivinar la palabra completa
    if len(intento) > 1:
        if intento == p_secreta:
            letras_adivinadas = list(p_secreta)  # Revelar toda la palabra
            break
        else:
            print("La palabra no es correcta.")
            intentos_restantes -= 1
    # Intento de una sola letra
    elif len(intento) == 1:
        if intento in letras_usadas:
            print("Ya usaste esa letra. Intenta con otra.")
            continue

        letras_usadas.append(intento)

        # Comprobar si la letra está en la palabra
        if intento in p_secreta:
            print(f"¡Bien hecho! La letra '{intento}' está en la palabra.")
            for i in range(len(p_secreta)):
                if p_secreta[i] == intento:
                    letras_adivinadas[i] = intento
        else:
            print(f"La letra '{intento}' no está en la palabra.")
            intentos_restantes -= 1
    else:
        print("Por favor, ingresa una letra o intenta adivinar la palabra completa.")

# Fin del juego: verificar si ganó o perdió
if "_" not in letras_adivinadas:
    print("\n¡Felicidades! Adivinaste la palabra:", p_secreta)
else:
    print("\nLo siento, te quedaste sin intentos. La palabra era:", p_secreta)
