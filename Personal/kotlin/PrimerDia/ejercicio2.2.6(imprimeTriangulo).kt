/*Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
*****/


fun dibujarTriangulo(altura: Int) {
    // El bucle externo recorre cada fila desde 1 hasta 'altura'
    for (i in 1..altura) {

        // El bucle interno imprime el número de asteriscos según la fila actual
        for (j in 1..i) {
            print("*") // Usamos print (sin 'ln') para que se queden en la misma línea
        }

        // Una vez terminada la fila, saltamos a la siguiente línea
        println()
    }
}

fun main(){
    print("Introduce la altura del triángulo (número entero): ")
    val altura = readLine()?.toIntOrNull()

    if (altura == null || altura <= 0) {
        println("Error: Por favor, introduce un número entero positivo.")
    } else {
        dibujarTriangulo(altura)
    }
}