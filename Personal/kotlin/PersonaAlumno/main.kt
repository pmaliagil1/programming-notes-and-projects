import java.time.LocalDate

fun main() {
    // 1. Módulos
    val programacion = Modulo("Programación", 200)
    val bd = Modulo("Bases de Datos", 150)

    // 2. Alumno (Ya no pasamos la lista al final, Kotlin usa la vacía por defecto)
    val alumno = Alumno("12345678Z", "Pepe", "Pérez", LocalDate.of(2000, 5, 15), "DAM"
    )

    // 3. Operaciones
    alumno.matricular(programacion)
    alumno.matricular(bd)

    alumno.calificar(programacion, 7)
    alumno.calificar(bd, 4)

    // 4. Salida
    println(alumno)
    println("Promociona: ${if (alumno.promociona()) "SÍ" else "NO"}")
}