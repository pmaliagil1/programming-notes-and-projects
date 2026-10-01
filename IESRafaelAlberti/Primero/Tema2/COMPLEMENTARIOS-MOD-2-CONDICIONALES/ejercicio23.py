"""Diseña un algoritmo en el que, dadas tres personas, por ejemplo Pedro, Alicia y Carla,
indique quiénes son de la misma quinta."""

def mismaQuinta():
    try:
        persona1 = input("Introduce el primer nombre: ")
        año1 = int(input("Introduce su año de nacimiento: "))
        persona2 = input("Introduce el segundo nombre: ")
        año2 = int(input("Introduce su año de nacimiento: "))
        persona3 = input("Introduce el tercer nombre: ")
        año3 = int(input("Introduce su año de nacimiento: "))



        if año1 == año2 == año3:        #ACUERDATE DE PONER LA MAS RESTRICTIVA AL PRINCIPIO
            print("Todos son de la misma quinta")
        elif año1 == año3:
            print(f"{persona1} y {persona3} son de la misma quinta.")
        elif año2 == año3:
            print(f"{persona2} y {persona3} son de la misma quinta.")
        elif año1 == año2:
            print(f"{persona1} y {persona2} son de la misma quinta.")
        else:
            print("Nadie es de la misma quinta")

    except ValueError:
        print("Valor no válido")
    except TypeError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal")
    

if __name__ == "__main__":
    mismaQuinta()