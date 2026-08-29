fun main(){
    var b: BicicletaElectrica = BicicletaElectrica(5,"hola",6,15)
    var p: Patinete = Patinete(7,"adios",101,30)
    var b2: BicicletaElectrica = BicicletaElectrica(6,"perro",10,14)
    var p2: Patinete = Patinete(4,"gato",66,23)

    var lista = listOf(b,p,b2,p2)
    val miFlota = Flota()
    for (vehiculo in lista) {
        miFlota.agregar(vehiculo)
    }

    for (elemento in miFlota.listarOrdenadosPorBateria()){
        println(elemento)
    }
    b.bateria = 3
    miFlota.eliminarPorId(7)
    println("CAMBIO")
    for (elemento in miFlota.listarOrdenadosPorBateria()){
        println(elemento)
    }


}