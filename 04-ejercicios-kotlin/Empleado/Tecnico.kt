class Tecnico (dni: String,nombre: String, apellidos: String, sueldoBase: Double,  categoria: Int): Empleado(dni,nombre,apellidos,sueldoBase) {

    var categoria: Int = 0
        set(value) {
            if (value in 1..5)
                field = value
            else
                field = 1
        }

    init {
        this.categoria = categoria
    }

    override fun getSueldo(): Double{
        return this.sueldoBase + this.categoria*100
    }

}
