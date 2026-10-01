"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión cada año
que dura la inversión.
# Formula para calcular El capital tras un año.
amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual"""

def inversion(amount, interest, años):
    for año in range(años):
        amount *= 1 + interest / 100
        print(f"Año {año+1}\nCapital total: {round(amount,2)}€")
    

if __name__ == "__main__":
    try:
        amount = float(input("Introduce la cantidad a invertir: "))
        interest = float(input("Introduce el interes porcentual anual: "))
        años = int(input("Introduce el número de años de la inversion: "))
        inversion(amount, interest, años)
    except ValueError:
        print("Valor no válido")
    except TypeError:
        print("Error de dato")
    except Exception as e:
        print(f"Error desconocido: {e}")