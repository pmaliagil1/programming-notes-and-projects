class Patinete(id:Int,modelo: String, bateria: Int,val autonomiaKm: Int): Vehiculo(id, modelo,bateria) {
    override fun calcularAutonomia(): Int {
        return autonomiaKm
}
}