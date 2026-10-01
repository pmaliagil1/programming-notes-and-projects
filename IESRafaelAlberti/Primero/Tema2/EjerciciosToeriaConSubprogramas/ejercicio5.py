#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
#ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al
#usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que
#tributar o no. 

def edadTributar(edad):
    if edad < 0 or edad >= 150:
        raise ValueError("VALOR EQUIVOCADO")
    elif edad > 16:
        return True
    else:
        return False
        

def ingresosTributar(ingresos):
    if ingresos <0:
       raise NameError("INGRESOS NEGATIVOS")
    elif ingresos >= 1000:
       return True
    else:
       return False





if __name__ == "__main__":
    try:
        edad = int(input("Introduzca su edad: "))
        ingresos = float(input("Introduzca sus ingresos mesuales: "))

        if edadTributar(edad) and ingresosTributar(ingresos):
            print("Usted debe tributar")
        else:
            print("Usted no debe tributar")
        
    except ValueError:
        print("Valor no valido")
    except TypeError:
        print("Dato incorrecto")
    except NameError:
        print("DATO NO VÁLIDO")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")
   

