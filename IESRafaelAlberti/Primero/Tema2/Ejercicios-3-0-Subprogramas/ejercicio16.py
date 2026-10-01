#Ejercicio 16: Realiza un subalgoritmo que permita a un usuario intentar 3 veces acertar el PIN 
#de acceso a un dispositivo. 
# Ejercicio 16: Intentar 3 veces acertar el PIN

def contraseña(correcta="HolaMundo", max_intentos=3):
    intentos = max_intentos

    while intentos > 0:
        entrada = input("Introduce la contraseña: ")
        if entrada == correcta:
            return "Contraseña correcta"
        intentos -= 1
        if intentos > 0:
            print(f"Contraseña incorrecta, te quedan {intentos} intentos.")
    return "Intentos agotados."

if __name__ == "__main__":
    print(contraseña())
