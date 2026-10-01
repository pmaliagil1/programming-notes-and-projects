"""""Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la 
frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el 
carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la 
posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se 
encontró y finalizar la ejecución."""

def buscaLetra(frase, letra):
    i = 0
    for caracter in frase:
        i += 1      #Con esto puedo saber la posición
        if caracter.lower() == letra.lower():
            print(f"La letra {letra} fue encontrada en la posicion {i}")
        elif caracter != letra:
            print(f"La letra {letra} no está en la posición {i}")

if __name__ == "__main__":
    try:
        frase = input("Introduce una frase: ")
        letra = input("Introduce una letra: ")

        buscaLetra(frase, letra)
    except TypeError:
        print("Carácter no válido")
    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Error desconocido: {e}")