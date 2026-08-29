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
    palabra_secreta = choice(PALABRAS_SECRETAS)
    palabra_oculta = list("_"*len(palabra_secreta))
    intentos = 0
    fallos = 0
    letras_intentadas = []
    print("Bienvenido al juego del ahorcado")
    while "_" in palabra_oculta:
        print(AHORCADO[fallos])
        print(f"Ronda: {intentos +1 }, palabra: {" ".join(palabra_oculta)}")
        letra_jugador = input("Introduzca una letra o palabra para adivinar: ").strip().lower()
        intentos +=1

        if len(letra_jugador) > 1:
            if letra_jugador == palabra_secreta:
                print("¡Felicidades has ganado!")
                break
            else:
                print("Has fallado, vuelve a intentarlo.")
                fallos += 1
                intentos += 1
                continue
        elif len(letra_jugador) == 1 and letra_jugador.isalpha():
            if letra_jugador in letras_intentadas:
                print("Esta letra ya ha sido intentada")
                intentos -=1
                continue

            letras_intentadas.append(letra_jugador)

            if letra_jugador in palabra_secreta:
                print("Felicidades, has acertado la letra")
                for i in range (len(palabra_secreta)):
                    if palabra_secreta[i] == letra_jugador:
                        palabra_oculta[i] = letra_jugador

            else:
                print(f"La letra {letra_jugador} no esta en la palabra oculta {palabra_oculta}")
                fallos += 1
                continue
        else:
            print("Entrada no valida, intentelo de nuevo")
            continue
    print(f"Enhorabuena, has adivinado la palabra {palabra_secreta} en {intentos} intentos, has tenido {fallos} fallos")

if __name__ == "__main__":
    ahorcado()
                    
            
