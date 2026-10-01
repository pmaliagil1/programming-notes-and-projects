"""16. Dibuja un ordinograma que lea una calificación numérica entre 0 y 10 y la transforma en
calificación alfabética, escribiendo el resultado.
• de 0 a <3 Muy Deficiente.
• de 3 a <5 Insuficiente.
• de 5 a <6 Bien.
• de 6 a <9 Notable
• de 9 a 10 Sobresaliente"""

def transformaCalificacion(nota):
    if nota >=0 and nota <3:
        print("Muy deficiente")
    elif nota >=3 and nota <5:
        print("Insuficiente")
    elif nota >=5 and nota <6:
        print("Bien")
    elif nota >= 6 and nota <9:
        print("Notable")
    elif nota >=9 and nota <11:
        print("Sobresaliente")

if __name__ == "__main__":
    try:
        nota = int(input("Introduce tu calificación: "))
        if nota <0 or nota >10:
            raise ValueError("DEBE ESTAR ENTRE 0 Y 10")
        transformaCalificacion(nota)

    except ValueError:
        print("Valor no válido")
    