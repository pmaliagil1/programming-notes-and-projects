fun main() {
    try {
        val miCoche = Coche("Rojo", "Seat", "Ibiza", 90, 5, "1234ABC")
        println(miCoche.toString())

        // Esto lanzará error por los caballos
        val cocheMalo = Coche("Azul", "Fiat", "500", 20, 3, "1111AAA")
    } catch (e: Exception) {
        println("Error: ${e.message}")
    }
}