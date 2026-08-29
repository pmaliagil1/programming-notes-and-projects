/*
* @brief Clase que modela una Persona
* @nombre Es como se llama la Persona
* @edad Puede ser un campo calculado a partir de fecha nacimiento
* */

class Persona (private val nombre: String, private var edad: Int) {
    //ZONA DE ATRIBUTOS
    var email: String? = null
    //Sobrecarga
    constructor(nombre: String, edad: Int, email: String) : this(nombre, edad) {
        this.email = email
    }

    //ZONA DE METODOS
    public fun presentarse(){
        println("Hola, me llamo $nombre, tengo $edad años")
        if (this.email != null) {//este es el de fuera(la variable declarada)
            println("Mi email es: $email")
        }
    }

}