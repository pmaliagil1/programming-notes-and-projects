/*Dado el conjunto de números enteros:
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
1. Crea un conjunto pares que contenga los números pares del conjunto numeros.
2. Crea un conjunto multiplos_de_tres que contenga los números que son
múltiplos de tres del conjunto numeros.
3. Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y
guárdala en un conjunto llamado pares_y_multiplos_de_tres.*/

fun main() {
    val numeros = setOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    // 1. Pares
    val pares = numeros.filter { it % 2 == 0 }.toSet()

    // 2. Múltiplos de tres
    val multiplos_de_tres = numeros.filter { it % 3 == 0 }.toSet()

    // 3. Intersección
    val pares_y_multiplos_de_tres = pares.intersect(multiplos_de_tres)

    // Mostrar resultados
    println("Números: $numeros")
    println("Pares: $pares")
    println("Múltiplos de 3: $multiplos_de_tres")
    println("Intersección (pares y múltiplos de 3): $pares_y_multiplos_de_tres")
}
