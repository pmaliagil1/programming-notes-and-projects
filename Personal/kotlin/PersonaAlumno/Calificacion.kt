class Calificacion (val modulo: Modulo) {

    var notaFinal: Int = 0

    override fun toString(): String {
        return "$modulo: $notaFinal"
    }
}