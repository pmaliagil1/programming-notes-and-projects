nota = int(input("Introduce tu nota: "))
match nota:
    case 0| 1 | 2:
        print("Muy deficiente")
    case 3|4:
        print("Insuficiente")
    case 5|6:
        print("Bien")
    case 7|8:
        print("Notable")
    case 9|10:
        print("Sobresaliente")
