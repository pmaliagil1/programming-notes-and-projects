#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
#introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
#mayúsculas y minúsculas.

def ComprobarContraseña(contraseña1, contraseña2):
    if contraseña1.lower() == contraseña2.lower():
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        contraseña1 = input("Introduzca contraseña: ")
        contraseña2 = input("Introduzca de nuevo su contraseña: ")
    except TypeError:
        print("El tipo de dato no es correcto")
    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")
    else:
        if ComprobarContraseña(contraseña1, contraseña2):
            print("Contraseña correcta")
        else:
            print("Contraseña incorrecta")
