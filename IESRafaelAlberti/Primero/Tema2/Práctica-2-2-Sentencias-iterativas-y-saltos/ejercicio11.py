#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a
#una las letras de la palabra introducida empezando por la última.

def desglosaPalabra(palabra):
    for letra in palabra[::-1]:
        print(letra)

if __name__ == "__main__":
    try:
        palabra = input("Introduce una palabra: ")
        desglosaPalabra(palabra)
    except TypeError:
        print("Error de escritura")
    except Exception as e:
        print(f"Error desconocido: {e}")