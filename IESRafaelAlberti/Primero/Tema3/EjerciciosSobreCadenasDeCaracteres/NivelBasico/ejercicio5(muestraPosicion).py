#Mostrar la posición que ocupa cada letra dentro de la cadena.

def muestraPosicion(frase):
    contador = 0
    for letra in frase:
        if letra != " ":
            print(f"{letra}: {contador}")
        contador +=1

if __name__ == "__main__":
    try:
        frase = input("Introduce una frase: ")
        muestraPosicion(frase)

    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")
