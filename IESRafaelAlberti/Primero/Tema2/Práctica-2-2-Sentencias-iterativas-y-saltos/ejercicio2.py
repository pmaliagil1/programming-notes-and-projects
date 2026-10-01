#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los
#años que ha cumplido (desde 1 hasta su edad).

def cuentaEdad(edad):
    for i in range(edad):
        print(i)

if __name__ == "__main__":
    edad = int(input("Introduce tu edad: "))

    cuentaEdad(edad)