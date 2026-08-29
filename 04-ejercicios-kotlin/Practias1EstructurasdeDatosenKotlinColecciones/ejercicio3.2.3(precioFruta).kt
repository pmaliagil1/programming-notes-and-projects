/*Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un
mensaje informando de ello.
Fruta Precio
Plátano 1.35
Manzana 0.80
Pera
0.85
Naranja 0.70*/

fun main() {
    val preciosFrutas = mapOf(
        "Plátano" to 1.35,
        "Manzana" to 0.80,
        "Pera" to 0.85,
        "Naranja" to 0.70
    )

    print("¿Qué fruta quieres comprar? ")
    val fruta = readLine()?.replaceFirstChar { it.uppercase() } ?: ""

    if (preciosFrutas.containsKey(fruta)) {
        print("¿Cuántos kilos quieres? ")
        val kilosStr = readLine() ?: "0"
        val kilos = kilosStr.replace(',', '.').toDoubleOrNull() ?: 0.0

        val precioFinal = preciosFrutas[fruta]!! * kilos
        println("El precio de $kilos kilos de $fruta es: %.2f€".format(precioFinal))
    } else {
        println("Lo siento, no tenemos la fruta: $fruta")
    }
}
