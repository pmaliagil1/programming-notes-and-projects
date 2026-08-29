class Triangulo (var l1: Int, var l2: Int, var l3: Int) : Poligono(), Comparable<Triangulo> {
    init {
        require((l1 < l2 + l3) && (l2 < l1 + l3) && (l3 < l1 + l2)) { "ERROR NO ES TRIANGULO" }
        println("Triángulo creado correctamente")
    }

    override fun perimetro(): Int {
        return (l1 + l2 + l3)
    }

    override fun area(): Int {
        var semiperimetro: Double = 0.0
        var aHeron: Double = 0.0

        semiperimetro = ((l1 + l2 + l3) / 2).toDouble()
        aHeron = Math.sqrt(semiperimetro * (semiperimetro - l1) * (semiperimetro - l2) * (semiperimetro - l3))

        return aHeron.toInt()
    }

    override fun toString(): String {
        var resultado: String = "Hola soy un triangulo de $l1, $l2, $l3 "
        return resultado
    }

    override fun compareTo(other: Triangulo): Int {
        return if (this.area() == other.area()) {
            0
        } else if (this.area() > other.area()) {
            1
        } else {
            -1
        }
    }
}


