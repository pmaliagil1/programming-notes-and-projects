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


rondas = 1
seguir = "s"
while seguir == "s":
    print(f"Ronda {rondas}")
    print("-----\n")

    p_secreta = choice(PALABRAS_SECRETAS)

cad_oculta = "-"*len(p_secreta)