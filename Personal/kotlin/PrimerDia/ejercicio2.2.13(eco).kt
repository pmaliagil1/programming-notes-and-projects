/*Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que
el usuario escriba “salir” que terminará. */

fun main(){
    var texto: String = ""
    while (!texto.equals("salir", ignoreCase = true)){
        print("Escrive algo ('salir' para terminar): ")
        texto = readLine()?.trim() ?: ""
        println("Eco: $texto")
    }
    println("Programa terminado.")
}