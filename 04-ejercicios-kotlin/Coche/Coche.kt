class Coche(val marca: String?, val modelo: String?) {
    var color: String? = null
        set(value) {
            if (value == null) throw IllegalArgumentException("Color no nulo")
            field = value
        }
    var nCaballos: Int? = null
    var nPuertas: Int? = null
    var matricula: String? = null

    constructor(color: String?, marca: String?, modelo: String?, nCaballos: Int?, nPuertas: Int?, matricula: String?) : this(marca, modelo) {

        if (nCaballos == null || nCaballos !in 70..700) throw IllegalArgumentException("Caballos incorrectos")
        if (nPuertas == null || nPuertas !in 3..5) throw IllegalArgumentException("Puertas incorrectas")
        if (matricula == null || matricula.length != 7) throw IllegalArgumentException("Matrícula incorrecta")

        this.color = color
        this.nCaballos = nCaballos
        this.nPuertas = nPuertas
        this.matricula = matricula
    }

    init {
        if (marca.isNullOrBlank()) throw IllegalArgumentException("Marca obligatoria")
        if (modelo.isNullOrBlank()) throw IllegalArgumentException("Modelo obligatorio")
    }

    override fun toString(): String {
        return "Coche: $marca $modelo, CV: $nCaballos, Matrícula: $matricula"
    }
}