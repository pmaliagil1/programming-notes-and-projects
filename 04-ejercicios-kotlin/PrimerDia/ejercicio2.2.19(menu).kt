/*Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3
finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó
3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a
mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las
opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión
del menú y el programa finalizará.*/

fun main() {
    var opcion: Int

    do {
        println("\n==== Menu ====")
        println("1- Comenzar programa")
        println("2- Imprimir listado")
        println("3- Finalizar programa")
        print("Seleccione una opcion: ")

        // Usamos toIntOrNull para que el programa no explote si escriben letras
        opcion = readLine()?.toIntOrNull() ?: 0

        when (opcion) {
            1 -> println("\nEjecutando: 'Comenzar programa'...")
            2 -> println("\nListado: Elemento 1, Elemento 2, Elemento 3.")
            3 -> println("\nSaliendo...")
            else -> println("\nOpción no válida. Intente de nuevo.")
        }

    } while (opcion != 3)

    println("Programa terminado con éxito.")
}