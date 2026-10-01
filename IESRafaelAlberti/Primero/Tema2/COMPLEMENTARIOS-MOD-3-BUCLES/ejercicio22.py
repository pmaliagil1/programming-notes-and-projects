"""Observa atentamente el siguiente algoritmo e indica los errores que presenta. Corrígelo
para que se ejecute correctamente.
Algoritmo Mod3_Ej22
Definir numIntentos Como Entero
Definir valorIntroducido Como Caracter
Definir MAX_INTENTOS Como Entero
//Inicialización de la variable numIntentos
numIntentos<-1
//Inicialización de la variable MAX_INTENTOS, la cual trataremos como si fuera una
//CONSTANTE
MAX_INTENTOS<-5
Escribir "¿Cuál es la capital de Francia?"
Leer valorIntroducido
Mientras valorIntroducido<>"París" o MAX_INTENTOS-numIntentos<>0 Hacer
Escribir "Respuesta incorrecta"
Escribir "Sólo quedan ", MAX_INTENTOS-numIntentos, " intentos"
Escribir "¿Cuál es la capital de Francia?"
Leer valorIntroducido
Fin Mientras
Si MAX_INTENTOS-numIntentos<>0 Entonces
Escribir "Bravo"
SiNo
Escribir "Revise sus conocimientos de geografía"
FinSi
FinAlgoritmo"""

def capitalFrancia():
    num_intentos = 0
    valor_introducido = ""
    MAX_INTENTOS = 5
    acertado = False

    valor_introducido = input("¿Cuál es la capital de Francia?: ")
    while valor_introducido.lower() != "paris" and MAX_INTENTOS-num_intentos!=1: #En el original pone 0 pero al poner 0 permite 6 intentos por eso el cambio
        num_intentos= num_intentos+1
        print("Respuesta incorrecta")
        print(f"Solo quedan {MAX_INTENTOS-num_intentos}, intentos")
        valor_introducido = input("¿Cuál es la capital de Francia?: ")
    
    if MAX_INTENTOS-num_intentos != 1:      #Aquí lo mismo
        print("Bravo")
    else:
        print("Revise sus conocimientos de geografía")
        


if __name__ == "__main__":
    capitalFrancia()

