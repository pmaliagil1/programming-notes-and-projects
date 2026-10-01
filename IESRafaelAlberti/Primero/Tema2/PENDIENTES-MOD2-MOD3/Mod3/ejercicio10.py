""""Dibuja un ordinograma de un programa que lee una secuencia de notas
(con valores que van de 0 a 10) que termina con el valor -1 y nos dice si
hubo o no alguna nota con valor 10."""


def buscaDiez():
    n = 0
    contiene = False
    contador = 0
    while n != -1:
        try:
            n = int(input("Introduce un número de 0 a 10 (-1 para terminar): "))
            if n >10 or n <-1:
                raise ValueError ("VALOR NO VÁLIDO")
            if n == 10:
                contador = contador+1
                contiene = True
        except ValueError:
            print("Valor no válido")
        except Exception as e:
            print(f"Algo ha salido mal: {e}")
    if contiene == True:
        return f"Has introducido un total de {contador} dieces"
    else:
        return "No has introducido ningún diez"

if __name__ == "__main__":
    
    print(buscaDiez())

