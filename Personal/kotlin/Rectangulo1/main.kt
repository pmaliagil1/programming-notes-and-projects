fun main(){

    var miRectangulo: Rectangulo? = null
    var tuRectangulo: Rectangulo? = null

    try {
        miRectangulo = Rectangulo(4, 3)
        tuRectangulo = Rectangulo(5, -8)
    } catch (e: Exception){
        println(e)
    }

    if (miRectangulo != null) {
        miRectangulo.altura=40
        println(miRectangulo.toString())
        println("El perimetro es: ${miRectangulo.perimetro()}")
        println("El perimetro es: ${miRectangulo.area()}")
    }

    //tuRectangulo.base = -10          AQUI ME SALTO EL ENUNCIADO
    println(tuRectangulo.toString())

}