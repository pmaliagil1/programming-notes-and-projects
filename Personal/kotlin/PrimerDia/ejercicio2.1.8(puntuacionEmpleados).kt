/*En una determinada empresa, sus empleados son evaluados al final de cada año. Los
puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados
pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
A continuación, se muestra una tabla con los niveles correspondientes a cada
puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada
por la puntuación del nivel.
Nivel
Puntuación
Inaceptable 0.0
Aceptable 0.4
Meritorio 0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de
rendimiento, así como la cantidad de dinero que recibirá el usuario.
*/

fun calcularNivel(puntos: Double): String{
    return when {
        puntos == 0.0 -> "Inaceptable"
        puntos == 0.4 -> "Aceptable"
        puntos in 0.6 .. 1.0 -> {
            "Meritorio"
        }
        else -> "Invalido"
    }
}

fun calcularBonificaciones(puntos: Double): Double{
    val baseMonetaria = 2400.0
    return puntos*baseMonetaria
}

fun mostrarResultado(puntos: Double){
    val nivel = calcularNivel(puntos)

    if (nivel == "Invalido"){
        println("Error: La puntuacion $puntos no es válida")
    }else{
        val dinero = calcularBonificaciones(puntos)
        println("Nivel de rendimiento: $nivel")
        println("Bonificación: ${"%.2f".format(dinero)}€")
    }
}


fun main(){
    println("Introduce tu puntuación (0.0, 0.4, 0.6 o más): ")
    val entrada = readLine()?.toDoubleOrNull()

    if (entrada == null){
        println("Error: Debes introducir un número decimal válido")
    }else{
        mostrarResultado(entrada)
    }
}