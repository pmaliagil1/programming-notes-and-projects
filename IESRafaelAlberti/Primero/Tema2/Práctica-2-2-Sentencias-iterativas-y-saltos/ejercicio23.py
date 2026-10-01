"""Crear un programa que permita al usuario ingresar títulos de libros por teclado, 
finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese 
un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una 
línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) 
aparecieron en total (en todos los títulos de libros que componen en esa línea). 
Finalmente, informar cuántas líneas completas se ingresaron.  
Ejemplo de ejecución: 
Libro: Los 3 mosqueteros 
Libro: Historia de 2 ciudades 
Libro: / 
Línea completa. Aparecen 2 dígitos numéricos. 
Libro: 20000 leguas de viaje submarino 
Libro: El señor de los anillos 
Libro: / 
Línea completa. Aparecen 5 dígitos numéricos. 
Libro: 20 años después 
Libro: * 
Fin. Se leyeron 2 líneas completas."""

def libros():
    numeros = "0,1,2,3,4,5,6,7,8,9"
    libro = ""
    cuentaDigitos = 0
    cuentaLineas = 0
    while libro != "*":
        libro = input("Libro: ")
        if libro != "/":
            for letra in libro:
                if letra in numeros:
                    cuentaDigitos += 1
        elif libro == "/":
            cuentaLineas +=1
            print(f"Linea completa. Aparecen {cuentaDigitos} dígitos numéricos")
            cuentaDigitos = 0

    print(f"Fin. Se leyeron {cuentaLineas} líneas completas")



if __name__ == "__main__":
    try:
        libros()

    except Exception as e:
        print(f"Error desconocido: {e}")