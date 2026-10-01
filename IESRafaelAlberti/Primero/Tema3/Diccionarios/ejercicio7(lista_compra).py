"""Escribir un programa que cree un diccionario simulando una cesta de la compra. El 
programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que 
el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y 
el coste total, con el siguiente formato
Lista de la compra
Artículo 1
Artículo 2
Artículo 3
…
Total
Precio
Precio
Precio
…
Coste"""

def cestaCompra(lista):
    acabado = True
    contador = 0
    total = 0
    while acabado:
        contador+=1
        print(f"Articulo nº{contador}:")
        articulo = input("Introduce el artículo que quieres meter en la lista de la compra (escriba '0' para acabar): ")
        if articulo == "0":
            acabado = False
        else:
            precio = float(input("Introduce el precio del artículo seleccionado: "))
            lista[articulo] = precio
    print("Lista de la compra")
    for clave, valor in lista.items():
        total+=valor
        print(f"{clave}       {valor}")
    print(f"Total         {total}")
#Imprimir el resultado deberia estar fuera de la funcion, las funciones deben hacer las minimas tareas para mejorar el mantenimiento
#Mejora la modularidad


if __name__ == "__main__":
    try:
        lista = dict()
        cestaCompra(lista)

    except Exception as e:
        print(f"Algo ha salido mal: {e}")