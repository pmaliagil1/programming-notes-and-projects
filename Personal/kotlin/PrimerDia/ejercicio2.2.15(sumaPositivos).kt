/*Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar
la sumatoria de todos los números positivos ingresados.*/

fun main() {
    var sumaPositivos = 0
    var numero: Int?

    do {
        print("Ingrese un número (0 para terminar): ")
        val entrada = readLine()

        numero = entrada?.toIntOrNull()

        if (numero == null) {
            println("Entrada inválida. Por favor introduzca un número entero.")
        } else {
            if (numero > 0) {
                sumaPositivos += numero
            }
        }

    } while (numero != 0)

    println("\n--- Resultado ---")
    println("La sumatoria de los números positivos ingresados es: $sumaPositivos")
    println("Programa terminado.")
}