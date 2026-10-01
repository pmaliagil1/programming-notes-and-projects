"""El programa debe mostrar un menú con una lista de películas y una opción para salir. Si el
usuario elige una de las películas, el programa mostrará una cita de esa película. Luego se
debe mostrar nuevamente el menú para que el usuario elija otra película o decida salir.
Ejemplo de ejecución:
Elija una opción:
1. Una cita de Forrest Gump.
2. Una cita de James Bond.
3. Una cita de Star Wars.
4. Una cita de El Sexto Sentido.
5. Una cita de El Padrino
6. Salir de la aplicación.
2
Me llamo Bond, James Bond.
5
Voy a hacerle una oferta que no podrá rechazar
3
Que la fuerza te acompañe
6
Hasta luego, Lucas."""

def menuPelicula():
    eleccion = 0
    while eleccion != 6:
        try:
            print("Elija una opción:\n1. Una cita de Forrest Gump.")
            print("2. Una cita de James Bond.\n3. Una cita de Star Wars.\n4. Una cita de El Sexto Sentido.")
            print("5. Una cita de El Padrino.\n6. Salir de la aplicación")
            eleccion = int(input())
            if eleccion == 1:
                print("Bubu es mi amigo")
            elif eleccion == 2:
                print("Me llamo Bond, James Bond")
            elif eleccion == 3:
                print("Que la fuerta te acompañe")
            elif eleccion == 4:
                print("Veo gente muerta")
            elif eleccion == 5:
                print("Voy a hacerle una oferta que no podrá rechazar")
            elif eleccion == 6:
                print("Hasta luego Lucas")
            else:
                raise NameError("ELECCIÓN NO VÁLIDA")
        except ValueError:
            print("Valor no válido")
        except NameError:
            print("Elección no válida")
        except Exception as e:
            print(f"Algo ha salido mal: {e}")
        
                
if __name__ == "__main__":
    menuPelicula()