def ordenar_inverso():
    n = int(input("¿Cuántos alumnos deseas ingresar en la lista? "))

    alumnos = []

    for i in range(n):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        alumnos.append(nombre)

    print("\nLista de alumnos original:")
    print(", ".join(alumnos))

    alumnos.sort(reverse=True)

    print("\nLista de alumnos ordenada en orden inverso:")
    print(", ".join(alumnos))

ordenar_inverso()
