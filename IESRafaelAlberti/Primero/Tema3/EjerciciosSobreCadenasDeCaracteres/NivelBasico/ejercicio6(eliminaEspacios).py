#Elimina los espacios de una frase.

def eliminaEspacios(frase):
    palabras = frase.split(" ")
    fraseSinEspacios = "".join(palabras)            #Puedes usar .strip o .replace de " " por "" y asi quita los espacios
    return fraseSinEspacios                     #strip quita solo los espacios de los extremos
if __name__ == "__main__":
    try:
        frase = input("Introduce una frase: ")
        print(eliminaEspacios(frase))

    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")

"""frase = "     Aprende Python       "
try:
    limpia = frase.strip()
    print("Frase sin espacios: ", limpia)
    
Except AtributeError"""
