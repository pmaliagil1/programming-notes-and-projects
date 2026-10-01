#Diseña un programa que permita contar vocales en una frase.


def cuentaVocales(frase):
    VOCALES = ("a,e,i,o,u,,á,é,í,ó,ú,A,E,I,O,U,Á,É,Í,Ó,Ú")
    contador = 0
    for letra in frase:
        if letra in VOCALES:
            contador +=1
    return f"Hay un total de {contador} vocales en la frase introducida"



if __name__ == "__main__":
    try:
        frase = input("Introduzca una frase: ")
        print(cuentaVocales(frase))

    except ValueError:
        print("Dato no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")