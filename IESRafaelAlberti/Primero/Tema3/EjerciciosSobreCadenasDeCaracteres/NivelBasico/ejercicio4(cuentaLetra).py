#Contar cuántas veces aparece una letra.

def cuentaLetra(frase):
    contador = 0                                        #USAR COUNT (MIRA DEBAJO)
    letraElegida = input("Introduce la letra que quieres contar: ")
    if len(letraElegida) >1 or len(letraElegida)<1:
        raise ValueError ("VALOR NO VÁLIDO")
    for letra in frase:
        if letra == letraElegida:
            contador+=1
    return f"La letra {letraElegida} aparece un total de: {contador} veces."

def cuentaLetra(frase):
    contador = frase.count("a")
    return contador

if __name__ == "__main__":
    try:
        frase = input("Introduzca una frase: ")
        print(cuentaLetra(frase))
    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")

"""
def cuentaLetra(frase):
    contador = frase.count("a")
    return contador"""
