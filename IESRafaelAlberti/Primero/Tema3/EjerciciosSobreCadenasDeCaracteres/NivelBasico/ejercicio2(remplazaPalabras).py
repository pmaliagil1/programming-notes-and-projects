#Reemplazar palabras enteras dentro de una cadena.

def remplazaPalabras(frase):
    try:                                        #CREO QUE PODRIA HABER USADO UN REPLACE (MIRA DEAJO)
        fraseSeparada = frase.split(" ")
        numero = int(input("Introduce la posicion de la palabra que deseas cambiar: "))
        if numero > len(fraseSeparada) or numero<0:
            raise ValueError("VALOR NO VÁLIDO")
        nuevaPalabra = input("Introduce la palabra que deseas introducir a cambio: ")
        fraseSeparada[numero] = nuevaPalabra
        nuevaFrase = " ".join(fraseSeparada)
        return f"La nueva fase es: {nuevaFrase}"
    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")


if __name__ == "__main__":
    try:
        frase = input("Introduce una frase: ")
        print(remplazaPalabras(frase))

    except ValueError:
        print("Valor no válido.")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")

#OTRA FORMA DE HACERLO!!!!!!
"""texto = "Me gusta programar en Java

try:
    nuevo_texto = texto.replace("Java","Python")
    print(nuevo_texto)
except AtributeError:
    print("Error")"""

