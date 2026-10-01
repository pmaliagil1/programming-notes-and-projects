class Plantilla {

    val empleados: MutableList<Empleado> = mutableListOf<Empleado>()

    fun contratarEmpleado(e: Empleado) {
        empleados.add(e)
    }

    fun getEmpleadosPorNombre(nombre: String): List<Empleado> {
        var resultado: MutableList<Empleado> = mutableListOf<Empleado>()

        for (empleado in empleados) {
            if (empleado.nombre.contains(nombre)) {
                resultado.add(empleado)
            }
        }
        return resultado.sorted()
    }
}