"""9. Generador de Contraseñas: Crea una función generar_password(longitud) que
combine letras mayúsculas, minúsculas, números y símbolos (usando el módulo
random y string) para devolver una clave aleatoria de la longitud indicada."""
import random
import string


def generarPassword(longitud, caracteres):
    password = ""

    for i in range(longitud):
        password += random.choice(caracteres)

    return password


if __name__ == "__main__":
    caracteres = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + string.punctuation
    )
     
    longitud = int(input("Introduce la longitud de la contraseña: "))

    print(generarPassword(longitud,caracteres))
     