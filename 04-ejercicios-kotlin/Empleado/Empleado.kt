//Mirar uml para ver si es var o val (si tiene get y set o solo get) /  se sabe que se usa comparable por esta frase "Muestre los empleados encontrados ordenados por sueldo NETO."
abstract class Empleado(val dni: String, val nombre: String, val apellido: String, sueldoBase: Double): Comparable<Empleado> {

    companion object {
        const val SALARIO_MINIMO = 1200.0
    }
//modificamos el set para cuando el salario esta por debajo del sueldo minimo que se cambie al sueldo minimo
    var sueldoBase: Double = SALARIO_MINIMO
        set(value) {
            if (value > SALARIO_MINIMO)
                field = value
            else
                field = SALARIO_MINIMO
        }
    //Primero hace esto, por eso sabe acceder al set
    init {
        this.sueldoBase = sueldoBase
    }
    abstract fun getSueldo(): Double

    override fun compareTo(other: Empleado): Int { //"if (empleado1 <empleado2)" llama a compareTo, tambien puedes usar empleado1.compareTo(empleado2)
        return(this.getSueldo()-other.getSueldo()).toInt()
    }

    override fun toString(): String {
        return "dni: $dni,apellidos: $apellido sueldo: $sueldoBase" + "Sueldo Total:"+getSueldo()
    }
}