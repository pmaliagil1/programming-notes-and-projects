/*Dado el conjunto de letras:
vocales = {'a', 'e', 'i', 'o', 'u'}
1. Crea un conjunto consonantes que contenga las letras del alfabeto que no son
vocales.
2. Crea un conjunto letras_comunes que contenga las letras que están tanto en el
conjunto vocales como en el conjunto consonantes*/

fun main() {
    val vocales = setOf('a', 'e', 'i', 'o', 'u')

    // 1. Consonantes (a-z menos vocales)
    val alfabeto = ('a'..'z').toSet()
    val consonantes = alfabeto.subtract(vocales)

    // 2. Comunes (Intersección)
    val letras_comunes = vocales.intersect(consonantes)

    // Mostrar resultados
    println("Vocales: $vocales")
    // Mostramos solo las primeras 10 consonantes para no llenar la pantalla
    println("Consonantes (algunas): ${consonantes.take(10)}...")
    println("Letras comunes: $letras_comunes")

    if (letras_comunes.isEmpty()) {
        println("Como era de esperar, no hay letras comunes entre vocales y consonantes.")
    }
}
