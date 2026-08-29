/*Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de
una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que
introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.
 Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin
repeticiones.
 Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
 Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
 Mostrar si todos los nombres de primaria están incluidos en secundaria.
*/

fun pedirNombres(nivel: String): Set<String> {
    val nombres = mutableSetOf<String>()
    println("Introduce los nombres de pila de los alumnos de $nivel (escribe 'x' para finalizar):")
    while (true) {
        val nombre = readLine()?.trim() ?: ""
        if (nombre.lowercase() == "x") break
        if (nombre.isNotEmpty()) nombres.add(nombre)
    }
    return nombres
}

fun main() {
    val primaria = pedirNombres("primaria")
    val secundaria = pedirNombres("secundaria")

    // 1. Todos los nombres sin repeticiones (Unión)
    val todosLosNombres = primaria.union(secundaria)
    println("\nTodos los nombres de alumnos (sin repeticiones):")
    println(todosLosNombres)

    // 2. Nombres que se repiten (Intersección)
    val nombresRepetidos = primaria.intersect(secundaria)
    println("\nNombres que se repiten en ambos niveles:")
    println(nombresRepetidos)

    // 3. Nombres de primaria que no están en secundaria (Diferencia)
    val soloPrimaria = primaria.subtract(secundaria)
    println("\nNombres de primaria que no se repiten en secundaria:")
    println(soloPrimaria)

    // 4. ¿Todos los de primaria están en secundaria? (Subconjunto)
    val primariaEnSecundaria = secundaria.containsAll(primaria)
    if (primariaEnSecundaria) {
        println("\nTodos los nombres de primaria están incluidos en secundaria.")
    } else {
        println("\nNo todos los nombres de primaria están incluidos en secundaria.")
    }
}
