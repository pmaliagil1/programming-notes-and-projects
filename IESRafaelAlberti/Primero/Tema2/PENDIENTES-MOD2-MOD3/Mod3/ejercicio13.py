"""Dibuja un ordinograma de un programa donde el usuario "piensa" un
número del 1 al 100 y el ordenador intenta adivinarlo. Es decir, el ordenador
irá proponiendo números una y otra vez hasta adivinarlo (el usuario deberá
indicarle al ordenador si es mayor, menor o igual al número que ha pensado)."""
from random import randint
def adivinaNumero():
    acertado = False
    mayor = 100
    menor = 1
    while acertado != True:
        try:
            intento = randint(menor,mayor)
            usuario = input(f"El numero es {intento}, ¿he adivinado? (S/N): ")
            if usuario.upper() == "S":
                return "Genial, ¡he acertado!"
            elif usuario.upper() == "N":
                duda = input("¿El número a acertar es mayor o menor? (MAYOR/MENOR): ")
                if duda.upper() == "MAYOR":
                    menor = intento
                elif duda.upper() == "MENOR":
                    mayor = intento
                else:
                    raise NameError ("ERROR")
            else:
                raise NameError("ERROR")
        except NameError:
            print("ERROR")
        except Exception as e:
            print(f"Algo ha salido mal: {e}")

if __name__ == "__main__":
    print(adivinaNumero())
