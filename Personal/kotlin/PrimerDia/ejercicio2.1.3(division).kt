/*Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error.*/


fun division(a: Int, b: Int): Unit {
    if (b == 0){
        println("Error: No se puede dividir por 0")
    }else{
        val resultado = a/b
        println("El resultado es: $resultado")
    }

}


fun main(){
    println("Introduce dividendo:")
    val a = readLine()?.toIntOrNull() ?:0
    println("Introduce divisor:")
    val b = readLine()!!.toIntOrNull() ?:0
    if (a == null || b == null) {
        println("Error: Debe introducir numeros validos")/*Esto serviria si no pongo toIntOrNull() ?:0*/
    }else{
        division(a, b)
    }


}