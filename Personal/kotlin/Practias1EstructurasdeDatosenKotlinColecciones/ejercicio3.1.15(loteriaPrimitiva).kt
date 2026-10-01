/* Genera una combinación válida para una apuesta de la lotería primitiva.*/

import kotlin.random.Random

fun main() {
    val combinacion = mutableSetOf<Int>()

    while (combinacion.size < 6) {
        val numero = Random.nextInt(1, 50)
        combinacion.add(numero)
    }

    val listaOrdenada = combinacion.toList().sorted()

    println("Combinación de la lotería primitiva:")
    println(listaOrdenada.joinToString(", "))
}
