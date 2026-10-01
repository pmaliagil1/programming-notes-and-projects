/*Escribe un bucle while que comience con el último carácter en la cadena y haga un
recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en
una línea independiente.*/

fun main(){
    val texto: String = "Kotlin"
    var i: Int = texto.length-1

    while (i>=0){
        println(texto[i])
        i--
    }
    println("----------------------------------")
    for(i in texto.length-1 downTo 0){
        println(texto[i])
    }
}