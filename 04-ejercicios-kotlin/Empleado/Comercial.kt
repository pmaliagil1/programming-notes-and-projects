class Comercial (dni:String, nombre: String, apellidos: String,sueldoBase: Double,  ventas: Double): Empleado(dni,nombre,apellidos,sueldoBase){

    var ventas: Double = SALARIO_MINIMO/10
        set(value) {
            if (value > (SALARIO_MINIMO / 10))
                field = value

        }
    init{
        this.ventas = ventas
    }

    override fun getSueldo(): Double{
        return sueldoBase + ventas*0.1
    }
}
