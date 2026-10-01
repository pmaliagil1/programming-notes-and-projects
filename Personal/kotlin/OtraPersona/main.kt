import OtraPersona.Companion.contadorPersonas

fun main(){
    var p: Programador = Programador("Pablo",20,2000.0, 1000, "Kotlin")
    var c: Comercial = Comercial("Juan",45,1500.0,10)
    var p2: Programador = Programador("CR7",40,1200.0, 3000, "Python")
    var c2: Comercial = Comercial("Mbappe",28,2500.0,5)

    val lista: MutableList<OtraPersona> = mutableListOf(p,c,p2,c2)
    for (i in lista) {
        println(i.toString())
        println(i.descripcion())

        // Para que kotlin me deje hacer salarioTotal tengo que comprobar que es Empleado
        if (i is Empleado) {
            // Aquí dentro, Kotlin ya sabe que 'i' es un Empleado
            println("Salario Total: ${i.salarioTotal()}")
        }

        // Comprobamos si además tiene bono
        if (i is Bonificable) {
            println("Bono: ${i.calcularBono()}")
        }
    }
    println("En total hay $contadorPersonas personas")



}