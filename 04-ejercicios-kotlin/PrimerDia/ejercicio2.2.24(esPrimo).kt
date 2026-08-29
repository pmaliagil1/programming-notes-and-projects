/*Escribir un programa que solicite el ingreso de una cantidad indeterminada de números
mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números
primos ingresados. */

fun esPrimo(n: Int): Boolean {
    if (n <= 1) return false

    for (i in 2..Math.sqrt(n.toDouble()).toInt()) {
        if (n % i == 0) return false
    }
    return true
}

fun main() {
    var numero: Int
    var cantidadPrimos = 0

    do {
        print("Ingrese un número > 1 (0 para salir): ")
        numero = readLine()?.toIntOrNull() ?: -1

        if (numero > 1) {
            if (esPrimo(numero)) {
                cantidadPrimos++
                println("$numero es primo.")
            } else {
                println("$numero no es primo.")
            }
        } else if (numero != 0) {
            println("Error: El número debe ser mayor que 1.")
        }

    } while (numero != 0)

    println("\n--- Resumen ---")
    println("Cantidad total de números primos ingresados: $cantidadPrimos")
}