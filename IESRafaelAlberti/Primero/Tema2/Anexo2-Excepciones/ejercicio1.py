#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los
#años que ha cumplido (desde 1 hasta su edad).

def edadCumplida(edad):
    for i in range (edad+1):
        print (i)
    if edad < 0:
        raise ValueError("La edad no puede ser menor que 0.")
if __name__ == "__main__":
    try:
        edad = int(input("Introduzca su edad: "))
        edadCumplida(edad)
    except ValueError as e:
        print(e)