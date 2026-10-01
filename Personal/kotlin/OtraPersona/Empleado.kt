abstract class Empleado(nombre: String, edad: Int,var salarioBase: Double): OtraPersona(nombre,edad) {

    abstract fun salarioTotal(): Double

    override fun descripcion(): String {
        var resultado = "Soy un empleado"
        return resultado
    }
}