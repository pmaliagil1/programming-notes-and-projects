/*Escribir un programa que pregunte por una muestra de números, los guarde en una lista
y muestre por pantalla su media y desviación típica.*/

import kotlin.math.sqrt

fun main() {
    print("Introduce los números de la muestra separados por espacios: ")
    val entrada = readLine() ?: ""

    // Convertimos la entrada en una lista de números Double
    val numeros = entrada.split(" ")
        .filter { it.isNotBlank() }
        .mapNotNull { it.toDoubleOrNull() }

    if (numeros.isEmpty()) {
        println("No se han introducido números válidos.")
    } else {
        // Media aritmética: la suma de todos los números dividida por la cantidad de números
        val media = numeros.average()

        // Varianza: promedio de los cuadrados de las desviaciones con respecto a la media
        val varianza = numeros.map { (it - media) * (it - media) }.average()

        // Desviación típica: raíz cuadrada de la varianza
        val desviacionTipica = sqrt(varianza)

        println("Muestra: $numeros")
        println("Media: %.2f".format(media))
        println("Desviación típica: %.2f".format(desviacionTipica))
    }
}