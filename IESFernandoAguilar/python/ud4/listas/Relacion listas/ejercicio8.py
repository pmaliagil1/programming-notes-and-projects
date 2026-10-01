def obtener_datos_alumnos():
    alumnos = []
    
    while True:
        nombre = input("Introduce el nombre del alumno (o * para terminar): ")
        
        if nombre == "*":
            break
        
        edad = int(input(f"Introduce la edad de {nombre}: "))
        
        alumnos.append((nombre, edad))
    
    return alumnos

def mostrar_mayores_de_edad(alumnos):
    print("Alumnos mayores de edad:")
    for nombre, edad in alumnos:
        if edad >= 18:
            print(nombre)

def alumno_mayor(alumnos):
    if alumnos:
        alumno_mayor = max(alumnos, key=lambda x: x[1])
        return alumno_mayor[0]
    return None

alumnos = obtener_datos_alumnos()

mostrar_mayores_de_edad(alumnos)

mayor_alumno = alumno_mayor(alumnos)
if mayor_alumno:
    print("\nEl alumno mayor es:", mayor_alumno)
else:
    print("\nNo se han registrado alumnos.")
