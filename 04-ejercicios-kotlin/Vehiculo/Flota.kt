class Flota {
    val vehiculos: MutableList<Vehiculo> = mutableListOf()

    fun agregar(v: Vehiculo) {
        vehiculos.add(v)
    }

    fun eliminarPorId(id: Int) {
        vehiculos.removeIf { it.id == id }
    }

    fun listarOrdenadosPorBateria(): List<Vehiculo> {
        return vehiculos.sorted()
    }

    fun autonomiaMedia(): Double {
        var sumaTotal = 0.0
        for (v in vehiculos) {
            sumaTotal += v.calcularAutonomia()
        }
        var media = sumaTotal / vehiculos.size
        return media
    }
}