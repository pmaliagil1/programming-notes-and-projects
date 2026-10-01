#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor
#de edad o no.

def mayorDeEdad(edad):
    if edad >= 18:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        n = int(input("Introduce tu edad: "))
    
    except TypeError:
        print("El tipo de dato no es correcto")
    except ValueError:
        print("Valor no válido")
    else:
        if mayorDeEdad(n):
            print("Usted es mayor de edad")
        else:
            print("Usted es menor de edad")