"""Tienes este código:
palabra = 'banana'
contador = 0
for letra in palabra:
 if letra == 'a':
 contador = contador + 1
print(contador)
Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda
aceptar una cadena y una letra como argumentos. De tal forma que pueda hacer la
siguiente llamada:
numero_de_os = cuenta("consuelo","o") # Resultado debe ser 2
"""

def cuenta(palabra, letra):
    contador = 0
    for caracter in palabra:      #En vez de usar un bucle puedo usar .count()
        if caracter == letra:
            contador = contador + 1
    print(contador)

if __name__ =="__main__":
    try:
        palabra = input("Introduzca una palabra: ")
        letra = input("Introduzca una letra: ")
        if len(letra) >1:
            raise ValueError ("DEBE SER UNA SOLA LETRA")
        cuenta(palabra, letra)

    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")