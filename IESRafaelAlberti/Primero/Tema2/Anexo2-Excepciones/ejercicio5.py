#Escribir que solicite una contraseña, y si no coincide con la que se tiene,
#  lance la excepción NameError con el mensaje, "Incorrect Password!!"

def comprobarContraseña(password, code):
    if password != code:
        raise NameError("Contraseña Incorrecta")
    else:
        return True
password = "alberti"
acceso = False

clave = input("Introduce la contraseña: ")
clave = clave.lower()

try:
    acceso = comprobarContraseña(password, clave)
except Exception as e:
    print(f"Algo ha salido mal: {e}")
else:
    if acceso:
        print("ACCESO OK")