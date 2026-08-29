class BicicletaElectrica(id:Int,modelo: String, bateria: Int, val asistenciaNiveles: Int): Vehiculo(id,modelo,bateria) {
    override fun calcularAutonomia(): Int {
        var resultado = 0
        resultado = ((bateria*10)/asistenciaNiveles)
        return resultado
    }
}