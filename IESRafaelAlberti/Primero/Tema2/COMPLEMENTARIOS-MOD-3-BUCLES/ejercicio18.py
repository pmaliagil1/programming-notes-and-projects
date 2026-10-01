"""Realiza el control de acceso a una caja fuerte. La combinación será un número de 4 cifras.
El programa nos pedirá la combinación para abrirla. Si no acertamos, se nos mostrará el
mensaje “Lo siento, esa no es la combinación” y si acertamos se nos dirá “La caja fuerte se
ha abierto satisfactoriamente”. Tendremos cuatro oportunidades para abrir la caja fuerte."""

def cajaFuerte(contraseña):
    acertado = False
    intentos = 5
    while acertado == False:
        try:
            intentos -= 1
            prueba = int(input(f"Introduzca la contraseña oculta (Le quedan {intentos} intentos): "))
            if prueba <=999 or prueba >9999:
                intentos +=1
                raise NameError ("DEBE SER DE 4 CIRRAS")
            if contraseña == prueba:
                print("La caja fuerte se ha abierto satisfactoriamente")
                acertado = True
            if contraseña != prueba:
                print("Lo siento, esa no es la combinación")
        except NameError:
            print("Debe ser de 4 cifras")

if __name__ == "__main__":
    try:
        contraseña = int(input("Introduce una contraseña de 4 cifras: "))
        if contraseña <=999 or contraseña >9999:
            raise TypeError ("DEBE SER DE 4 CIFRAS")
        cajaFuerte(contraseña)
    except TypeError:
        print("Debe ser de 4 cifras")
    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")
