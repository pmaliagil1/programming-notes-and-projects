/**
 * Ejercicio 3.1.6
 * Escribir un programa que almacene las asignaturas de un curso (por ejemplo
 * Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
 * nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
 * Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene
 * que repetir. Usa subprogramas cuando consideres de forma justificada.
 * Intenta controlar los posibles errores.
 */
fun obtenerNotaValida(asignatura: String): Double {
    while (true) {
        print("¿Qué nota has sacado en $asignatura? ")
        val entrada = readLine()
        try {
            val nota = entrada?.replace(',', '.')?.toDouble() ?: throw NumberFormatException()
            if (nota in 0.0..10.0) return nota
            else println("Por favor, introduce una nota entre 0 y 10.")
        } catch (e: NumberFormatException) {
            println("Entrada no válida. Por favor, introduce un número.")
        }
    }
}

fun main() {
    val asignaturas = mutableListOf("Matemáticas", "Física", "Química", "Historia", "Lengua")
    val aRepetir = mutableListOf<String>()

    for (asignatura in asignaturas) {
        val nota = obtenerNotaValida(asignatura)
        if (nota < 5.0) {
            aRepetir.add(asignatura)
        }
    }

    if (aRepetir.isEmpty()) {
        println("¡Felicidades! Has aprobado todas las asignaturas.")
    } else {
        println("Tienes que repetir las siguientes asignaturas:")
        for (asig in aRepetir) {
            println("- $asig")
        }
    }
}
