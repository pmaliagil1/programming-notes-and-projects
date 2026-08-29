/*Escribir un programa que cree un diccionario de traducción español-inglés. El usuario
introducirá las palabras en español e inglés separadas por dos puntos, y cada par
<palabra>:<traducción> separados por comas. El programa debe crear un
diccionario con las palabras y sus traducciones. Después pedirá una frase en español y
utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el
diccionario debe dejarla sin traducir.
*/

fun main() {
    println("Introduce las palabras (ej: hola:hello,casa:house,perro:dog): ")
    val entrada = readLine() ?: ""

    // 1. Creamos el diccionario a partir de la entrada
    val diccionario = mutableMapOf<String, String>()

    // Dividimos por comas para obtener cada par "español:ingles"
    val pares = entrada.split(",")

    for (par in pares) {
        val partes = par.split(":")
        if (partes.size == 2) {
            val espanol = partes[0].trim().lowercase()
            val ingles = partes[1].trim().lowercase()
            diccionario[espanol] = ingles
        }
    }

    // 2. Pedimos la frase a traducir
    println("\nIntroduce una frase en español para traducir:")
    val frase: String = readLine() ?: ""

    // 3. Traducimos palabra a palabra
    val palabrasFrase: List<String> = frase.split(" ")
    val fraseTraducida: MutableList<String> = mutableListOf<String>()

    for (palabra in palabrasFrase) {
        val limpia = palabra.lowercase().trim()
        // Si existe en el diccionario, usamos la traducción; si no, dejamos la original
        val traduccion = diccionario[limpia] ?: palabra
        fraseTraducida.add(traduccion)
    }

    // 4. Mostramos el resultado
    println("\nFrase traducida:")
    println(fraseTraducida.joinToString(" "))
}