/*La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
ingredientes para cada tipo de pizza aparecen a continuación.
 Ingredientes vegetarianos: Pimiento y tofu.
 Ingredientes no vegetarianos: Pepperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menú con los ingredientes disponibles para que
elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están
en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
vegetariana o no y todos los ingredientes que lleva. */

fun main(){
    println("Bienvenido a la pizzeria Bella Napoli")
    println("¿Desea una pizza vegetariana?(S/N)")
    val respuesta = readLine()?.uppercase() ?: ""

    val esVegetariana: Boolean
    var ingredienteElegido: String

    if (respuesta == "S"){
        esVegetariana = true
        println("Ingredientes vegetarianos disponibles: ")
        println("1.Pimiento")
        println("2.Tofu")
        print("Elija el número de su ingrediente: ")

        ingredienteElegido = when (readLine()) {
            "1" -> "Pimiento"
            "2" -> "Tofu"
            else -> "Ingrediente no válido"
        }
    } else {
        esVegetariana = false
        println("Ingredientes no vegetarianos disponibles:")
        println("1. Pepperoni")
        println("2. Jamón")
        println("3. Salmón")
        print("Elija el número de su ingrediente: ")

        ingredienteElegido = when (readLine()) {
            "1" -> "Pepperoni"
            "2" -> "Jamón"
            "3" -> "Salmón"
            else -> "Ingrediente no válido"
        }
    }

    mostrarResumen(esVegetariana, ingredienteElegido)
}

fun mostrarResumen(vegetariana: Boolean, ingrediente: String) {
    if (ingrediente == "Ingrediente no válido") {
        println("Error: No se pudo procesar su pedido por una selección incorrecta.")
    } else {
        val tipoPizza = if (vegetariana) "Vegetariana" else "No Vegetariana"
        println("\n--- Resumen de su pedido ---")
        println("Tipo de pizza: $tipoPizza")
        println("Ingredientes: Tomate, Mozzarella y $ingrediente.")
    }
}