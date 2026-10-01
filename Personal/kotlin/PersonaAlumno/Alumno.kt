import java.time.LocalDate

class Alumno(dni: String, nombre: String, apellidos: String, fechaNacimiento: LocalDate, var ciclo: String) : Persona(dni, nombre, apellidos, fechaNacimiento) {

    private val calificaciones: MutableList<Calificacion> = mutableListOf()

    fun matricular(modulo: Modulo) {
        val nuevaCalificacion = Calificacion(modulo)
        calificaciones.add(nuevaCalificacion)
    }

    fun calificar(modulo: Modulo, nota: Int) {
        // CAMBIO: it.modulo en lugar de it.getModulo()
        val calificacionEncontrada = calificaciones.find { it.modulo.nombre == modulo.nombre }

        // CAMBIO: .notaFinal en lugar de .setNotaFinal(nota)
        calificacionEncontrada?.notaFinal = nota
    }

    fun promociona(): Boolean {
        if (calificaciones.isEmpty()) return false

        var horasTotales = 0
        var horasAprobadas = 0

        for (calif in calificaciones) {
            // CAMBIO: calif.modulo.horas
            val horasModulo = calif.modulo.horas
            horasTotales += horasModulo

            // CAMBIO: calif.notaFinal
            if (calif.notaFinal >= 5) {
                horasAprobadas += horasModulo
            }
        }
        return horasAprobadas > (horasTotales / 2)
    }

    fun getNotaMedia(): Double {
        if (calificaciones.isEmpty()) return 0.0

        var sumaNotaPorHoras = 0.0
        var totalHoras = 0.0

        for (calif in calificaciones) {
            // CAMBIO: calif.modulo.horas y calif.notaFinal
            val horas = calif.modulo.horas
            val nota = calif.notaFinal

            sumaNotaPorHoras += (nota * horas)
            totalHoras += horas.toDouble()
        }
        return if (totalHoras > 0) sumaNotaPorHoras / totalHoras else 0.0
    }

    override fun toString(): String {
        var resultado = "${super.toString()} | Ciclo: $ciclo | Media: ${String.format("%.2f", getNotaMedia())}\n"
        resultado += "Notas:\n"
        for (c in calificaciones) {
            resultado += " - $c\n"
        }
        return resultado
    }
}