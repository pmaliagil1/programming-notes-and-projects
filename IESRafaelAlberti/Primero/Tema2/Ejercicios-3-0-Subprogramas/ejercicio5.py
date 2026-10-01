#Ejercicio 5: Mostrar menú con 3 opciones: 1. Nueva Tarea 2. Ver Tareas 3. Salir

def menu(eleccion):
    if eleccion ==1:
        print("Usted ha seleccionado Nueva Tarea")
    elif eleccion ==2:
        print("Usted ha seleccionado Ver Tarea")
    elif eleccion == 3:
        print("Usted ha seleccionado Salir")
    else:
        print("Error, opcion no valida")
    return (eleccion)
    
if __name__ == "__main__":
    print("1.Nueva Tarea\n2.Ver Tarea\n3.Salir")
    eleccion = int(input("Introduzca su elección: "))
    menu(eleccion)