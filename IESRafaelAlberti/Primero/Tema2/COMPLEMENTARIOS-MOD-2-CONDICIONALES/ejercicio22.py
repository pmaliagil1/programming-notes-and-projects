#Realiza un programa que diga si un número introducido por teclado es par y/o divisible entre 5.

def parDivisible(n):
    par = False
    divisible = False
    if n%2 == 0:
        par = True
    if n%5 == 0:
        divisible = True
    if par == False and divisible == False:
        return "El número introducido no es par ni divisible entre 5"
    elif par == True and divisible == False:
        return "El número introducido es par pero no es divisible entre 5"
    elif par == False and divisible == True:
        return "El número introducido no es par pero es divisible entre 5"
    elif par == True and divisible == True:
        return "El número introducido es par y divisible entre 5"
    else:
        raise NameError ("ERROR DESCONOCIDO")

if __name__ == "__main__":
    try:
        n = int(input("Introduzca un número: "))
        print(parDivisible(n))

    except TypeError:
        print("Error de escritura")
    except ValueError:
        print("Valor no válido")
    except NameError:
        print("Error desconocido")
    except Exception as e:
        print(f"Algo ha salido mal {e}")
