/*Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
sobre una persona (por ejemplo, nombre, edad, sexo, teléfono, correo electrónico, etc.)
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
contenido del diccionario.*/

/**
 * Inserta o actualiza los datos de una persona en el diccionario global
 * usando su teléfono como clave única.
 */
fun insertaPersona(diccionario: MutableMap<Int, MutableList<String>>, telefono: Int) {
    println("--- Introduciendo datos para el teléfono: $telefono ---")

    print("Introduce el nombre: ")
    val nombre = readLine() ?: "Desconocido"

    print("Introduce el correo electrónico: ")
    val correo = readLine() ?: "No proporcionado"

    // Creamos la lista de información para ese teléfono
    val datos = mutableListOf("Nombre: $nombre", "Email: $correo")

    // Guardamos en el mapa (si la clave existe, se sobreescribe)
    diccionario[telefono] = datos
}

/**
 * Muestra de forma limpia todo el contenido del diccionario.
 */
fun pintaDiccionario(d: MutableMap<Int, MutableList<String>>) {
    if (d.isEmpty()) {
        println("El diccionario está vacío.")
    } else {
        for ((tel, info) in d) {
            println("ID (Teléfono): $tel -> Datos: $info")
        }
    }
}

fun main() {
    // Mapa que usa el Teléfono (Int) como clave y una Lista de Strings como valor
    val personas = mutableMapOf<Int, MutableList<String>>()
    var continuar: String

    do {
        print("\nIntroduce el teléfono (clave): ")
        val telefono = readLine()?.toIntOrNull()

        if (telefono == null || telefono == 0) {
            println("ERROR: La clave debe ser un número válido y no cero.")
        } else {
            // Llamamos a la función que nos pediste
            insertaPersona(personas, telefono)

            println("\nContenido actual del diccionario:")
            pintaDiccionario(personas)
        }

        print("\n¿Deseas añadir a otra persona? (s/n): ")
        continuar = readLine()?.lowercase() ?: "n"

    } while (continuar == "s")

    println("\n--- Programa finalizado ---")
}