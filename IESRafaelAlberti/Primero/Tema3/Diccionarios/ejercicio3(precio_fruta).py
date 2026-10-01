"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un
mensaje informando de ello.
Fruta Precio
Plátano 1.35
Manzana 0.80
Pera 0.85
Naranja 0.70"""

def precioFruta(fruta):
    try:
        eleccion = input("Introduce la fruta que deseas: ").capitalize()
        if eleccion not in fruta:
            raise NameError("FRUTA NO ENCONTRADA")
        kg = float(input("Introduce el número de kg que deseas: "))
        if eleccion in fruta:
            precio = kg*fruta[eleccion]

        print(f"El precio es {precio}")
    except NameError:
        print("Fruta no encontrada")

if __name__ == "__main__":
    try:
        fruta = {'Plátano':1.35,'Manzana':0.80,'Pera':0.85,'Naranja':0.70}
        precioFruta(fruta)
    except Exception as e:
        print(f"Algo ha salido mal: {e}")