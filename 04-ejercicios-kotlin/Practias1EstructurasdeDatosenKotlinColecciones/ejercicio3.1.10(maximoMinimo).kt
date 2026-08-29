/*Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46,
22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios*/

fun main(){
    val lista: List<Int> = listOf(50, 75, 46, 22, 80, 65, 8)

    val maximo = lista.max()
    val minimo = lista.min()
    println("Máximo: $maximo")
    println("Minimo: $minimo")
}