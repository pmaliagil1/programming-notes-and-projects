def potencia(base,exponente):
    if exponente == 0:
        return 1
    return base*potencia(base,exponente-1)


if __name__=="__main__":
    base = int(input())
    exponente = int(input())
    print(potencia(base,exponente))