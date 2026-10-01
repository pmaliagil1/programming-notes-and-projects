"""El tiempo de cocción.
Sabiendo que:
● Para cocinar 500 gramos de carne de vacuno, se necesita:
○ 10 minutos si quieres una cocción casi cruda
○ 17 minutos si quieres una cocción al punto
○ 25 minutos si quieres una cocción bien hecha.
● Para cocinar 400 gramos de carne de cordero se necesita:
○ 15 minutos si quieres una cocción casi cruda
○ 25 minutos si quieres una cocción al punto
○ 40 minutos si quieres una cocción bien hecha.
● El tiempo de cocción es proporcional al peso.
Dependiendo de la información introducida por el usuario (tipo de carne, modo de cocción y
peso), mostrar el tiempo de cocción de una carne en segundos."""

def tiempoCoccion():
    try:
        tipoCarne = int(input("Introduzca el tipo de carne\n1.Vacuno\n2.Cordero\n(Introduzca 1 o 2): "))
        modoCoccion = int(input("Introduzca el modo de cocción\n1.Casi cruda\n2.Al punto\n3.Bien hecha\n(Introduzca 1, 2 o 3): "))
        peso = int(input("Introduzca el peso en gramos: "))

        if tipoCarne == 1: #vacuno
            if modoCoccion == 1: #casi cruda
                nuevoTiempo = (peso*(10*60))/500
                return f"El tiempo de cocción es de {nuevoTiempo} segundos"
            elif modoCoccion == 2: #al punto
                nuevoTiempo = (peso*(17*60))/500
                return f"El tiempo de cocción es de {nuevoTiempo} segundos"
            elif modoCoccion == 3: #bien hecha
                nuevoTiempo = (peso*(25*60))/500
                return f"El tiempo de cocción es de {nuevoTiempo} segundos"
            else:
                raise NameError("DATO NO VÁLIDO")
        elif tipoCarne ==2: #cordero
            if modoCoccion == 1: #casi cruda
                nuevoTiempo = (peso*(15*60))/400
                return f"El tiempo de cocción es de {nuevoTiempo} segundos"
            elif modoCoccion == 2: #al punto
                nuevoTiempo = (peso*(25*60))/400
                return f"El tiempo de cocción es de {nuevoTiempo} segundos"
            elif modoCoccion == 3: #bien hecha
                nuevoTiempo = (peso*(40*60))/400
                return f"El tiempo de cocción es de {nuevoTiempo} segundos"
            else:
                raise NameError("DATO NO VÁLIDO")
        else:
            raise NameError("DATO NO VÁLIDO")
    
    except ValueError:
        print("Entrada no válida")
    except NameError:
        print("Dato no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")



if __name__ == "__main__":
    print(tiempoCoccion())