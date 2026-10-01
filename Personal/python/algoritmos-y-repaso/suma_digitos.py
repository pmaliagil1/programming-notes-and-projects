def suma_digitos(numero):
    if numero == 0:
        return 0
    return numero % 10 + suma_digitos(numero//10)


if __name__=="__main__":
    numero=int(input())
    print(suma_digitos(numero))