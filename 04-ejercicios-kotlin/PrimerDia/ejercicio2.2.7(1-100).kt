/*Escribir un programa que pregunte al usuario un entero del 1 al 100 y a continuación
muestre por pantalla la tabla de multiplicar de ese número.*/

fun main(){
    print("Introduce un número entre 1 y 100: ")
    val n: Int? = readLine()?.toIntOrNull()

    if (n == null || n !in 1..100) {
        println("Debes introducir un entero valido entre 1 y 100")
    }else{
        println("Tabla de multiplicar del $n")
        tabla(n)
    }
}

fun tabla(num: Int?): Unit{

    if (num == null || num !in 1..100) {
        println("Debes introducir un entero entre 1 y 100")
    }else{
        for (i in 1..10){
            println("$num x $i = ${num*i}")
        }
    }
}