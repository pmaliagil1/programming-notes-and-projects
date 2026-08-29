/*Realiza un programa que compruebe la letra del DNI.*/

fun main() {
    val letrasDNI = "TRWAGMYFPDXBNJZSQVHLCKE"

    print("Introduce tu DNI (con o sin letra): ")
    val entrada = readLine()?.uppercase()?.replace(" ", "") ?: ""

    if (entrada.isEmpty()) {
        println("Entrada vacía.")
        return
    }

    // Extraer solo los números
    val soloNumerosStr = entrada.filter { it.isDigit() }

    if (soloNumerosStr.length != 8) {
        println("El número de DNI debe tener 8 dígitos.")
        return
    }

    val numero = soloNumerosStr.toInt()
    val letraCalculada = letrasDNI[numero % 23]

    // Si la entrada tenía letra, comprobamos si es correcta
    val letraEnEntrada = entrada.find { it.isLetter() }

    if (letraEnEntrada != null) {
        if (letraEnEntrada == letraCalculada) {
            println("El DNI $entrada es válido.")
        } else {
            println("El DNI $entrada no es válido. La letra correcta para $soloNumerosStr es $letraCalculada.")
        }
    } else {
        println("Para el número $soloNumerosStr la letra que le corresponde es: $letraCalculada")
    }
}
