#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que
#el usuario escriba “salir” que terminará.

def eco(frase):
    while frase.lower() != "salir":
        print(frase)
        frase = input("Introduce una frase para oir el eco (escribe 'salir' para salir): ")
    print("ECO APAGADO")

if __name__ == "__main__":
    try:
        frase = input("Introduce una frase para oir el eco (escribe 'salir' para salir): ")
        eco(frase)
    except Exception as e:
        print(f"Algo ha salido mal: {e}")