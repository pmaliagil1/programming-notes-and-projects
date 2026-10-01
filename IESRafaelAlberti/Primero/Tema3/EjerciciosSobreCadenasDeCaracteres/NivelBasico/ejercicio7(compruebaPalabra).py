#Comprueba que una palabra dada está en una frase.

def compruebaPalabra(frase, palabra):
    comprobante = False
    if palabra.lower() in frase.lower():
        comprobante = True
    return comprobante


if __name__ == "__main__":
    try:
        frase = input("Introduzca una palabra: ")
        palabra = input("Introduzca una palabra: ")

        if compruebaPalabra(frase, palabra):
            print(f"La palabra '{palabra}', está en la frase")
        else:
            print(f"La palabra '{palabra}', NO está en la frase")
  

    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")
