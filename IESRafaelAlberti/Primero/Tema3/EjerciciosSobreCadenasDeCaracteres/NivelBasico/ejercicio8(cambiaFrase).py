"""Dada una frase, convierte una cadena a mayúsculas, a minúsculas y la primera letra de cada
palabra a mayúscula."""

def cambiaFrase(frase):
    fraseMayusc = frase.upper()
    fraseMinusc = frase.lower()
    fraseTitle = frase.title()
    return f"{fraseMayusc}\n{fraseMinusc}\n{fraseTitle}"

if __name__ == "__main__":
    try:
        frase = input("Introduce una frase: ")
        print(cambiaFrase(frase))
    
    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")