/*Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
palíndromo.*/


fun main(){

    val esPalindromo = { palabra:String -> palabra.equals(palabra.reversed()) }

    print("Introduce una palabra: ")

    val palabra: String = readLine()?.trim()?:""
    //val inversa: String = palabra.reversed()

   // val esPalindromo = palabra.equals(inversa, ignoreCase = true)

    println("La palabra $palabra ${if (esPalindromo(palabra)) "es" else "NO es"} palindromo")
}