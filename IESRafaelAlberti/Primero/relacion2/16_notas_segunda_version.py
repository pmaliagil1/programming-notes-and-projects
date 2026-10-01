nota = int(input("Introduce tu nota: "))
if nota < 3 and nota >=0:
    print("Muy deficiente")
elif nota >=3 and nota < 5:
    print("Insuficiente")
elif nota >=5 and nota <6:
    print("Bien")
elif nota >=6 and nota <9:
    print("Notable")
elif nota >=9 and nota <= 10:
    print("Sobresaliente")