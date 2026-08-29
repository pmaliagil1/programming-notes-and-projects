class Programador(nombre: String, edad: Int, salarioBase: Double, var lineasCodigoPorDia: Int, var lenguajeFavorito: String): Empleado(nombre, edad, salarioBase), Bonificable {

    override fun salarioTotal(): Double {
        return salarioBase + (lineasCodigoPorDia * 0.5)
    }
    override fun descripcion(): String {
        var resultado = "Soy un programador y mi lenguaje favorito es $lenguajeFavorito"
        return resultado
    }

    override fun calcularBono(): Double{
        return salarioTotal()*0.10
    }
}