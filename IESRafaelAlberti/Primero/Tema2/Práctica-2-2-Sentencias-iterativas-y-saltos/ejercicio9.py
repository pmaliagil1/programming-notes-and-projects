#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def contraseña(contra, intento):
    if contra == intento:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        contra = input("Introduce tu contraseña: ")
        intento = input("Vuelva a introducir la contraseña: ")
        if contraseña(contra, intento):
            print("Contraseña correcta")
        else:
            print("Acceso denegado")
        while not contraseña(contra, intento):
            contra = input("Introduce tu contraseña: ")
            intento = input("Vuelva a introducir la contraseña: ")
            if contraseña(contra, intento):
                print("Contraseña correcta")
            else:
                print("Acceso denegado")
        

    except Exception as e:
        print(f"Error desconocido: {e}")
