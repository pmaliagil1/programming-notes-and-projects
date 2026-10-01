/*Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la
suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron
números pares. */

fun sumaDigitos(n: Int): Int {
    var numero: Int = Math.abs(n)
    var suma: Int = 0
    var digito: Int

    while (numero > 0) {
        digito = numero % 10
        suma += digito
        numero /= 10
    }
    return suma // Corregido: Ahora la función devuelve el valor
}

fun main() {
    var numero: Int
    var cantidadPares: Int = 0

    do {
        print("Ingrese un número entero positivo (-1 para salir): ")
        numero = readLine()?.toIntOrNull() ?: 0

        if (numero != -1) {
            // No hay problema con usar 'val' aquí, ya que se crea una
            // NUEVA variable en cada vuelta del bucle con el resultado actual.
            val sumaD = sumaDigitos(numero)
            println("La suma de los digitos de $numero es: $sumaD")

            if (numero % 2 == 0 && numero != 0) {
                cantidadPares++
            }
        }
    } while (numero != -1) // Corregido: Sin llaves después del while

    println("La cantidad de pares que tienes es: $cantidadPares")
}