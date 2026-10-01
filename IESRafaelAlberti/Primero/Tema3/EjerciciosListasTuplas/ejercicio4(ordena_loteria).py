"""Escribir un programa que pregunte al usuario los números ganadores de la lotería 
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a 
mayor"""

#RENTA MAS IR NUMERO A NUMERO PARA PONERLOS EN EL RANGO DE 1 A 50
def ordenaLoteria():            #MEJOR FORMA DEBAJO
    lista = []
    usuario = input("Introduce los números ganadores de la primitiva separados por '-': ")
    usuario = usuario.split("-")
    for numero in usuario:  #Convertimos los numeros a int porque sino por ejemplo el 14 lo pondria antes que 5
        numero = int(numero)
        lista.append(numero)
    lista.sort()  #Al hacer esto la variable lista se queda ordenada no hace falta guardarlo en otra variable

    return lista

if __name__ == "__main__":
    try:
        print(ordenaLoteria())
    except Exception as e:
        print(f"Algo ha salido mal: {e}")

"""
combinacion=[]
i = 0
while i<6:
    try:
        numero=int(input(f"Introduce el {i} numero de la combinación: "))
        if (numero>0) and (numero<50):
            combinacion.append(numero)
            i+=1
        else:
            raise NameError("Fuera de rango")
    except ValueError:
        print("Deben ser valores enteros dentro de rango")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")

combinacion.sort()

if len(combinacion) == 6:
    pintaCombinacion(combinacion)
else:
    print("Hubo algun error al introducir los numeros")
        """