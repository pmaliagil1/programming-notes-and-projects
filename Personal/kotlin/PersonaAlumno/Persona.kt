import java.time.LocalDate

abstract class Persona (val dni: String, val nombre: String, val apellidos: String, val fechaNacimiento: LocalDate) {
    override fun toString(): String {
        var resultado = "Me llamo $nombre $apellidos, mi dni es $dni y naci el $fechaNacimiento"
        return resultado
    }
}