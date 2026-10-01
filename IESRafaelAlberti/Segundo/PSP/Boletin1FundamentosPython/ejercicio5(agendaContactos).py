"""5. Agenda de Contactos (Diccionarios): Implementa un programa con un menú
interacAvo que permita:
a. Añadir un contacto (Nombre: Teléfono).
b. Buscar el teléfono de un contacto.
c. Mostrar todos los contactos."""

def agendaContactos(usuario,diccionario):
    while usuario != 4:
        usuario = int(input("Seleccione lo que desee hacer: \n1.Añadir un contacto (Nombre: Telefono)\n2.Buscar el telefono de un contacto.\n3.Mostrar todos los contactos\n4.Salir\n"))

        if usuario == 1:
            nombre = input("Introduzca el nombre del contacto que desea agendar: ")
            telefono = int(input("Introduce el telefono: "))
            diccionario[nombre] = telefono
        elif usuario == 2:
            busqueda = input("Introduzca el nombre del usuario que desea llamar: ")
            print(f"El telefono es {diccionario[busqueda]}")
        elif usuario == 3:
            for us in diccionario:
                print(f"{us}:{diccionario[us]}")
        


if __name__ == "__main__":
    diccionario = {}
    usuario = 0

    agendaContactos(usuario,diccionario)