while True:
    nombre = input("Ingresa tu nombre: ")
    if nombre != "Pedro":
        continue
    clave = input("Hola " + nombre + " dime tu clave:")
    if clave == "pulpo":
        break
print("Acceso otorgado")