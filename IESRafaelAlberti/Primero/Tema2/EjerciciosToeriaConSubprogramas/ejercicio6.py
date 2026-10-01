#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el
#nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los
#hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa
#que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le
#corresponde. 



def grupo(nombre,sexo):
    inicial = nombre[0].upper()
    sexo = sexo.upper()
    if sexo not in ("H", "M"):
        raise ValueError("El sexo debe ser 'H' (hombre) o 'M' (mujer)")
    
    if (sexo == "M" and inicial < "M") or (sexo == "H" and inicial > "N"):
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        nombre = input("Introduce tu nombre: ").upper()
        sexo = input("Introduce tu sexo(M para mujer/H para hombre): ")
        if not nombre.isalpha():
            raise ValueError("El nombre solo debe contener letras")
        if grupo(nombre, sexo):
            print("Grupo A")
        else:
            print("Grupo B")
            
    except ValueError:
        print("Valor no valido")
    except TypeError:
        print("Dato incorrecto")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")

   


