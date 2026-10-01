#Ejercicio 11: Realiza un subprograma que intercambie el valor de dos variables enteras.

def intercambiarValor(a,b):
    c = 0
    c = a
    a = b
    b  = c
    
    return a,b

if __name__ == "__main__":
    print(intercambiarValor(2,4))