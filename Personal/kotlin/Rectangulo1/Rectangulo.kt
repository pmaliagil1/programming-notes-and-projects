class Rectangulo (base: Int,altura: Int){

    var base: Int = base
        set(value) {
            require (value > 0){"error: SET: valor negativo"}
            field = value
        }
        public get

    var altura: Int = altura
        set(value) {
            require (value > 0){"error: SET: valor negativo"}
            field = value
        }
        public get

    init {
        require((altura > 0) && (base > 0)){"NO DIMENSIONES NEGATIVAS"}

        if (altura < 1) {
            throw IllegalArgumentException("ERROR: ALTURA NEGATIVA")
        }
    }

    public fun perimetro(): Int {
        return (2*base+2*altura)

    }
    public fun area(): Int {
        return this.base*this.altura
    }

    override fun toString(): String {
        val resultado = "Soy un rectangulo de base $base y altura $altura"
        return resultado
    }

}