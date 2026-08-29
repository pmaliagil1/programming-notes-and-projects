fun main(){

    var r: Rectangulo = Rectangulo(4,9)
    var c: Cuadrado = Cuadrado(4)
    var t: Triangulo? = null

    try {
        t = Triangulo(4,5,700 )//si no pones datos que sigan la regla no sera triangulo
    }catch(e:Exception){
        println(e.message)
        Poligono.contadorPoligonos-- //con esto si el triangulo es nulo lo quita del contador
    }
    try {
        var l: MutableList<Poligono?> = mutableListOf(r,c,t)

        for (poligono in l) {
            if (poligono != null) {
                println(poligono)
                println("Area: ${poligono.area()}")
                println("Perimetro: ${poligono.perimetro()}")
                //poligono.dibujar()
            }
        }
    } catch(e:Exception){
        println(e.message)

    }


    println("El numero de poligonos es en total: ${Poligono.contadorPoligonos}")



}