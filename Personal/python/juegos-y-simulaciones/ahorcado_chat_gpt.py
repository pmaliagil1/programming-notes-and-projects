from random import choice

# Lista de palabras para el juego
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
    print("¡Bienvenido al juego del Ahorcado!")
    seguir = "S"  # Variable para continuar el juego
    ronda = 1

    while seguir.upper() == "S":
        # Seleccionar una palabra secreta y configurar el estado inicial
        p_secreta = choice(PALABRAS_SECRETAS)
        p_oculta = ["_"] * len(p_secreta)
        intentos_restantes = 6
        letras_intentadas = []  # Ahora usamos una lista

        print(f"\nRonda número {ronda}")
        print("Palabra secreta:", " ".join(p_oculta))
        
        # Mientras queden intentos y no se haya adivinado la palabra
        while intentos_restantes > 0 and "_" in p_oculta:
            print(f"\nIntentos restantes: {intentos_restantes}")
            print(f"Letras intentadas: {', '.join(letras_intentadas) if letras_intentadas else 'Ninguna'}")
            letra = input("Ingresa una letra o la palabra completa: ").lower()

            # Validar entrada
            if len(letra) == 1 and letra.isalpha():
                if letra in letras_intentadas:
                    print("Ya intentaste esta letra. Intenta con otra.")
                elif letra in p_secreta:
                    letras_intentadas.append(letra)
                    print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
                    # Actualizar palabra oculta sin usar índices explícitos
                    p_oculta = [
                        letra if char == letra else p_oculta[i]
                        for i, char in enumerate(p_secreta)
                    ]
                else:
                    letras_intentadas.append(letra)
                    print(f"La letra '{letra}' no está en la palabra.")
                    intentos_restantes -= 1
            elif len(letra) == len(p_secreta) and letra.isalpha():
                if letra == p_secreta:
                    print(f"¡Felicidades! Has adivinado la palabra completa: {p_secreta}")
                    p_oculta = list(p_secreta)  # Marca la palabra como adivinada
                else:
                    print("La palabra no es correcta.")
                    intentos_restantes -= 1
            else:
                print("Entrada inválida. Ingresa una sola letra o la palabra completa.")

            # Mostrar el progreso de la palabra oculta
            print("Palabra secreta:", " ".join(p_oculta))
        
        # Resultado de la ronda
        if "_" not in p_oculta:
            print(f"¡Felicidades! Has adivinado la palabra: {p_secreta}")
        else:
            print(f"Lo siento, te quedaste sin intentos. La palabra era: {p_secreta}")

        # Preguntar si se quiere jugar otra ronda
        seguir = input("\n¿Quieres jugar otra ronda? (S/N): ").upper()
        ronda += 1

    print("Gracias por jugar al Ahorcado. ¡Hasta pronto!")

# Punto de entrada del programa
if __name__ == "__main__":
    ahorcado()
