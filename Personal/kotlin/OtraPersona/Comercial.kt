class Comercial(nombre: String, edad: Int, salarioBase: Double, var ventasRealizadas: Int): Empleado(nombre, edad, salarioBase), Bonificable {

    override fun salarioTotal(): Double {
        return (salarioBase + (ventasRealizadas*20))
    }

    override fun descripcion(): String {
        return "Soy un comercial y he realizado $ventasRealizadas ventas"
    }

    override fun calcularBono(): Double{
        return salarioTotal()*0.05
    }
}