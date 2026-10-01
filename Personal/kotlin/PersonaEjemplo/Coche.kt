


class Coche(private val marca: String, private val modelo: String) {

    init { //init hace que sea lo primero que hace el programa
        cuentaCoches++  //con esto actualizo el contador de coches
    }

    companion object { //sirve para crear objetos que podemos ir usando
        var cuentaCoches: Int = 0
    }

    public fun describir(){
        println("Mi marca es: $marca, mi modelo es: $modelo")
    }
}