fun main(){

    val persona1: Persona = Persona(70.65,1.75)
    val persona2: Persona = Persona("Ana",70.5,1.80,)
    val persona3: Persona = Persona("Carlos", 55.0, 1.88)
    val persona4: Persona = Persona("Lucía", 92.4, 1.65)

    val lista: List<Persona> = listOf(persona1,persona2,persona3,persona4)
    for(persona in lista){
        println(persona.saludar())
        println(persona.obtenerDesc())
    }


}