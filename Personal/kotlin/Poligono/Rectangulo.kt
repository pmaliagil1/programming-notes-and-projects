/*  open es para cuando vaya a crear cuadrado que pueda heredar/esto significa que hereda de poligono (: Poligono())*/
open class Rectangulo (var base: Int, var altura: Int) : Poligono(), Comparable<Rectangulo>, Dibujable {

    override fun perimetro(): Int {
        return (2*base+2*altura)
    }

    override fun area(): Int {
        return (base*altura)
    }

    override fun toString(): String {
        var resultado: String = "Soy un rectangulo de base $base y altura $altura"
        return resultado
    }

    //IGUALDAD DE RECTÁNGULOS
    override fun equals(other: Any?): Boolean {
        if (this === other)
            return true
        if (other == null)
            return false
        if (other !is Rectangulo)
            return false

        if ((this.base == other.base) && (this.altura != other.altura))
            return true
        else
            return false
    }
    //COMPARACION, NECESARIO PARA INTERFAZ COMPARABLE
    override fun compareTo(other: Rectangulo): Int {
        if (this.perimetro() == other.perimetro())
            return 0
        else
            return (this.perimetro() - other.perimetro())
    }

    // DIBUJAR RECTANGULOS
    override fun dibujar() {

        for (i in 0 until altura){
            for (j in 0 until base){
                print("*")
            }
            println()
        }

    }

}