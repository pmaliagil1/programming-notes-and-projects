#Ejercicio 15: Crea un subprograma que reciba una nota decimal y devuelva si está suspenso, 
#aprobado, notable o sobresaliente. 

def notas(nota):
    try:
        if nota < 0 or nota > 10:
            raise ValueError("Error: la nota debe estar entre 0 y 10.")
        if nota < 5:
            resultado = "Suspenso"
        elif nota <7:
            resultado = "Aprobado"
        elif nota <9:
            resultado = "Notable"
        elif nota <11:
            resultado = "Sobresaliente"
        return (resultado)
    
    except ValueError as e:
        return str(e)
    except TypeError:
        return "Error: el valor introducido no es un número."
    except Exception as e:
        return f"Algo ha salido mal: {e}"


if __name__ == "__main__":
    try:
        nota = float(input("Introduce tu nota: "))
        print(notas(nota))
    except ValueError:
        print("Error: Debes introducir un número válido.")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")