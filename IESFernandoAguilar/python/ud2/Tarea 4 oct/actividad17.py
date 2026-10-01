print("Menú principal")
print("Opción 1: Ver información")
print("Opción 2: Configuración")
print("Opción 3: Ayuda")
print("Opción 4: Salir")
opcion = int(input("Seleccione una opción del 1 al 4:"))

while opcion < 5 and opcion > 0:
    if opcion == 1:
        print("Has seleccionado la opción 1: Ver información")
    if opcion == 2:
        print("Has seleccionado la opción 2: Configuración")
    if opcion == 3:
        print("Has seleccionado la opción 3: Ayuda")
    if opcion == 4:
        print("Saliendo del sistema")
else:
    print("Opción no válida")
