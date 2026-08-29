abstract class OtraPersona (val nombre: String, var edad: Int) {
    companion object {
        var contadorPersonas = 0
            private set //esto se pone para que solo se pueda modificar el contador desde esta clase
    }

    init {
        contadorPersonas++
    }

    abstract fun descripcion(): String

    override fun toString(): String {
        var resultado = "Nombre: $nombre, Edad: $edad"
        return resultado
    }
}