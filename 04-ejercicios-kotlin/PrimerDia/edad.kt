/*
* PROGRAMA QUE TE PIDE LA EDAD Y TE DICE SI PUEDE PASAR A LA DISCOTECA
* */

fun sumaUno(e: Int): Int {
    return e+1
}

fun main(){
    var edad : Int

    print("Dime tu edad: ")
    edad = readLine()!!.toInt()
    edad = sumaUno(edad)
    println("Eres ${if (edad>=18) "mayor" else "menor"} de edad: $edad")


}