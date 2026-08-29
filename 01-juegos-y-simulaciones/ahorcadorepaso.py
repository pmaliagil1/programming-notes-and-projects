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
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

def ahorcado():
    print("Bienvenido al juego del ahorcado")
    palabra_secreta = choice(PALABRAS_SECRETAS)
    palabra_oculta = list("_" * len(palabra_secreta))  # Convertimos a lista
    intentos = 0
    fallos = 0
    letras_intentadas = []

    while "_" in palabra_oculta:
        print(AHORCADO[fallos])
        print(f"Intento {intentos + 1}, palabra: {''.join(palabra_oculta)}")
        entrada = input("Introduce una letra o palabra para adivinar: ").strip().lower()
        intentos += 1


        if len(entrada) > 1:  # Si el jugador introduce una palabra
            if entrada == palabra_secreta:
                print(f"¡Felicidades! Has acertado la palabra '{palabra_secreta}' en {intentos} intentos.")
                return
            else:
                print("Has fallado, inténtalo de nuevo.")
                fallos +=1
                continue

        if len(entrada) == 1 and entrada.isalpha():  # Si el jugador introduce una letra
            if entrada in letras_intentadas:
                print("Esta letra ya ha sido intentada, prueba otra.")
                intentos -= 1  # No penalizamos este intento
                continue

            letras_intentadas.append(entrada)

            if entrada in palabra_secreta:
                print(f"¡Bien hecho! La letra '{entrada}' está en la palabra secreta.")
                for i in range(len(palabra_secreta)):
                    if palabra_secreta[i] == entrada:
                        palabra_oculta[i] = entrada
            else:
                print(f"La letra '{entrada}' no está en la palabra oculta.")
                fallos +=1
        else:
            print("Entrada no válida, inténtalo de nuevo.")

    print(f"¡Enhorabuena! Has adivinado la palabra '{palabra_secreta}' en {intentos} intentos.")

if __name__ == "__main__":
    ahorcado()
