/*Archivo main para probar las clases del proyecto*/

fun main(){

    val fernando: Persona = Persona("Fernando",40)
    val pablo: Persona = Persona("Pablo",20, "pmaliagil@gmail.com")

    val guapo: Animal = Animal("Cocodrilo","Guapo")
    val noa: Animal = Animal("Perro","Noa", "Blanco")

    val mcqueen: Coche = Coche("Audi","A7")
    val mate: Coche = Coche("Mercedes","MG")

    val dicMascotas: MutableMap<Persona, Animal> = mutableMapOf()
    val dicCoches: MutableMap<Persona, Coche> = mutableMapOf()

    dicMascotas[fernando] = guapo
    dicCoches[fernando] = mate

    dicMascotas[pablo] = noa
    dicCoches[pablo] = mcqueen

    // Recorremos un diccionario
    println("Vamos a mostrar a los dueños y a sus mascotas: ")
    for ((persona,animal) in dicMascotas) {
        persona.presentarse()
        println("OS VOY A HABLAR DE MI MASCOTA")
        animal.presentarse()
    }

    println("En este programa hay: ${Coche.cuentaCoches} coches")
    println("Vamos a mostrar a las personas y sus coches: ")
    for((persona,coche) in dicCoches) {
        persona.presentarse()
        println("OS VOY A HABLAR DE MI COCHE")
        coche.describir()
    }

}