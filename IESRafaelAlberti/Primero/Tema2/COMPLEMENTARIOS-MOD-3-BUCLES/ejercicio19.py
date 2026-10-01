"""Escribe un programa que calcule la media de un conjunto de números positivos introducidos
por teclado. A priori, el programa no sabe cuántos números se introducirán. El usuario
indicará que ha terminado de introducir los datos cuando meta un número negativo."""

def calculaMedia():
    n = int(input("Introduce un número para calcular la media (introduce un negativo para terminar): "))
    
    contador = 0
    acumulador = 0
    
    if n > 0:
        acumulador = n
        contador = 1
        
    while n > 0:
        
        n = int(input("Introduce un número para calcular la media (introduce un negativo para terminar): "))
        
        if n > 0:
            contador += 1
            acumulador += n 
        
    if contador > 0:
        resultado = acumulador / contador
        print(resultado)
    else:
        print(0)
        
if __name__ == "__main__":
    try:
        calculaMedia()
    except ValueError:
        print("Error: Entrada no válida.")
    except Exception as e:
        print(e)