/*Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los
años que ha cumplido (desde 1 hasta su edad).*/

import kotlin.math.abs

fun main(){
    var edad: Int = 0
    val i: Int = 1

    print("Dime tu edad: ")
    try {
        edad = readLine()?.toInt() ?: 0

    }catch (e:NumberFormatException){
        println("Debe ser un número entero: ${e.message}")
    }
    if (edad >0){
        for (i in 1 .. edad){
            println("Has cumplido: $i años")
        }
    }else{
        for (i in 1 ..abs(edad)){
            println("Has cumplido: $i años")
        }
    }
}