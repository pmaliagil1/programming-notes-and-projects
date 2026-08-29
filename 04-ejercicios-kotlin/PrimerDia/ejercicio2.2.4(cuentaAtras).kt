/*Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas. */

fun main() {

    println("Introduce un numero positivo: ")
    val numero = readLine()?.toIntOrNull() ?: 0
    var resultado: String = ""

    for (i in numero downTo 0) {
        if (i == 0) {
            resultado = resultado + i.toString()

        } else {
            resultado += i.toString() + ", "
        }
    }
    println(resultado)
}