abstract class Vehiculo (val id: Int,val modelo: String,  bateria: Int ): Comparable<Vehiculo> {
    var bateria: Int = 0
        set(value){
           if ((value >100)){
                field = 100
            }else if(value <0){
                field = 0
            }else{
                field = value
            }
    }

    init {
        this.bateria = bateria
        println("El vehiculo con ID $id ha sido registrado en el sistema")
    }

    override fun compareTo(other: Vehiculo): Int {
        return this.bateria - other.bateria
    }

    override fun toString(): String {
        return "$modelo - $bateria - ${calcularAutonomia()}"
    }

    abstract fun calcularAutonomia(): Int
}
