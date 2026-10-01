#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error. 

def division(dividendo, divisor):
    if divisor == 0:
        raise ZeroDivisionError("INDETERMINACIÓN") #Esto lo que hace es que vaya a el except de debajo
    else:                                         #El rasie se usa cuando el error se captura dentro de la funcion  
        return dividendo/divisor

if __name__ == "__main__":
    try:
        dividendo = int(input("Introduce el dividendo: "))
        divisor = int(input("Introduce el divisor: "))
        resultado = division(dividendo, divisor) #se pone aqui y no en el else para que le afecten las excepciones
    except ValueError:
        print("Valor no valido")
    except TypeError:
        print("Dato incorrecto")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    else:
        print(f"El resultado es {resultado}")
    