/*Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
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
6. Terminar el programa.*/

fun main() {
    // Se define como MutableMap para que funcione como diccionario (NIF -> Datos)
    val clientes = mutableMapOf<String, MutableMap<String, Any>>()
    var opcion: Int

    do {
        println("\n--- MENÚ DE CLIENTE ---")
        println("1. Añadir cliente")
        println("2. Eliminar cliente")
        println("3. Mostrar cliente")
        println("4. Listar todos los clientes")
        println("5. Listar clientes preferentes")
        println("6. Terminar el programa")
        print("Opción: ")
        opcion = readLine()?.toIntOrNull() ?: 0

        when (opcion) {
            // 1. Añadir cliente
            1 -> {
                print("NIF: ")
                val nif = readLine() ?: ""

                print("Nombre: ")
                val nombre = readLine() ?: ""

                print("Direccion: ")
                val direccion = readLine() ?: ""

                print("Telefono: ")
                val telefono = readLine() ?: ""

                print("Correo: ")
                val correo = readLine() ?: ""

                print("¿Es preferente? (s/n): ")
                val prefEntrada = readLine() ?: "n"
                // Convertimos la entrada 's' en un Booleano True/False
                val esPreferente = prefEntrada.lowercase() == "s"

                val datos = mutableMapOf<String, Any>()
                datos["nombre"] = nombre
                datos["direccion"] = direccion
                datos["telefono"] = telefono
                datos["correo"] = correo
                datos["preferente"] = esPreferente

                clientes[nif] = datos
                println("Cliente añadido correctamente")
            }

            // 2. Eliminar cliente
            2 -> {
                print("Introduce el NIF del cliente para eliminar: ")
                val nif = readLine() ?: ""

                if (clientes.remove(nif) != null) {
                    println("Cliente eliminado")
                } else {
                    println("No existe un cliente con ese NIF")
                }
            }

            // 3. Mostrar cliente
            3 -> {
                print("Introduce el NIF del cliente a mostrar: ")
                val nif = readLine() ?: ""

                val cliente = clientes[nif]

                if (cliente != null) {
                    println("Datos del cliente:")
                    for ((clave, valor) in cliente) {
                        println("$clave: $valor")
                    }
                } else {
                    println("No existe con cliente con ese NIF")
                }
            }

            // 4. Listar todos los clientes
            4 -> {
                if (clientes.isEmpty()) {
                    println("No hay clientes registrados")
                } else {
                    println("Lista de todos los clientes:")
                    for ((nif, datos) in clientes) {
                        // Usamos ${} para acceder a propiedades del mapa dentro del texto
                        println("$nif: ${datos["nombre"]}")
                    }
                }
            }

            // 5. Listar clientes preferentes
            5 -> {
                println("Clientes preferentes:")
                var hayPreferentes = false

                for ((nif, datos) in clientes) {
                    val esPref = datos["preferente"] as? Boolean ?: false
                    if (esPref) {
                        println("$nif: ${datos["nombre"]}")
                        hayPreferentes = true
                    }
                }
                if (!hayPreferentes) {
                    println("No hay clientes preferentes")
                }
            }

            // 6. Terminar
            6 -> println("Programa terminado")

            else -> println("Opcion no valida")
        }

    } while (opcion != 6)
}