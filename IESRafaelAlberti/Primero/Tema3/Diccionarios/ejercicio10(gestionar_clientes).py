"""Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su 
NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, 
teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un 
cliente preferente. El programa debe preguntar al usuario por una opción del siguiente 
menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los 
clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el 
programa tendrá que hacer lo siguiente:
1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la 
base de datos.
2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
3. Preguntar por el NIF del cliente y mostrar sus datos.
4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
6. Terminar el programa"""

#Hacerlo mas modular
def gestionarClientes(base_datos):
    acabado = False
    
    while not acabado:
        print("\n--- MENÚ DE CLIENTES ---")
        print("1. Añadir cliente\n2. Eliminar cliente\n3. Mostrar cliente\n4. Listar todos\n5. Listar preferentes\n6. Terminar")
        opcion = input("Elija una opción: ")

        if opcion == "6":
            acabado = True

        elif opcion == "1":
            nif = input("NIF: ")
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")

            preferente = input("¿Es preferente? (S/N): ").lower() == "s"
            
            datos = {
                "nombre": nombre,
                "direccion": direccion,
                "telefono": telefono,
                "correo": correo,
                "preferente": preferente
            }
            base_datos[nif] = datos

        elif opcion == "2":
            nif = input("Introduce el NIF del cliente a eliminar: ")
            if nif in base_datos:
                base_datos.pop(nif)
                print("Cliente eliminado.")
            else:
                print("El cliente no existe.")

        elif opcion == "3":
            nif = input("Introduce el NIF: ")
            if nif in base_datos:
                print(f"Datos de {nif}:")
                for clave, valor in base_datos[nif].items():
                    print(f"{clave.capitalize()}: {valor}")
            else:
                print("Cliente no encontrado.")

        elif opcion == "4":
            print("\n--- LISTA DE TODOS LOS CLIENTES ---")
            for nif, datos in base_datos.items():
                print(f"NIF: {nif} - Nombre: {datos['nombre']}")

        elif opcion == "5":
            print("\n--- CLIENTES PREFERENTES ---")
            for nif, datos in base_datos.items():
                if datos["preferente"]:
                    print(f"NIF: {nif} - Nombre: {datos['nombre']}")

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    try:
        clientes = {}
        gestionarClientes(clientes)
    except Exception as e:
        print(f"Error inesperado: {e}")