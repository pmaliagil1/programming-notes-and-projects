def reemplazar_nombre():

    n = int(input("¿Cuántos alumnos deseas ingresar en la lista? "))

    alumnos = ""

    for i in range(n):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        alumnos += nombre + ", "

    alumnos = alumnos.strip(", ")

    print("\nLista de alumnos original:")
    print(alumnos)

    nombre_a_reemplazar = input("\nIngresa el nombre a reemplazar: ")
    nuevo_nombre = input("Ingresa el nuevo nombre que lo reemplazará: ")

    if nombre_a_reemplazar in alumnos:
        alumnos = alumnos.replace(nombre_a_reemplazar, nuevo_nombre)
        print(f"\nEl nombre '{nombre_a_reemplazar}' ha sido reemplazado por '{nuevo_nombre}'.")
    else:
        print(f"\nEl nombre '{nombre_a_reemplazar}' no se encuentra en la lista.")

    print("\nLista de alumnos final:")
    print(alumnos)

reemplazar_nombre()
