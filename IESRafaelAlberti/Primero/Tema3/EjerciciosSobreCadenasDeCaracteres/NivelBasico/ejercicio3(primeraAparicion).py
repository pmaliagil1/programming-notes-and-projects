#Buscar la primera aparición de una letra.

def primeraAparicion(frase):     #HACER CON INDEX(MIRA ABAJO)
    contador = 0
    letraElegida = input("Introduce la letra para decir su primera aparicion: ")
    if len(letraElegida) >1:
        raise ValueError ("VALOR NO VÁLIDO")
    for letra in frase:
        if letra.lower()  == letraElegida.lower():
            return f"La letra {letraElegida}, aparece por primera vez en la posición: {contador}"
        contador+=1


if __name__ == "__main__":
    try:
        frase = input("Introduce una frase: ")
        print(primeraAparicion(frase))

    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")


"""cadena ="Bienvenidos al mundo Python"

try:
    posicion = cadena.index("z")
    print(f"Primera "z", en la posicion {posicion}")
    
except ValueError:
    print("Error")
    """