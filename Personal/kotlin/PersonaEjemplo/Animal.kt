


class Animal(private val especie: String, private val nombre: String) {

    var color: String? = null
    constructor(especie: String, nombre: String, c: String) : this(especie, nombre) {
        this.color = c
    }

    public fun emitirSonido(){

        when(especie){
            "Gato" -> println("MIAUUUU")
            "Perro" -> println("GUAU GUAU")
            else -> println("ALIENIGENA")
        }
    }
    public fun presentarse(){
        println("Soy un $especie, me llamo $nombre  ")
        if (color != null) {
            println("Soy de color $color")
        }
        this.emitirSonido()
    }
}