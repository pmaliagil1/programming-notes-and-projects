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


def ahorcado():
    print("Bienvenido al juego del ahorcado")
    palabra_secreta = choice(PALABRAS_SECRETAS)
    palabra_oculta = list("_" * len(palabra_secreta))  # Representación de la palabra oculta como lista
    intentos = 0
    letras_intentadas = []

    while "_" in palabra_oculta:
        print(f"\nIntento {intentos + 1}: {''.join(palabra_oculta)}")
        entrada = input("Ingresa una palabra o una letra para adivinar: ").strip().lower()
        intentos += 1

        if len(entrada) > 1:  # Comprobamos si es una palabra
            if entrada == palabra_secreta:
                print(f"\n¡Enhorabuena! Has adivinado la palabra '{palabra_secreta}' en {intentos} intentos.")
                return
            else:
                print(f"Has fallado. La palabra '{entrada}' no es correcta.")
                continue

        if len(entrada) == 1 and entrada.isalpha():  # Comprobamos si es una letra
            if entrada in letras_intentadas:
                print("Ya intentaste esta letra. ¡Inténtalo de nuevo!")
                intentos -= 1  # No penalizamos este intento
                continue

            letras_intentadas.append(entrada)

            if entrada in palabra_secreta:
                print(f"¡Bien hecho! La letra '{entrada}' está en la palabra.")
                # Reemplazamos los guiones bajos con la letra correcta
                for i in range(len(palabra_secreta)):
                    if palabra_secreta[i] == entrada:
                        palabra_oculta[i] = entrada
            else:
                print(f"La letra '{entrada}' no está en la palabra.")
        else:
            print("Entrada no válida. Por favor, ingresa una letra o una palabra válida.")

    print(f"\n¡Felicidades! Adivinaste la palabra '{palabra_secreta}' en {intentos} intentos.")


if __name__ == "__main__":
    ahorcado()
