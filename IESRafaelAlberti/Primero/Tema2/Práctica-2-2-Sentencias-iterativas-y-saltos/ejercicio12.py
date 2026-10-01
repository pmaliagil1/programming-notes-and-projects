#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
#muestre por pantalla el número de veces que aparece la letra en la frase.

def cuentaLetra(frase, letra):
    letras = "abcdefghijklmnopqrstuvwxyz" 
    contador = 0
    if letra.lower() not in letras:
        raise NameError ("No es una letra")
    else:
        for caracter in frase.lower():
            if caracter.lower() == letra.lower():
                contador +=1
        return contador

if __name__ == "__main__":
    try:
        letras = "abcdefghijklmnopqrstuvwxyz" 
        frase = input("Introduzca una frase: ")
        letra = input("Introduzca la letra que desea buscar: ")
        print(cuentaLetra(frase, letra))
    except NameError:
        print("No es una letra")
    except Exception as e:
        print(f"Error desconocido: {e}")