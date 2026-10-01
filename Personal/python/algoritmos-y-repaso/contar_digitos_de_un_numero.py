def contar_digitos(numero):
    if numero == 0:
        return numero + 0
    return 1 + contar_digitos(numero//10)

if __name__=="__main__":
    numero = int(input())
    print(contar_digitos(numero))