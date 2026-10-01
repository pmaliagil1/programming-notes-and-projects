"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo
guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre>
tiene <edad> años, vive en <dirección> y su número de teléfono es
<teléfono>."""

def creaDiccionario(d):
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    direccion = input("Introduce tu dirección: ")
    telefono = int(input("Introduce tu telefono: "))

    d[telefono] = [nombre,edad,direccion]

    for i in d.items():
        print(f"{i[1][0]} tiene {i[1][1]} años, vive en {i[1][2]} y su número de teléfono es {i[0]}.")

if __name__ == "__main__":
    try:
        d = {}
        creaDiccionario(d)

    except Exception as e:
        print(f"Algo ha salido mal: {e}")