class Persona (var peso: Double, var altura: Double) {

    var nombre: String? = null

    val imc: Double
        get(){
            return peso/(altura * altura)
        }



    constructor(nombre: String, peso: Double, altura: Double):this(peso, altura) {
        this.nombre = nombre
    }

    fun saludar(): String{
        return "Hola, me llamo ${if (nombre == null) {"DESCONOCIDO"} else {"$nombre"}
        }"
    }

    fun alturaEncimaMedia(): Boolean{
        if (altura >= 1.75){
            return true
        }else{
            return false
        }
    }
    fun escribeAlturaEncimaMedia(): String{
        val resultado = "La altura de $nombre ${if (this.alturaEncimaMedia()){"esta por encima de la media"}else{"no esta por encima de la media"}}"
        return resultado

    }

    fun pesoEncimaMedia(): Boolean{
        if (peso >= 70){
            return true
        }else{
            return false
        }
    }
    fun escribePesoEncimaMedia(): String{
        val resultado = "El peso de $nombre ${if (this.pesoEncimaMedia()){"esta por encima de la media"}else{"no esta por encima de la media"}}"
        return resultado

    }

    fun obtenerDescImc(): String{
        if (imc<18.5){
            return "Peso insuficiente"
        }else if ((imc>=18.5)&&(imc <= 24.9)){
            return "Peso saludable"
        }else if ((imc>=25.0)&&(imc<=29.9)){
            return "Sobrepeso"
        }else if ((imc>=30)){
            return "Obesidad"
        }else{
            return "ERROR"
        }

    }
    fun obtenerDesc(): String{
        return "${if (nombre == null){"DESCONOCIDO"}else{"$nombre"}} con una altura de $altura (${escribeAlturaEncimaMedia()}) \n" +
                "y un peso de $peso (${escribePesoEncimaMedia()}) tiene \n" +
                "un IMC de ${"%.2f".format(imc)} (${this.obtenerDescImc()})"
    }

    override fun toString(): String{
        var resultado = "${if (this.nombre != null) "Me llamo $nombre" else "SIN NOMBRE"},Peso:$peso, altura:$altura, imc:$imc"
        return resultado
    }
    override fun equals(other: Any?): Boolean{
        if (this === other)
            return true
        if (other !is Persona)
            return false

        if ((this.nombre == other.nombre) && (this.imc == other.imc))
            return true
        else
            return false
    }
}