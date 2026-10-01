#Ejercicio 12: Calcula la solución de una ecuación de segundo grado contemplando las
#diferentes condiciones de entrada que se puedan dar

def ecuacionSegundoGrado(a,b,c):
    if a == 0:
        return "No es una ecuación de segundo grado"
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

    return x1, x2

if __name__ == "__main__":

    a = int(input("Introduzca el número 'a': "))
    b = int(input("Introduzca el número 'b': "))
    c = int(input("Introduzca el número 'c': "))
    print(ecuacionSegundoGrado(a,b,c))
