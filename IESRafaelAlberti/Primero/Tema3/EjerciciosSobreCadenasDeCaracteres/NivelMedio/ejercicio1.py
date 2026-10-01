"""Escribe un bucle while que comience con el último carácter en la cadena y haga un
recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en
una línea independiente."""

#EJERCICIO NO TERMINADO

def imprimeDelReves(frase):                     #USAR METODO REVERSE
    # 1. Empezamos en el índice del último carácter
    indice = len(frase) - 1
    
    # 2. Mientras el índice sea 0 o más...
    while indice >= 0:
        # 3. Imprimimos el carácter en esa posición
        print(frase[indice])
        
        # 4. Restamos 1 para movernos al carácter anterior
        indice = indice - 1

if __name__ == "__main__":
    try:
        frase = input("Introduce una frase: ")
        imprimeDelReves(frase)
    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal {e}")


"""cadena = 'hola'
i = len(cadena)-1
while i>=0:
    print(cadena[i])
    i = i-1"""
